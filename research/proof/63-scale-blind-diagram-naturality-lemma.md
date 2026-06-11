# 63 - Scale-blind diagram naturality lemma

Status: proof lemma for doc 51, 2026-06-11. This records the local
argument isolated by the citation audit in doc 62: the full bare
lattice diagram `lZ -> R -> R/lZ` is scale-blind before any metric,
liquid analytic-ring, equivariant, or kernel structure is added.

## 1. Statement

For `l > 0`, define the bare topological diagram:

```text
D_l:
  lZ -> R -> R/lZ.
```

The first map is inclusion and the second is quotient. Let `C` be a
fixed dualizable coefficient category. Let `F` be an accessible or
finitary localizing invariant for which the continuous extension
`F^cont` is defined on the sheaf categories in the diagram.

Assume the proposed observable is built naturally from:

```text
F^cont(Shv(lZ; C)),
F^cont(Shv(R; C)),
F^cont(Shv(R/lZ; C)),
and the maps induced by D_l.
```

Then the observable is independent of `l`.

Equivalently, the functorial localizing-invariant image of the bare
diagram `D_l` is equivalent to that of:

```text
D_1:
  Z -> R -> R/Z.
```

If `R` is contracted to its proper-homotopy value under the Efimov
line computation, this is the p-independent homotopy diagram:

```text
Z -> * -> BZ.
```

## 2. Proof

For `l > 0`, define maps:

```text
a_l: lZ -> Z,       a_l(ln) = n;
b_l: R  -> R,       b_l(x) = x/l;
c_l: R/lZ -> R/Z,   c_l([x]_l) = [x/l]_1.
```

These are homeomorphisms. They commute with inclusion and quotient:

```text
b_l(ln) = n = a_l(ln),
c_l([x]_l) = [b_l(x)]_1.
```

Thus `D_l` and `D_1` are isomorphic as diagrams of bare topological
spaces.

Applying `Shv(-; C)` and then `F^cont` gives equivalent diagrams of
localizing-invariant values, by functoriality and invariance under
isomorphism of the input diagrams. Therefore any natural operation or
trace built only from these values and maps takes the same value on
`D_l` and `D_1`.

This proves scale-blindness for the full bare diagram.

## 3. Relation To Efimov Citations

The diagram lemma itself is elementary at the level of bare topological
diagrams: scaling gives an isomorphism `D_l ~= D_1`.

Efimov's results supply the localizing-invariant computations used by
doc 51:

```text
Theorem 6.1
  F^cont(Shv(R/lZ; C)) ~= F^cont(C)^{S^1}
  because R/lZ is a finite CW complex with homotopy type S^1.

Proposition 4.18
  U^cont_loc(Shv(R; C)) ~= Omega U^cont_loc(C).

Theorem 0.2 / 6.11
  Localizing invariants of sheaves on locally compact Hausdorff spaces
  are computed by compactly supported sections of the invariant of
  the coefficient data, under the stated finitary hypotheses.
```

Thus the complete proof of doc 51 has two parts:

```text
1. Efimov computes the localizing-invariant values.
2. The scaling isomorphism above shows the whole bare diagram is the
   same for every l before metric/enriched data is added.
```

## 4. What The Lemma Does Not Cover

The lemma applies only to the bare diagram of topological spaces with
constant coefficients. It does not cover:

```text
metric R with a fixed length scale;
liquid/gaseous analytic-ring modules whose norms depend on l;
equivariant or parametrized traces over the group object R/lZ;
density data retaining l;
explicit kernels that use l before passing to localizing invariants;
same underlying spaces equipped with non-isomorphic enrichment.
```

Those are exactly the escape hatches in doc 51 and G60.2-G60.5.

## 5. Program Consequence

The full diagram claim in doc 51 no longer needs to be read as a
separate external citation. It is a local lemma:

```text
bare topology + constant coefficients + localizing-invariant functoriality
  => no log p in the diagram.
```

A candidate that wants to retain `log p` must name the enriched datum
before applying the trace. Appending `log p` after computing this
scale-blind diagram is external normalization, not candidate-native
structure. Doc 80 records this late-insertion consequence as a
standalone gate.
