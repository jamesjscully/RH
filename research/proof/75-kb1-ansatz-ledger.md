# 75 - K_B1 ansatz ledger

Status: construction ledger / no-witness filter, 2026-06-11. This
lists the first natural formula shapes for the S3 `K_B1` blank after
doc 74. It does not admit a B1 candidate and does not authorize a
numerical witness.

## 1. Purpose

Doc 73 preregisters the S3 kernel slot. Doc 74 rules out kernels that
factor only through theta/count/Poisson or generic discrete-measure
shadows. The remaining question is:

```text
Can K_B1 use valuation/depth carrier data in a load-bearing way while
also being a same-form comb-continuum coupling?
```

This ledger records the first ansatz classes and their current
verdicts.

Doc 93 now resolves the free-weight subcase: valuation/depth data do
not advance S3 if the weights, windows, bilinear forms, stress
parameters, determinant presentations, or codomains are externally
chosen rather than trace-derived.
Doc 94 states the positive escape target: a named L1 trace theorem
must derive the same-form object/codomain that reads carrier depth.
Doc 97 rejects trace-derived-looking forms whose naturality domain is
still broad enough to accept represented-norm, commutative-monoid, or
measure shadows for Epstein/DH controls.
Doc 98 states the remaining strict-domain target: a trace domain must
exclude controls at the first carrier-consuming map while still
supporting trace legality, bank embedding, and same-form coupling.
Docs 100-102 add the operation-level audit: if M_C, F_C, or Tr_L is
formed by broad shadow-stable operations before primitive carrier
checking, doc 97 carrier overreach applies; doc 102 applies that audit
to the A0-A6 ansatz classes below.

## 2. Verdict Summary

```text
A0 generic measure/theta/Poisson kernel
  REJECT. This is exactly doc 74.

A0p Poisson-dual comb kernel
  REJECT. This is exactly the B0 Poisson shadow.

A0t theta or represented-norm kernel
  REJECT. This factors through theta/count data.

A1 depth-weighted one-place comb
  HOLD as carrier-selective calibration; not B1 because no same-form
  LS4 coupling/codomain is written. REJECT if the weight is not
  trace-derived by doc 93.

A2 two-place valuation-vector kernel
  HOLD. It uses valuation data, but product-formula constraint and
  same-form codomain are missing. REJECT if the bilinear form/window
  is externally supplied by doc 93.

A3 HH graph-index lift kernel
  HOLD. It is the right D-side shape, but no liquid LS4 trace map or
  lift of the graph-index face is written.

A4 determinant/coker/regularized kernel
  REJECT if built from one shadow object; HOLD only with an
  independently defined carrier-depth domain and non-transport Count.
  REJECT if the determinant wrapper is a free regularization under
  doc 93.

A5 depth-wall stress kernel
  HOLD as diagnostic only; not B1 unless it becomes same-form LS4
  coupling with carrier-selective death. REJECT if the stress rule is
  externally supplied by doc 93.

A6 liquid trace ansatz
  HOLD. Best conceptual shape, but no trace-calibrated subcategory or
  carrier-selective formability theorem is written. REJECT if the
  trace theorem is natural for a broad monoid/measure shadow category
  that still accepts Epstein/DH controls by doc 97.
```

No ansatz is `ADVANCE`.

## 3. A0 - Generic Measure/Theta/Poisson Kernel

Shape:

```text
K_0(C, phi) = <mu_C, phi>
```

or any heat, Gaussian, Fourier, theta, Poisson, LCA/lattice, or
generic discrete-measure variant depending only on the shadow measure
or represented-norm data.

Verdict:

```text
REJECT.
```

Reason: doc 74 applies. The kernel computes for the Epstein
represented-norm shadow because theta/count/Poisson data survive. It
does not die at carrier/effectivity.

Two common subcases are separately rejected:

```text
Poisson-dual comb
  sum_n phihat(n log alpha)
    = (2 pi / log alpha) sum_k phi(2 pi k / log alpha).
  This is B0 calibration. It sees lattice spacing/density, not carrier
  selectivity.

theta / represented-norm kernel
  K_Q(t) = sum_{m in Shadow(C)} exp(-t m), or a log-version over
  represented values.
  This is theta/count data and computes for Epstein.
```

