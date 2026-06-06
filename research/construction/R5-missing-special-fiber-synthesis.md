# R5 — the missing idea, stated as ONE object; real lead vs irreducible terminus [SYNTHESIS · DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §1 (the polarization = duality), §4 (anchor first). **Block:** the RESIDUE (AGENDA `## NEXT`, item R5 — the TOP item).
**Built on:** R1 (the residue = an archimedean nilpotent `N` with `M(N)=W`, four axioms N1–N4); R2/R3/R3b (Schmid SL(2)-orbit, continuous scaling, orbit length, Bost–Connes multiplier — all supply the grading/phase/discreteness/EDGE for free, NONE the per-place radius); **R4** (the obstruction PINNED — the orbit `H^1(C_p)` is a smooth circle, **rank 1**, only `N=0`, no symmetric split; the missing object is a **special fiber / finite residue field / degeneration locus at `∞`**).
**Module:** `scripts/numerics/witness/missing_special_fiber.py` (run: `python3 -m scripts.numerics.witness.missing_special_fiber`). **Falsifier row added (41st wall confirmation).**

R5's mandate: STATE the shape of the missing idea as the single object whose construction is the open problem, and JUDGE — real lead (build next) or irreducible terminus? Either is the honest endpoint.

---

## The synthesis: R4's obstruction is a DIMENSION fact, not vague "continuity"

The four R-passes converged on "a missing special fiber at `∞`," and R4 phrased the cause as the **continuity** of the archimedean scaling. R5 sharpens that to its exact content, which turns out to be a **rank/dimension** statement — and a rank statement is *decidable* and *liftable*, whereas "continuity is irreducible" would be a terminus. The three exact checks (all integer linear algebra, no zeros assumed):

**[A] The orbit's rank-1 `H^1(C_p)` admits ONLY `N=0` — no symmetric split.** On a line `ℂ¹` the only nilpotent is `0`; `M(0)` is concentrated in a **single weight** (`{1:1}`), so there is no `0↔2` Hard-Lefschetz pairing — the symmetric-split mechanism is **vacuous**. (Reproduces R4 exactly.) The radius is unmarked.

**[B] rank-2 is the MINIMAL carrier of a nonzero degeneration.** The minimal nonzero nilpotent with a **symmetric, nontrivially-split** monodromy filtration `M(N)` about its centre is the **Jordan-2 block** on `ℂ²`, with `M(N)={0:1, 2:1}` symmetric about `w=1` — the even split made visible. Computed exactly:

| carrier dim | nonzero `N` with symmetric, split `M(N)`? | `M(N)` graded (centre `w=1`) |
|---:|:--:|---|
| 1 (orbit) | **NO** | `{1:1}` (single weight) |
| **2** | **YES (minimal)** | `{0:1, 2:1}` |
| 3 | yes | `{−1:1, 1:1, 3:1}` |
| 4 | yes | `{−2:1, 0:1, 2:1, 4:1}` |

So the obstruction is precisely: **the 1-dimensional orbit is too small to carry the Jordan-2 block.** A dimension count, not a metaphysics.

**[C] The SURFACE supplies the room the orbit cannot — and is DH-vacuous.** M2d's verdict: purity for `ζ` is **intrinsically GLOBAL** — the weight-1 carrier lives on the surface `S²/ℤ`, whose weight-2 piece `gr^W_2 = H^1 ⊗ H^1` (M4A/M4B/M4C) has rank `(2g)² = 4, 16, 36 ≥ 2` for `g=1,2,3`. **Rank `≥ 2` is exactly the minimal home of a Jordan-2 block.** So the surface's `gr^W_2` has room for the degeneration `N` the rank-1 orbit provably cannot carry. DH-vacuity is sharp and **one level earlier than for `ζ`**: DH has no `H^1` (no Euler product ⟹ no Frobenius weight ⟹ no weight-1 cohomology) ⟹ no `H^1⊗H^1` ⟹ **no surface special fiber to degenerate** — the construction fails *at the carrier*, before the radius.

---

## Verdict — REAL LEAD, not a terminus; the missing object named as ONE thing

