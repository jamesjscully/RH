# 66 - Unit covariance and threading lemma

Status: proof lemma for docs 55 and 60, 2026-06-11. This isolates the
C-side lesson from docs 43 and AB: signs or constants depending on a
chosen continuum unit are slot coordinates, while the live object-level
C-claim is local k=1 deficit plus global threading plus unit-free depth
wall.

## 1. Statement

Let `U` be a continuum unit used to compute local slot constants,
cell signs, payment margins, or Mellin/Fourier values. Suppose a
claimed obstruction `O(U)` changes under replacement of `U` by another
admissible self-dual unit while the carrier class and prime-power data
are unchanged.

Then `O(U)` is unit-slot data. It is not an object condition for the
missing structure.

Conversely, a C-side condition may be promoted only if it is either:

```text
1. derived from the candidate's own internal unit;
2. invariantly stated across admissible units; or
3. unit-free in covariant coordinates.
```

## 2. Decisive Banked Comparison

Doc 43 compares the Gaussian unit with AB's admissible self-dual
Hermite unit:

```text
f_C(x) = e^{-pi x^2}(1 + eps H4(sqrt(2pi)x))/(1+12eps),
eps = 1/100,
fhat_C = f_C.
```

The banked Gaussian decision cell:

```text
m+_gauss((11;2), 4.96) = -2.214249e-3
```

flips under the Hermite unit:

```text
m+_Hermite((11;2), 4.96) = +2.0913e-4.
```

The carrier class did not change. The unit slot changed. Therefore the
sign of this deep cell is not invariant object data.

The same comparison preserves the depth-wall reading:

```text
needed e^{-8} / (rho ~ Lambda^2) = 0.998..1.000
```

for the tested Gaussian and Hermite units. Thus the wall is the
object-level residue, while the named deep breaking phase is slot data.

## 3. Proof Of The Covariance Lemma

An object condition must be a property of the candidate object, not of
a chosen coordinate in the unit slot. If:

```text
O(U_1) != O(U_2)
```

for two admissible units `U_1` and `U_2` while the carrier, class, and
prime-power address are fixed, then `O` is not well-defined on the
candidate object before choosing a unit. It is a function on the pair:

```text
(candidate shadow, chosen unit).
```

A theorem depending on `O(U_1)` therefore proves a statement about that
presentation. It does not prove a unit-independent object condition.

To promote `O`, one must either:

```text
derive U as part of the object;
prove O is invariant under admissible replacement;
or restate O covariantly so its truth does not depend on the chosen
coordinate.
```

This proves the covariance lemma.

## 4. One-Place Threading Lemma

Let a construction have only one local place in its natural domain:

```text
{p, p^Z comb, local trace/count slot}.
```

Then it cannot prove global threading. The reason is structural: there
is no object or map in the domain that can transfer surplus across
places. The construction lacks:

```text
two or more places;
product-formula relation;
KMS-beta=1/2 global assembly;
cross-place comparison map.
```

Therefore a one-place construction can record local deficit or local
calibration, but it cannot establish doc-45 C3.

## 5. Surviving C-Side Normal Form

After unit covariance and one-place filtering, the live C-side normal
form is:

```text
C1 integer charge
  The d=1 / Lambda(p) continuum hole has charge -1, while truncation
  bands are 0-charge bookkeeping.

C2 local deficit
  The k=1 / Lambda(p)-class deficit is per-place unpayable in the
  candidate's covariant coordinates.

C3 global threading
  The KMS-beta=1/2 global aggregate pays local deficits by moving
  surplus across places through product-formula assembly.

C5 depth wall
  The exponential Frobenius-depth demand versus linear window supply is
  unit-free in covariant units, with law constant 1.
```

Demoted from object status:

```text
specific Gaussian deep-cell negativity;
specific Hermite deep-cell positivity;
Gaussian shape constants;
payment constants tied to an inserted unit;
one-place Poisson normalizations;
strict repair atoms.
```

## 6. Candidate Gate

Before promoting any C-side claim, require:

```text
G66.1 Unit status
  Is the unit candidate-native, or is the claim stated covariantly
  across admissible units?

G66.2 Slot test
  Does the claim change under admissible self-dual unit replacement?
  If yes, demote to slot data.

G66.3 Threading domain
  Does the construction contain a cross-place product-formula or
  KMS-beta=1/2 assembly map?
  If no, reject global-threading promotion.

G66.4 Depth wall
  Is the wall expressed without choosing Gaussian slot coordinates?
  If no, restate in covariant coordinates before promotion.
```

## 7. Escape Profile

A candidate escapes this no-go only by supplying:

```text
E1 internal unit
  U is derived by LS3-style internal Fourier self-duality, with
  normalization torsor pinned by internal R/T rigidity; or

E2 unit-covariant theorem
  the C-side claim is invariantly stated and proved over the
  admissible unit family; and

E3 threading assembly
  local deficits and global payability are both native statements of a
  multi-place object with product-formula/KMS-beta=1/2 structure.
```

## 8. Program Consequence

Doc 55 can now be read as an application of this lemma:

```text
unit-dependent sign or constant => slot data;
one-place local bookkeeping => not global threading;
unit-free depth wall + cross-place payability => live C-side target.
```

The next valid C-side construction work is not to find another
negative Gaussian cell. It is to derive the candidate's own unit and
prove the local-deficit/global-threading statement in its covariant
coordinates.
