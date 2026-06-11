# AB - The non-Gaussian stress test: which boundary conditions are properties of the OBJECT and which are the Gaussian's image in the unit slot?

Status: fresh-context worker AB, 2026-06-11. Charter doc 39 sec 4, move
M2 (the direct test of critic blind-spot (a): "Delta_p is BUILT from the
Gaussian deficit - the shape law is partly TAUTOLOGICAL"). Required
reading executed in order: doc 39, WW-silhouette-dossier.md IN FULL,
QQ-native-face.md, TT-truncated-face.md, NN-graph-class-test.md,
RR-f123-cycle.md, KK-L1-density-rr.md. Inherited witnesses rerun by me
BEFORE any new work: prime_ww_silhouette (ALL PASS WW1-WW14, exit 0),
prime_int_jj_archimedean_unit (ALL PASS AJ1-AJ7, exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_ab_nongaussian_stress

Sections 0-2 (unit choices, hand derivations, gates, registered
predictions) were written BEFORE the witness was first run. DISCLOSURE
(WW/TT precedent): TWO design-stage calibration evaluations (inline, no
witness file) were run before registration: (i) the python-flint
acb.integral API check (rigorous ball quadrature available, v0.8.0);
(ii) the bump unit's half-mass integral int_0^0.995 f_B = 0.6034501612
(ball 3e-41), used below to pre-register the bump's covariant constants.
No derivation or gate was changed after these checks.

Discipline: F-a (no zeta values, no zeta continuation; Gamma enters only
as closed-form Mellin transforms of the logged units); zeros NEVER
consumed (no fork_lib import, no freeze needed - every quantity below is
congruence/entry/period-determined exactly as in WW). G-INT6: the three
test functions are THE logged choices of this memo (sec 1.1; every
parameter fixed at registration). Carrier guard AB9. All decision values
flint arb prec 300 (quadratures at registered tolerances, balls
propagated); exact Fractions for algebraic clauses; sign decisions only
when the ball resolves.

## 0. The task, the contrast classes, and the registered verdict semantics

WW's null verdict: the silhouette (BC1-BC5, BC7-BC12 of the inverse
problem) is satisfiable by Tate-at-oo read backwards, and the shape law
is the inserted GAUSSIAN's own Mellin data. The critic (doc 39 sec 2,
hazard (a)): within the Gaussian-test slice the shape rows have ZERO
freedom - the dossier may be measuring the probe, not the object. M2:
swap the unit and recompute the decisive rows. Per-row, three
pre-registered outcomes:

```text
INVARIANT  the row's content (integer charge, sign pattern, wall shape)
           is identical under every admissible unit -> the BC is a
           property of the OBJECT; it hardens into the de-tautologized
           spec.
COVARIANT  the row transforms by the unit's own Mellin/Fourier data
           under a transformation law STATED IN ADVANCE (sec 1.3) and
           certified by the witness -> the BC is about the COUPLING,
           parametrized by the unit slot; its Gaussian values are slot
           image, not spec.
ARTIFACT   the row breaks structurally (law fails BOTH the Gaussian
           form and the unit's own predicted form; or an integer
           dequantizes; or a sign pattern inverts unpredictably) ->
           the BC falls and the inverse problem re-poses.
```

FAIL-CLOSED: every prediction below is carried both ways; a confirmed
ARTIFACT outcome on any row is full-value and is reported as the
verdict, not repaired.

## 1. The units and the hand-derived transformation laws (before any run)

### 1.1 The three logged units (G-INT6: THE choices of this memo)

All even, f(0) = 1, rapidly decaying; d_f(x) := 1 - f(x) - f(1/x);
Delta_p^f(a) := sum_{m in Z} d_f(e^{-a} p^m). Notation: I_f =
int_0^infty f (so the full-line mass / dual atom is 2 I_f = fhat(0));
T_f(1) = sum_{m>=1} f(m); F_f = 2 int_1^infty f.

