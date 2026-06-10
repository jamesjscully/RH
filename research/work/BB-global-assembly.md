# BB - PFD step 2: the global assembly, with the product formula spent; first gate = the archimedean constant

Status: fresh-context worker BB, 2026-06-10. Doc 28 step 2 (the global
assembly demand). Required reading executed in order: doc 28, doc 29,
Z-u2-gluing.md IN FULL, AA-cc-thh-probe.md IN FULL, docs 19/20
(corrected), docs 24/25 (odd-p fold data, degenerate sector), doc 21
(Q-SCHEME). Inherited witnesses rerun by me before any new work:
prime_int_z_u2_glue.py ALL PASS (exit 0), prime_cc_thh_norm_filtration
ALL PASS (exit 0).

Witness (NEW): scripts/numerics/witness/prime_int_bb_global_assembly.py
(gates GB1-GB5, pre-registered fail-closed readings below and in the
docstring, exit-code gated).

Sections 1-2 (registrations + the assembly's definition) were written
BEFORE the witness was first run; the verdict sections after.

## 1. PRE-REGISTERED READINGS (before running)

The gate (doc 28 step 2 / doc 29 continuation 1): does the explicit
formula's archimedean constant -(1/2) log pi - equivalently the 1/(2pi)
scale of doc 20 C2 - EMERGE from the cross-place trace of the assembled
PFD object? Pre-registered branch readings: B1 (it emerges - K1
discharged globally), B2 (a different constant emerges - report exactly,
apply doc-21 Q-SCHEME bookkeeping before judging), B3 (no constant is
determined - the assembly is still scale-free; then name exactly the
missing ingredient). FAIL-CLOSED: B3 with the exact missing ingredient
is full-value.

EXPECTED READING, fixed in advance: B3, in the following sharp form.
Every banked gluing input is invariant under rescaling kappa -> lambda
kappa of the degenerate sector's regularization unit (the G_p are
exactly scale-free by Z's K1 mechanism; the glued traces are lattice
combs containing no kappa; the product formula log N = sum_p v_p log p
is an identity among weights containing no kappa; the residue pairings
are exact/F_2-level, kappa-free). Hence NO function of the banked
inputs can determine kappa: the gate observable c_oo(kappa) =
-(1/2) log kappa (the constant multiplying the degenerate sector in the
critical-line density) is not a function of the assembly. The missing
ingredient, named in advance: the ARCHIMEDEAN POISSON EXCHANGE - the
comb <-> continuum duality at the infinite place (equivalently: a
self-dual archimedean unit/test object), i.e. exactly the properness
theorem of doc 19 sec 5, now localized to the degenerate-sector
coupling.

Two registered sub-findings to test (both would sharpen B3 to
full-value):

```text
BB-r1 (FE-layer blindness): the FE-paired degenerate sector has
      CONSTANT total anomalous dimension: zeta_H(0, s/2) +
      zeta_H(0, (1-s)/2) = 1/2 exactly (from zeta_H(0,a) = 1/2 - a).
      Hence kappa enters the s <-> 1-s SYMMETRIC global determinant
      only as the s-independent constant kappa^{-1/2}: the functional
      equation of the assembly holds for EVERY kappa. Consequence: a
      properness theorem that only reproduces the FE cannot determine
      the constant (doc 21 sec 4's vacuity guard, instantiated
      quantitatively); the constant is a DENSITY/index-layer datum.
      FAIL: the paired anomaly is s-dependent, or the FE ratio
      depends on kappa.
BB-r2 (the constant is present but uncoupled): each finite place's
      glued trace is the lattice comb with atom weight = atom spacing
      = 2 pi / log p (in t-units): the Abel-limit of the two-sided
      geometric series IS the Poisson exchange at the finite place -
      duality works there (K2), and the 2 pi is carried by the banked
      vertical periodicity. The per-place scale-free observable
      weight/spacing = 1 exactly, so the 2 pi cannot be extracted by
      any one-place observable; extraction requires comparing comb
      mass against a CONTINUUM density - the archimedean Poisson
      exchange again. FAIL: comb weight != spacing, or the comb
      identity fails numerically.
```

