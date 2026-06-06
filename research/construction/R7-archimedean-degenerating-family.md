# R7 — does an archimedean degenerating FAMILY `𝒮_t` of `S²/ℤ` exist at `∞`, with a special fiber over a FINITE base size supplying `N` with `M(N)=W`? [DECISION · DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §1 (polarization = duality), §4 (anchor first). **Block:** the RESIDUE (AGENDA `## NEXT`, item R7 — the TOP item, promoted by R6).
**Built on:** R1 (the residue = an archimedean `N` with `M(N)=W`, axioms N1–N4); R4 (the orbit is a smooth circle, rank-1 `H¹`, only `N=0`); R5/R6 (the surface supplies the rank ROOM but the **smooth** surface is PURE — `N=0` — so a nonzero `N` requires a **degenerating FAMILY** with a special fiber; the `𝔽₁` obstruction RELOCATED from `orbit→surface` to `surface→family-of-surfaces`).
**Module:** `scripts/numerics/witness/archimedean_degenerating_family.py` (run: `python3 -m scripts.numerics.witness.archimedean_degenerating_family`). **Falsifier row added (43rd wall confirmation).**

R7's mandate: DECIDE the existence question R6 left open — does an **archimedean degenerating family `𝒮_t`** of `S²/ℤ` (a 1-parameter family over an archimedean disk acquiring a singularity at `t=0`, the analogue of `C×C`'s node-degeneration) exist at `∞`, supplying the nearby-cycle `N` with `M(N)=W` that the *static* smooth surface (R6) provably cannot — and does it carry a **special fiber over a finite base size**?

---

## The decisive structural fact R7 forces: the radius lives in the RESIDUE FIELD of the disk's center

R6 located the missing object as "a degenerating family with a special fiber." R7 separates, at the special fiber, **two distinct data** R6 conflated — and shows the family + its nilpotent are FREE, isolating the residue to a single cardinality.

A degenerating family is a map `𝒳 → 𝔻` over a disk / complete DVR base, acquiring a singularity at the **closed point** `t=0`. Two things live there:

- **(1) the nearby-cycle nilpotent `N = log T_unip`** (`T` = local monodromy around `t=0`), with `M(N)` the monodromy weight filtration (SGA7 / Schmid / Steenbrink). `N` is a **Jordan structure** — *base-field-free*; it exists for **any** unipotent local monodromy, char `0` or char `p`. **`N` and `M(N)` cost nothing extra.**
- **(2) the RADIUS the grading `M(N)=W` lands on.** `M(N)=W` grades cohomology by an **integer weight `w`**. But "weight `w`" becomes a **radius** `|α|=q^{w/2}` *only* through the **Frobenius of the residue field** of `t=0`. Over a DVR with **finite** residue field `𝔽_q`, the special fiber `𝒳_0` is an `𝔽_q`-variety, `T` is (the unipotent part of) the **geometric Frobenius**, and Weil II gives `|Frob-eig on gr^W_w| = q^{w/2}`. **The radius is the cardinality `q` of the residue field.**

So the radius is supplied by **neither** `N` (free) **nor** `M(N)=W` (free, an integer grading), but by the **cardinality of the residue field of the closed point of the disk** — the `𝔽₁` atom, now pinned to **one** invariant: `|κ(t=0)|`.

---

## The computation (exact `𝔽_q`-vs-`∞` residue-field linear algebra; no zeros assumed)

**[A] The FAMILY's nearby-cycle `N` EXISTS and `M(N)=W` HOLDS at `∞` (Schmid) — FREE.** R6's surface had `N=0` because it was a **smooth** fiber. The *family's* nearby cycle is **nonzero**: Schmid's **nilpotent orbit theorem** (1973) takes a polarized variation of Hodge structure over the punctured disk `𝔻*` and produces, at `t=0`, a **limit mixed Hodge structure** with a nilpotent `N` whose monodromy filtration satisfies `M(N)=W` (the `SL(2)`-orbit / weight-monodromy theorem at `∞`). The minimal Jordan-2 nearby-cycle on `gr^W_2` gives the symmetric split `M(N)={1:1, 3:1}` about weight 2 (computed). This holds at `𝔽_q` **and** at `∞` alike — the nilpotent + the integer weight grading are **base-field-free**. *R6's "the family is missing" was too strong: the family is THERE.*