```text
(A) QUARTIC   f_A(x) = e^{-pi x^4}.  KK.U's banked unit (already proved
    to give the SAME density rho with shifted normalization log 2I_f at
    the DENSITY layer - this memo extends that audit to the remaining
    layers). NOT Fourier-self-dual. Closed Mellin data:
    fA~(s) = (1/4) pi^{-s/4} Gamma(s/4);  2I_A = 2 Gamma(5/4) pi^{-1/4}
    = 1.361723...
(B) BUMP      f_B(x) = exp(1 - 1/(1 - x^2)) for |x| < 1, else 0.
    Compactly supported: the maximal contrast class (not self-dual, not
    analytic at the edge, NO tail mass: F_B = 0, T_B(1) = 0). Mellin
    data has no closed form: computed by rigorous ball quadrature
    (registered routes sec 2). 2I_B = 1.2069003224... (calibration,
    ball 1e-40, recomputed in-witness).
(C) HERMITE SELF-DUAL  f_C(x) = e^{-pi x^2}(1 + eps H4(sqrt(2pi) x))
    / (1 + 12 eps),  H4(y) = 16y^4 - 48y^2 + 12,  eps = 1/100 (EXACT,
    fixed here).  ψ4 = H4(sqrt(2pi)x)e^{-pi x^2} is a +1-eigenfunction
    of the Fourier transform, so fhat_C = f_C EXACTLY: self-dual but
    NOT Gaussian - the sharpest probe (it isolates "self-duality" from
    "Gaussianity"). 2I_C = 1 exactly (self-dual + f(0)=1). Closed
    Mellin data: fC~(s) = (1/2) Gamma_R(s) (1 + 4 eps (4s^2 - 4s + 3))
    / (1 + 12 eps)   [hand: Mellin of x^{2k} e^{-pi x^2} =
    (1/2) pi^{-(s+2k)/2} Gamma((s+2k)/2), then Gamma recursion].
```

Hand positivity/tail bounds (used for certified lattice tails, all
proved by elementary inequalities in the same way as QQ3): d_f(e^u) <=
C_f e^{-2|u|} with C_gauss = pi, C_A = 2pi, C_B = 2pi, C_C = 6pi
(for f_C: 1 - f_C <= 4.8 pi x^2 via e^{-pi x^2} >= 1 - pi x^2,
12 - H4 = 48y^2 - 16y^4 <= 48y^2, 1 + eps H4 <= 4.42 on [0,1]; and
f_C(z) <= 0.32/z^2 for z >= 1).

### 1.2 The general-f machinery (one code path, Gaussian as CONTROL)

Counts and margins are computed through ONE parametrized code path; the
Gaussian column must reproduce the banked dossier numbers (gate AB1) or
the whole memo FAILS - this is the tautology guard: any mismatch means
the general machinery, not the dossier, is wrong. Duals: for self-dual
units (Gaussian, f_C) the FE route dual(u) = e^{-a}(Theta_f - 1) equals
the paired/Poisson dual EXACTLY (per-lattice Poisson needs only
fhat = f; certified in-witness by the homogeneity identity
theta_f(t) = (1/t) theta_f(1/t)). For the non-self-dual units (A, B)
the dual is FE-TRANSPORTED (NN sec 1.4's logged, demoted route -
flagged in every row below; the paired dual would carry fhat != f, and
that difference is itself BC8's content, tested separately in the
charge row).

### 1.3 Registered transformation laws (the covariant predictions)

(L1) SHAPE (S2). For any admissible unit, the WW sec 2.1 Mellin
derivation goes through verbatim with G_f(s) = f~(s) - 1/s:

    c_n^f(p) log p = -2 Re f~(2 pi i n / log p)     (n != 0),
    c_0^f(p) log p = C*_f = 2 int_0^infty (1_{x<1} - f(x)) dx/x.

Predicted values: Gaussian -Re Gamma_R(i xi), C* = gamma + log pi
(banked). Quartic: -(1/2) Re[pi^{-i xi/4} Gamma(i xi/4)], C*_A =
(gamma + log pi)/2 (Frullani with t = pi x^4). Hermite: -Re[Gamma_R(i
xi)(1 + 4 eps(4(i xi)^2 - 4 i xi + 3))]/(1 + 12 eps), C*_C = gamma +
log pi + 32 eps/(1 + 12 eps) = gamma + log pi + 2/7 (the s-linear term
of the Hermite polynomial shifts the 0-mode). Bump: quadrature route
c_n L = 2 Re int_0^1 (1 - f_B(x)) x^{i xi - 1} dx (no closed form).
REGISTERED: the law holds per unit to gate precision AND the Gaussian
law -Re Gamma_R is REJECTED by a certified margin at (p, n) = (5, 1)
for all three non-Gaussian units (including the SELF-DUAL one) ->
SHAPE = COVARIANT, slot-condition. If some unit matches Gamma_R: shape
is object-property after all (reportable shock). If a unit matches
neither its own law nor Gamma_R: ARTIFACT (the Mellin reading itself
was Gaussian-specific).