COMPARISON-ONLY check, registered with its F-a flag: with kappa = pi
(real-place/spacing-2 units) the gate observable equals the EF's
-(1/2) log pi exactly, and via Legendre duplication this is the same
datum as scale 2 pi on the spacing-1 (complex/unfolded) ladder
(Deninger Prop 2.1 line 2; doc 25's Gamma_C degeneration at p = 2);
the 2-power discrepancies are EF-invisible (doc 20 C3). This determines
what the missing theorem must OUTPUT; it is not an internal derivation
(doc 14 fork discipline: EF as comparison only).

Evaluation rules fixed in advance: flint (prec 333) Hurwitz/Lerch
pipeline reused unchanged from prime_int_deninger_convention.py
(zeta_H(0,a) = 1/2 - a; reg_half(a, kappa) = kappa^{-zeta_H(0,a)}
exp(-zeta_H'(0,a))); exact rational arithmetic for the glued-trace
identity; integer-exact factorization for the product formula;
tolerances per gate in the witness docstring. No RH/zero-side input
anywhere in the assembly; the EF constant appears only in the
comparison gate GB4, flagged.

## 2. THE ASSEMBLY, DEFINED PRECISELY (with the assumption ledger)

### 2.1 Local glued objects G_p

p = 2 (CONSTRUCTED, Z-doc): G_2 = D cup_Lin D', D = pi_*
THR(F_2)^{tC_2} = F_2[[z]][t^{+-1}] (Theorem S.1), D' its Matlis /
divided-power dual, residue pairing perfect, duality (j, m) ->
(1-j, -m); determinant layer scheme-FORCED c = 1/2 (ZG4); vertical
lattice spacing pi i / log 2 (t-lattice, N2 forced); glued trace =
lattice-delta at 2^{-s} = 1 (ZG5); anomalous dimension 0 (exactly
scale-free).

odd p (STATED from doc 24's data; gluing transfer ASSUMED): the fold
is theorem-grade (DMPR Cor 5.19: pi_* THR(F_p)^{C_2} = F_p[y], |y| = 4;
reflection-Tate contractible, Quigley-Shah) and the rotation/parametrized
Tate keeps the full two-sided ladder (Z_p[w^{+-1}], anomalous dimension
0, doc 24 r2). G_p := the two-sided weight lattice per degree obtained
by gluing the THH(F_p) half-ladder supply (weights >= 1, log-cardinality
log p per step, doc 19 L1) to its Matlis dual over the weight-0 line,
with the perfect residue pairing implementing m <-> -m and the
negation-forced c = 1/2 determinant layer: per weight w the factor
2 sinh(w log p / 2) = p^{w/2}(1 - p^{-w}); vertical spacing
2 pi i / log p; glued trace = lattice comb at p^{-s} = 1. ASSUMED,
flagged: (a) the Matlis gluing (Z's ZG1-ZG3) transfers verbatim to the
odd-p carrier - structurally SIMPLER than p = 2 (doc 25's anomaly
factorization is empty at odd p: no Euler tower F_2[y], no Gamma_C
doubling, clean fold), but NOT re-executed here; (b) O's Thm A1 forcing
of c = 1/2 transfers (A1 itself is prime-independent; the existence of
the glued duality at odd p is the assumed part); (c) the doc-19/20
dictionary (degree <-> vertical lattice, weight n <-> p^{-ns} supply)
is spent as at p = 2. Odd-p instances are therefore ASSUMED-STRUCTURAL
grade pending doc 28 step 2's odd-p execution.

### 2.2 Degenerate sector at unknown scale kappa

(V_oo, Theta_oo): the half-ladder {nu + s/2 : nu >= 0} (spacing 2 in s,
start 0; docs 20/24), regularized at scale kappa > 0:

    D_oo,kappa(s) := prod_reg_{nu>=0} ((nu + s/2)/kappa)
                   = kappa^{-(1-s)/2} sqrt(2pi) / Gamma(s/2),

anomalous dimension zeta_H(0, s/2) = (1-s)/2 != 0: the value is
scale-DEPENDENT - kappa is real data the assembly must supply (doc 20
C2). The rank-2 Barnes Gamma_2 tower and the Gamma_C degeneration at
p = 2 (doc 25) are carried along but EXCLUDED from this gate (K3 is
untested; their anomalies are also nonconstant, so the kappa question
includes them a fortiori).

### 2.3 The gluing datum and the global object

The product formula AS AN IDENTITY (AA Theorem AA.1, zero free
choices): on the character lattice Z[Z\0], for every monoid class [A],

    w_oo([A]) = log N([A]) = log|A| = sum_p v_p(A) log p
              = sum_p w_p([A])     (exact; A <= 20000 witnessed),

i.e. the archimedean MAX face and the p-adic MIN faces of the SAME
classes are identified - this is the identification ι spent as the
cross-place gluing (Z's ledger L6, now spent).

    D_glob := ( {G_p}_p prime, (V_oo, Theta_oo)_kappa ; ι ).

GLOBAL TRACE (distribution on the critical vertical line, t-units):

    T_kappa(t) = sum_p (2pi/log p) sum_{n in Z} delta(t - 2pi n/log p)
                 (+) rho_kappa(t),
    rho_kappa(t) = -(1/2) log kappa + (1/2) Re psi(1/4 + it/2)
                 ( = -d/ds log D_oo,kappa on s = 1/2 + it ).

GLOBAL DETERMINANT (rank sector excluded as in docs 19/20):

    Xi_kappa(s) = [ (x)_p per-weight p^{w/2}(1 - p^{-w}) layers ]
                  (x) D_oo,kappa(s) D_oo,kappa(1-s).

GATE OBSERVABLE: c_oo(kappa) = -(1/2) log kappa, the constant
multiplying the degenerate sector in rho_kappa. B1 = the assembly
forces kappa = pi (so c_oo = -(1/2) log pi); B2 = it forces some other
kappa; B3 = kappa undetermined.

## 3. VERDICT: B3, AS REGISTERED - WITH BOTH SHARPENINGS PROVED
## [GB1-GB5 ALL PASS]

Witness ALL PASS (GB1-GB5, exit 0) on the FIRST run, after sections 1-2
were written; no gate predicate amended at any point. (Discipline
record: this section's numeric tolerances were drafted as expectations
and corrected to the MEASURED values after the run; every gate verdict
and every claim is unchanged from the registration.)

(i) SCALE-BLINDNESS IS EXACT (GB2; Proposition BB.1). Every banked
input of D_glob is invariant under R_lambda: kappa -> lambda kappa:
the full-ladder anomaly is 0 (|zeta_full(0)| = 0.0 at flint precision,
all (p, s) tested); the glued trace identity 1/(1-x) + 1/(1-1/x) - 1
= 0 holds in EXACT rational arithmetic; the product formula is
integer-exact (prod_p p^{v_p} = A recomposed for all A <= 20000,
log identity to 1.8e-15) and contains only {log p}; the residue
pairings are F_2-exact. Meanwhile the gate observable transforms:
D_oo,lambda kappa / D_oo,kappa = lambda^{-(1-s)/2} (witnessed
5.9e-16). An observable that moves under a
group fixing every input is not a function of the inputs: NO CONSTANT
IS DETERMINED. B3.

(ii) THE FE LAYER IS kappa-BLIND (GB3; reading BB-r1 confirmed). The
paired anomaly zeta_H(0, s/2) + zeta_H(0, (1-s)/2) = 1/2 exactly
(witnessed 0.0 at flint precision, complex grid), so kappa enters
Xi_kappa's FE-paired archimedean factor only as the s-INDEPENDENT
constant kappa^{-1/2} (ratio constant in s to 5.6e-16): the functional
equation of the
assembly holds FOR EVERY kappa. Quantitative instantiation of doc 21
sec 4's standing guard: a global duality that only reproduces the FE
is structurally INCAPABLE of producing the archimedean constant. The
constant lives one layer deeper - the critical-line DENSITY (index /
zero-counting) layer, where -(1/2) log kappa is visible (GB4).

(iii) THE CONSTANT IS PRESENT BUT UNCOUPLED (GB1, GB5; reading BB-r2
confirmed). The glued trace of each G_p, Abel-regularized from the two
branches, IS the lattice comb: pairing against Gaussian test functions
converges to (2pi/log p) sum_n phi(2pi n/log p) (rel err < 7.7e-7 at
eps = 1e-6, monotone in eps; p = 2, 3, 5) - this convergence is
EXACTLY Poisson summation on (log p)Z <-> (2pi/log p)Z: the comb <->
test-function exchange WORKS at finite places (it is what K2's
compactification bought). The atom weight EQUALS the spacing
(weight x log p / 2pi = 1 to 1.6e-7): per-place observables are
scale-free, so the 2pi carried by the banked vertical periodicity
cannot be extracted at one place - only a comb-vs-CONTINUUM comparison
can read it off, and the only continuum in D_glob is the degenerate
sector.

THE MISSING INGREDIENT, EXACTLY (the full-value B3 deliverable): the
ARCHIMEDEAN POISSON EXCHANGE - a theorem-grade duality at the infinite
place exchanging the finite-place combs with the degenerate sector's
continuum density, equivalently supplying the self-dual archimedean
unit (the role e^{-pi x^2} plays in vdGS/Tate, witness P1 of
prime_int_thh_supply.py). The product formula CANNOT do this job: it
is a filtration-layer identity (weights, values in the Q-span of
{log p}), while kappa is a determinant-layer scheme/scale datum
(doc 21's quadruple) visible only through the nonzero anomaly
(1-s)/2; at finite places the filtration -> determinant crossing is
done by the negation duality (c = 1/2 forced), but at oo negation
fails on the half-ladder (that failure IS the nonzero anomaly), so
nothing banked crosses the layers there. Properness = Poisson at oo,
now localized: it is precisely the DEGENERATE-SECTOR COUPLING, and by
(ii) it must be demanded at the density layer, not the FE layer.

(iv) COMPARISON ONLY (GB4, F-a-flagged): the kappa-parametrized
density -d/ds log D_oo,kappa(1/2 + it) = -(1/2) log kappa +
(1/2) psi(1/4 + it/2) (witnessed 1.6e-9, kappa in {1, e, pi, 2pi});
the classical EF shadow selects kappa* = pi uniquely (monotone solve,
exact to machine precision). Q-SCHEME bookkeeping: pi on the spacing-2
(real, folded) ladder = 2pi on the spacing-1 (complex, unfolded) ladder
(Deninger Prop 2.1 line 2 re-witnessed: prod_reg((nu+z)/2pi) =
Gamma_C(z)^{-1}, 1.5e-15; classical duplication Gamma_R(s)Gamma_R(s+1)
= 2 Gamma_C(s), 5.8e-16; 2-powers EF-invisible per doc 20 C3). So the
missing theorem's required output is, in either normalization, THE
COMB NORMALIZATION ITSELF: 2pi per lattice cell - the same 2pi the
finite-place combs already carry. The B1 target is well-posed and the
assembly is exactly ONE theorem short of it.

## 4. WHAT THE GLOBAL TRACE ALREADY IS (no kappa needed)

The assembled prime side sum_p (2pi/log p) sum_n delta(t - 2pi n/log p)
is the shape of the EF's prime side at the |x| = 1 shell (sigma = 0
reading); the c = 1/2-forced determinant layer shifts the reading to
the critical line: -d/ds log[2 sinh(s log p/2)] = -(log p)/2 -
log p sum_{k>=1} p^{-ks}, whose atom part assembles over p to the
Lambda(n)-supply (doc 19 L2-L3, banked). So D_glob's trace/determinant
layer reproduces, from banked counts alone: the prime atoms with
KMS-1/2 weights (scheme forced per place), the lattice-delta combs
(Poisson at finite places), and the degenerate sector's digamma shape -
everything in the EF supply EXCEPT the one number -(1/2) log kappa and
the rank/pole sector (K3/K4, owed). The gate has isolated the entire
remaining archimedean content of step 2 into one coupling constant.

## 5. G-INT6 LEDGER

```text
input                          choices spent
G_2                            0 new (Z's construction, ledger inherited)
G_p odd                        the TRANSFER ASSUMPTION (sec 2.1 a-c):
                               structural, flagged, demotes odd-p to
                               assumed-structural; no numeric choice
degenerate sector              0 new (docs 20/24/25 banked ladders);
                               kappa is the UNKNOWN, not a choice
gluing ι                       0 (Theorem AA.1, exact)
GB1/GB5 test functions         Gaussians: an EXHIBITION device for a
                               distributional identity (Abel limit of
                               geometric series = classical Fourier
                               analysis); no zeta input
GB4 comparison constant        the EF's -(1/2) log pi: COMPARISON ONLY,
                               F-a-flagged; determines the target, not
                               the verdict
```

Verdict B3 rests only on rows 1-4 (exact identities + the equivariance
argument); it survives even if GB1/GB4's numerics were discarded.

## 6. HONEST LIMITS

- Proposition BB.1 is a no-go about THIS object's banked inputs: it
  proves the assembly AS POSED determines no kappa; it does not prove
  that no enrichment of D_glob (e.g. a spectrum-level realization with
  genuine O(2)-structure, C5''') carries the scale. That is exactly
  what it should not prove - the missing theorem is the program's
  properness target, not a refuted hope.
- Odd-p G_p is assumed-structural (sec 2.1); the verdict does not
  depend on it (B3 already follows with G_2 alone plus the product
  formula), but the global trace's comb-sum shape does.
- The rank/pole sector (s(s-1), Barnes Gamma_2 rank-2) is excluded;
  K3/K4 remain owed (doc 29). If the rank sector turns out to carry
  its own scale coupling, the gate must be rerun with it included.
- The distributional comb identity is exhibited against Gaussian test
  functions (three places, one width per gate); it is classical
  Fourier analysis, not a new theorem.
- No RH/zero-side input; the EF appears only in GB4, comparison-only,
  flagged. The vdGS theta FE (P1) is cited as the classical shadow of
  the missing theorem, not used in the assembly.

## 7. HAND-OFF (for the lead)

```text
ASSEMBLY:   D_glob defined (sec 2.3): all G_p + degenerate sector at
            unknown scale kappa, product formula SPENT as the
            identification (AA.1); global trace = comb sum (+) smooth
            degenerate density; determinant = forced-scheme Euler
            layers (x) FE-paired degenerate sector.
GATE:       B3, as pre-registered, full-value: NO constant emerges -
            and provably none CAN from the banked inputs
            (Prop BB.1, equivariance under kappa-rescaling; all
            inputs exactly scale-free).
SHARPENING: (1) the FE layer is kappa-blind (paired anomaly = 1/2
            const): properness-as-FE is structurally vacuous for the
            constant - demand it at the DENSITY layer (doc 21 sec 4,
            now quantitative). (2) the 2pi is already IN the object
            (comb weight = spacing = 2pi/log p; Poisson works at
            finite places); the missing ingredient is exactly the
            archimedean Poisson exchange = the self-dual unit = the
            degenerate-sector coupling. Target (comparison-only):
            kappa = pi (folded) = 2pi (unfolded), 2-powers invisible.
NEXT:       pose the archimedean exchange as the step-3 demand: a
            duality on D_glob pairing the comb sector with the
            degenerate continuum, normalized by the object (candidate
            carriers: the rank-2 Barnes sector (K3), the spectrum-
            level O(2) realization (C5''')); plus execute the odd-p
            gluings to discharge the transfer assumption.
```
