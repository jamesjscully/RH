# 73 - S3 kernel preregistration

Status: pre-registration / construction guard, 2026-06-11. This
records the smallest honest S3 kernel target before any new witness is
written. It is not a B1 construction and does not claim an LS4 map.

## 1. Purpose

Doc 72 identifies S3, the explicit comb-continuum kernel slot, as the
nearest buildable direction. The danger is that an ordinary
Poisson/theta kernel will compute equally for prime powers and
Epstein represented norms, proving only carrier-blindness.

This preregistration fixes what must be stated before computation:

```text
1. the carrier interface the kernel is allowed to read;
2. the frozen test family and constants;
3. the pass/fail criteria for the Epstein/DH carrier guard;
4. the boundary between a calibration kernel and an admitted B1 LS4
   coupling.
```

No zeta zeros, zero-side signs, RH-line facts, or fitted constants are
allowed anywhere in this preregistration.

## 2. Frozen Carrier Interface

An S3 kernel may read only the following carrier data.

```text
C = (A, v, depth, ell, mu_C)

A
  a pointed multiplicative carrier with distinguished atom alpha;

v
  a candidate-native valuation/tower coordinate;

depth
  the graph-depth or prime-power exponent k;

ell
  the address map ell(k) = k log alpha;

mu_C
  the comb measure sum_k delta_{ell(k)} on R, with the allowed index
  set stated before computation.
```

For the prime-power carrier:

```text
A_p = {p^k};
alpha = p;
v(p^k) = k;
depth(p^k) = k;
ell(k) = k log p.
```

For a two-place attempt, the interface must be declared before any
witness as either:

```text
product carrier:
  (p^a q^b, a, b, a log p + b log q),

or product-formula constrained carrier:
  a stated subobject/cokernel/kernel of the above.
```

The choice between these two is load-bearing and must be frozen. A
post hoc choice based on signs, zero comparisons, or numerical
behavior is forbidden by doc 69.

## 3. Frozen Test Family

The first admissible test family is deliberately small.

```text
test functions:
  Gaussian probes phi_sigma(x) = exp(-x^2/(2 sigma^2));

sigma list:
  0.37, 0.73, 1.41;

prime list:
  2, 3, 5, 11;

control:
  p and p^2 address spacings, matching B0.
```

These are inherited from the B0 witness. They are calibration probes,
not evidence for RH. They may be changed only by a new preregistration
before any run.

For S3/B1, a second-stage two-place list may be added only after the
carrier interface is written:

```text
prime pairs:
  (2,3), (2,5), (3,5);

allowed depth window:
  explicitly frozen before computation;

product-formula constraint:
  explicitly frozen before computation.
```

No second-stage run is licensed by this document, because the
same-form LS4 coupling is not yet written.

## 4. Kernel Target

The one-place calibration kernel is allowed to be only:

```text
K_C(phi) = <mu_C, phi>
```

and its Fourier/Poisson dual, with the normalization fixed by B0:

```text
sum_n phihat(n log p)
  = (2 pi / log p) sum_k phi(2 pi k / log p).
```

This is not B1. It is the carrier-interface calibration floor.

The B1 kernel target must be stronger:

```text
K_B1(C, phi, psi)
  a same-form comb-continuum coupling whose domain requires the
  carrier interface (A, v, depth, ell, mu_C), and whose codomain is an
  index/Gram/count object named before computation.
```

At preregistration time, `K_B1` is a required blank. Filling that blank
is the next construction task.

## 5. Epstein Guard

The Epstein replacement is fixed as:

```text
Q(x,y) = x^2 + 5y^2;
R_Q = positive represented norms of Q.
```

The guard facts are fixed by doc 64:

```text
1,4,6,9,36 in R_Q;
2,3 notin R_Q;
4,6,9 are irreducible in represented-norm factorization;
36 = 4*9 = 6*6.
```

The required S3 death profile is:

```text
theta/count shadow:
  defined;

carrier interface (A, v, depth, ell, mu_C):
  undefined, because no distinguished atom and no unique tower
  coordinate are available;

failure point:
  carrier/effectivity before signs.
```

Pass/fail rule:

```text
PASS as carrier-selective preregistration
  K_B1 requires (A, v, depth, ell), and those fields are unformable for
  R_Q while theta/count remains meaningful.

FAIL as carrier-blind
  K_B1 can be evaluated using only represented norms, theta values,
  Poisson summation, density, or a generic discrete measure.

HOLD
  K_B1 is not written, or the failure point is not proved.
```

