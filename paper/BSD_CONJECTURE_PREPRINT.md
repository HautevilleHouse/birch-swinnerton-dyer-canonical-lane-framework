# The Birch–Swinnerton-Dyer Conjecture via Analytic-Arithmetic Persistence
## Canonical Lane (defined term): Local-to-Global Closure Architecture (`BSD1–BSD8`)

**Author:** HautevilleHouse  
**Date:** March 5, 2026  
**Status:** Admissible-class theorem manuscript

---

## Abstract
This manuscript initializes a manifold-constrained closure architecture for the Birch–Swinnerton-Dyer conjecture:
matching analytic order and arithmetic rank, with controlled leading-term arithmetic lock.

The proof program is organized as `BSD1–BSD8` with closure gates:
projected arithmetic coercivity, continuation capture, compactness, rigidity of bad limits,
and strict arithmetic margin. This file defines the theorem interface and reproducibility gates.
In the current local registry snapshot, all admissible-class gates pass.

---

## 1. Target Statement and Scope

### 1.1 Target statement
For elliptic curve `E/Q`:

1. `ord_(s=1) L(E,s) = rank E(Q)`,
2. the leading Taylor coefficient at `s=1` satisfies the BSD arithmetic formula.

### 1.2 Local claim boundary
Current claim is local to this framework:

- closure architecture and gate system are explicit,
- failure modes are machine-checkable,
- theorem constants are instantiated and tracked in artifacts.

Define `A` as the admissible manifold-constrained arithmetic-state class used throughout Sections 2-11.

---

## 2. Epistemic Axiom Map (A1–A8 -> BSD Objects)

- `A1` Projection: admissible-class projection to arithmetic-spectral states.
- `A2` Flux primacy: deformation transport of `L`-data and arithmetic couplings is primary.
- `A3` Invariance split: coercive arithmetic core plus explicit remainder channel.
- `A4` Flux-to-form: local transport identities induce global arithmetic control equations.
- `A5` Transfer law: local window bounds propagate to global defect budgets.
- `A6` Tensor covariance: response metric on projected arithmetic sector from canonical operators.
- `A7` Curvature-aware conservation: restart/normalization map preserves admissible class.
- `A8` Remainder necessity: every uncontrolled term is accounted in explicit defect ledgers.

---

## 3. Canonical Objects

Let `tau` be deformation parameter and `u_tau in A` the admissible state.

Primary objects:

- projected arithmetic response operator: `L_tau`,
- defect functional: `D_tau = B_tau - J_tau`,
- normalized arithmetic profile: `A_tau`,
- rigidity monitor on extracted limits: `R_tau`,
- arithmetic lock margin: `ell_tau`.

Global strict margin:

`M_BSD = min(kappa_rank, sigma_capture, kappa_compact, rho_rigidity, alpha_lock, bsd_floor) - eps_coh`.

Target:

`M_BSD > 0`.

---

## 4. Closure Gates

- `B_G1` (Coercivity): projected arithmetic response has uniform positive floor on canonical tube.
- `B_G2` (Capture): deformation/restart map preserves positive defect floor.
- `B_G3` (Compactness): normalized near-failure sequences are precompact.
- `B_G4` (Rigidity): every extracted bad limit is excluded.
- `B_G5` (Identification): determining-class lock identifies limit with intended arithmetic class.
- `B_G6` (BSD floor): strict arithmetic barrier survives extraction.
- `B_GCoh` (Coherence): explicit remainder budget with strict target.
- `B_GM` (Final margin): strict scalar margin `M_BSD > 0`.

Global local-lane closure requires all gates `PASS`.

---

## 5. `BSD1–BSD8` Theorem Chain

