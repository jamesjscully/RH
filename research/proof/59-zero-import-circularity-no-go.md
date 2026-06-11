# 59 - Zero-import circularity no-go

Status: protocol no-go gate, 2026-06-11. This turns T48.8 into a
standing theorem-shaped filter. It rules out candidates that read zeta
zeros, zero-side signs, zero-side eigenvalues, or RH-line information
before constructing the carrier, odd slot, and comparison theorem. Doc
69 isolates the reusable zero-free freeze normal form behind this gate.

## 1. Statement

Let a proposed candidate attempt to supply the doc-45 package:

```text
carrier + liquid address + derived unit + Frobenius action
+ nonempty odd slot + forced-nonnegative index/Gram
+ independent Count evaluation + Compare.
```

Assume that before these objects are constructed, the proposal uses
zero-side data to choose, tune, or define any of the following:

```text
1. eigenvalues or spectral parameters of H_odd;
2. signs, positive cones, or repair terms;
3. class families or selected test loci;
4. normalization constants, units, scales, or phases;
5. the comparison theorem or agreement locus;
6. coefficients whose only source is the explicit formula's zero side.
```

Then the proposal is circular. It cannot satisfy doc 45 E3 or E4, and
it cannot serve as a supply-side proof of RH.

Zero data may be used only after the candidate-side objects and loci
are frozen, and only for comparison or fork diagnosis.

## 2. Local Protocol

Doc 14 is the standing fork protocol. Its key point is conservation:
every quantity built from the explicit-formula ingredients is
transported losslessly to a zero-side functional. Therefore matching a
zero-side image is not by itself new structure; it may be only a
coordinate change.

The permitted zero contact is:

```text
comparison only:
  after the candidate quantity Q is defined without zeros, compute its
  zero-side image through fork_lib.zero_gram or a comparable fork tool.
```

The forbidden zero contact is:

```text
construction input:
  read zeta zeros, zero-side signs, zero-side eigenvalues, or RH-line
  information before defining Q, then use them to choose Q.
```

The HANDOFF freeze rule records the operational version:

```text
freeze loci and hash them before fork_lib.zeta_gammas is imported;
comparison only after the freeze.
```

## 3. Proof

Doc 45 E3 requires:

```text
The odd-slot eigenvalues must be supplied by the carrier/slot
structure independently of the acting map. The acting correspondence
queries them; it does not define them.
```

If zero-side data supplies the eigenvalues or spectral parameters, then
the carrier/slot did not supply them. E3 fails.

Doc 45 E4 requires:

```text
The agreement between evaluations must consume mathematics beyond the
definitions of the two sides.
```

If the agreement locus, class choices, signs, or comparison theorem are
chosen from the zero side, then the comparison is not a supply-side
theorem. It imports the target spectral answer into the construction.
E4 fails.

Doc 14 adds the fork consequence. If a candidate quantity is defined
from explicit-formula data and then matches its zero-side image, the
match shows that the candidate is in the EF orbit unless it also
contains extra information and existence-selectivity. If the zero-side
image was used to build the candidate, even that fork diagnosis is
invalid: the construction has already consumed the answer.

Thus zero import before construction is circular.

## 4. Allowed Uses Of Zero Data

The following are allowed and useful.

```text
A1 fork comparison
  Define Q without zero data, freeze the construction, then compare Q
  to fork_lib.zero_gram. A tight match demotes Q to EF-derived
  coordinates; a mismatch may identify extra structure or a bug.

A2 post hoc sanity check
  After proving a candidate-side theorem, compare its predicted
  spectral behavior against known zeros to check normalization.

A3 negative control
  Use DH, beta != 1/2, smooth surrogates, or other deformation kills to
  test overreach. This is not zero import when the candidate was built
  before the control.

A4 implication audit
  Use zero-side logic to ask whether the constructed package would
  imply RH. This is an implication check, not construction input.
```

The following are forbidden.

```text
F1 eigenvalue import
  Set H_odd eigenvalues equal to zeta zero ordinates, zero-side
  spectral parameters, or fitted zero data.

F2 sign import
  Choose positive cones, repair atoms, phases, or units because they
  match zero-side signs.

F3 locus import
  Select class families, windows, or test points after looking at zero
  data.

F4 normalization import
  Choose kappa, a Gaussian scale, a Haar density, or a phase using the
  zero side.

F5 theorem import
  Define Compare by analytic continuation or explicit-formula equality
  whose load-bearing input is the zero expansion.
```

## 5. Candidate Gate

Before a candidate is allowed to claim E-grade content, require this
ledger.

```text
G59.1 Construction freeze
  List the files, formulas, loci, class families, and constants that
  define the candidate before any zero data is loaded.

G59.2 Hash or reproducibility record
  Record a hash, deterministic witness output, or proof-local
  statement fixing those choices.

G59.3 Zero-contact point
  State the first point at which zero data, fork_lib.zeta_gammas, or a
  zero-side identity enters.

G59.4 Role of zero data
  Classify the role as comparison, sanity check, deformation control,
  implication audit, or construction input.

G59.5 Supplier audit
  Prove that H_odd eigenvalues, signs, unit, class family, Count, and
  Compare were supplied before zero contact.
```

If G59.4 is construction input, reject. If G59.5 fails, reject or
demote to explicit-formula transport.

## 6. Relation To The Fork Protocol

The zero-import no-go and fork protocol are complementary.

```text
Fork F1:
  If a frozen candidate matches its zero-side image, it is EF-derived
  unless it carries extra information.

Zero-import gate:
  If the candidate was not frozen before zero contact, it never reaches
  F1 as a legitimate supply-side object.
```

Passing the zero-import gate does not prove independence. It only
means the candidate is allowed to be fork-tested. It must still pass
doc-14 P1/P2, doc-52 P3 independence, and the carrier/positivity gates.

## 7. Escape Profile

A candidate escapes this no-go only by satisfying all of the following.

```text
E1 zero-free construction
  Carrier, address, unit, H_odd, index/Gram value, Count, and Compare
  are defined without zeta zeros or RH-line information.

E2 frozen choices
  Loci, classes, constants, and witnesses are fixed before zero-side
  comparison.

E3 independent supplier
  H_odd eigenvalues are supplied by the carrier/slot, not by imported
  zero ordinates or fitted spectral data.

E4 comparison role
  Any later zero contact is comparison, fork diagnosis, or implication
  audit only.
```

This is a minimal protocol escape. The candidate still has to satisfy
the substantive A-E clauses.

## 8. Program Consequence

T48.8 is now a standing gate:

```text
No zero-side data before construction freeze.
No zero-side eigenvalues as H_odd.
No zero-side signs as positivity.
No zero-side tuning as unit derivation.
```

The explicit formula may verify, compare, or diagnose. It may not
construct the missing object. See doc 69 for the protocol normal form.
