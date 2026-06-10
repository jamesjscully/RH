# 21 - Fleet synthesis: the scheme question, the genus clash, the ku ladder, and T1 certified

Status: 2026-06-10. Synthesis of the four-front verified research fleet
(workers I/J/K/L in research/work/, each adversarially verified against
primary sources and independent re-runs; a completeness critic ran over
the verified set). Corrections propagated: doc 20 corrected in place
(C1-C3 + section 6), doc 18 scale note added, all worker-doc errata
applied. New witnesses: prime_int_ku_ladder.py,
prime_int_deninger_convention.py, prime_defect_t1_interval_certificate.py
(all ALL PASS / CERTIFIED).

## 1. What the fleet established

(I) THE KU LADDER (worker I, verifier re-derived independently). The
connective square ku ^ ku has diagonal THH(ku) (Lee arXiv:2206.02411,
table transcribed and archived). Its torsion obeys the exact closed form

    |T_2w| = lcm(1..w+1) / (w(w+1)),
    log|T_2w| = psi(w) + Lambda(w+1) - log w - log(w+1)

(psi = Chebyshev; three implementations + external replication, exact
integers to w <= 3000). The HZ square needed doc 19 to assemble the EF
supply place-by-place; the ku square's torsion carries the GLOBAL
Chebyshev function in single cardinalities - the fracture square
internalizes the sum over places. The free lattice F has denominators
lcm(1..k+2)/2 (von Mangoldt as divisibility). The Adams graph shadow is
Z/|k-l| per weight (trivially so - a definition-level pi_0 computation,
correctly read as shadow only). Sign: ALL ku-square torsion is
even-degree (motivic filtration 2, the H^2/surface slot) and pairs
POSITIVELY - opposite to HZ.

(J) THE SCHEME SEPARATION (worker J; the only outright refutation of a
rung record). Deninger 1992 Prop 2.3 - the identity Hesselholt's
theorem runs on - gives 1 - lambda q^{-s} on the SAME full ladder:
doc 20's p^{s/2} prefactor belongs to the conjugation-symmetric
regularization scheme alone, and Hesselholt's Theorem A selects the
prefactor-FREE scheme. KMS-1/2 is therefore STILL UNDERIVED: ladder =
homotopy-theoretic (at finite places), scheme = analytic layer with no
selecting theorem. New invariants: anomalous dimension 0 (full ladders)
vs (1-s)/2 (half-ladders) is a scale-invariant form of the place
dichotomy, and Deninger's 1/(2pi) scale anomaly is exactly the EF's
-(1/2) log pi supply term. The BMS triple (p-complete, phi-semilinear,
empty archimedean fracture corner) kills "TP of the square" as doc 20
sec 5 posed it; the replacement gate C5''-infty (J-doc sec 5) demands a
real-cyclotomic/O(2) object whose reflection C_2 BOTH supplies the
archimedean fixed-point ladder AND selects the symmetric scheme - the
scheme question and the archimedean question are the same question.

(K) THE CURVE-LEVEL EXISTENCE THEOREM (worker K). Connes-Consani have
PROVED an integer-valued Riemann-Roch with Pontryagin-Serre duality for
compactified Spec Z over their categorical base (arXiv:2205.01391
Thm 1.1-1.2; arXiv:2306.00456 Thm 1.1; circularity audit clean - no RH,
no zeros, no theta input; their 2026 Jacobian paper builds the Pic
infrastructure). The program's missing object EXISTS AT CURVE LEVEL as
a theorem. Demotions: BK/Ngo Poisson is PD-only and PD is CARRIER-BLIND
(classical Poisson holds for every lattice - Epstein passes - so a
functional-equation layer alone can never discriminate); monitor, not
vessel. Blumberg-Mandell spectral Tate-Poitou = the only existing
arithmetic duality over the sphere (etale side; diagnostic value).

