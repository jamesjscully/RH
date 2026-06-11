# 62 - Scale-blind citation audit

Status: citation/dependency audit, 2026-06-11. This hardens doc 51 by
checking its Efimov dependencies against the archived PDF
`research/proof/refs/efimov-2024-k-theory-localizing-invariants-large-categories.pdf`
and the local transcriptions in XX/MM.

## 1. Purpose

Doc 51 is the closest broad gate to a citable theorem. The audit asks:

```text
Which parts of the scale-blind localizing-trace no-go are directly
backed by archived source statements, and which parts are derived
program lemmas that still need formal proof wording?
```

## 2. Archived Source Checked

Local source:

```text
research/proof/refs/efimov-2024-k-theory-localizing-invariants-large-categories.pdf
```

Extraction command:

```text
pdftotext research/proof/refs/efimov-2024-k-theory-localizing-invariants-large-categories.pdf - |
  rg -n -C 4 "Theorem 0\\.2|Proposition 4\\.18|Theorem 6\\.1|Theorem 6\\.11"
```

PDF metadata:

```text
file: efimov-2024-k-theory-localizing-invariants-large-categories.pdf
pages: 133
creation date in metadata: 2025-02-06
```

The text extraction has encoding artifacts, but the theorem labels and
formulas are legible and match the XX transcription.

## 3. Directly Verified Statements

### Theorem 0.2

Verified in the archived extraction:

```text
Theorem 0.2. With the above notation, let E be a presentable stable
infinity-category, and F : Cat^perf -> E a localizing invariant which
commutes with filtered colimits. Then we have a natural isomorphism

    F^cont(Shv(X; C)) ~= Gamma_c(X, F^cont(C)).
```

Local transcription in XX matches this statement.

Use in doc 51:

```text
legitimate for finitary / filtered-colimit-preserving localizing
invariants on locally compact Hausdorff spaces with dualizable
coefficient presheaves.
```

### Proposition 4.18

Verified in the archived extraction:

```text
Proposition 4.18. For a dualizable category C we have

    U^cont_loc(Shv(R; C)) ~= Omega U^cont_loc(C)

and a second vanishing statement for R union {-infty}.
```

The extraction also shows the surrounding paper later notes this result
feeds Theorem 6.1.

Use in doc 51:

```text
legitimate for the line component of the lattice diagram after
applying the continuous localizing motive or localizing invariant.
```

### Theorem 6.1

Verified in the archived extraction:

```text
Theorem 6.1. Let X be a finite CW complex, considered as a topological
space. Let C be a dualizable category. Then for any accessible
localizing invariant F : Cat^perf -> E we have an isomorphism

    F^cont(Shv(X; C)) ~= F^cont(C)^X.

Here in the right hand side we consider X as an object of S^fin.
```

Local transcription in XX matches this statement.

Use in doc 51:

```text
directly proves that for T_l = R/lZ, the value
F^cont(Shv(T_l; C)) depends only on the finite homotopy type S^1 and
not on l.
```

### Theorem 6.11

Verified in the extraction at statement level:

```text
Theorem 6.11 treats localizing invariants of sheaves on locally
compact Hausdorff spaces with Cat^dual_st-valued coefficient
presheaves, in Mot^loc.
```

Use in doc 51:

```text
supporting source for the sheaf-level form mentioned in XX. Doc 51
does not need to quote the full theorem beyond the Theorem 0.2 / 6.1 /
4.18 package.
```

## 4. What Is Directly Citable

The following claim is directly citable from Efimov plus the elementary
homeomorphism `R/lZ ~= S^1`:

```text
For l > 0, constant dualizable C, and accessible localizing invariant
F, the value F^cont(Shv(R/lZ; C)) is naturally equivalent to
F^cont(C)^{S^1}. Thus a bare-circle localizing invariant cannot
distinguish l.
```

This is the core of doc 51 and is the theorem-grade part after this
audit.

## 5. Derived Program Lemma

The stronger doc-51 language about the full lattice diagram

```text
lZ -> R -> R/lZ
```

being sent to the `l`-independent homotopy diagram

```text
Z -> * -> BZ
```

is not a separately quoted Efimov theorem in the checked source. It is
a derived program lemma using:

```text
1. naturality of Efimov's constructions;
2. the homeomorphism lZ ~= Z as a discrete space;
3. the contractibility/proper-homotopy behavior of R;
4. Theorem 6.1 for R/lZ;
5. Proposition 4.18 / Theorem 0.2 for the line and locally compact
   pieces.
```

This lemma is plausible and already argued in XX, but it should be
separated from the direct citation. A polished version of doc 51 should
state it as:

```text
Lemma 51.D (diagram naturality lemma).
  Under H1-H4, any observable built naturally from the
  localizing-invariant image of lZ -> R -> R/lZ is invariant under
  replacing l by 1.
```

Then prove it in program language instead of attributing it wholesale
to Efimov. Doc 63 supplies this lemma.

## 6. Escape Boundary Confirmed

The audit also confirms the escape boundary used in docs 51 and 60.
Efimov's statements apply to:

```text
bare sheaf categories Shv(X; C);
constant dualizable coefficients for Theorem 6.1;
Cat^dual_st-valued coefficient presheaves for Theorem 0.2/6.11;
localizing invariants of Cat^perf and their continuous extensions.
```

They do not compute:

```text
liquid/gaseous analytic-ring module categories over T_logp;
metric coefficient systems whose norms retain log p;
equivariant/parametrized traces over the group object T_logp;
explicit kernel or correspondence traces that do not factor through
bare localizing-invariant sheaf data;
non-Sp-linear liquid trace theories.
```

Therefore docs 51 and 60 are right to classify these as live escape
profiles rather than contradictions.

## 7. Consequence For Doc 51

Doc 51 should be read with this grade:

```text
Core circle statement:
  citable after this audit.

Full lattice-diagram statement:
  theorem-shaped derived lemma; needs a polished naturality proof if
  promoted to publication.

Liquid analytic-ring/kernel/equivariant escapes:
  not touched by the Efimov citation.
```

The practical gate remains unchanged:

```text
Any candidate whose p-place is only Shv(R/(log p)Z; C) with constant
coefficients, or whose trace factors through accessible/continuous
localizing invariants of that bare sheaf category, fails scale
retention before B/C/D/E are reached.
```

## 8. Patch Guidance

For future hardening:

```text
1. Split doc 51 proof Step 2 into direct citation and the doc-63
   diagram lemma.
2. Quote Efimov only for Theorem 0.2, Proposition 4.18, Theorem 6.1,
   and optionally Theorem 6.11.
3. State the diagram result as a program lemma with a proof.
4. Keep the escape hatches exactly as written; the audit supports
   their boundary.
```
