# 173 - PFV2 GPF residual monodromy filtration bookkeeping collapse

Status: bounded no-go from the PFV2-GPF-RMON-FILT-SELECT target /
Q134.1 internal result, 2026-06-12. This is not a B1 construction, not
an external answer, and not a witness license. It kills only filtered
action proposals where the filtration is degree/order/valuation
bookkeeping already determined by scalar product-formula data, p,q
marking, or complement readout.

## 1. Purpose

Doc 172 writes the filtered action shot:

```text
PFV2-GPF-RMON-FILT(p,q).
```

The first false positive is bookkeeping filtration: `Fil_C` is named,
but it is just a degree, order, valuation, support, or layer index
already determined by scalar PF, p,q marking, complement bookkeeping,
or the assembled all-places object. This document rejects that class.

## 2. Covered Class

Call a proposal `PFV2_GPF_FILT_book` if it satisfies all of:

```text
D173.1 filtered syntax
  The proposal names Fil_C, rho_G^{fil}, and kappa_G^{fil} before an
  assembly functor.

D173.2 bookkeeping filtration
  Fil_C is fully determined by one of:
    p,q valuation labels or lengths;
    scalar product-formula balance;
    complement degree/order/support bookkeeping;
    an already assembled all-places filtration;
    a filtration functorial for broad marked local diagrams.

D173.3 no structural complement residue
  No theorem shows that changing the internal complement structure
  while fixing scalar PF, p,q marking, and complement degree changes
  Fil_C or rho_G^{fil}.

D173.4 inherited first map
  kappa_G^{fil} factors through the bookkeeping filtration, scalar PF,
  p,q marking, complement readout, or D after forgetting object-level
  filtered action data.

D173.5 downstream bookkeeping
  M_C/F_C/Tr_L sees only D, scalar PF, p,q marking, complement degree,
  or the bookkeeping filtration.
```

This class includes:

```text
degree filtrations of the complement;
support/order filtrations determined by valuation labels;
filtrations by scalar product-formula defect;
assembled all-places filtrations with p,q marks;
broad functorial filtrations available to local-shadow controls.
```

## 3. Lemma

### Lemma 173.1

`PFV2_GPF_FILT_book` does not satisfy PFV2-GPF-RMON-FILT-SELECT.

Verdict:

```text
REJECT_FILT_BOOKKEEPING
  if Fil_C is only degree/order/valuation/support bookkeeping
  determined by scalar PF, p,q marking, complement readout, or D.

REJECT_FILT_INHERITED_MAP
  if kappa_G^{fil} factors through bookkeeping data after forgetting
  object-level filtered action residue.

REJECT_FILT_DOWNSTREAM_BOOK
  if downstream sees only D, scalar PF, p,q marking, complement degree,
  or the bookkeeping filtration.

HOLD_FILT_STRUCTURAL
  if a later proposal supplies a filtration whose layers are structural
  complement objects not determined by scalar/readout data.
```

### Proof

PFV2-GPF-RMON-FILT-SELECT requires `Fil_C` to be source-native
structure of the complement. It is not enough to attach a filtration
that can be read off from scalar PF, p,q labels, degree, support, or
the assembled object.

Under D173.1-D173.2, the proposal has filtered syntax but no
structural residue. The filtration is recovered from bookkeeping data
already available to scalar or marked descriptions. Such a filtration
does not make the p/q commutator a new source primitive.

Under D173.3, the filtration is insensitive to internal complement
structure. If changing the complement while holding scalar PF, p,q
marking, and complement degree fixed does not change `Fil_C` or
`rho_G^{fil}`, then the residue is not object-level.

Under D173.4, the first map is inherited from bookkeeping data. After
forgetting object-level filtered action residue, `kappa_G^{fil}`
still factors through the same scalar/readout filtration.

Under D173.5, downstream dependence fails. If M_C/F_C/Tr_L sees only
the bookkeeping filtration, scalar PF, p,q marking, or D, doc 111
rejects the route.

Therefore bookkeeping filtrations do not satisfy
PFV2-GPF-RMON-FILT-SELECT. QED.

## 4. What Bookkeeping Filtrations Still Supply

Allowed:

```text
normalization checks for a later structural filtration;
diagnostics for whether a proposed Fil_C is scalar/readout determined;
compatibility conditions after a stricter filtered residue passes;
examples for external questions about what does not count.
```

Not allowed:

```text
claiming PFV2-GPF-RMON-FILT-SELECT;
claiming FIRST_MAP_PASS;
claiming control non-formability;
running an A2 witness;
promoting degree/order/valuation bookkeeping to complement structure;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 filtered-action route is:

```text
PFV2-GPF-RMON-FILT-STRUCT.
```

The target:

```text
There is a structural filtration, grading, or layer decomposition
Fil_C^{str} of C_{not p,q} inside the p,q+complement GPF source such
that Fil_C^{str} is not determined by scalar PF, p,q marking,
complement degree/order/support bookkeeping, broad marked local
diagrams, or the assembled all-places object.

The p/q commutator induces a filtered action residue rho_G^{str};
changing the structural filtration or residue while holding D, p,q
marking, scalar PF, complement bookkeeping, and presentation data fixed
changes kappa_G^{str} or its target; Epstein/DH controls cannot form
the same filtered residue; B0_p and B0_q embed conservatively; and
rho_G^{str} remains load-bearing in M_C/F_C/Tr_L.
```

This is narrower than PFV2-GPF-RMON-FILT-SELECT because it removes
degree/order/valuation/support bookkeeping filtrations.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named structural filtration
proposal:

```text
KILL-FILT-STRUCT.1 bookkeeping collapse
  The proposed Fil_C^{str} is determined by scalar PF, marking,
  complement degree/order/support, broad marked diagrams, or D.

KILL-FILT-STRUCT.2 control formability
  Epstein/DH controls can instantiate the same structural filtration,
  filtered residue, and first map while retaining theta/count shadows.

KILL-FILT-STRUCT.3 inherited first map
  kappa_G^{str} is unchanged when the structural filtration/residue is
  changed while D, marking, scalar PF, complement bookkeeping, and
  presentation data are fixed.

KILL-FILT-STRUCT.4 bank replacement
  the structural filtration requires replacing B0_p/B0_q by a full
  global source.

KILL-FILT-STRUCT.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets the structural filtered residue.
```

Do not apply these beyond the named structural filtration proposal.

## 7. Board Update

```text
PFV2_GPF_FILT_book:
  REJECT_FILT_BOOKKEEPING.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-FILT-STRUCT or another
  structural filtered p,q+complement GPF action class.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 172
  Supplies PFV2-GPF-RMON-FILT(p,q) and the
  PFV2-GPF-RMON-FILT-SELECT target.

doc 171
  Rejects scalar/abelian/bookkeeping commutators.

doc 154
  Rejects residual fields that are only marking or bookkeeping.

doc 159
  Rejects broad carrier-torsor/groupoid packages formable by controls.

doc 111
  Still blocks downstream forgetfulness.
```
