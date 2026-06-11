# 117 - A2 two-place calibration record

Status: smallest post-B0 calibration record / no-witness ledger,
2026-06-11. This fills one concrete doc-103/doc-113 route at record
level. It is not a B1 construction and does not license computation.

## 1. Purpose

Doc 116 says the next honest construction-side move is not a witness.
It is to fill one strict-route record and classify it. This document
chooses the smallest nontrivial slot:

```text
A2 two-place valuation-vector kernel.
```

The point is to record exactly what the program currently can and
cannot name after B0.

## 2. Calibration Object

The calibration object is only a routed pre-object:

```text
C117(A2) =
  (B0_p, B0_q, intended valuation-vector source,
   intended product-formula constraint, control profile, route verdict).
```

where:

```text
B0_p, B0_q
  Two copies of the B0 Tate/RR calibration data from doc 49:
  p^Z and q^Z comb addresses, RR/Serre trace shadows, Count0 layers,
  and Epstein guard data.

intended valuation-vector source
  A would-be source S_C whose primitive fields should include
  alpha_p, alpha_q, v_p, v_q, ell_p=log p, ell_q=log q, and a
  two-place carrier-depth coordinate.

intended product-formula constraint
  A would-be first map kappa_C should consume the two-place valuation
  vector before any kernel, bilinear form, codomain, determinant, or
  trace package exists.

control profile
  Epstein/DH controls are required to keep theta/count shadows but fail
  to form the same primitive valuation-vector source or kappa_C.
```

This is larger than B0 because it asks for a two-place carrier field
and product-formula constraint. It is smaller than B1 because it does
not assert L1, Tr_L, M_C, F_C, LS3, LS4, positivity, odd slots, Count,
Compare, or a zero-side contact.

## 3. Filled Doc-103 Record

```text
candidate:
  C117(A2) two-place valuation-vector calibration record

ansatz class:
  A2 two-place valuation-vector kernel

source theorem:
  none. B0 supplies only one-place calibration data.

ECar_L1 source:
  category/subcategory:
    not named.
  object S_C:
    not named as an object in a strict carrier category.
  primitive fields present before maps:
    intended fields are alpha_p, alpha_q, v_p, v_q, ell_p, ell_q,
    and two-place carrier depth.
  proof these are object data, not labels:
    absent.

first carrier-consuming map:
  name kappa_C:
    not named.
  source:
    intended S_C only.
  target:
    not named.
  exact primitive field consumed first:
    intended product-formula constrained valuation vector.
  why kappa_C is before M_C/F_C/Tr_L:
    not proved; this is the missing theorem.
  proof before M_C? NO.
  proof before F_C? NO.
  proof before Tr_L? NO.
  operation type:
    intended first carrier constraint, not a kernel operation.
  functoriality domain:
    not named.

operation audit before kappa_C:
  tensor/product used before first map? NO by intention, not theorem.
  sum/completion/pushforward/coend used before first map? NO by
    intention, not theorem.
  kernel/correspondence/determinant/cokernel used before first map? NO
    by intention, not theorem.
  trace-class closure used before first map? NO by intention, not
    theorem.
  doc100/doc101 escape reason:
    incomplete until S_C and kappa_C are named independently of the
    later kernel package.

B0 bank embedding before kappa_C:
  p^Z comb preserved:
    intended from B0_p and B0_q.
  q/log p address preserved:
    intended for both places.
  Count0/RR layer preserved:
    intended for both places.
  graph-depth data preserved, if claimed:
    not claimed.
  Epstein guard preserved as control test:
    intended from docs 49 and 64.

control exclusion at kappa_C:
  Epstein represented-norm shadow exists? YES.
  Epstein S_C object? UNKNOWN.
  Epstein kappa_C formable? UNKNOWN.
  exact failed field or axiom:
    expected missing free rank-one valuation tower, but not proved at
    S_C/kappa_C level.
  DH shadow exists? YES at theta/count level.
  DH S_C object? UNKNOWN.
  DH kappa_C formable? UNKNOWN.
  exact failed field or axiom:
    expected missing Euler-product carrier, but not proved at
    S_C/kappa_C level.

post-kappa construction:
  M_C operation:
    not written.
  F_C operation:
    not written.
  trace theorem:
    not written.
  why docs 100-102 do not apply:
    not yet established.

downstream obligations, not yet promotion:
  trace legality still needed:
    YES.
  conservative B0 bank embedding still needed:
    YES.
  same mixed M_C still needed:
    YES.
  trace-derived F_C still needed:
    YES.
  zero-free freeze still needed:
    YES.

freeze:
  S_C frozen before zero contact:
    NO.
  kappa_C frozen before zero contact:
    NO.
  control exclusions frozen before zero contact:
    NO.
  first zero contact:
    none.

verdict:
  FIRST_MAP_HOLD.
```

## 4. Why This Is Honest Calibration

This record does not add a formula. It calibrates the A2 route by
showing the exact point where B0 data stops being enough:

```text
B0 supplies one-place comb and count shadows.
C117 needs a two-place strict source and first carrier-consuming map.
The program does not currently have either theorem.
```

The expected Epstein/DH death point is also not promoted. It remains a
target:

```text
theta/count shadows survive;
free valuation-vector source and kappa_C should fail;
failure must be proved before M_C/F_C/Tr_L.
```

Until that proof exists, the control row is UNKNOWN, not PASS.

## 5. Route Through Doc 113

```text
Step 0 existing broad no-goes:
  no rejection yet if no kernel, bilinear form, determinant, or trace
  package is formed before kappa_C.

Step 1 first-map record:
  doc 103 -> FIRST_MAP_HOLD.

Step 2 relabeling guard:
  not triggered only because no S_C is claimed. If S_C is later just
  decorated B0_p x B0_q shadow data, doc 109 rejects it.

Step 3 downstream dependence guard:
  not reached. If a future kappa_C is named and then forgotten before
  M_C/F_C/Tr_L, doc 111 rejects it.

Step 4 late-reintroduction guard:
  not reached. If the kernel/trace package is built first and carrier
  fields are added later, doc 112 rejects it.

Step 5 strict-domain target:
  not reached.

Step 6 trace-derived codomain target:
  not reached.
```

Therefore the local route verdict is:

```text
A2 C117 route:
  HOLD_STRICT_ROUTE, no witness.
```

## 6. Next Falsifiable Question

The next useful question is not "can one write a two-place kernel?"
That is too easy and routes to doc 93. The falsifiable question is:

```text
Can a strict source category ECar_L1 and first map kappa_C be named
where the product-formula constrained valuation vector is object data
and is consumed before any mixed object, codomain, determinant, kernel,
or trace package exists?
```

Decision:

```text
ADVANCE
  Name S_C and kappa_C, prove primitive fields are object data, and
  prove Epstein/DH cannot form S_C or kappa_C.

KILL
  Prove every such two-place source/map is either decorated shadow
  data, a broad product/kernel operation, or downstream-forgetful.

SHARPEN
  Name the exact source-category axiom or product-formula theorem that
  decides whether S_C and kappa_C exist.
```

## 7. Use Rule

Use this record as the smallest construction-side calibration after
B0. Do not run a numerical A2 witness from it. A future A2 witness
requires at least:

```text
FIRST_MAP_PASS in doc 103;
no docs 109, 111, or 112 rejection;
PASS_STRICT_EULER in doc 98;
PASS_TRACE_DERIVED in doc 94;
doc 71 B1 fields filled without HOLD rows.
```