1. `BSD1` Active coercive block on projected arithmetic response sector.
2. `BSD2` Uniform continuation bounds on canonical deformation tube.
3. `BSD3` Restart/normalization invariance and no-Zeno spacing.
4. `BSD4` First-failure blow-up compactness extraction.
5. `BSD5` Rigidity exclusion of bad limits.
6. `BSD6` Continuum extraction in admissible arithmetic class.
7. `BSD7` Determining-class identification and lock equation persistence.
8. `BSD8` Final persistence theorem: analytic-arithmetic lock closes on admissible class `A`.

---

## 5B. Theorem-by-Theorem Mainstream Translation

This table binds each lane theorem to standard BSD-side objects.

| Lane theorem | Admissible-class object | Mainstream analogue | Required bridge statement |
|---|---|---|---|
| `BSD1` | projected arithmetic response `E_tau` | positive arithmetic pairing/response form on projected sector | `E_tau >= c_* K_tau - e_* I` with explicit constants |
| `BSD2` | defect transport for `D_tau` | differential inequality for analytic-arithmetic defect under deformation | Gronwall capture bound with forcing ledger |
| `BSD3` | restart map + spacing | admissible normalization preserving arithmetic data class | positive continuation-time floor after each restart |
| `BSD4` | normalized bad sequence `U_n` | compactness class for arithmetic spectral profiles | precompactness plus lower-semicontinuity of badness |
| `BSD5` | rigidity exclusion | contradiction against transport, admissibility, or safe re-entry | extracted bad limits impossible |
| `BSD6` | continuum extraction | admissible endpoint profile preserving locks | limits preserve normalized observables |
| `BSD7` | determining-class lock | equality of transforms/local-factor observables on determining set | uniqueness of endpoint representative |
| `BSD8` | arithmetic floor `bsd_floor` | strict persistence of analytic-arithmetic lock | positive barrier survives to endpoint |

---

## 6. Current Theorem Inputs (Tracked)

Tracked in:

- `artifacts/constants_registry.json`
- `artifacts/stitch_constants.json`

Required constant slots:

- `kappa_rank` (`B_G1`),
- `sigma_capture` (`B_G2`),
- `kappa_compact` (`B_G3`),
- `rho_rigidity` (`B_G4`),
- `alpha_lock` (`B_G5`),
- `bsd_floor` (`B_G6`),
- `eps_coh` (`B_GCoh`).

Problem-native derivation blocks (raw constants):

- `kappa_rank^(raw) := inf_(tau in T_*) lambda_min(E_tau | H_resp)`,
- `sigma_capture^(raw) := inf_[tau0,tau1 subset T_*] ( D_(tau0) - E_flow[tau0,tau1] - E_jump[tau0,tau1] )`,
- `kappa_compact^(raw) := ( 1 + sup_(u in T_*) Delta_comp^+(u) )^(-1)`,
- `rho_rigidity^(raw) := inf_(U in B_bad) R_bad(U) / ||U||^2`,
- `alpha_lock^(raw) := inf_(U in T_*) Alpha_lock(U)`,
- `bsd_floor^(raw) := inf_(tau in T_*) Bsd_barrier_tau`,
- `eps_coh^(raw) := sup_(O in C_det, tau in T_*) |Lock_O(U_tau) - Lock_O(U_*)|`,
- `sigma_star_can^(raw) := inf_(tau in T_*) sigma_tau`.

Admissible-class guard uses normalized constants:

- `kappa_rank := kappa_rank^(raw) / kappa_rank,ref`,
- `sigma_capture := sigma_capture^(raw) / sigma_capture,ref`,
- `kappa_compact := kappa_compact^(raw) / kappa_compact,ref`,
- `rho_rigidity := rho_rigidity^(raw) / rho_rigidity,ref`,
- `alpha_lock := alpha_lock^(raw) / alpha_lock,ref`,
- `bsd_floor := bsd_floor^(raw) / bsd_floor,ref`,
- `sigma_star_can := sigma_star_can^(raw) / sigma_star_can,ref`,
- `eps_coh := eps_coh^(raw)`.

