# 276 - Carrier-first categorical square contract

Status: construction-spec categorical anchor, 2026-06-21.
One-hundred-thirty-ninth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Docs 219 and 252 killed the shortcut from formal composition or generic
span/profunctor bicategories to `End(S^2/Z)`. Docs 256 and 257 then froze
the actual square-carrier contract and the DD.4/SCC boundary interface. This
document records the admissible categorical route:

```text
construct a specific compactified zeta square first,
then use its proper correspondence category as the organizing language.
```

Witness, lead-reran this cycle:
`prime_int_n1b_carrier_first_categorical_square_contract`
(CFC1-CFC7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_square_carrier_contract`,
`prime_int_n1b_dd4_scc_interface`,
`prime_int_n1b_span_profunctor_bicategory_no_go`, and
`prime_int_n1b_formal_correspondence_composition_no_go`.

## 1. Purpose

The useful categorical idea is not "take a category of correspondences" in
the abstract. That route is already closed. The useful idea is to demand a
single carrier object whose structural maps force the square data together.

The target is a compactified square

```text
        boundary dQ  ->  compact square Qbar  <-  open square Q
                              | p1, p2
                              v
                         arithmetic base
```

together with a proper correspondence category or derived enhancement

```text
Corr^prop(Qbar).
```

The category is allowed only if the object `Qbar` already supplies the
source/target maps, the boundary/localization sequence, integral cycle
pushforwards, Frobenius/Hecke graph, and duality. In that case category
theory is not decoration: it is the mechanism forcing composition, projection
formula, Rosati, and control death to be formation data rather than later
filters.

## 2. Contract

A carrier-first categorical construction must provide the following
generators before any downstream language counts.

```text
CFC.1  A compactified zeta square Qbar over Z, with open square Q and
       boundary dQ.

CFC.2  Two structural maps p1,p2 from Qbar to the arithmetic base.

CFC.3  Integral cycle or K-theoretic groups on Qbar with proper pushforward
       along p1,p2. Endpoint integrality and the two degree maps must be
       pushforwards, not labels.

CFC.4  A proper correspondence category Corr^prop(Qbar), or a carrier-native
       proper derived enhancement, with composition by fiber product.

CFC.5  An integral representability functor

           rep_NS : Corr^prop(Qbar) -> (Z-lattice, intersection form)

       whose finite-field model is the Neron-Severi triple
       (d1,z,d2) with

           (d1,z,d2).(e1,w,e2) = d1 e2 + d2 e1 - Tr(z w).

CFC.6  An identity/diagonal correspondence Delta and Frobenius/Hecke graph
       correspondences Gamma_n, with graph composition induced by fiber
       product and Delta.Gamma_n equal to the explicit-formula count term.

CFC.7  A boundary localization sequence or exact triangle whose connecting
       map kills the DD.4 class

           [(1+z)^-1] in H^1(<phi>; 1 + z F_2[[z]]) = Z/2

       through carrier boundary/properness/self-duality, not through a free
       splitter.

CFC.8  A duality functor or adjoint-correspondence operation D induced by
       the carrier, with D^2=id and evaluation

           P_NS(z,w) = Tr(z w^dag).

CFC.9  The primitive positive Rosati/Hodge-index sign on the carrier.

CFC.10 DH/Epstein/control death at formation: controls must fail to
       instantiate Qbar, p1,p2, dQ, Gamma, rep_NS, or D before any period,
       trace, quotient, or positivity filter is applied.
```

## 3. Lemma

```text
Lemma 276.1 (carrier-first category is the admissible categorical route).

In the finite-field square anchor q=7, Tr(F)=1, the represented diagonal and
Frobenius graph satisfy

    Delta . Gamma_n = #C(F_{q^n})       for n=1,2,3,

and the graph law Gamma_1 o Gamma_2 = Gamma_3 is induced by the proper
correspondence model. The primitive Hodge/Rosati sign is negative on-circle
and flips under an off-circle plant.

The DD.4 obstruction remains the nonzero class

    [(1+z)^-1] in H^1(<phi>;1+zF_2[[z]]) = Z/2

in the tested truncations L=6,8,10,12. A formal splitter can kill this class
only as an inserted coboundary generator. A carrier-first boundary slot kills
it only when the same square also supplies boundary localization and
self-duality.

An abstract span/profunctor bicategory, a symbolic triple-composition law, a
free DD.4 splitter, or a control trace/profile cannot instantiate the
carrier-first generators. They lack Qbar, p1,p2, dQ, integral pushforward,
proper correspondences, Frobenius graph, and carrier duality.

Consequently a categorical approach is admissible exactly when it starts
from the compactified square carrier and proves the correspondence category,
boundary localization, endpoint degree maps, graph composition, Rosati, and
control death as structure of that one carrier.
```

## 4. Proof

`prime_int_n1b_carrier_first_categorical_square_contract` verifies seven
gates.

CFC1 records the finite dependency graph. A carrier-first datum containing
`Qbar`, `Q`, `dQ`, `p1`, `p2`, integral cycles, proper pushforwards,
proper correspondences, fiber products, localization, boundary self-duality,
the Frobenius/Hecke graph, and duality derives all square slots together:
endpoint integrality, degree maps, `rep_NS`, diagonal, graph, fiber-product
composition, projection formula, DD.4 boundary killing, Rosati, primitive
sign, and control death.

CFC2 reruns the finite-field anchor at q=7. The diagonal/graph intersections
match the point counts for n=1,2,3, graph composition gives
`Gamma_1 o Gamma_2 = Gamma_3`, and the primitive Rosati sign detects an
off-circle plant.

CFC3 recomputes the DD.4 obstruction in truncations L=6,8,10,12:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

It then distinguishes carrier boundary localization from a free splitter:
only the boundary/localization/self-duality generators satisfy the
`dd4_boundary_killing` dependency.

CFC4 checks that generic spans/profunctors, symbolic triple composition,
free DD.4 splitting, and control profiles derive none of the carrier slots
that matter.

CFC5 records the universal-property filter: a candidate is allowed through
only if it supplies the required square generators. The carrier-first square
passes; generic spans, formal triples, free splitters, and controls fail
before detailed theorem work begins.

CFC6 records control death as a formation condition. Controls may declare
traces, projection formulas, or positive pairings, but with no square maps or
boundary they derive no carrier slots.

CFC7 records the status: over `Z`, this is a categorical contract only. The
compactified square carrier and its structural generators remain
unconstructed.

## 5. Impact on R1

```text
R1 after docs 138-276:
  NEWLY FIXED THIS CYCLE:
    - the admissible categorical method. Category theory is allowed only as
      the proper correspondence category of an actual compactified zeta
      square. It must make endpoint integrality, degree maps, DD.4 boundary,
      graph composition, Rosati, and control death consequences of one
      carrier object.

  STILL ADMISSIBLE:
    - a compactified zeta square Qbar over Z with Q, dQ, p1,p2, integral
      cycles, proper correspondences, fiber-product composition, boundary
      localization killing the DD.4 class, Frobenius/Hecke graph, canonical
      D^2=id Rosati, primitive sign, and control death;
    - categorical, six-functor, motivic, topos, shtuka, or trace-formula
      realizations downstream of that carrier, provided they preserve the
      carrier endpoint and correspondence data.

  STILL OPEN:
    - construct Qbar and its boundary/properness/self-duality mechanism over
      Z.
```

## 6. Acceptance and kill conditions

```text
ACCEPT-CFC.1  Produce Qbar, Q, dQ, p1, and p2 over Z.
ACCEPT-CFC.2  Construct integral cycles/K-groups and proper pushforwards
              making d1,d2 carrier-native.
ACCEPT-CFC.3  Construct Corr^prop(Qbar) and prove composition by fiber
              product.
ACCEPT-CFC.4  Construct rep_NS, Delta, Gamma_n, and the projection formula
              from the carrier.
ACCEPT-CFC.5  Kill the DD.4 class through boundary localization tied to the
              same carrier.
ACCEPT-CFC.6  Realize D^2=id Rosati and the primitive sign through carrier
              duality.
ACCEPT-CFC.7  Prove DH/Epstein/controls cannot instantiate the carrier
              generators.

KILL-CFC.1    Reject generic span/profunctor/correspondence-bicategory
              language until Qbar and its maps exist.
KILL-CFC.2    Reject symbolic composition on triples unless it is induced by
              proper fiber products on Qbar.
KILL-CFC.3    Reject endpoint labels, parity tags, or degree codecs unless
              d1,d2 are pushforwards along p1,p2.
KILL-CFC.4    Reject DD.4 free splitters, acyclic replacements, or quotient
              tricks unless the killing map is the carrier boundary map.
KILL-CFC.5    Reject Rosati as a chosen metric or abstract adjoint unless it
              is evaluation of an involutive carrier duality.
KILL-CFC.6    Reject any route that remains formable on controls until a
              later positivity, period, quotient, or trace filter.
```
