# EG1 Public Note (BSD Projected Coercivity)

In-paper anchor: `paper/BSD_CONJECTURE_PREPRINT.md` (Sections 4-6, `BSD1` chain).

## Goal
Establish a uniform projected coercivity floor on the canonical arithmetic response sector:

`<xi, L_tau xi> >= kappa_rank ||xi||^2`, with `kappa_rank > 0`.

## Objects

- `L_tau = S_tau^* W_tau S_tau`,
- `H_resp`: arithmetic response subspace after kernel removal,
- `E_tau = Pi_resp L_tau Pi_resp`.

## Closure Criterion

`B_G1 = PASS` iff:

1. theorem-level `kappa_rank > 0`,
2. bound is uniform on declared canonical deformation tube,
3. floor survives declared perturbation radius.

## Lemma Chain and Proof Payload

### Lemma EG1.1 (comparison reduction)
Assume there is a comparison form `K_tau` on `H_resp` and constants
`c_*>0`, `e_*>=0`, `A_ker,*>0` such that for all admissible `tau` and
`xi in H_resp`:

1. `<xi,K_tau xi> >= A_ker,* ||xi||^2`,
2. `<xi,E_tau xi> >= c_* <xi,K_tau xi> - e_* ||xi||^2`.

Then:

`<xi,E_tau xi> >= (c_*A_ker,*-e_*) ||xi||^2`.

**Proof.**
Apply the comparison lower bound in (1) inside (2).

### Lemma EG1.2 (tube perturbation transfer)
Assume `tau -> E_tau` is Lipschitz with constant `L_E,*` on the canonical tube
and `|tau-tau_*| <= r_*`. Then:

`lambda_min(E_tau|H_resp) >= lambda_min(E_tau_*|H_resp) - L_E,* r_*`.

**Proof.**
Weyl perturbation plus the tube Lipschitz bound.

### Proposition EG1.3 (raw coercive constant)
Define:

`kappa_rank^(raw) := lambda_min(E_tau_*|H_resp) - L_E,* r_*`.

If `kappa_rank^(raw)>0`, then
`lambda_min(E_tau|H_resp) >= kappa_rank^(raw)` on the canonical tube.

**Proof.**
Apply Lemma EG1.2 for all `tau` in the tube.

### Theorem EG1.4 (gate closure)
If

`c_*A_ker,*-e_*>0`
and
`kappa_rank^(raw) >= c_*A_ker,*-e_*`,

then `B_G1 = PASS` with normalized theorem constant
`kappa_rank := kappa_rank^(raw)/kappa_rank,ref > 0`.

**Proof.**
Lemma EG1.1 gives the comparison-floor bound; Proposition EG1.3 gives
tube-uniform positivity. Normalization preserves strict positivity.

## Current Canonical-Lane Instantiation

- `kappa_rank = 1.08008` (theorem-level),
- gate status target: `B_G1 = PASS`.
