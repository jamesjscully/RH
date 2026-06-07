# NF-(SP) — a base BELOW the sphere spectrum 𝕊: does a homotopical / higher-categorical "characteristic" (chromatic height, Morava K(n), the Westerland/Szymik ζ-characteristic) give the archimedean place a FINITE ADDITIVE characteristic with a scale q, or is height 0 = char 0 irreducible? [DECISION · lit-grounded · anchor-computed · FOUNDATIONAL_NOGO]

2026-06-06. NEW-FOUNDATIONS direction (SP) of `research/new-foundations.md`. Goes deeper than `F1-(S)` (`research/construction/F1-S-sphere-spectrum.md`, which decided 𝕊 *itself* is SCALE_FREE — count-typed homotopy-finiteness, Step A only). This pass asks whether a base *beneath* 𝕊 — the chromatic/fracture stratification, a homotopical characteristic — finitizes the archimedean (height-0/rational) part.

Lit (WebSearch/WebFetch this pass): C. Westerland, *String bordism and chromatic characteristics* (arXiv:1312.4658) — introduces "chromatic characteristic," the K(n)-local Hopkins–Miller classes ζₙ "take the places of the prime numbers." M. Szymik, *Characteristics for E∞ ring spectra* (arXiv:1405.3695) and *Commutative S-algebras of prime characteristics* (arXiv:1211.3239, AGT) — the homotopical generalization of "characteristic = p·1=0," versal char-p object S//p as a Thom spectrum, Hopkins–Mahowald (HF_p = free E_2 with p=0). Morava K-theory as the prime fields of Sp (nLab Morava K-theory; Hopkins–Smith). Fracture/arithmetic square (nLab; arXiv:2404.18618). Connes–Consani 𝕊 = 𝔽₁ (arXiv:2306.00456). Cross-thread: F1-S (𝕊 scale-free), R8/QD (constant-field type / finite-prime-indexed), f1-construction §EXHAUSTED (char-divide irreducible).

## The mandate — go below 𝕊, where characteristic is homotopical