## 4. A1 - Depth-Weighted One-Place Comb

Shape:

```text
K_1(C, phi, w) = sum_k w(depth(k)) phi(ell(k))
```

with:

```text
ell(k) = k log alpha;
depth(k) = v(alpha^k) = k.
```

Possible weights include a frozen polynomial, exponential, or bounded
function of `k`, provided the source of `w` is proof-local and not fit
to zeros or signs.

Verdict:

```text
HOLD.
```

Why it is not rejected immediately: unlike A0, `K_1` explicitly
requires the valuation/depth coordinate. For `Q=x^2+5y^2`, represented
norms have no distinguished atom and no unique tower coordinate, so
the depth field is unformable.

Why it is not B1: this is still one-place carrier calibration. It does
not name a same-form index/Gram/count codomain, a two-place
product-formula coupling, or an LS4 trace map. It may locate a
carrier-selective ingredient, but it is not yet the B1 coupling.

Missing theorem:

```text
T_A1
  A depth-weighted comb must arise from the candidate trace itself,
  not from an externally chosen weight w, and must pair with R on the
  same form.
```

If `w` is arbitrary, fitted, or only coefficient-shadow data, A1 is
rejected by doc 93 as a free-weight carrier readout.

## 5. A2 - Two-Place Valuation-Vector Kernel

Shape:

```text
K_2(C_{p,q}, Phi, B)
  = sum_{a,b in W} B(a,b) Phi(a log p + b log q)
```

where the frozen carrier domain is:

```text
C_{p,q} = (p^a q^b, a, b, a log p + b log q),
```

and `W` plus `B(a,b)` are fixed before computation. A product-formula
constrained version must name the subobject, quotient, kernel, or
relation before any run.

Verdict:

```text
HOLD.
```

Why it is not rejected immediately: the valuation vector `(a,b)` is
load-bearing. Epstein represented norms do not supply a unique
prime-power valuation vector, so this ansatz can in principle die at
carrier/effectivity.

Why it is not B1: `B(a,b)` and the product-formula constraint are not
derived. A freely chosen bilinear form, truncation window, or weight
turns this into calibration. The codomain is also not yet a named
index/Gram/count object in `L1`.

Missing theorem:

```text
T_A2
  The product-formula constrained valuation-vector object is native to
  L1 and the trace pairs it with the continuum on one same-form
  index/Gram/count object.
```

Without that theorem, doc 93 rejects A2 as a free bilinear/windowed
carrier readout.

## 6. A3 - HH Graph-Index Lift Kernel

Shape:

```text
K_3(n, phi)
  = trace_L(b(graph-depth class n), phi_R)
```

where `n` lies in the HH Frobenius-graph/index face and the trace is
supposed to couple the graph class to the archimedean continuum in
`L1`.

Verdict:

```text
HOLD.
```

Why it is not rejected immediately: this is closest to the final D-side
shape. It uses graph-depth carrier data rather than only theta/count
shadows.

Why it is not B1: no liquid lift of the HH graph-index face has been
constructed, no LS4 trace map is written, and no same-form codomain is
named. If `K_3` is implemented merely by re-reading a max-Gram or
theta shadow, docs 70 and 74 reject it.

Missing theorem:

```text
T_A3
  The HH Frobenius-graph/index face embeds conservatively in L1, and a
  liquid trace couples its graph-depth classes to R/T on the same
  index/Gram/count form.
```

## 7. A4 - Determinant/Coker/Regularized Kernel

Shape:

```text
K_4(C) = det_reg(1 - T_C) or coker(1 - T_C)
```

with `T_C` built from the same comb, theta, or trace object.

Verdict:

```text
REJECT
```

if `T_C` is only a presentation of the same shadow data. This is
regularization or determinant algebra on one object; docs 65, 68, and
70 apply.

Conditional status:

```text
HOLD
```

only if the determinant object is defined on a carrier-depth domain
that Epstein cannot form and if any Count/Compare claim has a distinct
natural domain. That extra structure is not currently written.

