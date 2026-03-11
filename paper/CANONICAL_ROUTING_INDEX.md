# Canonical Routing Index (BSD)

This file is the single routing map for where each proof package lives in:

- main preprint sections,
- mirror note files,
- certificate/artifact keys.

## Gate Routing

| Gate | Main preprint location | Mirror note | Registry/artifact key(s) |
|---|---|---|---|
| `B_G1` (coercivity) | `Section 4/5` (`BSD1`) | `notes/EG1_public.md` | `kappa_rank` |
| `B_G2` (capture) | `Section 4/5` (`BSD2`,`BSD3`) | `notes/EG2_public.md` | `sigma_capture`, `sigma_star_can` |
| `B_G3` (compactness/no-Zeno) | `Section 5` (`BSD4`) | `notes/EG3_public.md` | `kappa_compact` |
| `B_G4` (rigidity) | `Section 5` (`BSD5`) | `notes/EG4_public.md` | `rho_rigidity` |
| `B_G5` (identification lock) | `Section 5` (`BSD7`) | `notes/IDENTIFICATION_BRIDGE.md` | `alpha_lock` |
| `B_G6` (arithmetic floor) | `Section 5` (`BSD8`) | `notes/EG4_public.md` | `bsd_floor` |
| `B_GCoh` (strict coherence) | `Sections 3/4` | `notes/IDENTIFICATION_BRIDGE.md` | `eps_coh` |
| `B_GM` (final strict margin) | `Section 3` margin formula | derived | all above keys |

## Repro Routing

| Artifact | Path |
|---|---|
| Runner | `repro/run_repro.sh` |
| Guard | `scripts/bsd_closure_guard.py` |
| Runtime certificate | `repro/certificate_runtime.json` |
| Baseline certificate | `repro/certificate_baseline.json` |
| Registry | `artifacts/constants_registry.json` |
| Stitch constants | `artifacts/stitch_constants.json` |
| Third-party rerun protocol | `repro/THIRD_PARTY_RERUN_PROTOCOL.md` |