(L) T1 CERTIFIED (worker L; rung R2 endpoint reached). H = S + G > 0
now holds by rigorous ball arithmetic (interval Cholesky on A_+, all 21
pivots; Sylvester h11 = [+3.610e-2 +/- 2.2e-5], det H = [+4.817e-3 +/-
5.4e-6]; T=1500 floor; starved run aborts fail-closed). Two soundness
bugs in the older Arb diagnostics found and fixed (Re inside an acb
integrand breaking holomorphy; endpoint rounding outside the balls).
Confirmation branch of the pre-registered asymmetric test: closes doc
08's "interval certificate pending"; adds nothing to the asymptotic
mechanism (R1's verdict stands).

## 2. The three tensions, collapsed to one question

```text
T-a  doc 20 refuted in part: KMS-1/2 is scheme, not ladder  (J)
T-b  genus clash: CC's proper Spec Z is genus-0 (deg K = -2 log 2 =
     -1.386 nats); doc 18's diagonal gives g = 1.459 (deg K = -zeta'(0)
     = +0.919 nats) - opposite SIDES of g = 1                (K)
T-c  sign flip: HZ-square torsion is odd-degree (pairs negative);
     ku-square torsion is even-degree (pairs positive); doc 18 called
     the negative sign load-bearing                          (I)
```

All three are the same disease: nobody has stated WHICH invariant each
construction computes, in which units, under which scheme. The genus
numbers cannot clash until both are shown to compute the same pairing;
the signs cannot contradict until the two squares' filtrations are put
in one indexing; doc 20's refutation happened exactly because a scheme
was silently attributed to a theorem. THE ONE QUESTION (pre-registered,
the rung's next gate):

```text
Q-SCHEME: for each square (HZ ^ HZ, ku ^ ku, CC's Spec Z bar), state the
computed invariant as (ladder data, weight dictionary, scale, scheme) and
verify the cross-dictionary consistency in common units. First gate:
the genus-probe witness (K's step A, sign-corrected): does CC's chi(D)
and doc 18's <Delta,Delta> refer to the same canonical class? Reading
(a) one dictionary error found -> fix and re-derive; (b) genuinely
different invariants -> the program must SAY which one it needs and why.
```

Partial answer already in hand (J, verified): doc 18's constant is
scheme-independent (positive-real half-ladder) but scale-dependent
(anomalous dimension -(s+1/2)); the scale note is now in doc 18. The
invariant content of "the torsion produces the archimedean place" is
the Gamma SHAPE + anomalous dimension, not the numerical constant.

## 3. New standing guard: G-INT6, the degrees-of-freedom audit

From the critic (unguarded failure mode: fitted-dictionary circularity).
Every ladder/dictionary claim must now ship with a DOF ledger:

```text
G-INT6: count the free modeling choices (weight grading, scale, scheme,
ladder start, spacing, place dictionary) against the independently
matched constraints (exact integer identities, shape matches that no
affine reparametrization can produce, cross-place consistency). A claim
with #constraints <= #choices is a FIT, not a derivation - record it as
calibration. Additionally, prefer negative controls WITH a carrier:
DH/Epstein die at the no-ring level, so they cannot catch a fitted
dictionary. Candidate ring-bearing control: THH of O_K for a number
ring (Lindenstrauss-Madsen): the ladder MUST produce the Dedekind
zeta_K supply (different different ideal, different discriminant), not
zeta's. If a dictionary maps O_K's ladder to zeta's supply, the
dictionary is fitting.
```

Scorecard of existing claims under G-INT6: doc 19's L1 (Lambda(p^i) =
log|THH_{2i}(F_p)|) and worker I's lcm ladder are exact integer
identities with zero free parameters once the ring is named - they pass.
Doc 19's archimedean dictionary spends the weight choice + scale; the
digamma SHAPE survives (affine-invariant), the constants are
calibration. Doc 20's W3 = ladder (derived) + scheme (spent choice).

## 4. The wall, restated after the fleet

Properness still = the global Poisson/duality step, but the map is now
concrete: CC have the integer H^0/H^1 and duality at CURVE level; the
program has the sign-bearing SQUARES; the FF index lives on the square.
Even in the proven char-p case (Hesselholt), properness is used only as
FINITENESS - the duality/index layer (PD/PR/PS) is never exercised and
the zeros are imported from Weil; and PD alone is carrier-blind. So the
kill-test the program must keep in front: a candidate S-level duality
must be shown to do more than reproduce the functional equation - the
scenario "S-level Poisson achieved and still vacuous for RH" has no
other guard.

## 5. Ranked continuations (TODO updated to match)

```text
1. Q-SCHEME first gate (witness-grade, this context or next): the
   genus-probe reconciliation prime_int_genus_audit.py with the
   verifier's sign correction baked in; plus the O_K control design.
2. CC-square posing (doc-level): Arakelov divisors on the square in
   CC's tolerant-module formalism; integer dims; Pontryagin-Serre
   duality; pre-registered fail-closed criterion (K-doc sec 6.B).
3. THR fold test (fresh-context, paper-scale): RO(C_2)-graded
   THR(F_p)^{tC_2} vs readings r1 (ladder fold) / r2 (anomalous
   dimension (1-s)/2) - gate C5''-infty's first checkpoint; doubles as
   the only candidate SELECTOR for the symmetric scheme (KMS-1/2).
4. C6' (D_ku constant after scheme fix), C6'' (minimal twisted
   instance: Lee's descent SS with psi^alpha, alpha = 1+p), C6'''
   (doc 17 signature protocol on the family matrices log|k-l|).
5. T2 interval certification over refinement bases (L's pipeline,
   now cheap); optional second-library cross-validation.
```

Genealogy note: the question "what selects the scheme" is this
program's instance of the question CC's archimedean work, Deninger's
conventions, and the KMS-1/2 input have circled for thirty years; the
fleet's contribution is to have FORCED it into a single pre-registered
gate with a computable first test.