Missing theorem:

```text
T_A4
  The determinant/coker object is not a re-reading of the same shadow;
  it has a carrier-depth domain and, if promoted to E, an independent
  Count domain.
```

## 8. A5 - Depth-Wall Stress Kernel

Shape:

```text
K_5(C, t) = stress/depth-wall response of the valuation or graph-depth
            classes under a frozen deformation t.
```

Verdict:

```text
HOLD as diagnostic only.
```

Reason: depth-wall and stress data can be useful carrier diagnostics,
but doc 70 blocks promotion of stress flow to P3 or BC13 by re-reading
itself. It becomes B1 only if the stress response is the output of a
same-form LS4 comb-continuum coupling and fails structurally for
Epstein/DH.

Missing theorem:

```text
T_A5
  The stress/depth-wall response is produced by the L1 trace coupling,
  not inserted as a separate diagnostic block.
```

Without that theorem, doc 93 rejects A5 as diagnostic stress data.

## 9. A6 - Liquid Trace Ansatz

Shape:

```text
K_6(C, X)
  = Tr_L(b1(comb_C) acting on a trace-class object X over R_L/T_C).
```

Here `T_C` is not merely a bare circle. It must retain `log alpha` in
metric, liquid analytic-ring, equivariant, density, kernel, or stronger
data before trace evaluation.

Verdict:

```text
HOLD.
```

Why it is the best conceptual shape: it is the only ansatz in this
ledger that directly matches the B1 demand for a trace-calibrated
subcategory and a same-form comb-continuum coupling.

Why it is not B1: no such trace-calibrated subcategory is currently
written. In particular, there is no theorem that:

```text
1. log alpha survives before trace evaluation;
2. b1 preserves prime-power valuation/depth data;
3. the trace/coupling is defined for p^Z carriers;
4. the Epstein replacement has no object on which the same coupling is
   formable while theta/count shadows remain alive.
```

Missing theorem:

```text
T_A6
  A liquid/gaseous trace-class category over R_L/T_C supports a trace
  coupling b1(comb_C) to R_L on one same-form object, and its domain
  requires carrier valuation/depth data.
```

Doc 97 adds the carrier-overreach test: the trace theorem must not be
functorial for a broader represented-norm, commutative-monoid, or
measure-shadow category that also contains the Epstein/DH controls.

## 10. Freeze Obligations For Any HOLD

Before any HOLD ansatz becomes a witness, freeze:

```text
formula:
carrier-depth fields used:
same-form codomain:
source of all weights/constants:
two-place/product-formula constraint, if any:
Epstein formability proof:
DH formability proof or declared not tested:
zero-free supplier ledger:
planned deterministic command:
first zero contact:
```

If any weight, window, deformation, or bilinear form is selected by
numerical convenience, zero agreement, or sign behavior, the ansatz
fails doc 69.

## 11. Program Consequence

The next valid S3 work is now one of:

```text
1. satisfy doc 103 for A1 by naming the strict first map, then satisfy
   doc 94/doc 98 by deriving the depth weight from a candidate-native
   trace;
2. satisfy doc 103 for A2 by making the product-formula constrained
   valuation-vector object a strict first carrier source, then satisfy
   docs 94 and 98;
3. satisfy doc 103 for A3 by making the HH graph-index face a strict
   first carrier object, then construct the liquid lift and same-form
   codomain through docs 94 and 98;
4. state a strict carrier-consuming A6 liquid trace theorem through
   docs 76, 92, 105, and 106, or route broad trace-operation packages
   to docs 105, 107, and 108;
5. prove that all A1-A6 shapes collapse to A0, doc-93 free-weight
   calibration, or doc-97 carrier overreach under the available
   printed trace formalisms, using docs 100-102 for operation-level
   shadow-stability checks;
6. satisfy doc 103, survive docs 109/111/112, and then satisfy doc 98
   by naming a strict Euler-carrier source and first carrier-consuming
   map whose primitive field remains load-bearing downstream, or prove
   that strictness destroys traceability, bank embedding, or same-form
   coupling.
```

Until one of these happens, `K_B1` remains blank and S3 remains `HOLD`.
