# M2d — Is the purity functor `rad : LocFac → 𝔾_m` well-typed for `ζ`? [DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §1 (clause C3b), §4 (anchor first). **Built on:** M2b
(`M2b-radius-functor-C3b.md`), which refined C3b to the **purity functor**
`rad = (·)^{1/2} ∘ (edge-abscissa) : LocFac → 𝔾_m`, leaving open the **square-root/purity step over `ℤ`**.
**Module:** `scripts/numerics/witness/purity_carrier.py`
(run: `python3 -m scripts.numerics.witness.purity_carrier`). **Falsifier row added.**

This is the M2d mandate executed: **DEFINE the weight/purity structure a single local factor must
carry, and DECIDE the typing question** — is `rad` even well-typed for `ζ`, or does the edge→centre
square root require the surface `S²/ℤ` (the missing `H^1`) *before* purity has a carrier?

---

## The deliverable — the input slot of the purity functor, defined per place

> **[DEF · the weight-1 carrier].** The purity functor `rad = (·)^{1/2} ∘ (edge)` factors as two
> operations. The **edge** operation reads the abscissa of the local product (`q ↔ Re s=1`); it needs
> only the *local product's convergence edge*. The `(·)^{1/2}` (**purity**) operation acts on a
> **weight-1 graded piece `gr^W_1`** — and `gr^W_1` at a place is the carrier read off the **numerator
> of the local zeta factor**: writing the local factor `L = P/Q`, the numerator `P` carries the
> weight-1 cohomology (the `αᵢ`), the denominator `Q` the weight-0/weight-2 (`H^0`/`H^2`). The rank of
> `gr^W_1` available at a place is **`deg P`**. The purity step has an **input at a place iff
> `deg P > 0`** (a nonzero weight-1 carrier to take the square root of).

This makes "is `rad` well-typed for `ζ`?" a **computable** question: count `deg P` per place.

---

## The computation (exact, all integer degrees) — the carrier is empty per-prime in BOTH cases

| place / object | `deg P` = rank `gr^W_1` | purity carrier? | edge? |
|---|---:|:--:|:--:|
| FF **GLOBAL** `Z_C`, genus `g` (the **curve**) | `2g` (= 2,4,6) | **YES** | YES |
| FF **LOCAL** `L_x=(1−T^d)^{-1}` (a **point**) | `0` | **NO** | YES |
| `ζ/ℤ` factor `L_p=(1−p^{-s})^{-1}` (a **prime**) | `0` | **NO** | YES |
| `ζ/ℤ` factor `Γ_ℝ(s)` (place `∞`) | infinite product | NO (no finite numerator) | N/A |

**The decisive exact fact:** per-place the weight-1 carrier is **empty for BOTH the FF local factors
AND `ζ`'s primes** — numerator degree `0` in both. A single local factor is a **weight-0 "point"** in
both worlds. **The difference is NOT at the prime.** (`ζ`'s prime factor `(1−p^{-s})^{-1}` is *exactly*
an FF closed point of degree 1: `(1−T)^{-1}`.)

---

## The decisive structural output (M2d) — purity is intrinsically GLOBAL for `ζ`

What separates the FF from `ℤ` is **not** a per-prime property; it is that the FF **assembles a global
weight-1 `H^1`** (rank `2g`) from its local factors, because the **curve** is a 1-dimensional geometric
object whose `H^1` the Euler product computes (Lefschetz: `N_n = q^n + 1 − Σαᵢⁿ`). `ζ`'s primes
assemble **no** weight-1 cohomology: `Spec ℤ` is 0-dimensional arithmetically, and `ζ`'s "`H^1`" (the
nontrivial zeros) is **not** realized as the weight-1 cohomology of any geometric carrier. That missing
carrier is the **surface `S²/ℤ`** (`F-sym2-os-bridge.md`).

> **[TYPING VERDICT for `ζ`].**
> - `rad_edge : LocFac → 𝔾_m` (the abscissa `Re s=1`) **IS well-typed** for `ζ` — the abscissa of
>   absolute convergence of `∏_p (1−p^{-s})^{-1}` is a local-product property (M2b).
> - `rad = (·)^{1/2} ∘ (edge)` is **NOT well-typed per-prime** for `ζ` — the `(·)^{1/2}` (purity) step
>   needs a weight-1 carrier `gr^W_1` that **no single prime supplies** (per-prime `deg P = 0`,
>   *identical* to the FF local factors).
> - `rad` is well-typed **only on a GLOBAL glued object that SUPPLIES `gr^W_1` first.**
>
> **Therefore C3b is NOT a per-prime condition.** It is a condition on the **weight filtration of the
> global glued object**. Purity has **no local carrier** for `ζ`; it is **intrinsically global**.