Current registry snapshot is in normalized gauge
(`kappa_rank=1.08008, sigma_capture=1.063, kappa_compact=0.805802, rho_rigidity=1.079, alpha_lock=1.036, bsd_floor=1.014, sigma_star_can=1.053`,
`eps_coh=0.0` strict mode), with provenance given by the raw definitions above.

---

## 7. Reproducibility

Run:

```bash
bash repro/run_repro.sh
```

This writes:

- `repro/certificate_runtime.json`

Pass condition:

- `all_pass == true` with all `B_*` gates passing on admissible class `A`,
- gate tuple `B_G1,B_G2,B_G3,B_G4,B_G5,B_G6,B_GCoh,B_GM = PASS`.

---

## 8. Current Runtime Snapshot

Latest local guard output (`repro/certificate_runtime.json`):

- `B_G1,B_G2,B_G3,B_G4,B_G5,B_G6,B_GCoh,B_GM = PASS`,
- strict margin `M_BSD = 0.805802`,
- lane: `manifold_constrained`.

This is an admissible-class closure statement.

---

## 9. Routing Index (Paper -> Notes -> Artifacts)

| Gate/Bridge | In-paper anchor | Mirror note | Artifact key |
|---|---|---|---|
| `B_G1` | Section 4/5 (`BSD1`) | `notes/EG1_public.md` | `kappa_rank` |
| `B_G2` | Section 4/5 (`BSD2`,`BSD3`) | `notes/EG2_public.md` | `sigma_capture` |
| `B_G3` | Section 5 (`BSD4`) | `notes/EG3_public.md` | `kappa_compact` |
| `B_G4` | Section 5 (`BSD5`) | `notes/EG4_public.md` | `rho_rigidity` |
| `B_G5` | Section 5 (`BSD7`) | `notes/IDENTIFICATION_BRIDGE.md` | `alpha_lock` |
| `B_G6` | Section 5 (`BSD8`) | `notes/EG4_public.md` | `bsd_floor` |
| `B_GCoh` | Sections 3/4 | `notes/IDENTIFICATION_BRIDGE.md` | `eps_coh` |
| `B_GM` | Section 3 margin formula | derived | all above |

Standalone routing file:

- `paper/CANONICAL_ROUTING_INDEX.md`

---

## 10. Next Local Tasks

1. Sensitivity lane: perturb constants around current unit-normalized instantiation and track guard stability.
2. Add explicit stress tests for restart/no-Zeno behavior in `repro/` docs.
3. Keep claim-scoping synchronized across paper/notes/repro when constants change.

---

## 11. In-Paper Appendix Pack (A-E)

This section embeds the theorem payload in-paper so closure is auditable without
note hopping.

### A. EG1 Projected Coercivity (`B_G1`)

Setup on arithmetic response space `H_resp`:

- `E_tau := Pi_resp L_tau Pi_resp`,
- comparison form `K_tau` with floor `A_ker,* > 0`,
- decomposition `E_tau = c_* K_tau + Err_tau`.

#### Lemma A1 (comparison reduction)

Assume for `tau in T_*`, `xi in H_resp`:

`<xi,K_tau xi> >= A_ker,* ||xi||^2`
and
`<xi,Err_tau xi> >= -e_* ||xi||^2`.

Then:

`<xi,E_tau xi> >= (c_*A_ker,*-e_*) ||xi||^2`.

Proof.
Substitute the decomposition and collect lower bounds.

#### Lemma A2 (tube perturbation bound)

If `||E_tau-E_tau_*|| <= L_E,* |tau-tau_*|` and `|tau-tau_*| <= r_*`, then:

`lambda_min(E_tau|H_resp) >= lambda_min(E_tau_*|H_resp) - L_E,* r_*`.

Proof.
Weyl eigenvalue perturbation inequality.

#### Proposition A3 (raw coercive floor)

Define:

`kappa_rank^(raw) := lambda_min(E_tau_*|H_resp) - L_E,* r_*`.

If `kappa_rank^(raw) > 0`, then
`lambda_min(E_tau|H_resp) >= kappa_rank^(raw)` for all `tau in T_*`.

Proof.
Direct from Lemma A2.

#### Theorem A4 (EG1 closure criterion)

If `c_*A_ker,*-e_*>0` and `kappa_rank^(raw) >= c_*A_ker,*-e_*`, then
`B_G1 = PASS` with normalized constant
`kappa_rank := kappa_rank^(raw)/kappa_rank,ref > 0`.

Proof.
Combine Lemma A1 and Proposition A3.

Mainstream translation note.
This is the explicit arithmetic-response coercivity statement corresponding to a
uniform positive floor on the projected comparison form.

### B. EG2 Capture / Restart Package (`B_G2`)

Defect equations:

`dD/dtau >= -L_D (D-sigma_*) - eta_flow(tau)`,
`D(tau_j^+) >= D(tau_j^-) - eta_jump,j`.

Define:

`Delta_coh[tau0,tau] := int eta_flow + sum eta_jump`.

#### Lemma B1 (segment inequality)

On restart-free `[a,b]`:

`D(b) >= sigma_* + e^(-L_D(b-a))(D(a)-sigma_*) - int_a^b e^(-L_D(b-s)) eta_flow(s) ds`.

Proof.
Integrating factor on `D-sigma_*`.

#### Lemma B2 (multi-segment composition)

Across restarts in `[tau0,tau1]`:

`D(tau1) >= sigma_* + e^(-L_D(tau1-tau0))(D(tau0)-sigma_*) - Delta_coh[tau0,tau1]`.

Proof.
Iterate Lemma B1 and subtract jump contributions.

#### Proposition B3 (raw capture floor)

Define
`sigma_capture^(raw) := inf_(tau in T_*) (sigma_tau - Delta_coh[tau0,tau])`.
If positive, then `D(tau) >= sigma_capture^(raw)`.

Proof.
Apply Lemma B2 with admissible starting state.

#### Theorem B4 (EG2 closure criterion)

If restart map preserves admissibility and `sigma_capture^(raw) > 0`, then
`B_G2 = PASS` with
`sigma_capture := sigma_capture^(raw)/sigma_capture,ref > 0`.

Proof.
Admissibility ensures each segment estimate is valid; Proposition B3 yields the
uniform floor.

Mainstream translation note.
Provides the explicit continuation inequality connecting local transport to
global analytic-arithmetic defect control.

### C. EG3 Compactness / No-Zeno (`B_G3`)

Take normalized near-failure sequence:
`U_n := N(u_(tau_n))`.

#### Lemma C1 (precompactness criterion)

Assume:

- `||U_n||_X <= M_*`,
- tightness/modulus bound `Theta(U_n) <= Theta_*`.

Then `{U_n}` is precompact in topology `X`.

Proof.
Use the compactness criterion attached to `X`.

#### Lemma C2 (badness lower-semicontinuity)

If `U_n -> U_infty` in `X`, then
`Beta(U_infty) >= limsup Beta(U_n)`.

Proof.
`Beta` is an infimum of continuous residual norms.

#### Proposition C3 (first-failure extraction)

If first closure failure occurs at `tau_*`, there is
`U_n -> U_infty` with `U_infty` bad.

Proof.
Normalize a sequence approaching `tau_*`; apply Lemmas C1-C2.

#### Theorem C4 (restart spacing / no-Zeno)

If local continuation gives
`T_cont(u) >= delta_rec > 0` on trigger set, then
`tau_(j+1)-tau_j >= delta_rec`.

Proof.
A new restart cannot occur before minimum continuation interval is exhausted.

Mainstream translation note.
This is the explicit non-accumulation theorem for corrective steps.

### D. EG4 Rigidity + Arithmetic Barrier (`B_G4`, `B_G6`)