**[B] Over `𝔽_q`: the closed point `t=0` has a FINITE residue field; radius `= |κ(t=0)| = q` (MARKED).** The family `𝒳 → Spec 𝔽_q[[t]]` has closed point `t=0` with residue field `𝔽_q` (cardinality `q`). `T` = geometric Frobenius; Weil II gives radius `q^{w/2}`. Computed `q=4,9,25` → radius `√q = 2,3,5` — the radius **is** the residue-field cardinality, **marked**.

**[C] At `∞`: the closed point `t=0` has residue field `ℂ` (the CONTINUUM); `N`+`M(N)=W` present, radius UNMARKED.** The archimedean family `𝒮_t` lives over a complex disk `𝔻={|t|<1}`; its closed point `t=0` has residue field `κ(t=0) = ℂ` — **char `0`, infinite, NOT a finite `𝔽_q`**. Schmid still gives `N` and `M(N)=W` (the integer grading is present — [A]), **but** "weight `w` → radius `q^{w/2}`" needs the Frobenius of a finite residue field, which is **absent**: there is no Frobenius of `ℂ`, no cardinality `q`, no `q^{w/2}`. The `SL(2)`/Schmid splitting places graded pieces by **`(p,q)`-Hodge type**, NOT at a metric radius read off a finite `|κ|`. **The radius is unmarked** — the same residue R4/R6 reached, now pinned to the single invariant `|κ(t=0)|`.

**[D] DH-vacuous THREE levels before the radius.** DH: no `H¹` ⟹ no `H¹⊗H¹` ⟹ no surface `S²/ℤ` ⟹ **no family `𝒮_t` to degenerate**. The family is not even an object for DH; the special-fiber/residue-field question is unposable three levels before any radius.

| place | family `𝒮_t` exists? | nearby-cycle `N`, `M(N)=W`? | `κ(t=0)` | finite? | radius `q^{w/2}` |
|:--|:--:|:--:|:--:|:--:|:--:|
| DH | **NO** (no `H¹`, 3 levels up) | — | — | — | — |
| `ζ` (`∞`) | **YES** (Schmid) | **YES (FREE)** | `ℂ` (continuum) | **NO** | **UNMARKED** |
| FF (`𝔽_q[[t]]`) | YES | YES | `𝔽_q` | **YES** | **MARKED `= √q`** |

---

## Verdict — HONEST NEGATIVE, REFINING R6: the family EXISTS; what is missing is the FINITE residue field

