# Third-Party Rerun Protocol (BSD XG7 analogue)

## Inputs

- `scripts/bsd_closure_guard.py`
- `artifacts/constants_registry.json`
- `artifacts/stitch_constants.json`
- `repro/repro_manifest.json`
- `repro/certificate_baseline.json`

## Command

```bash
bash repro/run_repro.sh
```

## Required Checks

1. `repro/certificate_runtime.json` produced,
2. lane field: `"active_lane": "manifold_constrained"`,
3. `"all_pass": true`,
4. gate tuple all `PASS` for `B_G1,B_G2,B_G3,B_G4,B_G5,B_G6,B_GCoh,B_GM`,
5. runtime certificate hash recorded:

```bash
shasum -a 256 repro/certificate_runtime.json
```

## Attestation Record

Publish:

- UTC timestamp,
- machine + Python version,
- local snapshot hash/commit,
- runtime certificate SHA-256,
- gate tuple,
- pass/fail.