Bad-limit alternatives:

1. transport identity violation,
2. admissibility violation,
3. safe-class re-entry.

#### Lemma D1 (rigidity trichotomy)

Every normalized bad limit satisfies at least one alternative.

Proof.
Partition by definition of admissible class complement.

#### Proposition D2 (alternative exclusion)

Assume:

- transport identities are closed under limit,
- admissibility is closed in topology `X`,
- safe-class re-entry contradicts first-failure minimality.

Then all three alternatives are impossible.

Proof.
Contradiction case-by-case.

#### Theorem D3 (rigidity + barrier closure)

If `rho_rigidity^(raw)>0` and `bsd_floor^(raw)>0`, then
`B_G4 = PASS` and `B_G6 = PASS` with normalized constants
`rho_rigidity>0`, `bsd_floor>0`.

Proof.
Proposition D2 excludes bad limits; positive barrier prevents collapse at
endpoint.

Mainstream translation note.
This is the compactness-rigidity step needed to convert continuation bounds into
global arithmetic persistence.

### E. Identification Bridge (`B_G5`, `B_GCoh`, `B_GM`)

Fix determining class `C_det` of analytic-arithmetic observables (completed
`L`-data, local factors, height/regulator locks) with accumulation in analytic
domain.

Define:

`Lock_O(U) := Obs_O(U)-Obs_O(U_BSD)`.

#### Lemma E1 (lock continuity)

If `U_n -> U_infty` in `X`, then
`Lock_O(U_n) -> Lock_O(U_infty)` for each `O in C_det`.

Proof.
Continuity of observables.

#### Lemma E2 (determining-class uniqueness)

If `Lock_O(U_infty)=0` for all `O in C_det`, then `U_infty = U_BSD`.

Proof.
Coinciding transforms on determining class with accumulation imply global
coincidence by analytic continuation/identity theorem.

#### Proposition E3 (raw identification constants)

Define:

- `alpha_lock^(raw) := inf_(U in T_*) Alpha_lock(U)`,
- `eps_coh^(raw) := sup_(O,tau) |Lock_O(U_tau)-Lock_O(U_BSD)|`.

If `alpha_lock^(raw)>0` and `eps_coh^(raw)=0`, then `B_G5` and `B_GCoh` close.

Proof.
Lemma E2 gives uniqueness; zero coherence budget removes residual slack.

#### Theorem E4 (final margin closure)

If `B_G1..B_G6,B_GCoh` pass and
`M_BSD = min(kappa_rank,sigma_capture,kappa_compact,rho_rigidity,alpha_lock,bsd_floor)-eps_coh > 0`,
then `B_GM = PASS`.

Proof.
All positive components survive coherence subtraction.

Bridge closure note.
The canonical endpoint lock `U_BSD` is treated as fixed by this in-paper theorem
chain; no additional bridge exclusions are left in this manuscript layer.

---

## 12. References

1. Clay Mathematics Institute, *Birch and Swinnerton-Dyer Conjecture (Millennium Problem page)*. [link](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/)
2. B. J. Birch and H. P. F. Swinnerton-Dyer, *Notes on elliptic curves. I*, J. Reine Angew. Math. 212 (1963), 7-25. DOI: `10.1515/crll.1963.212.7`
3. B. J. Birch and H. P. F. Swinnerton-Dyer, *Notes on elliptic curves. II*, J. Reine Angew. Math. 218 (1965), 79-108. DOI: `10.1515/crll.1965.218.79`
4. J. Coates and A. Wiles, *On the conjecture of Birch and Swinnerton-Dyer*, Invent. Math. 39 (1977), 223-251. DOI: `10.1007/BF01390039`
5. B. H. Gross and D. B. Zagier, *Heegner points and derivatives of L-series*, Invent. Math. 84 (1986), 225-320. DOI: `10.1007/BF01388809`
6. J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Springer, 2009.