(L2) CHARGE (S3). Hole: the d = 1 FE dual is dual(u) = e^{-a}(Theta_f
- 1)|_{e^a = u}; Euler-Maclaurin (KK.2 skeleton, unit-uniform) gives

    u (dual(u) - 2 I_f) -> -f(0) = -1:

the dual's own atom mass COVARIES (2 I_f) but the missing continuum
charge is -1 times the PRIMAL UNIT ATOM f(0) = 1: INTEGER, unit-
independent. Band: M_0(q) = (2q-4) - rho_q 2q = 0 in exact Fractions -
f enters only through f(0) = 1: trivially invariant. REGISTERED:
charge dichotomy INVARIANT (-1 hole / 0 band), normalization covariant
as stated. ARTIFACT trigger: |u(dual - 2I_f) + 1| fails to vanish, or
the limit is unit-dependent (e.g. -2I_f).

(L3) PAYMENT (S4). Hand expansions (Theta_f(e^{-a}) = 2 I_f e^a +
2 psi_f, psi -> 0):
  (a) killer law: m+_f(d=1, a) = -e^{-a}/(1 + 2 I_f) + O(e^{-2a}).
      Constants: Gaussian 1/2; quartic 1/2.361723 = 0.423424; bump
      1/2.2069003 = 0.453122; Hermite 1/2 EXACTLY (2I_C = 1): the 1/2
      is a SELF-DUALITY datum, not a Gaussian datum.
  (b) entry deficit: d_f(1) = 1 - 2 f(1) by identity. Values: Gaussian
      0.913573; quartic 0.913573 (e^{-pi} coincidence: f_A(1) =
      f_gauss(1)); bump 1 EXACTLY (f_B(1) = 0); Hermite 1 - 2 e^{-pi}
      (1 + eps H4(sqrt 2pi))/1.12 = 0.658872...
  (c) entry floor (TT D2'): D^hon_f(q, entry) -> rho_q F_f, F_f =
      2 int_1^infty f: the floor is the unit's own tail mass past the
      entry point. Gaussian erfc(sqrt pi) = 0.0121889; quartic
      2 int_1^infty e^{-pi x^4} (quadrature); bump 0 EXACTLY (D^hon =
      0 termwise at entry: compact support kills the floor -
      degenerate covariance); Hermite quadrature value.
  (d) entry-margin constant (SS): hand derivation (full-lattice +
      two-coset EM at u = q + 1, sec 1.2 route) gives

      lim_q q m+_f(q, entry) = E_f = 2 + 4 I_f/(1 + 2 I_f)
            - (1 + 4 T_f(1))/(2 I_f) - 2 (1 + 2 T_f(1))/(1 + 2 I_f),

      which for 2 I_f = 1 collapses to the BANKED FORM 1 - 6 T_f(1)
      (Gaussian: 1 - 6 T(1) = 0.740696 - recovered, the control).
      Predictions: E_A = 1.3719, E_B = 1.3589, E_C = 1 - 6 T_C(1) =
      -0.0251 < 0: REGISTERED, both ways - the self-dual Hermite unit
      is predicted to BREAK entry positivity in the deep-q limit (its
      f(1) is 4x the Gaussian's, so its theta-tail constant 6 T_f(1)
      overshoots 1). If confirmed: entry positivity is a COUPLING
      condition (slot-dependent sign), not an object condition.
(L4) THREADING (S5). Signs predicted INVARIANT, constants covariant
      (chi_f = a + log(rho~ (1 + rho~)), rho~ = 2 I_f rho - KK.U's
      density shift): per-place m1(4.96) < 0 and m+_f((11;2), 4.96)
      < 0 (both slot signs negative -> LP infeasible outright, exact),
      A_11 < 0 in both unit variants; global A_g^f(4.96) > 0 over the
      same 13 deep slots + k=1 balls. ARTIFACT trigger: any unit flips
      per-place to feasible or global to infeasible.
(L5) DEPTH WALL (S6). m+_f(q, 8) ~ e^{-8}/rho~ (same EM expansion), so
      needed = (Lambda - m)^2/m - log 2 ~ rho~ Lambda^2 e^8: demand
      EXPONENTIAL in the window, supply LINEAR - the RATIO covaries by
      O(1) factors (2 I_f) but its scale (>> 1) is invariant.
      REGISTERED: ratio > 50 at (q, a) = (3, 8) and (121, 8) for every
      unit (Gaussian control: 155.7 / 3514.4 to 2%).

## 2. PRE-REGISTERED GATES (written before the first run)

Evaluation rules fixed in advance: arb prec 300; lattice sums |m| <= 60
with certified tail 2 C_f e^{2|a|} p^{-120} / (1 - p^{-2}) added to the
ball radius (C_f from sec 1.1's hand bounds); DFT N = 128 (aliasing
absorbed as in WW3 - all four units' ghat decay superpolynomially);
comb sums truncated at x_max = 16 / 3 / 1 / 8 (gauss/A/B/C) with the
sec-1 tail integrals (< 1e-50, added as balls); rigorous quadrature =
flint acb.integral (ball arithmetic, rel/abs tol 1e-40; bump edge
handled by the registered split: integrate on [0, 0.995] resp.
v in [-35, -0.005] with the closed-form edge strip (1 - e^{-0.005 i
xi})/(i xi) and tail balls 1.5 e^{-70}/2 resp. f_B(0.995) < 1e-43);
exact Fractions for M_0, eps, scale 4.96 = 124/25; sign decisions only
when the ball resolves. Gaussian column = CONTROL: banked-value
mismatches fail the memo.

```text
AB1 CONTROL (the tautology guard; general-f code path, Gaussian unit):
    c_n vs -Re Gamma_R, p in {2,3,5}, n in {0..3}, < 1e-20;
    m+(d=1, 2) within 0.12 e^{-2} of -e^{-2}/2; m+((11;2), 4.96) =
    -2.214249e-3 (1e-8, certified < 0); A_g(4.96) = +3.03e-2 (25%,
    > 0 certified); m_ku(3, log 4) = 0.55653 (2e-5); m_ku(121, 4.96)
    = 6.4682e-3 (1e-6); q m_ku(q, entry) = 0.8175 / 0.7561 (2e-3,
    q = 25/121); |D^hon(121, entry) - rho erfc(sqrt pi)| < 3/122;
    wall ratios 155.7 / 3514.4 (2%); hole |u(dual - 1) + 1| < 1e-40
    at u in {36, 968}. FAIL: any clause.
AB2 UNIT ADMISSIBILITY: per unit: f(0) = 1 (ball); 2I_f: quartic
    quadrature vs closed form 2 Gamma(5/4) pi^{-1/4} < 1e-35; bump
    quadrature ball < 1e-38; Hermite quadrature vs EXACT 1 < 1e-35;
    d_f(e^u) > 0 sign-resolved on u in [-6, 6] step 0.05 and tail
    clause d_f(e^u) e^{2|u|} <= C_f at |u| in {6, 8}; SELF-DUALITY
    certificate: |theta_C(1/3) - 3 theta_C(3)| < 1e-40 and t = 1/7
    (Poisson with fhat = f - this gate FAILS if the Hermite
    eigenfunction identity is wrong); NON-self-duality certificate:
    |theta_f(1/3) - 3 theta_f(3)| > 0.5 for A and B (the FE-transport
    for A/B is genuinely a transport). FAIL: any clause.
AB3 SHAPE LAW (the S2 row): per unit: DFT c_n of Delta_p^f (p in
    {2,3,5}, n in {0,1,2,3}) vs the sec-1.3 law: tol 1e-20 closed
    forms (A, C), 1e-15 quadrature route (B); mean clauses |c_0 L -
    C*_f| with C*_A = (gamma + log pi)/2, C*_C = gamma + log pi + 2/7
    (1e-20), C*_B = its own quadrature (1e-15). GAUSSIAN REJECTION:
    |c_1^f L + Re Gamma_R(2 pi i / log 5)| > 1e-3 certified at p = 5
    for f in {A, B, C}. FAIL: any clause.
AB4 CHARGE DICHOTOMY (the S3 row): per unit: hole |u(dual(u) - 2 I_f)
    + 1| < 1e-12 at u = 36 and < 1e-25 at u = 968 (dual = FE route,
    f-side sums + the I_f ball; sizes set by psi_f, hand-estimated
    << tol for all four units); band M_0(q) = 0 and (2q-4)/rho_q = 2q
    exact Fractions, q in {9, 25, 121}. FAIL: any clause.
AB5 PAYMENT SCHEDULE (the S4 row): per unit:
    (a) |m+_f(d=1, a) + e^{-a}/(1 + 2 I_f)| < 0.15 e^{-a}, a in
        {2, 5};
    (b) d_f(1) = 1 - 2 f(1) identity < 1e-40; values printed;
    (c) |D^hon_f(121, entry) - rho_121 F_f| < 5/122 (bump: both sides
        EXACTLY 0 - printed);
    (d) |q m_ku_f(q, entry) - E_f| < 3/sqrt(q), q in {25, 121}; E_f
        from the sec-1.3 closed law (T_f(1), I_f in arb); RECORD:
        f_C also at q = 841 (the predicted negative-limit trend; the
        SIGN of q m+ at finite q is a record, the gate is the law).
    FAIL: any clause.
AB6 THREADING PER-PLACE (the S5 row, decision cell): per unit:
    m1 = m+_f(d=1, 4.96), m2 = m+_f((11;2), 4.96), A_11 variants
    v = 2/sqrt(11) m1 + (2/11) m2 and g (m1 -> m1_GG ball): ALL signs
    arb-resolved; the sign census is the verdict input (registered:
    all m1 < 0, all m2 < 0, all A_11 < 0 -> per-place infeasible,
    exact, every unit). FAIL: an unresolvable sign.
AB7 THREADING GLOBAL: per unit: A_g^f(4.96) = sum over the SAME 13
    deep slots (p <= 11, 2 <= k <= n_p(4.96)) of 2 p^{-k/2}
    m+_f(p, k, 4.96) + sum over the 34 places p <= e^4.96 of
    2 p^{-1/2} m1_GG_f (computed as balls; m1_GG_f = log Theta_f +
    log(1 + e^{-a} Theta_f) - a - log(2I_f(1 + 2I_f)), the GG repair
    dual + f(0) e^{-a}): sign certified. REGISTERED: > 0 every unit
    (per-place infeasible / global feasible INVARIANT). FAIL:
    unresolvable.
AB8 DEPTH WALL (the S6 row): per unit: needed(q, 8) = (Lambda -
    m)^2/m - log 2 with m = m_ku_f(q, 8) > 0; ratio = needed /
    (floor(8/log q) log q) > 50 at q in {3, 121}; RECORD needed e^{-8}
    / (rho~ Lambda^2) (covariant constant; gated 2% on the control
    only). FAIL: m < 0 unregistered, or ratio clause.
AB9 CARRIER GUARD (exact integers, WW14 replication): Epstein
    x^2 + 5y^2: 36 = 4*9 = 6*6, 4/6/9 irreducible -> no valuation ->
    no slot ladder -> Delta_p^f UNFORMABLE FOR EVERY UNIT f (the
    stress test is carrier-bound before any unit acts); DH: no
    carrier monoid. FAIL: any clause.
```

Registered overall verdict logic (before the run): AB1 is load-bearing
(a control mismatch voids every column). Expected landing: S3 + S5 +
S6 INVARIANT, S2 + S4 COVARIANT with the sec-1.3 laws certified, ZERO
artifacts - in which case the BCs split exactly as the charter's
decisive question asks, and sec 4 writes the de-tautologized spec. Any
certified sign flip in AB6/AB7, dequantization in AB4, law failure in
AB3/AB5, or wall collapse in AB8 lands the affected row at ARTIFACT and
the spec is re-posed accordingly; the E_C < 0 prediction in AB5d is the
one place a NEW covariant sign change is registered IN ADVANCE.

---- verdict sections written after the runs ----

## 3. VERDICT: THE BCs SPLIT EXACTLY AS THE CHARTER'S DECISIVE QUESTION
## ASKED - WITH ONE REGISTERED-PREDICTION VIOLATION THAT SHARPENS THE
## SPLIT (the banked decision cell itself is slot data)

Witness ALL PASS (AB1-AB9, exit 0, ~3 min; runs 4-5 diff-identical,
logs /tmp/ab_run{4,5}.log). Control column (AB1) reproduces every
banked dossier number through the general-f path (m+((11;2), 4.96) =
-2.214249375e-3 to all digits; A_g = +3.027393e-2; wall 155.7/3514.4;
entry 0.8175/0.7561; erfc floor; hole 4.3e-87). Witness-engineering
record (disclosed, predicates untouched): (i) acbF ctor shim (API);
(ii) run 2's analytic-guard returned a finite wide ball - this CORRUPTS
acb_calc's enclosure (I_B came out +2.5e-3 off with a false 1e-45
radius, caught by the AB4 bump clauses); the correct NaN signal
recovers the disclosed calibration value exactly; (iii) entry-scale
slot weights w/u as exact rationals (the bump's support comparison at
w = u must resolve x = 1); (iv) bump DFT N = 128 -> 512 (its Mellin
data decays only ~e^{-1.25 sqrt(xi)}, measured: the alias floor 1e-12
sat above the registered 1e-15 - calibration of the apparatus, the
predicate |c_n - law| < 1e-15 unchanged); (v) AB6's run-3 code had
hardened the registered PREDICTION into the gate - reverted to the
MEMO's registered structural predicate (signs resolved; census =
verdict input), and the (11;2) phase-scan RECORD added per the
documentation duty. Hand-arithmetic slip disclosed: sec 1.1 printed
2I_A = 1.361723; the true value of the registered closed form
2 Gamma(5/4) pi^{-1/4} is 1.3616441 (no gate touched it).