---

## Why the FF gets purity "for free" and `ℤ` does not (the contrast that names the next step)

Over `𝔽_q` the weight-1 carrier `H^1(C)` is a **geometric object** (étale cohomology of an actual
curve), and Deligne purity (`|αᵢ|=q^{1/2}`) is a **theorem about it**; the Euler product merely
*computes* this pre-existing carrier. Over `ℤ` there is **no pre-existing geometric weight-1 carrier**
for `ζ` — so purity has **nothing to be a theorem about** until a carrier is **constructed**.
Construction (M4 descent + the `S²/ℤ` surface) must come **before** purity, not after.

> **This is the precise sense in which C3b is the OPEN PROBLEM:** not "*prove* purity" but
> "**BUILD the carrier purity would be a property of**." The square-root step is well-defined once
> `gr^W_1` exists; the open problem is upstream of it — supplying `gr^W_1`.

This **re-routes M4**: the descent must **FIRST** construct the weight-1 carrier `gr^W_1` (the `H^1` no
single prime supplies), **THEN** the purity functor sets the centre `Re s=½ = (Re s=1)^{1/2}`.

---

## The DH falsifier (C6), refined to a strict carrier-level ladder

DH has an FE (so `rad_FE=1` survives — DH-shared) but **no Euler product**, hence no local factors,
hence **neither the edge** (no abscissa-of-product) **nor any hope of assembling a weight-1 carrier**
from local factors. For DH the purity functor fails at the **first** factor (edge: empty `LocFac`) — it
never reaches the carrier question. This makes C6 a **strict refinement** — a three-rung ladder on
*how much of the purity functor types*:

| object | edge `(Re s=1)` | weight-1 carrier `gr^W_1` | purity status |
|---|:--:|:--:|---|
| **FF** | YES | **global YES** (the curve, rank `2g`) | **THEOREM** (Deligne) |
| **`ζ`** | YES | local NO, **global OPEN** (`S²/ℤ`) | **OPEN** |
| **DH** | **NO** (no product) | — | **N/A** |

So `DH < ζ < FF`: DH lacks even the edge; `ζ` has the edge and the *open* carrier problem; the FF has
both. C3b's open content is *exactly* the gap between the `ζ` and FF rows — the carrier.

---

## Falsifier verdict (M2d — DEF/coherence, not a `ℤ`-candidate)

M2d is a **definitional/coherence** result (it types the purity functor and locates the missing
carrier), not a new `ℤ`-positivity object. Its three-axis verdict is the FF archetype's, on record:
**Euler-borne Y**, **sees-zeros Y**, **independent N** (purity = Deligne = FF Weil positivity)
→ **CIRCULAR over `ℤ`** — expected and correct. The **new content** is the precise typing fact: the
per-prime carrier is empty *identically in the FF and over `ℤ`* (numerator degree 0 both), so the
hardness is **not** per-prime — it is the **global carrier**, which is open over `ℤ` and is the
`S²/ℤ` surface.

---

## Verdict

`[DEF · coherence-checked vs 𝔽_q]` — **the purity functor `rad = (·)^{1/2} ∘ (edge)` is NOT well-typed
per-prime over `ζ`**: the `(·)^{1/2}` step needs a weight-1 carrier `gr^W_1` (numerator degree `> 0`)
that no single prime supplies — `ζ`'s prime factor `(1−p^{-s})^{-1}` has numerator degree `0`,
**identical** to an FF closed point. `rad_edge` alone **is** well-typed (the abscissa is local). The
carrier exists **globally** in the FF (the curve's `H^1`, rank `2g`) but is the **open object over `ℤ`**
(the surface `S²/ℤ`). So **C3b is a condition on the weight filtration of the GLUED object**, and M4
must supply the carrier **before** purity sets `Re s=½`. Purity is **intrinsically global** for `ζ` —
not a per-prime property. **Not overclaimed:** this types the functor and locates the open carrier; it
does not build it. **Successor named:** M4-A — DEFINE/BUILD the weight-1 carrier `gr^W_1` the descent
must supply (the global `H^1` of the `S²/ℤ` surface) **before** the purity functor can act.
