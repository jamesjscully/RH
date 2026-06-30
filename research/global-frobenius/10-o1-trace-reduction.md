# 10 — O1 reduced: the self-intersection IS the trace of the identity

Status: THEOREM step (T), 2026-06-30. Addresses doc-08 obligation O1 (the
load-bearing soft spot): "<Delta,Delta>_E = the regularized additive tower sum,
for every additive E." Reduces it from a modeling assumption to a known trace
theorem + one sharp residual. Anti-trap checked: RH-clean.

## What O1 must establish, and the worry

```text
O1: for any integer-valued additive/localizing invariant E, the diagonal
    self-intersection <Delta,Delta>_E equals the regularized sum of E down the
    tower (the quantity W1/doc-04 show diverges-or-transcendental).
WORRY: if <Delta,Delta> were something OTHER than the tower sum, the whole
    dichotomy (which is about the tower sum) would miss it -- the theorem could
    be vacuous or wrong.
```

## The reduction (to a trace theorem)

```text
The self-intersection of the diagonal is NOT an ad-hoc choice -- it is forced:
  <Delta, Delta> = tr(id_X) = the categorical TRACE OF THE IDENTITY = the
  Euler characteristic chi(X). [Normal bundle of Delta in X x X is T_X, so
  Delta.Delta = integral of c_top(T_X) = chi(X); equivalently the diagonal is the
  unit/counit of a self-duality and its self-composite is the trace.]

For a LOCALIZING invariant E and a DUALIZABLE object, this is a THEOREM:
  E(<Delta,Delta>) = tr_E(id) = chi_E = Sum_i (-1)^i E(H^i)
  -- the additivity of traces (Ponto-Shulman; May's axioms for traces in
  symmetric monoidal / bicategorical settings). The Euler characteristic is the
  trace of the identity, and a localizing invariant sends it to the alternating
  sum. [This is the F_q case: X proper => dualizable => chi finite integer = 2-2g.]
```

So O1 is the trace/Euler-characteristic identity. The only question is what
happens over `bar(Spec Z)`, where it is NOT proper:

```text
NON-DUALIZABILITY OVER bar(Spec Z): the object is affine over S; the Ext /
homotopy tower NEVER truncates (doc 18/19's named wall = no properness). A
non-proper object is NOT dualizable, so there is no honest categorical trace:
<Delta,Delta> does NOT exist as a finite trace. It exists ONLY via
REGULARIZATION, and the regularized trace IS the regularized tower sum (the
alternating/zeta-regularized Sum_i (-1)^i E(H^i) over the infinite tower). That
is exactly the object W1 (diverges) and doc 04 (transcendental) analyze.
```

## The true residual (sharper than O1)

```text
O1 does NOT fully close. The remaining gap is REGULARIZATION-UNIQUENESS:
  the categorical trace is undefined (non-dualizable), so <Delta,Delta> requires
  CHOOSING a regularization; the dichotomy is proved for the zeta-regularization
  (and the natural 2-variable models, doc 04), NOT for every conceivable one.

BUT the gap is tied to CANONICITY (spec S1): a CANONICAL invariant must use a
CANONICAL regularization. The canonical regularization of a localizing-invariant
trace over S is the zeta-determinant / TP regularization (Hesselholt), which is
zeta-type -- hence the dichotomy applies. So:
  O1 closes  <=  "canonicity forces the zeta-type regularization."
This is the precise residual, and it is a structural question about canonical
regularizations, NOT a modeling guess.
```

## Net status of O1

```text
BEFORE: "Reading -- modeling assumption" (the soft spot).
AFTER:  reduced to
  (i)   <Delta,Delta> = tr(id) = chi  [Theorem: trace = Euler characteristic],
  (ii)  E(chi) = alternating tower sum for dualizable objects
        [Theorem: additivity of traces, Ponto-Shulman],
  (iii) non-dualizability over bar(Spec Z) => trace only via regularization
        [structural, = non-properness wall],
  (iv)  regularization-uniqueness: canonicity (S1) forces zeta-type
        [THE SHARP RESIDUAL, open, structural].
The load-bearing identification is now a theorem (i,ii); the residual (iv) is a
single structural question, not a modeling assumption. O1 substantially closed.
```

## Anti-trap + scope

```text
RH-CLEAN: the trace/Euler-characteristic identity references no zeros, no
positivity -- chi is structural (the trace of the identity). No RH-input enters;
this is NOT a circling to RH-equivalence (Outcome-D guard passed).
SCOPE: improves the rigor of doc 08's additive theorem; bounds the route, not RH.
Grade: O1 reduced to a trace theorem (cited: Ponto-Shulman / May) + the
regularization-uniqueness residual (iv).
```

## Next

The additive theorem (doc 08) now rests on a trace theorem, not a guess; its one
open hinge is (iv) regularization-uniqueness via canonicity. Pair with doc 11
(the multiplicative extension), whose own residual is the F_1 problem -- together
they bound the canonical class.