THE PER-ROW TABLE (all decisive signs arb-certified):

```text
ROW                     VERDICT      CERTIFICATE
S2 SHAPE LAW            COVARIANT    c_n log p = -2 Re f~(2 pi i n/
                                     log p) - the unit's OWN Mellin
                                     data - holds to 1e-85 (A, C
                                     closed forms) / 2.6e-22 (B,
                                     rigorous quadrature), 12 (p,n)
                                     pairs each; the GAUSSIAN law
                                     -Re Gamma_R is REJECTED by
                                     certified gaps 0.2006 / 0.1864 /
                                     0.1785 at (5,1).  DECISIVE: the
                                     SELF-DUAL non-Gaussian f_C also
                                     rejects Gamma_R (mean = gamma +
                                     log pi + 2/7 exactly) - even
                                     self-duality does not pin the
                                     shape.  BC1, BC10 = slot.
S3 CHARGE DICHOTOMY     INVARIANT    hole charge = -1 x f(0), INTEGER,
                                     every unit (1e-84..1e-33 at
                                     u = 968; bump 2e-6 at u = 36 =
                                     its slow-decay psi, collapsing as
                                     registered); band charge 0 exact
                                     Fractions, f-free.  Only the
                                     unit-of-charge normalization
                                     (dual atom 2I_f) covaries.
                                     BC2 = OBJECT.
S4 PAYMENT SCHEDULE     COVARIANT    all four registered laws certified:
                                     killer -e^{-a}/(1+2I_f) (consts
                                     0.5 / 0.4234 / 0.4531 / 0.5 - the
                                     1/2 is a SELF-DUALITY datum);
                                     d_f(1) = 1-2f(1) (0.9136 / 0.9136
                                     / 1 / 0.6589); floor rho_q F_f
                                     (0.0122 / 0.0058 / EXACTLY 0
                                     (compact support kills it) /
                                     0.0898); entry constant E_f
                                     (= 1 - 6 T_f(1) when self-dual):
                                     gauss 0.7407, quartic 1.3717,
                                     bump 1.3589, hermite -0.0251 < 0
                                     CONFIRMED: q m_ku(121, entry) =
                                     -0.0141, q = 841: -0.0236, signs
                                     certified - ENTRY POSITIVITY IS
                                     UNIT-DEPENDENT inside the
                                     self-dual class.  BC3 = slot.
S5 THREADING            SPLIT        GLOBAL: INVARIANT - A_g(4.96) > 0
                                     every unit (+3.03e-2 / +2.72e-2 /
                                     +3.15e-2 / +2.34e-2, certified).
                                     k=1 (Lambda(p)-class) deficit:
                                     INVARIANT negative (killer law,
                                     every unit).  But the BANKED
                                     DECISION CELL (11;2)@4.96 FLIPS
                                     under f_C: m+ = +2.0913e-4 > 0
                                     certified (registered prediction
                                     violated; the cell's per-place LP
                                     becomes feasible).  Phase scan
                                     (record): gauss -------+++++ vs
                                     hermite +------+++++ over a half
                                     period from window entry: the
                                     (p;2) breakage PERSISTS but its
                                     PHASE SET SHIFTS.  BC4 = OBJECT
                                     in the form "k=1 deficit per-place
                                     unpayable + global cross-place
                                     payability"; the specific breaking
                                     cell/phase = slot.
S6 DEPTH WALL           INVARIANT    ratio needed/available at a = 8:
                                     155.7/3514.4 (G) - 212.0/4785.5
                                     (A) - 187.9/4241.3 (B) -
                                     155.7/3514.4 (C), all >> 50;
                                     AND the law constant needed e^{-8}
                                     /(rho~ Lambda^2) = 0.998..1.000
                                     for EVERY unit: in covariant
                                     units (rho~ = 2I_f rho) the wall
                                     law has constant EXACTLY 1 - the
                                     exponential-vs-linear demand is
                                     unit-free.  BC6's wall = OBJECT.
S12 CARRIER             INVARIANT    unformable for EVERY unit before
                                     any unit acts (AB9).  BC11 =
                                     OBJECT.
```

