# The Birch–Swinnerton-Dyer Conjecture via Analytic-Arithmetic Persistence
## Canonical Lane (defined term): Local-to-Global Closure Architecture (`BSD1–BSD8`)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18876077.svg)](https://doi.org/10.5281/zenodo.18876077)

Canonical Lane research workspace for the Millennium problem:
rank and leading-value structure of elliptic-curve `L`-functions.

## Main Manuscript

- [paper/BSD_CONJECTURE_PREPRINT.md](paper/BSD_CONJECTURE_PREPRINT.md)

## Structure

- `paper/`: main theorem architecture (`BSD1–BSD8` chain).
- `notes/`: closure notes (`EG1`–`EG4`) + identification bridge.
- `repro/`: local certificate workflow and rerun protocol.
- `scripts/`: local guard and extraction scripts.
- `artifacts/`: constants registries and stitched constants.

## Local Repro Command

```bash
bash repro/run_repro.sh
```

This writes `repro/certificate_runtime.json`.

## How To Read This Professionally

1. Theorem chain first: read `paper/BSD_CONJECTURE_PREPRINT.md`.
2. Constants provenance second: audit `paper/EXTRACTION_SPEC.md`, `artifacts/constants_extraction_inputs.json`, `artifacts/constants_extracted.json`, and `artifacts/promotion_report.json`.
3. Pipeline third: run `bash repro/run_repro.sh` to audit hashes/provenance/gates; it is reproducibility infrastructure, not theorem generation.

Release modes:

- `normalized`: `status=normalized_placeholder` allowed when explicitly labeled.
- `fully_extracted`: requires `status=derived_numeric` for all required constants/stitch keys.

Current BSD runner policy:

- `repro/run_repro.sh` enforces `fully_extracted` mode.

## Citation

- Metadata: [CITATION.cff](CITATION.cff)
- Manuscript target: [paper/BSD_CONJECTURE_PREPRINT.md](paper/BSD_CONJECTURE_PREPRINT.md)

## Authorship

- Program author: **HautevilleHouse**
- Canonical attribution source: [`CITATION.cff`](CITATION.cff)

## Local-Only Policy

- See [LOCAL_ONLY_POLICY.md](LOCAL_ONLY_POLICY.md).
- Remote publish is blocked unless explicitly overridden.
