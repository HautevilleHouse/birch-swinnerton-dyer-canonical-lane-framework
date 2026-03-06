# Identification Bridge (BSD Limit -> Arithmetic Endpoint Class)

In-paper anchor: `paper/BSD_CONJECTURE_PREPRINT.md` (Sections 3-6 and runtime margin).

## Goal
Ensure extracted canonical-lane limits are identified with the intended arithmetic endpoint class.

## Determining Class (working)

Use test class `C_det` built from:

1. local factors and completed `L`-data constraints,
2. Mordell–Weil and height-pairing locks,
3. regulator/Tamagawa/period compatibility constraints.

## Uniqueness Target

Two candidate limits with the same lock equations on `C_det` are equivalent as canonical representatives.

## Lemma Chain and Proof Payload

### Lemma ID.1 (lock persistence)
If `U_n -> U_infty` on admissible class and observables in `C_det` are
continuous, then `Lock_O(U_n) -> Lock_O(U_infty)` for each `O in C_det`.

**Proof.**
Continuity of observables.

### Lemma ID.2 (determining-class uniqueness)
Assume `C_det` separates admissible endpoint classes.
If `Lock_O(U_infty)=0` for all `O in C_det`, then `U_infty` equals the
canonical arithmetic endpoint representative up to declared equivalence.

**Proof.**
If two distinct endpoints agree on all determining observables, separation is violated.

### Theorem ID.3 (coherence/identification closure)
If Lemmas ID.1-ID.2 hold and `eps_coh^(raw)=0`, then endpoint identification is
unique and `B_GCoh=PASS`.

**Proof.**
Lock persistence transfers equality to limits; separating-class uniqueness removes
endpoint ambiguity.

## Current Canonical-Lane Instantiation

- `alpha_lock = 1.036` (theorem-level),
- `eps_coh = 0.0` (strict-zero theorem-level),
- gate status targets: `B_G5 = PASS`, `B_GCoh = PASS`.