The current status is `HOLD`.

## 6. DH Guard

The DH control must be named before a run. At minimum the record must
state:

```text
DH carrier data:
  what replaces A, alpha, v, depth, ell;

expected death point:
  no carrier | no effectivity | computes;

theta/count shadow:
  alive | absent | not applicable.
```

No DH test is licensed until this replacement is defined. A kernel
that computes for DH using the same generic theta/Poisson interface is
carrier-blind.

## 7. Zero-Free Freeze

Before a witness is written, freeze:

```text
kernel formula:
  exact symbolic expression for K_p(x,n), K_C(phi), K_B1, or the
  equivalent operator;

formula source:
  proof-local definition, citation, or derivation;

carrier interface:
domain:
  p^Z or p^N and the tower coordinate/depth convention;

continuum variable:
  explicit R or R/T variable;

test functions:
sigma list:
prime list:
prime-pair list, if any:
depth window, if any:
product-formula constraint, if any:
normalization constants:
constant sources:
  no fitted constants;

count layer:
  what is counted, and whether it is only B0-style Count0;

Epstein replacement:
DH replacement:
expected death profiles:
planned deterministic command:
input data hashes, if any:
first zero contact:
```

The current first zero contact is:

```text
after frozen record and witness output; zero comparison is otherwise
forbidden for S3 preregistration.
```

If any constant, depth window, test function, kernel term, or carrier
choice is selected by fit to zero-side data, the preregistration fails
doc 69.

The freeze record must also state that no `fork_lib.zeta_gammas`, zero
tables, explicit-formula signs, RH-line facts, or zero-side validation
were used before the frozen record.

## 8. Overclaim Guard

The following claims are explicitly not licensed.

```text
Not licensed:
  K_C Poisson calibration is LS4.

Not licensed:
  one-place p^Z comb address is a candidate-native unit.

Not licensed:
  theta/count survival for Epstein is carrier selectivity.

Not licensed:
  failure of represented-norm unique factorization proves RH content.

Not licensed:
  any finite window proves BC13 or P3.

Not licensed:
  numerical agreement as structure before the freeze ledger is
  complete.
```

The only licensed conclusion is:

```text
An S3 witness may be written only after K_B1 is specified and the
Epstein/DH death profiles are frozen as formability tests.
```

## 9. Next Construction Task

The next valid construction task is narrow:

```text
Write the doc-103 strict first carrier-consuming map kappa_C, whose
source object S_C requires the frozen carrier interface
(A, alpha, v, depth, ell, mu_C) before M_C, F_C, or Tr_L exists.
```

If no such first map can be written without forming M_C, F_C, or Tr_L by
a generic theta/Poisson/measure/kernel/determinant/trace-class shadow
operation first, S3 remains `HOLD` or routes to docs 100-102 as
carrier-overreach. No numerical run should occur before that fork.

Doc 74 proves the generic-kernel side of this fork: kernels factoring
only through theta/count/Poisson or discrete-measure shadows are
carrier-blind.

Doc 93 proves the next false-positive boundary: kernels that mention
valuation/depth but read them through externally supplied weights,
windows, bilinear forms, stress parameters, determinant wrappers, or
codomains are free-weight calibration, not B1.

Doc 94 states the remaining positive escape target: the S3 form and
codomain must be derived by a named L1 trace theorem on a mixed object
M_C, not supplied externally.

Doc 97 adds the overreach guard: even trace-derived forms fail S3 if
their naturality domain still accepts represented-norm,
commutative-monoid, or measure shadows for Epstein/DH controls.

Doc 98 names the only remaining strict-domain escape: an Euler-carrier
trace domain `ECar_L1` that excludes Epstein/DH at the first
carrier-consuming map while preserving trace legality, bank embedding,
same-form coupling, and freeze.

Docs 100-102 prove and apply the shadow-stability rejection for mixed
objects, codomains, or traceable objects formed before primitive carrier
checking.

Docs 103-104 give the positive-side first-map record and the current
filled ledger: no A1-A6 class has `FIRST_MAP_PASS`.

Doc 75 records the remaining ansatz classes after doc 74. None is
currently advanced to a witness.
