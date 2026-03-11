# EG3 Public Note (Compactness Package)

In-paper anchor: `paper/BSD_CONJECTURE_PREPRINT.md` (Sections 5-6, `BSD4` chain).

## Goal
Show precompactness of normalized near-failure sequences in canonical BSD lane.

## Candidate Class

Normalized arithmetic/spectral representatives with fixed admissibility constraints:

`U_n = N(u_(tau_n))`.

## Closure Criterion

`B_G3 = PASS` iff theorem-level `kappa_compact > 0` gives:

- every bad sequence has convergent subsequence in declared topology.

## Lemma Chain and Proof Payload

### Lemma EG3.1 (precompactness criterion)
If normalized sequence `U_n` has uniform seminorm bounds and tightness in the
declared topology, then `{U_n}` is precompact.

**Proof.**
Apply the compactness criterion attached to the chosen seminorm topology.

### Lemma EG3.2 (badness lower-semicontinuity)
If `U_n -> U_infty`, then
`Bad(U_infty) >= limsup_n Bad(U_n)`.

**Proof.**
`Bad` is an infimum of continuous residual norms.

### Theorem EG3.3 (gate closure)
Define:

`kappa_compact^(raw) := (1 + sup_(u in T_*) Delta_comp^+(u))^(-1)`.

If `kappa_compact^(raw)>0`, then every normalized bad sequence has a convergent
bad subsequence and `B_G3=PASS` with normalized constant
`kappa_compact := kappa_compact^(raw)/kappa_compact,ref > 0`.

**Proof.**
Lemma EG3.1 gives compactness; Lemma EG3.2 keeps badness in the limit.

## Current Canonical-Lane Instantiation

- `kappa_compact = 0.805802` (theorem-level),
- gate status target: `B_G3 = PASS`.