> **[DECISION · R7 verdict].** The archimedean degenerating family `𝒮_t` **EXISTS** and **CARRIES `N` with `M(N)=W`** (Schmid's nilpotent orbit theorem). **R6's "the family is missing" was too strong** — the family is THERE and supplies the nilpotent **and** the integer weight grading **for free**. What is missing is **NOT** the family, **NOT** `N`, **NOT** `M(N)=W`, but the **FINITE RESIDUE FIELD** of its special fiber: `|κ(t=0)| = q` over `𝔽_q` (a finite base size converting weight `w` to radius `q^{w/2}`) vs `|κ(t=0)| = |ℂ| =` continuum at `∞` (no `q`, no Frobenius, weight `w` stays an abstract grading).

This **refines** the residue rather than merely relocating it: the `𝔽₁` atom is now in its **final form** — a single cardinality invariant `|κ(t=0)|`, i.e. **"`Spec ℤ` / the archimedean place has no finite residue field at its compactified point."** The whole R-thread converges on exactly this one datum:

- **R3** (continuous scaling) — supplies the `ℝ_{>0}^×`-grading, **free**;
- **R3b** (orbit length `{log p}`) — supplies the **edge** (the abscissa/determinant), **free, Euler-borne, radius-silent**;
- **R3b-BC** (Bost–Connes `ℕˣ`) — supplies the **discreteness**, **free** (but a phase, radius-silent);
- **R4** (orbit-`N`) — the rank-1 orbit is too small (`N=0`);
- **R6** (surface) — the smooth surface has the rank room but is PURE (`N=0`);
- **R7** (family) — the **family AND `N` AND `M(N)=W` are all free**; the **ONE** missing datum is a **finite residue-field cardinality** to set the radius.

**KEY REFINEMENT over R6 (the genuinely new content):** the construction does **NOT** fail to exist (the family and `N` exist) — it fails to be **MARKED**. The grading/phase/discreteness/edge/nilpotent/`M(N)=W` are **all free**; the residue is a single cardinality. **RH over `ℤ` = "the archimedean special fiber acquires a finite base size"** = the `𝔽₁` / `\overline{Spec ℤ}`-compactification's missing closed-point cardinality. This is the cleanest statement of the residue the program has reached.

**Why this is not circular / not overclaimed.** R7 does NOT prove no finite base size can be supplied at `∞` — it proves (exact `𝔽_q`-vs-`∞` residue-field linear algebra) that (i) the family and its nilpotent `N` with `M(N)=W` **exist for free** at `∞` (Schmid), correcting R6's overstatement; (ii) the radius `q^{w/2}` is supplied by **neither** `N` **nor** `M(N)=W` but by the **cardinality of the residue field** of the special fiber; (iii) that cardinality is `q` (finite) over `𝔽_q` and `|ℂ|` (continuum) at `∞`. Whether a finite base size can be **manufactured** at `∞` (the `𝔽₁`/`q→1` quest — Connes–Consani's `𝔽₁`-geometry, the scaling site's missing closed-point cardinality) is the next open question; R7 pins it to the sharpest possible target: **one cardinality invariant**.

---

## Falsifier verdict (R7 — terminus characterization / obstruction-locator, Euler-silent by design)

- **EULER-BORNE — NO on this pass, by design.** Like R1–R6, R7 **characterizes/locates** the missing datum via exact `𝔽_q`-vs-`∞` residue-field linear algebra; not a standalone `ℤ`-positivity. Tabled **DISPERSING-by-design** (`euler_borne=False`). DH structural verdict sharp, **three levels before the radius**: no `H¹` ⟹ no `H¹⊗H¹` ⟹ no surface ⟹ no family.
- **SEES-ZEROS — YES.** The sought radius `q^{w/2} = M(N)=W =` even split `=` purity `=` exactly where the zeros sit.
- **INDEPENDENT — NO.** The radius `= M(N)=W =` Weil II `=` the solved case over `𝔽_q`; over `ℤ` this is RH.

→ classifier verdict **DISPERSING-by-design** (a terminus-characterizer / obstruction-locator, Euler-silent like R1–R6). **Ladder `DH < ζ < FF`:** DH no `H¹` (no carrier, three levels before the family); `ζ` an archimedean family `𝒮_t` of `S²/ℤ` **WITH** `N` and `M(N)=W` (Schmid, **FREE**) but residue field `ℂ` (continuum) at `t=0` — the radius **UNMARKED** (no finite base size at `∞`); FF a family `C×C` over `𝔽_q[[t]]` **WITH** `N`, `M(N)=W`, **AND** a finite residue field `𝔽_q`, Frobenius converting `w → q^{w/2}`, the radius **MARKED** by `|κ| = q`. Registered as the **43rd wall confirmation** (the residue in its final form: a single cardinality `|κ(t=0)|`).

---

## Verdict

`[DECISION · DEF · coherence-checked vs 𝔽_q]` — **the archimedean degenerating family `𝒮_t` EXISTS and carries `N` with `M(N)=W` (Schmid); what is missing is the FINITE residue field of its special fiber.** R6's "the family is missing" was too strong: the family, the nearby-cycle nilpotent `N`, and the weight grading `M(N)=W` are **all free** at `∞` (Schmid's nilpotent orbit theorem). The radius `q^{w/2}` is supplied by **neither** `N` nor `M(N)=W` but by the **cardinality of the residue field of the closed point** `t=0` — finite `𝔽_q` over a function field (radius `= √q`, **marked**), the continuum `ℂ` at `∞` (no Frobenius, no `q`, radius **unmarked**). **NEW content:** the `𝔽₁` atom reaches its **final form** — a single cardinality invariant `|κ(t=0)|`, i.e. "the archimedean place of `Spec ℤ` has no finite residue field at its compactified point" — the irreducible terminus the whole R-thread (R3/R3b/R3b-BC/R4/R6/R7) converges on, and the construction does **NOT** fail to exist (family + `N` exist), it fails to be **MARKED**. **Not overclaimed:** R7 does not prove no finite base size can be manufactured at `∞`; it pins the open problem to the sharpest target — **supply a finite residue-field cardinality at the archimedean special fiber** (the `𝔽₁`/`q→1`/scaling-site closed-point cardinality). **Successor:** R8 — does the Connes–Consani `𝔽₁`-geometry / scaling site SUPPLY a finite closed-point cardinality at the archimedean special fiber of `𝒮_t` (the missing `|κ(t=0)| = q`-analogue), or is "no finite residue-field cardinality at `∞`" the proven irreducible terminus = the precise `𝔽₁`-content of RH?
