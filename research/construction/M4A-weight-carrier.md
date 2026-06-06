# M4A — The weight-graded carrier the descent must supply: it is `gr^W_2` (the NS lattice), NOT `gr^W_1` [DEFINE/BUILD · anchored vs 𝔽_q]

**Charter:** `construction-program.md` §1 (clause C3b), §4 (anchor first), §5 (M4). **Built on:** M2d
(`M2d-purity-carrier.md`), which DECIDED that the purity functor `rad = (·)^{1/2} ∘ (edge)` is **not
well-typed per-prime** for `ζ` (no per-prime `gr^W_1`), and named the successor: **DEFINE/BUILD the
weight-1 carrier the descent must supply BEFORE purity acts**, anchoring on the FF rank-`2g` `H^1`, with
the self-product surface `S²/ℤ` (`F-sym2-os-bridge.md`) as candidate (a). **Module:**
`scripts/numerics/witness/weight_carrier.py` (run: `python3 -m scripts.numerics.witness.weight_carrier`).
**Falsifier row added** (`falsify.py`, 44 rows).

This is M4A executed: ANCHOR FIRST — build the carrier for the **function-field self-product surface**,
read off its **weight grading**, and decide what types over `ℤ`.

---

## The deliverable — the carrier the self-product surface actually supplies, weight by weight

ANCHOR (the one place the mechanism is a theorem). For a curve `C/𝔽_q` of genus `g`:
`H^0(C)` rank `1` weight `0` (eig `{1}`), `H^1(C)` rank `2g` weight `1` (eigs `{αᵢ}`, `|α|=√q`),
`H^2(C)` rank `1` weight `2` (eig `{q}`). The self-product surface `S = C×C` carries, by **Künneth**
`H^n(C×C)=⊕_{i+j=n} H^i(C)⊗H^j(C)` with **purity** `weight(H^i⊗H^j)=i+j`:

| carrier of `S=C×C` | rank | weight | Frobenius eigenvalues | purity |
|---|---:|:--:|---|---|
| `gr^W_1 H^•(C×C) = H^0⊗H^1 ⊕ H^1⊗H^0` | `4g` | **1** | `{1·αᵢ}` (= **two copies of `H^1(C)`**) | `|α|=√q` |
| **`H^1(C)⊗H^1(C)` ⊂ `H^2(C×C)`** (the **NS lattice**) | `4g²` | **2** | `{αᵢ·αⱼ}` | `|αᵢαⱼ|=q` |

Computed EXACT over **6 Weil curves** (`g=1`: `q=2,5,7,11,13`; `g=2`: `q=2`,
`T⁴−T³+2T²−2T+4`) — all purity checks pass to `< 1e-14`.

> **[DEF/BUILT · the carrier].** The self-product surface supplies **two** weight-graded carriers. Its
> **weight-1** carrier is *nothing new* — literally two copies of the curve's own `H^1` (tensored with
> the weight-0 `H^0`), eigenvalues the same single zeros `αᵢ`. Its **load-bearing** carrier is the
> **weight-2** middle piece `H^1(C)⊗H^1(C)` — the **Néron–Severi lattice** `NS(C×C)`, where the
> **diagonal `Δ`** and the **graph `Γ_F`** of Frobenius live, `Δ·Γ_{Fⁿ} = #C(𝔽_{qⁿ})`, and **Weil's
> Hodge-index theorem (= RH) operates**. Its eigenvalues are the **products `αᵢαⱼ`**, not the single
> zeros.

---

## The decisive M4A structural output — the carrier is at WEIGHT 2 (a correction to the naming)

M2d, working from the per-prime numerator degree, named the target `gr^W_1`. The FF anchor of the
**self-product surface** (the candidate M2d itself pointed at) shows the surface delivers its RH content
at **weight 2**:

> **[FINDING · the loop correcting the agenda's naming].** The "weight-1 carrier `gr^W_1`" and the
> "self-product surface `S²/ℤ`" — named together in M2d/M4A — are at **different weights**. The
> surface's RH-bearing carrier is **`gr^W_2`** (the NS lattice `H^1⊗H^1`), whose Frobenius eigenvalues
> are the **products `αᵢαⱼ`**. The "weight-1 carrier" `gr^W_1 H^•(C×C)` is the **shadow** — the
> diagonal pullback `C ↪ C×C` restricting `H^1⊗H^1` — of the weight-2 lattice; it carries no content
> the curve did not already have. **The load-bearing object the descent must build is `gr^W_2`.**

This is *not* a setback; it is the loop working — M2d's per-prime measurement found "no `gr^W_1` at a
prime," and M4A's anchor explains *why*: the carrier is the **global weight-2 lattice of the
self-product**, whose pieces `αᵢ(p)αⱼ(p)` are assembled from the **whole Euler product** (every prime
contributes its Satake `αᵢ(p)`), never from one prime. The absence of a per-prime weight-1 numerator
(M2d) is the absence of the curve, and the surface restores the missing object **one weight up**.

---

## The purity square-root, correctly typed: weight-2 → weight-1 (= the Petersson edge → the line)

M2b refined C3b to a **purity functor** `(·)^{1/2}∘(edge)`; M2d found it had no per-prime carrier. M4A
**types the square root correctly**:

> **[DEF · the purity descent].** The surface's **edge is weight 2**: `|αᵢαⱼ|=q` — exactly the
> **Petersson pole** of `L(s,f×f̄)=ζ(s)L(s,sym²f)` at `s=1`, residue `‖f‖²>0`
> (`F-sym2-os-bridge.md`, the unfolding). The curve's **centre is weight 1**: `|αᵢ|=√q` — the line.
> The purity step `(·)^{1/2}` **descends weight 2 to weight 1**, `√q = (q)^{1/2}` (verified `=|αᵢ|` on
> all 6 curves). So M2b's "edge → centre square root" is **placed on the surface's weight-2 NS lattice**
> — *not* on a per-prime weight-1 numerator (which does not exist, M2d).

This closes the typing puzzle M2d left: the `(·)^{1/2}` acts on the **weight-2 self-intersection**
(the Petersson edge), and its square root is the centre `Re s=½`. The square root M2b wanted was
**always weight-2 → weight-1**; M2d's per-prime search looked one weight too low.

---

## RE-TARGETS M4 (the descent)

> **[for M4].** The descent must build the **global weight-2 NS lattice `gr^W_2` of `S²/ℤ`** — the
> Petersson self-intersection lattice carrying the arithmetic diagonal and Frobenius/Hecke graph — and
> the **purity functor is the weight-2 → weight-1 square root** (`|αᵢαⱼ|=q` (edge `Re s=1` of `f×f̄`)
> → `|αᵢ|=√q` (centre `Re s=½`)). C3b becomes: **`gr^W_2(S²/ℤ)` is pure of weight 2**
> (`|αᵢαⱼ|=q`), equivalently its Hodge index on `NS`-primitives is negative-definite = RH. The carrier
> is Euler-assembled (products across all primes), supplying the global object M2d proved no single
> prime supplies.

---

## Falsifier verdict (M4A — anchor/DEF, not a `ℤ`-candidate)

M4A is a **definitional/anchor** result (it builds the FF carrier and types the purity square root); its
three-axis verdict is the FF archetype's, on record:

- **Euler-assembled YES** — the weight-2 eigenvalues `αᵢαⱼ` are products of Euler-borne Satake `αᵢ`;
  **DH has no `sym²`/`f×f̄` product ⟹ no weight-2 lattice** (`S²/DH` is not a carrier). DH-failing.
- **sees-zeros YES** — purity `|αᵢαⱼ|=q ⟺ |αᵢ|=√q ⟺ RH`; the NS Hodge index on primitives flips when a
  zero leaves the line (the `(0,1,1)→(1,0,1)` flip of M2/`euler_movable_inertia.py`, now read on the
  weight-2 lattice).
- **independent NO** — over `𝔽_q` this **is** the Hodge index = Deligne purity = Weil ⟹ **CIRCULAR over
  `ℤ`**, expected and correct for an anchor (the FF owns the radius via the curve).

**NEW content (not circular):** the carrier **weight is 2, not 1**; the purity square root is
**weight-2 → weight-1** (Petersson edge `q` → line `√q`); the carrier is the **global self-product NS
lattice**, Euler-assembled from products `αᵢαⱼ` across all primes — *which is precisely why M2d found no
per-prime weight-1 carrier*.

---

## Verdict

`[DEFINE/BUILD · anchored vs 𝔽_q]` — **the carrier the descent must supply is `gr^W_2` (the
weight-2 Néron–Severi lattice `H^1⊗H^1` of the self-product surface), not the `gr^W_1` M2d named.**
Anchored exactly on 6 Weil curves: the surface's weight-1 carrier is a redundant double of the curve's
`H^1` (eigs `αᵢ`); its weight-2 carrier is the NS lattice where Weil's Hodge-index proof lives (eigs
`αᵢαⱼ`, `|αᵢαⱼ|=q`). The M2b/M2d **purity square root is correctly typed weight-2 → weight-1** — the
Petersson edge `|αᵢαⱼ|=q` (the pole of `L(s,f×f̄)` at `s=1`, residue `‖f‖²`) descends under `(·)^{1/2}`
to the centre `|αᵢ|=√q` (`Re s=½`). This **re-targets M4**: build the global weight-2 NS lattice of
`S²/ℤ`; purity is the weight-2 → weight-1 descent. **Not overclaimed:** this builds and types the FF
carrier and corrects the weight; the `ℤ` lattice is untouched and the FF anchor is CIRCULAR over `ℤ` as
expected. **Successors named:** M4B (the weight-2 NS lattice over `ℤ` as a representability problem —
what represents the self-intersection of the arithmetic diagonal of `S²/ℤ`?); M4C (the Hodge-index /
polarization on `gr^W_2`-primitives as the categorical duality pairing of M1's C4, on the weight-2
lattice).
