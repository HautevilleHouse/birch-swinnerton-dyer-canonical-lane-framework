#!/usr/bin/env python3
"""Canonical-lane closure guard for BSD conjecture workspace."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

DEFAULT_REGISTRY = "artifacts/constants_registry.json"
DEFAULT_STITCH = "artifacts/stitch_constants.json"
DEFAULT_OUT = "repro/certificate_runtime.json"
DEFAULT_HISTORY = "repro/drift_guard_runs.jsonl"

REQUIRED_KEYS = (
    "kappa_rank",
    "sigma_capture",
    "kappa_compact",
    "rho_rigidity",
    "alpha_lock",
    "bsd_floor",
    "eps_coh",
)


def _finite(v: Any) -> bool:
    return isinstance(v, (int, float)) and math.isfinite(float(v))


def _resolve(path_str: str) -> Path:
    p = Path(path_str).expanduser()
    if p.is_absolute():
        return p
    return PROJECT_ROOT / p


def _bootstrap_registry(path: Path) -> None:
    payload = {
        "constants": {
            k: {
                "value": None,
                "theorem_level": False,
                "source": "",
                "notes": "pending theorem extraction",
            }
            for k in REQUIRED_KEYS
        }
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def _load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        _bootstrap_registry(path)
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        raise ValueError("registry must be JSON object")
    consts = data.get("constants")
    if not isinstance(consts, dict):
        raise ValueError("registry missing constants object")
    return data


def _load_sigma_from_stitch(path: Path) -> float | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except Exception:  # noqa: BLE001
        return None
    consts = data.get("constants")
    if not isinstance(consts, dict):
        return None
    sigma = consts.get("sigma_star_can")
    if isinstance(sigma, dict):
        v = sigma.get("value")
        return float(v) if _finite(v) else None
    return float(sigma) if _finite(sigma) else None


def _entry(constants: dict[str, Any], key: str) -> tuple[float | None, bool]:
    obj = constants.get(key)
    if isinstance(obj, dict):
        v = obj.get("value")
        theorem = bool(obj.get("theorem_level", False))
        return (float(v) if _finite(v) else None, theorem)
    if _finite(obj):
        return float(obj), False
    return None, False


def compute_report(data: dict[str, Any], sigma_star: float | None, strict_coh_zero: bool) -> dict[str, Any]:
    consts = data["constants"]

    kappa_rank, t1 = _entry(consts, "kappa_rank")
    sigma_capture, t2 = _entry(consts, "sigma_capture")
    kappa_compact, t3 = _entry(consts, "kappa_compact")
    rho_rigidity, t4 = _entry(consts, "rho_rigidity")
    alpha_lock, t5 = _entry(consts, "alpha_lock")
    bsd_floor, t6 = _entry(consts, "bsd_floor")
    eps_coh, t7 = _entry(consts, "eps_coh")

    b_g1 = t1 and _finite(kappa_rank) and float(kappa_rank) > 0.0
    b_g2 = t2 and _finite(sigma_capture) and float(sigma_capture) > 0.0
    b_g3 = t3 and _finite(kappa_compact) and float(kappa_compact) > 0.0
    b_g4 = t4 and _finite(rho_rigidity) and float(rho_rigidity) > 0.0
    b_g5 = t5 and _finite(alpha_lock) and float(alpha_lock) > 0.0
    b_g6 = t6 and _finite(bsd_floor) and float(bsd_floor) > 0.0
    b_gcoh_base = t7 and _finite(eps_coh) and float(eps_coh) >= 0.0
    b_gcoh = b_gcoh_base and ((abs(float(eps_coh)) < 1e-15) if strict_coh_zero else True)

    margin = None
    if all(
        _finite(x)
        for x in (kappa_rank, sigma_capture, kappa_compact, rho_rigidity, alpha_lock, bsd_floor, eps_coh)
    ):
        margin = min(
            float(kappa_rank),
            float(sigma_capture),
            float(kappa_compact),
            float(rho_rigidity),
            float(alpha_lock),
            float(bsd_floor),
        ) - float(eps_coh)

    b_gm = b_g1 and b_g2 and b_g3 and b_g4 and b_g5 and b_g6 and b_gcoh and _finite(margin) and float(margin) > 0.0

    gates = {
        "B_G1": "PASS" if b_g1 else "FAIL",
        "B_G2": "PASS" if b_g2 else "FAIL",
        "B_G3": "PASS" if b_g3 else "FAIL",
        "B_G4": "PASS" if b_g4 else "FAIL",
        "B_G5": "PASS" if b_g5 else "FAIL",
        "B_G6": "PASS" if b_g6 else "FAIL",
        "B_GCoh": "PASS" if b_gcoh else "FAIL",
        "B_GM": "PASS" if b_gm else "FAIL",
    }
    blockers = {
        "B_G1": [] if b_g1 else ["kappa_rank missing/nonpositive or not theorem-level"],
        "B_G2": [] if b_g2 else ["sigma_capture missing/nonpositive or not theorem-level"],
        "B_G3": [] if b_g3 else ["kappa_compact missing/nonpositive or not theorem-level"],
        "B_G4": [] if b_g4 else ["rho_rigidity missing/nonpositive or not theorem-level"],
        "B_G5": [] if b_g5 else ["alpha_lock missing/nonpositive or not theorem-level"],
        "B_G6": [] if b_g6 else ["bsd_floor missing/nonpositive or not theorem-level"],
        "B_GCoh": [] if b_gcoh else ["eps_coh missing/invalid or strict-zero target failed"],
        "B_GM": [] if b_gm else ["strict margin <= 0 or upstream gates failed"],
    }
    normalized_gates = {
        "G1": gates["B_G1"],
        "G2": gates["B_G2"],
        "G3": gates["B_G3"],
        "G4": gates["B_G4"],
        "G5": gates["B_G5"],
        "G6": gates["B_G6"],
        "GCoh": gates["B_GCoh"],
        "GM": gates["B_GM"],
    }
    normalized_blockers = {
        "G1": blockers["B_G1"],
        "G2": blockers["B_G2"],
        "G3": blockers["B_G3"],
        "G4": blockers["B_G4"],
        "G5": blockers["B_G5"],
        "G6": blockers["B_G6"],
        "GCoh": blockers["B_GCoh"],
        "GM": blockers["B_GM"],
    }

    report = {
        "meta": {
            "computed_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
            "framework": "birch_swinnerton_dyer",
        },
        "schema": {
            "normalized_gate_keys": ["G1", "G2", "G3", "G4", "G5", "G6", "GCoh", "GM"],
            "g6_policy": "G6 is a standalone theorem gate in this framework",
        },
        "lane": {
            "canonical_theorem_lane": "manifold_constrained",
            "active_lane": "manifold_constrained",
        },
        "inputs": {
            "kappa_rank": kappa_rank,
            "sigma_capture": sigma_capture,
            "kappa_compact": kappa_compact,
            "rho_rigidity": rho_rigidity,
            "alpha_lock": alpha_lock,
            "bsd_floor": bsd_floor,
            "eps_coh": eps_coh,
            "sigma_star_can": sigma_star,
        },
        "derived": {
            "strict_margin": margin,
            "strict_coh_zero": bool(strict_coh_zero),
        },
        "gates": gates,
        "blockers": blockers,
        "normalized": {
            "gates": normalized_gates,
            "blockers": normalized_blockers,
        },
    }
    report["all_pass"] = all(v == "PASS" for v in gates.values())
    report["all_pass_normalized"] = all(v == "PASS" for v in normalized_gates.values())
    return report


def append_history(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "timestamp_utc": report["meta"]["computed_at_utc"],
        "all_pass": report["all_pass"],
        "gates": report["gates"],
        "strict_margin": report["derived"]["strict_margin"],
    }
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, sort_keys=True) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--registry", default=DEFAULT_REGISTRY)
    ap.add_argument("--stitch", default=DEFAULT_STITCH)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--history", default=DEFAULT_HISTORY)
    ap.add_argument("--strict-coh-zero", action="store_true")
    ap.add_argument("--pretty", action="store_true")
    ns = ap.parse_args()

    registry_path = _resolve(ns.registry)
    stitch_path = _resolve(ns.stitch)
    out_path = _resolve(ns.out)
    history_path = _resolve(ns.history)

    data = _load_registry(registry_path)
    sigma_star = _load_sigma_from_stitch(stitch_path)
    report = compute_report(data, sigma_star=sigma_star, strict_coh_zero=bool(ns.strict_coh_zero))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2 if ns.pretty else None, sort_keys=True) + "\n")
    append_history(history_path, report)

    if ns.pretty:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