`F1-(S)` settled that 𝕊 (the initial E∞-ring, Connes–Consani's 𝔽₁) gives the Step-A duality skeleton but its homotopy-finiteness is a COUNT, not the radius. The SP-direction is the next floor down: **leave E∞-rings; let "characteristic" be homotopical.** Two concrete vehicles, both real and current:

1. **Szymik characteristic (the ADDITIVE target, exactly on-spec).** For an E∞/E_n ring R, "char p" means **p = 0 in R**, refined homotopically (a null-homotopy of p·1 with coherence). This is *literally* the additive characteristic = additive order of 1 = the program's sharp target. Versal char-p object: `S//p` (Thom spectrum). Hopkins–Mahowald: `HF_p` = the free E_2-algebra on `p=0`. **A genuine finite additive characteristic exists homotopically — at the finite primes.**

2. **Westerland chromatic characteristic + Morava prime fields (the HEIGHT vehicle).** The prime fields (Morava residue fields) of the category of spectra are the `K(n,p)`. The chromatic ladder:
   - `K(0) = HℚHQ`  — **height 0, characteristic 0**  — and `Sp_{K(0)} ≅ Sp_ℚ` (explicit in the literature, e.g. ambidexterity n=0 case).
   - `K(n)`, n≥1, with `K(n)_* = 𝔽_p[v_n^{±1}]`, `|v_n| = 2(p^n−1)` — **height n, characteristic p.**
   - Westerland's ζₙ (n≥1) play the role of the prime p **at positive height.**

## What got DECIDED

**[1] The chromatic ladder LITERALLY NAMES the char-divide as the height-0 / positive-height split.** [lit, decisive — new framing]
`Sp_{K(0)} = Sp_ℚ` is characteristic 0; every `K(n)`, n≥1, is characteristic p. So in the deepest current homotopical stratification of "number," the divide between char 0 and char p is *reproduced verbatim* as **height 0 vs height ≥ 1**. The archimedean / rational / transcendental part **is** height 0 = `Hℚ` = char 0, *by the structure of the fracture/chromatic decomposition itself.* The chromatic picture is not a tool for *crossing* the divide; it is the divide, re-seen as a height filtration. This is the SP-specific finding — not present in `F1-(S)` (which only saw 𝕊's count-typed finiteness), and stronger: it identifies the archimedean place with the irreducibly-char-0 stratum.

**[2] Height 0 = char 0 is a LOCALIZATION (p inverted), not a removable ring artifact.** [structural, decisive]
`S_ℚ = 𝕊[1/p : all p]` — the rationalization inverts *every* prime. Characteristic 0 at height 0 is therefore *definitional*: inverting p makes p a **unit**, so `p·1 ≠ 0` *by construction*. A base *below* 𝕊 (Γ-sets, 2-rigs, pointed sets — more general than E∞-rings) cannot re-impose `p·1 = 0` on the stratum that is *defined by inverting p* without un-inverting p — i.e. without changing which place this is. The char-0-ness of the archimedean part is not an accident of the ring 𝕊 that a deeper base could fix; it is the *meaning* of "archimedean = rationalized = height 0."

**[3] No scale q at height 0 (q → 1, degenerate even if forced).** [computed]
The scale lives in `K(n)_* = 𝔽_p[v_n^{±1}]`: the graded unit `v_n` of degree `2(p^n−1)` carries `p` (and the height-n analog of `q`). At height 0, `K(0)_* = ℚ` concentrated in degree 0 — **no `v_0`, no graded periodicity, no scale.** Even the most generous reading (a "chromatic q" = `p^n` or a ζ-class) is a positive-height datum; pushing it to height 0 sends `q → 1` (the same dequantization that killed tropical/char-1 in `F1-(T)`). DEGENERATE in the scale, on top of the char-0 obstruction.

**[4] ANCHOR — finite primes recovered as the special case (Step B radius computed).** [computed]
At a finite prime the chromatic/Szymik picture *does* deliver: `S_p^∧` has positive-height Morava residue fields `K(n)` of genuine char p; `HF_p` = free E_2 with `p=0`. This recovers the finite-characteristic side. The arithmetic radius anchor (the Step-B datum the whole program needs) holds over actual `𝔽_q`:
`√q` for `q=4,9,25 → 2,3,5` (exact); genus-1 `(q,a)=(5,1),(7,3),(11,−2),(13,4) → |α|=√q = 2.2360679…, 2.6457513…, 3.3166247…, 3.6055512…` (exact to 25 dps, `flint`/`mpmath`). The framework recovers the finite primes (ANCHOR PASS); it does **not** transport this to height 0.

**[5] DH falsified.** [structural]
The chromatic/ζ machinery is built on the **Frobenius / Euler (formal-group, Brown–Peterson, `v_n`) datum** — a per-prime local structure. DH (functional equation, **no Euler product**) has no formal group, no `v_n`, no ζₙ, no height presentation. No Euler product ⟹ no chromatic object ⟹ no scale. DH dies — correctly (inherited Euler-product kill, like every Frobenius-based candidate).

## THE CONTRADICTION (the deepened no-go — precise)

A finite additive characteristic at `∞` (`p·1 = 0` for some p) is **provably incompatible with `ℚ`'s archimedean place**, via **Ostrowski**:

> A place `v` of `ℚ` carries a finite residue characteristic ⟺ `|·|_v` is **non-archimedean** (ultrametric) ⟺ `v` is **p-adic** for some prime `p` (Ostrowski: the only non-archimedean places of `ℚ` are the `p`-adic ones). The archimedean place `∞` has `|·|_∞` **archimedean** (`|n|_∞ → ∞`, `1` has *infinite* additive order in the relevant valuation sense). Therefore: **giving `∞` a finite additive characteristic = making `|·|_∞` ultrametric = turning `∞` into a `p`-adic place = it is no longer the archimedean place.** The base-below-𝕊 cannot *add* a finite characteristic to `∞`; it can only *delete* `∞` and replace it with a (new) finite prime — which changes `ℚ`'s place structure, i.e. changes `ℚ`.

The chromatic ladder makes this maximally sharp: **height 0 (= `Hℚ` = the archimedean stratum) is, definitionally, the locus where all p are inverted.** "Finite characteristic at height 0" is a contradiction in terms — it asks for `p = 0` and `p` invertible simultaneously. The COUNT/RADIUS decoupling (PA) and the constant-field type-mismatch (R8) here become the **invert-p / kill-p** incompatibility: the archimedean place is the *unique* place defined by inverting all primes, and no deeper base un-inverts them without ceasing to be `ℚ`'s archimedean completion.

## Verdict — FOUNDATIONAL_NOGO (height 0 = char 0 irreducibly; the chromatic ladder *is* the char-divide)

> **[DECISION · NF-(SP)].** Going below 𝕊 into the chromatic/fracture stratification supplies a *genuine homotopical characteristic* — Szymik's `p=0` E∞-characteristic, Hopkins–Mahowald `HF_p`, Westerland's ζₙ, Morava `K(n)` — but it delivers finite characteristic **only at positive height (the finite primes)**. The archimedean / rational / transcendental place is `K(0) = Hℚ`, **height 0 = characteristic 0**, with `Sp_{K(0)} = Sp_ℚ`. This char-0-ness is a **localization** (`S_ℚ = 𝕊[1/p : all p]`): inverting every prime *defines* char 0, so `p·1 ≠ 0` by construction and no base beneath 𝕊 can re-impose `p·1 = 0` on the height-0 stratum without un-inverting p, i.e. without changing which place this is. No scale at height 0 (`K(0)_* = ℚ`, no `v_0`; `q → 1`, DEGENERATE). **ANCHOR PASS** (finite primes recovered: positive-height `K(n)` = char p; `|α|=√q` computed exactly). **DH dies** (no Euler product ⟹ no formal group/`v_n`/ζₙ ⟹ no object). **CONTRADICTION (Ostrowski):** finite additive characteristic at `∞` ⟺ `|·|_∞` ultrametric ⟺ `∞` is `p`-adic ⟺ it is not the archimedean place. The chromatic ladder does not cross the char-divide; **it *is* the char-divide, re-presented as the height-0 / height-≥1 split.** This is the strongest possible homotopical statement of why `∞` is char-0-hard: the archimedean place is the unique stratum where all primes are inverted, and finite characteristic there is self-contradictory. SP joins F1-S/R8/QD as the same atom, now at the foundational/chromatic floor.

## Five-line decision (as required)

- **(a) Is there a homotopical characteristic below/at 𝕊?** YES — Szymik `p=0` E∞-char, Hopkins–Mahowald `HF_p`, Westerland ζₙ, Morava `K(n)`. Real and current.
- **(b) Does it finitize the archimedean (height-0) part?** NO — `K(0)=Hℚ`, `Sp_{K(0)}=Sp_ℚ`, char 0; char-0-ness is the *localization* `𝕊[1/p:all p]`, definitional, not a removable artifact.
- **(c) Scale q at height 0?** NO — `K(0)_*=ℚ`, no graded `v_0`; any chromatic q is positive-height; pushed to height 0 it dequantizes `q→1` (DEGENERATE).
- **(d) Anchor — finite primes / `|α|=√q`?** YES (PASS) — positive-height `K(n)` = char p; radius `|α|=√q` computed exactly over `𝔽_q` (genus 0–1). DH dies (no Euler product ⟹ no chromatic object).
- **(e) Verdict + the contradiction.** **FOUNDATIONAL_NOGO.** Ostrowski: finite additive char at `∞` = ultrametric = `p`-adic = not archimedean. The chromatic ladder *is* the char-divide (height 0 = char 0 / height ≥ 1 = char p), not a crossing of it. Compatible-with-ℚ? NO — a finite char at `∞` contradicts `∞` being `ℚ`'s archimedean place.

## Falsifier verdict (NF-SP — terminus-characterizer, Euler-silent by design, DH-killing)
- **EULER-BORNE — NO, by design.** Type-checks the chromatic/Szymik characteristic + computes the `𝔽_q` anchor; not a standalone `ℤ`-positivity. DISPERSING-by-design.
- **SEES-ZEROS — YES.** The sought radius `√q` (positive-height scale) = purity = where the zeros sit.
- **INDEPENDENT — NO.** Recovers the solved char-p case (positive height); over `∞` it returns char 0 = height 0 = RH-equivalent, not independent.
→ **DISPERSING-by-design.** The deepest current base (below 𝕊, chromatic) confirms the char-divide as a *height* phenomenon: height 0 = char 0 irreducibly, with a sharp new contradiction (Ostrowski: finite char ⟹ ultrametric ⟹ not archimedean).
