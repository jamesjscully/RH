# 17 - The integer search: pipeline, grammar refinements, and the mapped boundary (R-INT, first pass)

Status: R-INT rung, first execution pass (2026-06-09/10). Pipeline built and
calibrated; grammar refined twice by measurement and once by a structural
counterexample; C4's opening question partially answered. Witness:
count_fingerprint.py.

## 1. The pipeline (gate G-INT2, operational)

Any integer count table c(n) (c(1)=1) is processed:
counts -> generalized von Mangoldt by the Dirichlet-log recursion
lambda(n) = c(n) log n - sum_{d|n, d<n} lambda(d) c(n/d) (exact) ->
correlation profile B_L(t) -> regression against zeta's fingerprint.
Calibration: C0 (d(n), Z = zeta^2) returns k_hat = +2.0000, residual
2.2e-16 (machine floor). The AB cell (abelian-group counts, prod_k zeta(ks))
and R2 cell (r_2(n)/4 = ideal counts of Z[i], zeta * L(chi_4)) return
residuals supported EXACTLY on prime powers with the predicted structures
(sigma(m) log p tail; the chi_4 comb). The pipeline reports WHICH zeros a
count structure touches.

## 2. Grammar refinement I: self-duality (C0')

The ZN probe (c(n) = n, Z = zeta(s-1)) shows count structures see zeros at
the line set by their counting growth. The critical line s = 1/2 is reached
by SELF-DUAL count structures: d(n) sits at 1/2 because ab = n is a <-> b
symmetric. In count language, the functional equation IS the duality of the
pairing. Fourth independent convergence on the square.

## 3. Grammar refinement II: temperedness

Self-duality alone does not put zeros ON the self-dual line. Counterexample
inside the grammar: the subgroup structure of Z^2 is perfectly self-dual
(order-m subgroups <-> index-m subgroups via annihilators), yet its zeta
zeta(s) zeta(s-1) has zeros PROVABLY off its self-dual line Re s = 1 - that
is the prime number theorem. What d(n) has and c(n) = n lacks is
TEMPEREDNESS: subpolynomial counts at the sqrt-normalized scale (no growth
skew between the dual variables). Grammar demand: self-dual + tempered +
Euler. This combination has a name: the Selberg-class shape, restricted to
nonnegative-integer (cardinality) coefficients.

## 4. The Epstein boundary (the structural wall of the count grammar)

Epstein zeta functions are count structures (r_Q(n) >= 0 counts lattice
vectors), self-dual (Epstein FE), tempered - AND have off-line zeros.
Therefore: counts + self-duality + temperedness do NOT force the critical
line. The Euler product (multiplicative closure: ideal counts multiply,
generic quadratic-form counts do not) remains the irreducible discriminating
ingredient - exactly as gate G-INT3 pre-registered. CONSEQUENCE, the mapped
reachable set:

```text
The count grammar's nonnegativity, by itself, lands exactly on the standard
conjectural landscape (Selberg class with cardinality coefficients: ideal
counts of number fields and their products). It does not escape it. The
index, if it exists, is NOT the counts' entrywise nonnegativity - it must be
a SIGNATURE THEOREM on a pairing matrix built from the counts, which is
precisely the function-field structure (entrywise positivity of intersection
numbers is the input; the Hodge index is a lattice-signature statement on
top). The search narrows accordingly: not "find positive counts touching
zeros" (mapped, classical), but "find an integer pairing matrix from
multiplicative count data whose SIGNATURE is theorem-constrained".
```

## 5. C4 opening question: partially answered

Question (from TODO): does an integer-valued self-dual Hall pairing on
finite Z-modules exist?

```text
YES at the structure-constant level: the Hall numbers g^G_{H,K} =
#{N <= G : N iso K, G/N iso H} are integers, definitionally nonnegative,
and SYMMETRIC in (H,K): Pontryagin duality (N -> Ann(N), G* iso G for
finite abelian G) bijects {N iso K, G/N iso H} with {M iso H, G*/M iso K}.
CAVEAT localized: only the metrized (Green) form needs 1/|Aut| weights
(groupoid cardinalities - the q->1 rational leak); the bare integer
matrices M_w[H,K] = sum_G g^G_{H,K} w(G), integer weights w, are legitimate
candidates whose SIGNATURES are finite, exactly computable questions.
```

NEXT (C4 execution): compute the signatures of the Hall matrices M_w over
the finite p-groups of bounded order, for the natural weight families
(w = 1; w = indicator by |G|; w = the flow weights |G|^{-1/2}-rounded);
look for a stable signature law; THEN ask the comparison question (does any
signature-constrained combination produce the EF fingerprint at the
self-dual normalization). C1 and C2 inherit refinement II (only self-dual
tempered instances are worth feeding to the pipeline).

## 6. C4 executed: the Hall form is a metric; the Euler form vanishes; the
## index demands a two-dimensional category (2026-06-10)

`count_hall_signature.py` (exact integer enumeration, symmetry = duality
theorem verified in-data): the self-dual-grade Hall forms S_m are POSITIVE
DEFINITE for all computed cells (p = 2: m = 1,2,3; p = 3: m = 1,2) -
signature (k, 0). Pre-registered reading: metric-like, no index at this
grade (consistent with Zelevinsky's PSH positivity for Hall structures).

WHY, structurally - and the finding that redirects the rung: the FF
intersection form's signed structure is the EULER FORM
chi(H, K) = sum (-1)^i dim Ext^i(H, K). For finite Z-modules it VANISHES
IDENTICALLY: |Ext^1(A, B)| = |Hom(A, B)| for finite abelian groups (apply
Hom(-, B) to 0 -> Z -> Z -> Z/n -> 0: |B[n]| = |B/nB|), so
chi = log|Hom| - log|Ext| = 0. This is the categorical incarnation of
"Spec Z is one-dimensional, no room for signature" - the same fact the
Arakelov audit (log/2026-06-06) found numerically and doc 16 found
analytically. Torsion sheaves on a CURVE always pair to zero; they acquire
nonzero (negative) self-pairing only on a SURFACE.

THE REDIRECTED QUESTION (precise, computable by established machinery, and
NOT covered by the F1 survey's scale-criterion kill): the derived square

    Z (x)^L_S Z      (tensor over the sphere spectrum; pi_* (HZ ^ HZ) has
                      genuinely nontrivial torsion in higher degrees)

is a non-scheme thickening of the arithmetic square in which the Euler form
on finite (torsion) objects acquires ALTERNATING higher contributions and
need not vanish. Question C4': compute the Euler pairing on the derived
category of finite complexes over HZ ^ HZ - does it have nonvanishing
signature content on torsion classes? A YES with Lorentzian-type signature
would be the first integer-valued, sign-bearing pairing on an arithmetic
square passing the G-INT5 no-scale check (homotopy provides the second
dimension, not a finite residue field at infinity). This is a homotopy-
theory computation (dual-Steenrod-type rings), fresh-context scale.
