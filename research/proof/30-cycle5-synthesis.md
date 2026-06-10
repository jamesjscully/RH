# 30 - Cycle-5 synthesis: the object exists, the duality does triple duty, and the remainder is one conjecture

Status: 2026-06-10. Synthesis of the PFD step-2 cycle (workers
BB/CC/DD, records in research/work/; all witnesses lead-rerun ALL
PASS; commits 870d8c7..2ec11c6). Follows docs 28-29.

## 1. Results

(DD) THE OBJECT EXISTS: Xbar = fib(X x X' -> Y) is an honest spectrum
with pi_* Xbar = G exactly (theorem mod Theorem S.1, zero free
choices); Z's forced D' IS the continuous Brown-Comenetz dual of the
THR Tate tower (theorem at filtered level). Plain BC self-duality is
unsatisfiable (Erdos-Kaplansky) - U.2 repaired to CONJECTURE DD.4:
continuous self-duality I^cont(Xbar) ~ Sigma Xbar (DGI complete/
torsion home; no real-cyclotomic BC/Anderson duality in print; nearest
theorem = C_2-equivariant Anderson self-duality). N1 reduced to three
gaps, minimal = a finite Borel computation; the three loose units
(N1's torsor, the tower's (1+z)^{-1} defect, Z's kappa nullity) are
ONE torsor.

(BB) K1 GATE = B3 WITH A PROOF (Prop BB.1, equivariance no-go): no
function of the banked inputs determines the scale - every input is
scale-invariant, the observable is not. The FE layer is kappa-BLIND
(exact identity): doc 21 sec 4's vacuity guard is now quantitative -
properness-as-FE can never produce the constant; the demand lives at
the density/index layer. The 2pi is IN the object (each G_p's
regularized trace IS the comb (2pi/log p) Sum delta, Poisson on
(log p)Z) but uncoupled. MISSING INGREDIENT NAMED: the archimedean
Poisson exchange - the comb <-> continuum duality whose classical
shadow is the Gaussian's self-duality in Tate's thesis; required
output kappa = pi (comparison-only).

(CC) CONSOLIDATION: the gluing is NOT 2-specific (executed p = 3, 5;
c = 1/2 forced; the structural deltas are absences; N2's t-lattice
forcing is 2-specific as expected). K3 PASS: the Barnes Gamma_2 sector
enters G via S's fix -> Tate map; the s(s-1) gate candidate is
witnessed - zeta_2(0, s+1 | 1, 2) = s(s-1)/4 - 1/24, SELF-DUAL under
s -> 1-s with the unique recentring equal to G's forced shift (the
1/4-vs-1/2 and -1/24 open). K4 PASS BY A THIRD MECHANISM: G's atoms
are exactly Q's pole-support set and each branch carries the pole -
but the K2 duality CANCELS the pole pair exactly (residue 0 to 1e-86).
Properness as pole-cancellation. The survivor is the lattice delta at
2^{-s} = 1 - precisely the cross-place attachment point.

## 2. The state of the program after five cycles

```text
The compactified object: EXISTS at spectrum level (Xbar, theorem mod
  S.1), instantiated at p = 2, 3, 5, with K2 (KMS-1/2 forced), K3
  (rank sector present, s(s-1)-shaped), K4 (pole cancelled by the
  duality), K5/K6 (carrier/DOF audits clean) all PASS.
The duality (Conjecture DD.4) does TRIPLE DUTY: restores negation
  (=> the scheme), cancels Q's pole (=> the integer layer), and is
  the unique candidate carrier of BB's Poisson exchange (=> the
  scale, and with it the EF's archimedean constant).
What remains is ONE mathematical object: the continuous self-duality
  of Xbar covering s -> -s - DD.4 - whose proof would simultaneously
  discharge the scheme question, K1, and the properness package at
  the instance level. Behind it, unchanged and explicitly guarded:
  the index/density layer where the zeros live (BB proved FE-level
  properness is structurally insufficient - the program cannot
  mistake DD.4 for RH-grade content; doc 21 sec 4 stands).
```

## 3. Ranked continuations

1. DD.4 ON THE LIN BLOCK (theorem-reachable: Greenlees-May duality is
   available exactly there; DD's restriction demand is stated) - then
   the finite Borel computation (N1's g2) against S.1's square.
2. BB's kappa-gate RERUN ON Xbar (the enrichment BB's no-go left
   open): does the spectrum-level continuous duality couple the comb
   to the continuum - i.e. is DD.4's I^cont the Poisson exchange?
3. The all-places assembly of the duality-cancellation mechanism (CC
   part 3's burden: does pole-cancellation survive globalization?).
4. The s(s-1) bookkeeping (1/4 vs 1/2, -1/24) under the Q-SCHEME
   dictionary.
Background: C6', cross-edge certificates, AHL verification debt.

## 4. Discipline ledger

BB: registrations before runs; numerics corrected to measured values
post-run with gates untouched. CC: one vacuous gate clause found on
self-review and STRENGTHENED (rerun PASS); design-stage hand
derivations disclosed. DD: registrations before first run, ALL PASS
first run; everything riding on S.1 stated. Zero fits; one
pre-registered dichotomy (K4) honestly amended by a mechanism neither
reading anticipated.
