# R6 — does the SURFACE `S²/ℤ` archimedean fiber carry the degeneration `N`, or does the no-special-fiber obstruction RECUR in dimension 2? [DECISION · DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §1 (polarization = duality), §4 (anchor first). **Block:** the RESIDUE (AGENDA `## NEXT`, item R6 — the TOP item, promoted by R5).
**Built on:** R1 (the residue = an archimedean `N` with `M(N)=W`, axioms N1–N4); R4 (the obstruction PINNED to a missing special fiber: the orbit `H¹(C_p)` is a smooth circle, rank 1, only `N=0`); **R5** (the obstruction is a RANK fact, and a REAL LEAD — the minimal carrier of a nonzero `N` with a symmetric split is dim 2, the Jordan-2 block; the surface `S²/ℤ`'s `gr^W_2 = H¹⊗H¹` has rank `(2g)² ≥ 4 ≥ 2`, supplying the room).
**Module:** `scripts/numerics/witness/surface_archimedean_N.py` (run: `python3 -m scripts.numerics.witness.surface_archimedean_N`). **Falsifier row added (42nd wall confirmation).**

R6's mandate: DECIDE the existence question R5 left open — does the surface's archimedean fiber actually carry a nonzero degeneration `N` on `gr^W_2` (inherit `C×C`'s transverse node over `𝔽_q`), or is the surface's archimedean fiber ALSO smooth (the `𝔽₁`/no-special-fiber obstruction recurring in dimension 2)?

---

## The decisive separation R6 forces: ROOM (a rank fact) ≠ USAGE (a degeneration fact)

R5's verdict "the surface supplies the room" is correct but conflated two distinct statements. R6 separates them, and the separation is the same `𝔽₁` obstruction recurring one dimension up:

- **room for a Jordan-2 block** — a *rank* fact: `gr^W_2` has rank `(2g)² ≥ 2`. **TRUE** (R5).
- **a Jordan-2 block is THERE** — a *degeneration* fact: a nonzero `N` actually acts. **This is the open question, and it is FALSE on the smooth fiber.**

The bridge between them is a theorem of Hodge theory / Weil II: **a nonzero monodromy nilpotent `N` is not a property of a smooth fiber of any dimension.** It is the **log of the local monodromy of a DEGENERATING FAMILY** (SGA7 / Schmid's nilpotent orbit / Steenbrink's limit MHS): `N = log T_unip`, the vanishing-cycle nilpotent of a 1-parameter family `𝒳_t → 𝔻` acquiring a singularity at `t=0`. A **smooth proper** variety has **pure** cohomology — `N = 0`, `M(N)` concentrated in a single weight.

---

## The computation (exact `𝔽_q` weight/rank linear algebra; no zeros assumed)

**[A] The smooth surface `C×C` over `𝔽_q` has `gr^W_2 = H¹⊗H¹` PURE of weight 2 — `N=0`, NO split.** `C×C` (the FF anchor of `S²/ℤ`) is a **product of smooth curves** = **smooth and proper**. By Künneth its `gr^W_2 = H¹(C)⊗H¹(C)` carries Frobenius eigenvalues `αᵢαⱼ`, and by Weil purity on the *smooth curve* `|αᵢ| = √q`, so `|αᵢαⱼ| = √q·√q = q` **exactly** (computed: all `(2g)²` moduli `= q`, `pure_weight2 = True`). The monodromy nilpotent on the smooth surface is `N = 0`; `M(0) = {2 : (2g)²}` is a **single weight** — NO `1↔3` Hard-Lefschetz pairing, NO symmetric split. **Exactly the smooth-orbit picture (R4/R5), now in dimension 2.** Decisively: the radius `|αᵢ| = √q` on `H¹` is a Weil **theorem about the smooth curve**, never *produced* by any `N` on `C×C`.

**[B] R5's room is real but EMPTY on the smooth fiber.** Computed for `g = 1,2,3`: `rank gr^W_2 = (2g)² = 4,16,36 ≥ 2` (room for a Jordan-2 block — R5 correct), but `N = 0` on the smooth fiber, so `split_realized_on_smooth_fiber = False`. **Room ≠ usage.**

| genus | `rank gr^W_2 = (2g)²` | room for Jordan-2 (≥2)? | `N` on smooth fiber | split realized? |
|---:|---:|:--:|:--:|:--:|
| 1 | 4 | YES (R5) | **0 (pure)** | **NO (R6)** |
| 2 | 16 | YES (R5) | **0 (pure)** | **NO (R6)** |
| 3 | 36 | YES (R5) | **0 (pure)** | **NO (R6)** |

**[C] Only a DEGENERATING FAMILY supplies the nonzero `N` + symmetric split.** The minimal sufficient datum is a 1-parameter family acquiring a singularity, whose nearby-cycle Jordan-2 nilpotent gives the symmetric split `M(N) = {1:1, 3:1}` about the centre weight 2 (computed). This is a **FAMILY, not the smooth surface**, and over `𝔽_q` it has a **special fiber over a finite residue field** (base size `q`) — **exactly R4's missing object**.

**[D] DH-vacuous TWO levels before the radius.** DH has no `H¹` ⟹ no `H¹⊗H¹` ⟹ **no surface `S²/ℤ` at all** ⟹ no family-of-surfaces to degenerate. The construction fails *at the carrier*, two levels before any radius — the special-fiber question is not even posable for DH.

---

## Verdict — HONEST NEGATIVE: the no-special-fiber obstruction RECURS in dimension 2

> **[DECISION · R6 verdict].** R5's lead is **partially relieved and partially recurring**, and R6 decides which: the surface supplies the **rank room** (R5 correct — `gr^W_2` rank `(2g)² ≥ 4`, a Jordan-2 home) but **NOT the degeneration**. The smooth `S²/ℤ` archimedean fiber is **PURE** (`N=0`, `M(0)` a single weight, no symmetric split) — *exactly as the smooth orbit was* (R4/R5), because `C×C` is a smooth proper product and purity is Weil II about it, not a monodromy. A nonzero `N` is **not** a property of a smooth fiber of any dimension; it is the log-monodromy of a **DEGENERATING FAMILY** with a special fiber over a finite base. **Therefore the `𝔽₁`/no-special-fiber obstruction is NOT relieved by `orbit → surface`; it is RELOCATED to `surface → family-of-surfaces` — the SAME atom, one dimension up.**

This is an **honest negative that sharpens the residue.** R5 narrowed the missing object to "an archimedean transverse degeneration of the surface"; R6 shows the *static surface* is the wrong carrier for the *same reason* the static orbit was (both smooth ⟹ pure ⟹ `N=0`), and pins the missing object precisely: a **1-parameter archimedean degeneration of `S²/ℤ`** (a family `𝒮_t` over an archimedean disk acquiring a singularity, with a **special fiber / finite base size** at `t=0`), **NOT** the static surface. The radius `|αᵢ| = √q` remains a Weil theorem about the smooth curve, never produced by any `N` on a smooth fiber.

**Why this is not circular / not overclaimed.** R6 does NOT prove no archimedean degeneration *exists* — it proves (exact `𝔽_q` weight/rank linear algebra) that (i) the smooth surface fiber is pure (`N=0`, no split), so R5's "room" is empty on it; (ii) a nonzero `N` requires a *family* with a special fiber, the same `𝔽₁` object R4 named; (iii) the dimension lift `orbit → surface` does NOT by itself manufacture the degeneration. Whether the *family* `𝒮_t` exists at `∞` (an archimedean analogue of the node-degeneration of `C×C`, with a special fiber over a finite base) is the next open existence question — and R5's dimension-relief of the rank obstruction is genuine: the *room* now exists, only the *family* is missing.

---

## Falsifier verdict (R6 — decision / obstruction-locator, Euler-silent by design)

- **EULER-BORNE — NO on this pass, by design.** Like R1–R5, R6 **decides/locates** the missing object via exact `𝔽_q` rank/weight linear algebra; it is not a standalone `ℤ`-positivity. Tabled **DISPERSING-by-design** (`euler_borne=False`). The **structural DH verdict is sharp and TWO levels before the radius**: no `H¹` ⟹ no `H¹⊗H¹` ⟹ no surface ⟹ no family to degenerate.
- **SEES-ZEROS — YES.** The sought radius `= M(N)=W =` even split `=` purity `=` exactly where the zeros sit.
- **INDEPENDENT — NO.** The radius `= M(N)=W =` Weil II `=` the solved case over `𝔽_q`; over `ℤ` this is RH.

→ classifier verdict **DISPERSING-by-design** (a decision/obstruction-locator, Euler-silent like R1–R5). **Ladder `DH < ζ < FF`:** DH no `H¹` (no carrier); `ζ` a **smooth** surface `S²/ℤ` whose `gr^W_2` has the rank room but `N=0` (pure) on the smooth archimedean fiber, with the degeneration **family still missing**; FF a **smooth** surface `C×C` (also pure, `N=0`) **PLUS** an external degenerating node-family with a special fiber over the finite base size `q` (Weil's theorem about the smooth curve supplies the radius; the node-family supplies the geometric `N` — **both absent at the archimedean place of `ζ`**). Registered as the **42nd wall confirmation**.

---

## Verdict

`[DECISION · DEF · coherence-checked vs 𝔽_q]` — **the no-special-fiber (`𝔽₁`) obstruction RECURS in dimension 2.** R5's "the surface supplies the room" is correct as a **rank** fact (`gr^W_2 = H¹⊗H¹`, rank `(2g)² ≥ 4`) but R6 separates room from usage: the **smooth** surface `C×C`/`S²/ℤ` has `gr^W_2` **PURE** of weight 2 (`|αᵢαⱼ| = q` exactly, Weil II), monodromy `N = 0`, `M(0)` a single weight — **NO symmetric split**, exactly as the smooth orbit (R4/R5). A nonzero `N` requires a **degenerating family** with a special fiber / finite base size — R4's missing object, **relocated** from `orbit → surface` to `surface → family-of-surfaces`, not relieved. **Not overclaimed:** R6 decides that the *static surface* is the wrong carrier (smooth ⟹ pure ⟹ `N=0`) and pins the missing object as a **1-parameter archimedean degeneration of `S²/ℤ` with a special fiber**; R5's rank-relief is genuine (the room now exists), only the family is missing. **Successor:** R7 — does an **archimedean degenerating family `𝒮_t` of `S²/ℤ`** (the analogue of `C×C`'s node-degeneration, with a special fiber over a finite base) exist at `∞`, or is "no special fiber over a finite base at `∞`" the irreducible `𝔽₁`-terminus the four discretizations (R3/R3b/R4) and the dimension lift (R5/R6) all converge on?
