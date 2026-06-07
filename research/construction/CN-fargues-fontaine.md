# Candidate N — Fargues–Fontaine curve / twistor P¹ as the finite ground at ∞ (2026-06-06)

**Lead.** The Fargues–Fontaine curve `X_FF` is a *proper* "genus‑0" curve that GEOMETRIZES a local field
`Q_p` (a field with no finite ground) into a genuine projective curve with structure sheaf, cohomology, a
degree theory, and a Frobenius. This is verbatim candidate N's spec (a place ↦ a proper curve over a ground).
The archimedean analog is the **twistor P¹** (Connes; Fargues; Viehmann–Zeff seminar). **Test:** does the
archimedean FF / twistor object supply a genuine **finite constant field** and force `|α|=√q` at `∞` — or only
a complex/continuum (Step A)?

## [computed/cited] What `X_FF` actually does (the non‑archimedean curve)

- **Proper, "genus 0".** `X_FF` is a complete (proper) curve. Closed points ↔ **untilts** of an alg. closed
  perfectoid field `C` (Frobenius‑equivalence classes). Schematically `X = Proj ⊕_{n≥0} B_C^{φ=p^n}`, and the
  adic version is `Y_S/φ_S^ℤ` (quotient by Frobenius). [nLab; Lurie 205; Anschütz].
- **THE CONSTANT FIELD IS CHAR 0.** `H^0(X_FF, O_X) = E`, a **finite extension of `Q_p`** — characteristic 0,
  NOT a finite field. Residue fields of closed points are **perfectoid fields** (alg. closed, char 0, untilts
  of `C`), never finite. So the "ground" of `X_FF` is the p‑adic field `E`, a continuum. [nLab: "defined over a
  p‑adic field `E`… a finite extension of `Q_p`"; "residue field… a complete algebraically closed field"].
- **The Frobenius is the CRYSTALLINE `φ` on the period ring**, with grading `B^{φ=p^n}`; its eigenvalue is `p`.
  The scale `p` (and `q = |residue field of E| = p^f`) is **the residue characteristic of `Q_p`, IMPORTED as an
  input parameter** — `Q_p` *already* carries a finite residue field `F_p` at its closed point `Spec F_p`. `X_FF`
  **repackages** that pre‑existing finite ground; it does **not manufacture** one. The construction needs `W(O_F)`
  (Witt vectors) — finite‑characteristic data fed IN.
- Vector bundles on `X_FF` classify `p`‑adic Galois/`φ`‑modules (Fargues–Scholze geometrization of local
  Langlands). This is genuine and deep — but it is a statement ABOUT a local field that already has `F_p`.

**Consequence for the program:** `X_FF` is *not a counterexample* to the f1‑closure — it is an *illustration*
of it. It produces a proper curve with a finite‑flavored scale **exactly when and because the input local field
`Q_p` already has a finite residue field.** It transports a finite ground; it never creates one.

## [computed/cited] The archimedean analog — twistor P¹

- The twistor P¹ is the established `∞`‑analog of `X_FF` (Connes; Fargues "twistor‑P¹"; Viehmann–Zeff 2024).
  It is the **quotient of `P¹_C` by the antipodal/conjugate involution** — a **real‑analytic continuum over
  `C`/`R`**. [Viehmann–Zeff seminar; "Notes on the twistor P¹"].
- Its "Weil group / Frobenius" at `∞` is **complex conjugation `= Gal(C/R) = ℤ/2`** — an **order‑2** datum, NOT
  a degree‑`q` Frobenius. Fetched source (Notes on twistor P¹) states it plainly: "at archimedean places it's a
  **real‑analytic continuum**" with a "**conjugation action**," contrasting the non‑arch "Frobenius action."
- **NO finite constant field.** `H^0` is `R`/`C`; the residue object is the continuum. There is no finite `F_q`,
  no `q > 1`.

## [computed] Anchor

| object | "Frobenius" | scale carried | finite ground? |
|---|---|---|---|
| curve `C/F_q` | `Frob_q : x↦x^q` | `q` finite discrete, `|α|=√q` | **YES** (`F_q`) |
| `X_FF` over `E/Q_p` | crystalline `φ`, eigenvalue `p` | `q=p^f` = residue card of `E` | **imported** from `Q_p`'s `Spec F_p` |
| twistor P¹ at `∞` | complex conjugation | conjugation eigenvalues `±1`, `|·|=1` ⇒ `q=1` | **NO** (continuum, `q→1`) |

`scripts`: conjugation on `C=R²` has eigenvalues `±1`, modulus `1` ⇒ dequantized scale `q=1` (the f1‑closure's
`q→1` continuum). Contrast `|α|=√q`, `q>1` for a genuine finite field. **The twistor / archimedean‑FF returns
exactly the order‑2 free involution + a continuum — the SAME type the f1‑closure already proved every base
returns.** It is Step A (a complex/twistor structure), not the finite ground.

## DH falsification

DH (`ζ` with a removed Euler factor / wrong functional structure) has no role here: the FF/twistor construction
attaches to a *place* of a field, not to an Euler product, and carries no mechanism distinguishing `ζ` from a DH
‑type Dirichlet series. It supplies no Euler‑product‑load‑bearing discriminator ⇒ **does not fail for DH**
(consistent with "no `𝔽₁`" — it does not even reach the stage where DH could be falsified). FAIL the DH test.

## Verdict — CHAR_DIVIDE_CLOSED

`X_FF` is the strongest possible witness *for the closure*, not against it: it shows precisely that a proper
curve with a genuine finite scale arises **iff** the input field already has a finite residue field. `Q_p` has
`Spec F_p`; **`R` has no finite residue field**, and the twistor P¹ — the actual archimedean analog used by the
experts — confirms this by being a real‑analytic **continuum** whose "Frobenius" is the order‑2 conjugation with
modulus 1 (`q→1`). The char‑0 / char‑`p` divide is **irreducible**: degeneration/geometrization can transport a
finite ground (FF curve) but cannot synthesize one where the residue field is archimedean (twistor). This
**completes the exhaustion** begun in `f1-construction.md`: not only does no `𝔽₁`‑base supply the scale, the
single most powerful modern "place → proper curve" machine (Fargues–Fontaine) supplies a finite scale only by
*importing* the one `R` structurally lacks.

- supplies_finite_ground at `∞`: **NO** (continuum, conjugation order 2, `q→1`).
- forces_radius `|α|=√q`: **NO_GO** — modulus is `1`, not `√q`.
- anchor over `F_q`/`Q_p`: PASS for `Q_p` (recovers `q=p^f`) **because `Q_p` already has `F_p`**; FAIL at `∞`.
- DH: FAIL (no Euler discriminator).

**Next step.** None toward construction along this axis. The remaining honest move is to *record the divide as a
theorem of obstruction* (a clean statement: "any 'place → proper curve over a finite ground' functor that is
natural in the place sends archimedean places to continuum/twistor objects, because the finite scale is the
residue cardinality and `R` has residue field `R`"), i.e. promote the no‑go to a structural lemma rather than
seek a new candidate. Candidate N is the last road; with FF/twistor it is **closed**.

Sources: nLab Fargues–Fontaine curve; Lurie IAS 205 Lecture 10; Anschütz lectures; Viehmann–Zeff "Twistor P¹ as
the archimedean FF curve" (Berkeley 2024); "Notes on the Twistor P¹" (arXiv 2202.02657); Fargues–Scholze
2102.13459; Connes essay on RH (arXiv 1509.05576); Connes–Consani arithmetic/scaling site (arXiv 1502.05580).
