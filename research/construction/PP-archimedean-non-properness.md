# PP — the archimedean fibre is NON-PROPER (an OPEN fibre missing its weight-pure boundary), and properness ENABLES but does not directly IMPLY the reality condition F†=F̄ [computed · coherence-checked vs 𝔽_q]

**Charter:** `the-complete-account.md` §4–5 (the residue = `F†=F̄` = the radius / reality / even split = purity). **Built on:** R6/R7/R8 (the residue pinned to a missing finite residue-field cardinality `|κ(∞)|`), M2d (the purity carrier: `deg P` = rank `gr^W_1`, empty per-prime, infinite at `∞`).
**Module / computations:** `/tmp/proper_vs_open.py` (proper-vs-open curve weights over `𝔽_q`), `/tmp/arch_fibre.py` (the archimedean fibre's pole spectrum + duality), `/tmp/forces_reality.py` (does properness force reality?). All recomputed live; no zeros assumed.

ANGLE under test: the program's terminus `F†=F̄` (Rosati adjoint = conjugation = `|α|=√(deg)` = the line) reframed as **PROPERNESS of the archimedean fibre** — because over `𝔽_q`, **purity = `F†=F̄` IS Deligne proper-pushforward purity** (a smooth PROPER variety has pure cohomology). The hope: compactify the archimedean fibre; properness forces purity, no imposed positivity. This is the test of whether `F†=F̄` is PROPERNESS (a real theorem) rather than imposed positivity (the dead branch).

---

## [computed] ANCHOR — over `𝔽_q`, purity IS genuinely PROPER-pushforward purity, and an OPEN curve LOSES it

Exact integer/algebraic weight bookkeeping (`/tmp/proper_vs_open.py`), no zeros input:

| object | H⁰ weights | H¹ (or H¹_c) weights | H² | PURE? | PD perfect? |
|:--|:--|:--|:--|:--:|:--:|
| **SMOOTH PROPER** elliptic `E/𝔽_q` | `[0]` | `[1,1]` (all = 1) | `[2]` | **YES** | **YES** (top class wt 2 present, ranks `1,2,1`) |
| **OPEN** `U=E∖{P}` (affine), `H_c` | `[]` | `[0,1,1]` (MIXED) | `[2]` | **NO** | — |
| **OPEN** `U` ordinary `H^*` | `[0]` | `[1,1,2]` (MIXED) | `[]` (no top!) | **NO** | **NO** (no top class, ranks `1,3,0`) |

**The decisive 𝔽_q fact:** removing ONE point from the proper curve injects a **weight-0** class into `H¹_c` (the boundary/puncture), so `H¹_c(U)` is MIXED `{0,1,1}` — **purity LOST**. Dually `H¹(U)` acquires a **weight-2** residue class `{1,1,2}` and `H²(U)=0` — **no weight-pure top class, Poincaré duality NON-PERFECT**. Purity is restored only by the **proper compactification `E`**, which supplies the missing weight-pure boundary/top. **This confirms ANCHOR_PROPER_VS_OPEN: purity over `𝔽_q` is genuinely proper-pushforward purity, and a non-proper (open) curve genuinely loses it.** Properness is the real, load-bearing hypothesis.

---

## [computed] The archimedean fibre IS NON-PROPER — an OPEN/affine-type fibre with the SAME signature as `H¹_c(U)`

`/tmp/arch_fibre.py`. Deninger's archimedean cohomology: `Γ_ℝ(s)=π^{-s/2}Γ(s/2)` is a **regularized determinant of an UNBOUNDED operator** Θ on an infinite-dimensional `H^1_arch`; its "eigenvalue spectrum" = the poles of `Γ(s/2)` at `s = 0,−2,−4,−6,…` — an **INFINITE arithmetic progression**.

- **TEST (1) NON-PROPER — CONFIRMED.** `dim H^1_arch = ∞` (infinite pole spectrum), versus a proper `𝔽_q` curve's `H¹` with finitely many `2g` eigenvalues. Regularized det of an unbounded operator = finite VALUE (zeta-reg) over an INFINITE-dim space = the exact signature of a **non-proper / open / infinite-type** fibre.
- **TEST (2) DUALITY GAP — CONFIRMED.** `Γ_ℝ(s)Γ_ℝ(1−s)` (what the FE-pairing would land in if PD were perfect) is **not a constant / single pure weight** — it is meromorphic with infinitely many poles (computed: `8.94, 7.42, 0.00087…, 11.9` at `s=0.3,0.5,0.5+5i,0.8`). There is **no finite-dim weight-pure `H²` top class** to pair into. The archimedean Poincaré duality is **NON-PERFECT**.
- **The M2d match.** Proper `𝔽_q` local zeta `= P(T)/((1−T)(1−qT))`: finite numerator (deg `2g` = the weight-1 carrier) and a **weight-pure top `(1−qT)^{-1}`**. `Γ_ℝ` has **`deg P = 0`** (no finite weight-1 carrier — exactly M2d's per-place finding) and an **INFINITE denominator** (the gamma poles). The archimedean fibre is the **OPEN/affine-type object**: it carries the "boundary" poles but **no weight-pure finite top class** — the **same signature as the open curve's `H¹_c`** (mixed, no proper top).

> **[computed verdict, TESTS 1–3].** The archimedean fibre is NON-proper. Its failure mode is **non-perfect Poincaré duality** = a missing weight-pure top/`H²` = behaving like an **OPEN (affine, non-compact) variety missing its boundary**. What a proper compactification must ADD is precisely the **weight-pure boundary/top class** that makes cohomology finite and PD perfect — and this is the **SAME object** R6/R7/R8 chased: not "a finite field" loosely, but the **missing PROPER BOUNDARY (a weight-pure special fibre / top class) of an open archimedean fibre**, whose presence over `𝔽_q` is exactly the finite constant field supplying the weight-pure `(1−qT)^{-1}`.

---

## [computed] THE DISCIPLINE TEST — does properness FORCE `F†=F̄` without assuming the zeros?

This is where the angle is decided. `/tmp/forces_reality.py` + literature check (Kedlaya ch.17, Katz AWS lectures, Conrad seminar L24).

**The theorem is real:** smooth + proper `⟹` pure (`|α|=q^{w/2}`) is Deligne Weil II. So *if* the archimedean fibre were smooth proper, reality would follow. **But the PROOF of that theorem is not "properness alone."** Confirmed two ways:

1. **Simulation (`/tmp/forces_reality.py`).** Take an FE-paired (perfect-PD) eigenvalue multiset with the COUNT fixed on the line: `|α| = {5, 1.8, 1.8, 5}`, products `α·α_dual = q^w = 9`, geometric mean `= 3 = √q` exactly — yet **variance > 0**, individual `|α|` OFF the line. **Perfect Poincaré duality (the FE-pairing `α·α_dual = q^w`) forces only the EDGE/count (the geometric mean), NOT the per-eigenvalue reality `|α|=q^{w/2}`.** This is the program's own **count/radius decoupling** (`the-complete-account` §5), now attributed to PD: PD gives the count, not the radius.

2. **Literature (WebSearch).** "All eigenvalues satisfy `w=i` if `X` is proper and smooth" is the THEOREM, but Deligne's proof of it runs through **Rankin's trick + the tensor-power trick** — a domination/positivity argument. Properness/smoothness make the L-factors **polynomials** (finite degree) and PD **perfect**, which is what makes the Rankin-squaring positivity **runnable**; the reality `|α|=q^{w/2}` is the **OUTPUT of that positivity**, the last step, not a direct corollary of properness.

> **[computed verdict — FORCES_REALITY = ENABLED-NOT-FORCED].** Properness `⟹` finite-dim + perfect PD `⟹` `α·α_dual = q^w` (the EDGE/count) — **this much IS forced, with no zeros assumed.** But the LINE/reality (`|α|=q^{w/2}` for EVERY `α`, zero variance) is **not forced by properness alone**: it is the conclusion of Deligne's **Rankin-squaring positivity**, which properness ENABLES (by making cohomology finite and PD perfect) but does not constitute. Over `𝔽_q` that positivity is FREE (a theorem about the proper family's `sym²`/`X×X` L-function). **At `∞` there is no proper family to run it on** — and that is exactly because the archimedean fibre is non-proper / open (no finite-dim space, no perfect PD, no polynomial L-factor) so the Rankin argument is **not even runnable**.

So the reframe is **half-true and sharper for it**: properness is the genuine, load-bearing hypothesis that is MISSING at `∞` (confirmed: the fibre is open, PD non-perfect), and it is **necessary** — without it the reality argument cannot even start. But properness does **not** discharge `F†=F̄` as a free corollary; it is the **enabling precondition** for the positivity (Rankin/Hodge–Riemann) that does. This neither collapses to "imposed positivity" (the dead branch — the positivity is not imposed, it is a theorem on a proper family) nor to "pure properness forces it for free."

---

## Where RH (the zeros) enters — proof none is used

No zero locations are input anywhere: the weight tables are integer/algebraic bookkeeping (Künneth + excision + Weil II radius `q^{w/2}` as a symbol), the archimedean spectrum is the gamma-pole set, and the forcing test uses an abstract eigenvalue multiset. The zeros would enter ONLY at the final step that is shown to be MISSING: the place where Rankin positivity on a PROPER archimedean family would force `|α|=q^{w/2}` — i.e. RH is exactly the assertion that this missing step holds, which is why no computation here can supply it.

---

## Verdict

`[computed · coherence-checked vs 𝔽_q]` — **PARTIAL / GENUINE-LEAD-with-a-caveat.** The reframe survives its two anchor tests cleanly: (i) over `𝔽_q`, purity is **genuinely** proper-pushforward purity and an **open curve LOSES it** (`H¹_c` mixed `{0,1,1}`, PD non-perfect, top class absent) — properness is the real hypothesis; (ii) the **archimedean fibre is NON-proper** — `Γ_ℝ` is a regularized det of an unbounded operator (infinite-dim `H^1_arch`, gamma-pole spectrum), its duality `Γ_ℝ(s)Γ_ℝ(1−s)` has no weight-pure top class (**PD non-perfect**), and it carries the **exact open/affine signature** of `H¹_c(U)` (`deg P = 0`, infinite denominator — the M2d match). The missing PROPER BOUNDARY = the missing weight-pure top/special-fibre = R6/R7/R8's object, now **correctly named**: not loosely "a finite field," but the **proper boundary of an open archimedean fibre**, equivalently the finite constant field that supplies the weight-pure `(1−qT)^{-1}`.

**The honest caveat (the discipline result):** properness does **NOT directly force** `F†=F̄`. It forces the **edge/count** (`α·α_dual=q^w`, via perfect PD) — confirmed by the off-line FE-paired multiset with correct count but nonzero variance — while the **reality/line** (each `|α|=q^{w/2}`) is the output of Deligne's **Rankin-squaring positivity**, which properness ENABLES (finite-dim, perfect PD, polynomial L-factor) but does not constitute. This is the program's **count/radius decoupling re-derived from properness**, and it relocates the residue precisely: `F†=F̄ ⟺` the archimedean fibre is **compactifiable to a proper fibre on which the Rankin/Hodge–Riemann positivity is RUNNABLE**. The lead is GENUINE (properness is real, missing, necessary, and a living target — condensed/Deninger compactification) but **not a free forcing**: it converts "impose positivity" into "**supply the proper compactification that makes the positivity runnable**," which is strictly sharper but still an open construction, not a discharged corollary.

**Successor:** PP2 — in a CANDIDATE compactification (condensed mathematics / Clausen–Scholze, or Deninger's archimedean Frobenius flow), is the archimedean fibre's `H^1_arch` rendered **finite-dim with perfect PD** (genuinely proper), and if so does Deligne's Rankin-squaring step become runnable there — or is the infinite-dim gamma-pole spectrum **intrinsically non-compactifiable** (a genuine duality-gap TERMINUS, no proper model existing)?