> **[SYNTHESIS · R5 verdict].** R4's "missing special fiber at `∞`" is **NOT an irreducible terminus.** Its exact content is a **rank fact** — the bare scaling orbit `C_p` has rank-1 `H^1`, which admits only `N=0` (no symmetric split, no Jordan-2 block, radius unmarked). The minimal carrier of the degeneration `N` (a nonzero nilpotent with a symmetric, split `M(N)`) is **dimension 2**. The would-be motive of `ζ` is the **surface `S²/ℤ`** (M2d), whose `gr^W_2 = H^1⊗H^1` has rank `(2g)² ≥ 4 ≥ 2` — it **supplies exactly the room** the orbit lacks. **Therefore the single missing object is: an archimedean transverse degeneration / special fiber of the SURFACE `S²/ℤ` (not the 1-dimensional orbit), supplying a nonzero archimedean `N` on `gr^W_2` whose `M(N)=W` forces the radius — i.e. exactly R6.**

This is the positive culmination of the R-thread. The residue is characterized to its atom, the missing idea's shape is named as ONE object with a **decidable existence question** (does the surface's archimedean fiber carry a nonzero `N`?), and the obstruction that closed the orbit route (rank 1) is *explicitly relieved* by the correct carrier (the surface, rank `≥2`). The honest endpoint is **not** "irreducible" — it is "**lift the search from the orbit to the surface,**" which is R6, already named.

**Why this is not circular / not overclaimed.** R5 does NOT construct the surface's archimedean `N` — it PROVES (exact linear algebra) that (i) the orbit cannot carry it (rank 1 ⟹ only `N=0`), (ii) dimension 2 is the minimal home, (iii) the surface `gr^W_2` has the room. Whether the surface's *archimedean* fiber actually degenerates (inherits `C×C`'s transverse node over `𝔽_q`) is the **open question R6 must decide** — possibly with the SAME `𝔽₁`/no-special-fiber obstruction recurring at the surface (the smooth-vs-degenerate question now in dimension 2), possibly relieved. Either is the next honest measurement.

---

## Falsifier verdict (R5 — synthesis / lead-locator, Euler-silent by design)

- **EULER-BORNE — NO on this pass, by design.** Like R1–R4, R5 **types/locates** the missing object and **anchors** on `𝔽_q` (rank counts); it is not a standalone `ℤ`-positivity form. Tabled **DISPERSING-by-design** (`euler_borne=False`). The **structural DH verdict is sharp and one level earlier than for `ζ`**: DH has no `H^1` ⟹ no `H^1⊗H^1` ⟹ no surface special fiber (fails at the carrier, before the radius).
- **SEES-ZEROS — YES.** The radius `= M(N)=W =` even split `=` purity `=` exactly where the zeros sit.
- **INDEPENDENT — NO.** The radius `= M(N)=W =` Weil II `=` the solved case over `𝔽_q`; over `ℤ` this is RH.

→ classifier verdict **DISPERSING-by-design** (a lead/obstruction-locator, Euler-silent like R1–R4). **Ladder `DH < ζ < FF`:** DH no `H^1` (no carrier at all); `ζ` a surface `S²/ℤ` with an **OPEN** archimedean degeneration `N` on rank-`(2g)²` `gr^W_2`; FF a surface `C×C` with a **GEOMETRIC node** (transverse degeneration) supplying `N` + the base size `q` forcing the radius. Registered as the **41st wall confirmation**.

---

## Verdict

`[SYNTHESIS · DEF · coherence-checked vs 𝔽_q]` — **R4's missing special fiber is a REAL LEAD, not an irreducible terminus.** Its exact content is a rank fact: the 1-dimensional orbit admits only `N=0` (rank 1, no symmetric split), the minimal carrier of the degeneration `N` is dimension 2 (the Jordan-2 block, `M(N)={0:1,2:1}`), and the surface `S²/ℤ` supplies exactly that room (`gr^W_2 = H^1⊗H^1`, rank `(2g)² ≥ 4`). **The single missing object is named: an archimedean transverse degeneration of the SURFACE, supplying a nonzero `N` on `gr^W_2` with `M(N)=W` forcing the radius — exactly R6, the standing constructive successor.** **Not overclaimed:** R5 decides the lead-vs-terminus question (real lead) and relieves R4's rank-1 obstruction by naming the correct carrier; it does NOT construct the surface's `N` — that is R6's open existence question, which may recur or relieve the obstruction. **Successor:** R6 promoted to TOP ITEM — does the surface `S²/ℤ`'s archimedean fiber carry a nonzero `N` (inherit `C×C`'s transverse node), or is the surface's archimedean fiber ALSO smooth (the `𝔽₁` obstruction recurring in dimension 2)?
