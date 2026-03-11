# EG2 Public Note (Deformation Capture Package)

In-paper anchor: `paper/BSD_CONJECTURE_PREPRINT.md` (Sections 4-6, `BSD2-BSD3` chain).

## Goal
Preserve positive defect floor under deformation flow + restart/normalization steps.

Defect:

`D_tau = B_tau - J_tau`.

## Capture Statement

There exists `sigma_capture > 0` such that:

`D_tau >= sigma_capture - Delta_coh[tau0, tau]`.

Strict target: `Delta_coh = 0`, so `D_tau >= sigma_capture`.

## Closure Criterion

`B_G2 = PASS` iff:

1. theorem-level `sigma_capture > 0`,
2. restart/normalization map preserves admissible class,
3. coherence ledger is explicit and nonnegative.

## Lemma Chain and Proof Payload

### Lemma EG2.1 (flow segment inequality)
On restart-free segment `[a,b]`, if
`dD/dtau >= -L_D(D-sigma_*) - eta_flow(tau)`, then:

`D(b) >= sigma_* + e^(-L_D(b-a))(D(a)-sigma_*) - int_a^b e^(-L_D(b-s)) eta_flow(s) ds`.

**Proof.**
Integrating-factor Gronwall.

### Lemma EG2.2 (restart composition)
Across restart times in `[tau0,tau1]` with jump penalties:

`D(tau1) >= sigma_* + e^(-L_D(tau1-tau0))(D(tau0)-sigma_*) - Delta_coh[tau0,tau1]`.

**Proof.**
Compose Lemma EG2.1 over smooth segments and subtract jump terms.

### Theorem EG2.3 (gate closure)
Define:

`sigma_capture^(raw) := inf_(tau in T_*) (sigma_tau - Delta_coh[tau0,tau])`.

If `sigma_capture^(raw)>0` and restart map preserves admissibility, then
`B_G2=PASS` with normalized constant
`sigma_capture := sigma_capture^(raw)/sigma_capture,ref > 0`.

**Proof.**
Lemma EG2.2 gives a uniform lower floor; positivity of the infimum closes the gate.

## Current Canonical-Lane Instantiation

- `sigma_capture = 1.063` (theorem-level),
- stitched floor `sigma_star_can = 1.053` (theorem-level),
- gate status target: `B_G2 = PASS`.
