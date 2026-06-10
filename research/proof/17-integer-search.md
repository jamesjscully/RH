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