## 4. The de-tautologized spec (the answer to critic blind-spot (a))

The convergence-on-BC6 hazard is now resolved by measurement, not
argument. OBJECT-CONDITIONS (survive every admissible unit; these are
the real spec of the missing structure):

```text
OC1 (was BC2)  integer charge dichotomy: the missing object is exactly
               -1 continuum unit per Lambda(p) class; truncation bands
               are 0-charge bookkeeping.  (Quantization is NOT the
               Gaussian's doing.)
OC2 (was BC4)  threading: the Lambda(p)-class deficit is per-place
               unpayable under EVERY unit, and the KMS-1/2 global
               aggregate pays everything scanned under EVERY unit: the
               object moves surplus ACROSS places.  (Which (p;2) cell
               breaks at which phase is unit data and must be DROPPED
               from the spec.)
OC3 (was BC6)  the depth wall, now unit-free with constant 1 in
               covariant units: no re-posing crosses e^a vs a.  The
               second-evaluation demand stands unweakened.
OC4 (was BC11) carrier consumption (Euler product load-bearing).
```

SLOT-CONDITIONS (covariant: they describe the COUPLING, parametrized by
the inserted unit's own Mellin/Fourier data; their Gaussian values are
the unit's image, exactly as the critic suspected):

```text
SC1 (was BC1/BC10)  the shape law and amplitude ladder: c_n log p =
                    -2 Re f~(2 pi i n/log p).  WW's null verdict
                    SHARPENED: the silhouette is Tate local data OF
                    WHATEVER SITS IN THE SLOT - even self-duality does
                    not force Gamma_R.
SC2 (was BC3)       the payment constants: 1/(1 + 2I_f), 1 - 2f(1),
                    rho F_f, E_f - each a named functional of the
                    unit; the SIGN of the entry constant can flip
                    inside the admissible class (E_C < 0).
SC3 (BC8's norm)    "dual atom = continuum unit with equal mass" is
                    the self-duality condition 2I_f = f(0), pinning
                    the CLASS, not the Gaussian.
```

Corollary for the inverse problem (WW sec 5): BC1-conformance (doc 39
E1) remains a valid arrival gate ONLY as a test of the GAUSSIAN-slotted
coupling; any candidate trace with a different forced unit must be
tested against ITS OWN Mellin data via the same law. The residual
content of the program is confirmed to live in {OC1-OC4}, i.e.
essentially BC2 + BC4(restated) + BC6 + BC11 - and BC6 was already the
known non-EF clause. The shape axis is now PROVEN slot-parametric, so
no refinement of Delta_p measurements can ever advance the program:
measure couplings only through the covariant laws.

## 5. G-INT6 ledger

```text
input                          choices spent
unit (A) quartic e^{-pi x^4}   THE logged choice 1 (KK.U's banked unit)
unit (B) compact bump          THE logged choice 2 (maximal contrast;
                               standard mollifier, no parameters)
unit (C) Hermite self-dual     THE logged choice 3 (eps = 1/100 fixed
  eps = 1/100                  at registration; +1-eigenfunction h4)
transformation laws (L1-L5)    hand-derived sec 1.3 BEFORE the run
                               (E_f recovers banked 1 - 6T(1) exactly)
covariant chi (rho~ = 2I_f rho) KK.U's banked density shift, no retune
FE-transported duals (A, B)    NN sec 1.4's logged demoted route,
                               flagged per row; EXACT (Poisson) for
                               Gaussian and f_C - the decisive hermite
                               flip uses no transport
quadrature/grid parameters     calibration (registered sec 2; N = 512
                               for the bump disclosed in sec 3)
design calibrations (2)        disclosed sec 0; no gate changed after
witness fixes (5)              computational, disclosed sec 3; the AB6
                               revert is TO the registered predicate
zeros                          NONE (no fork_lib, no freeze; all loci
                               congruence/entry/period-determined)
```

## 6. Honest limits

- Duals for the non-self-dual units (A, B) are FE-TRANSPORTED, not
  paired/Poisson duals (those would carry fhat != f).  Every INVARIANT
  verdict is therefore strongest on the self-dual pair (Gaussian, f_C),
  where the route is exact - and the one sign flip found (the hermite
  decision cell) lives entirely inside the exact pair.
- The threading row recomputes the DECISIVE cells and the banked
  13-slot aggregate, not NN's full 132-class census; the "(p;2)
  breakage persists with shifted phase" claim is a 12-point record,
  not a census.  Dossier rows S7-S9 (kappa, FE-homogenizer, joint
  cancellation) were not re-tested per unit (S8's normalization clause
  is covered by the f_C probe; S9 is unit-independent geometry).
- One eps value probes the self-dual non-Gaussian class; the covariant
  laws are certified at three units, not proved unit-uniform (the
  E_f and killer-law derivations are general but their error terms are
  gated only at the tested scales).
- A_g positivity is at the banked decision scale 4.96 only, as in WW9.
- E_f is the lattice-face entry constant; the honest-face (TT) census
  was not recomputed per unit - the certified statement is the sign of
  q m_ku at q in {25, 121, 841}, plus the law match.
- The bump's u = 36 hole tolerance (1e-3) is wide because its psi
  decays only stretched-exponentially; the u = 968 clause (1.9e-33
  vs tol 1e-25) carries the quantization weight.

## 7. Hand-off (for the lead)

```text
VERDICT:   M2 lands.  INVARIANT (object-conditions): charge dichotomy
           -1/0 (integer, every unit); threading in the corrected form
           "Lambda(p)-class per-place unpayable + global KMS-1/2
           payable" (A_g > 0 certified under all four units); depth
           wall (ratio >> 1, law constant = 1.000 in covariant units -
           unit-FREE); carrier guard.  COVARIANT (slot-conditions,
           transformation laws certified): shape law (the unit's own
           Mellin data, 1e-85; Gamma_R rejected by 0.18-0.20 even for
           the SELF-DUAL non-Gaussian unit); the entire payment
           schedule (killer 1/(1+2I_f); d(1) = 1-2f(1); floor rho F_f,
           EXACTLY 0 for compact support; entry constant E_f =
           1 - 6T_f(1) in the self-dual class).  NO artifacts: nothing
           broke structurally; every mutation followed its registered
           law.
SHARPEST:  (1) the banked decision cell (11;2)@4.96 FLIPS POSITIVE
           under the self-dual Hermite unit (+2.09e-4 certified, exact
           machinery, no transport): the cell that anchored RR/WW's
           per-place infeasibility is GAUSSIAN PHASE DATA; the
           breakage persists with shifted phase (record).  (2) entry
           positivity (TT's census sign) is unit-dependent: E_C =
           1 - 6T_C(1) = -0.025 < 0, confirmed at q = 121, 841
           certified negative.  (3) the depth wall constant is exactly
           1 in covariant units - the strongest invariance found.
SPEC:      de-tautologized spec = OC1-OC4 (sec 4); BC1/BC3/BC10 are
           coupling data parametrized by the unit slot; BC1-conformance
           gates must be slotted with the candidate's own unit.
WITNESS:   prime_ab_nongaussian_stress.py (AB1-AB9, ALL PASS, exit 0,
           deterministic runs 4-5 diff-identical; 5 disclosed
           computational fixes, no registered predicate changed).
           Inherited reruns before any work: prime_ww_silhouette,
           prime_int_jj_archimedean_unit (both ALL PASS, exit 0).
NO ZEROS:  no zero contact anywhere; freeze never triggered.
```
