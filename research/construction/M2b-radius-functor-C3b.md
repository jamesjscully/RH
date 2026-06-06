# M2b — C3b as a representability sub-problem: the radius datum as a functor `{L_p} ↦ μ` [DEF · anchored]

**Charter:** `construction-program.md` §1 (the contract clause C3b), §4 (anchor first). **Contract:**
`construction/M1-universal-property-S_Z.md` C3a/C3b (the FE-borne relation vs the Euler-borne value).
**Built on:** M2 (`M2-ff-hodge-datum.md`) — which confirmed in the working FF model that **C3b is the
SOLE non-categorical residue**, every other clause (C1, C2, C3a, C4, C5) being a categorical structure on
one object. **Module:** `scripts/numerics/witness/radius_functor.py`
(run: `python3 -m scripts.numerics.witness.radius_functor`).

This is the M2b mandate executed: **DEFINE, precisely, what it would mean for the similitude multiplier
`μ` of C3a (`Φ^*φ_{FE}Φ = μφ_{FE}`) to be "read off the local Euler factors `{L_p}`" rather than off the
FE** — i.e. write C3b as a *representability* problem (the radius datum as a functor of the local factors)
— and ANCHOR it in the function field, where C3b is a theorem.

---

## The deliverable — C3b as a functor (the definition)

> **[DEF · C3b as representability].** Let `LocFac` be the category of *local-Euler-factor data*
> (objects: the family `{L_p}` of local factors / point-count data of an arithmetic scheme; morphisms:
> base-change / Frobenius-compatible maps). Let `𝔾_m` be the multiplier group. **C3b holds for an object
> `X`** iff there is a **functor**
> `  rad : LocFac → 𝔾_m  `
> and a **natural isomorphism** `rad({L_p(X)}) ≅ μ(X)`, where `μ(X)` is the C3a similitude multiplier,
> **AND `rad` factors through the local product** (it is a functor of `LocFac`, not of the global FE datum).
> *"Euler-borne"* is precisely this factorization. **C6/DH is built in:** `LocFac` is *empty* for
> Davenport–Heilbronn (no Euler product ⟹ no `{L_p}`), so `rad` has no input ⟹ no `μ` ⟹ no object.

This converts the program's 32-confirmation wall from an after-the-fact falsifier test into a **typed
representability question**: *does the radius datum factor through the local Euler factors?*

---

## The FF anchor — what the functor actually is (computed, 5 Weil curves)

The module builds `LocFac` for genus-1 curves `E/𝔽_q` (objects = Frobenius eigenvalues on `H^1`, the
local datum; the zeros are derived from it) and exhibits **two** candidate radius functors:

| functor | reading | value (FF) | Euler-borne? |
|---|---|---|---|
| `rad_edge` | the **abscissa** / rightmost pole `T=1/q` of `Z_C = ∏_x L_x` — the base size `q = #𝔸¹(𝔽_q)`, a purely local datum | `q` (exact) | **YES** (reads only `{L_p}`, no zeros) |
| `rad_FE` | the multiplier of the FE `Z_C(1/(qT)) = q^{1-g}T^{2-2g}Z_C(T)` | `μ_FE = 1` | DH-shared |

**Computed (all PASS, 5 curves `q=2,5,7,11,13`):**
- `rad_edge = q` **exactly**, and read the hard way as `N_n^{1/n} → q` (the asymptotic growth rate of the
  point counts `N_n = #C(𝔽_{q^n}) = q^n + 1 − Σαᵢⁿ`), with the subleading term `O(q^{n/2})` *being the
  `√q` zeros* — so the edge is `q` and the centre correction is `√q`, made visible numerically.
- **`rad_edge` is a genuine FUNCTOR**: naturality under base change `C/𝔽_q → C/𝔽_{q^k}` holds exactly,
  `rad_edge(C/𝔽_{q^k}) = q^k = rad_edge(C/𝔽_q)^k` (`k=1,2,3`, OK). So `rad_edge : LocFac → 𝔾_m` is
  well-defined — **the radius datum is representable on the local factors.**
- `rad_FE = 1` for every curve — the FE similitude `T ↔ 1/(qT)` (and over `ℤ`, `s ↔ 1−s`) is
  multiplier-1, weight-preserving.

---

## The decisive structural output — C3b refines to a **PURITY functor**

The load-bearing subtlety M2b surfaces, and the genuine refinement of M2's localization:

**`rad_edge` gives only the EDGE weight `q`** (the abscissa, Worker E's `Re s=1`). The **centre radius the
zeros sit on is `√q = (edge)^{1/2}`** — the map `w ↦ w^{1/2}`. In the FF, *that square-root step is
Deligne purity*: `H^1(C/𝔽_q)` is **pure of weight 1**, so `|αᵢ| = q^{1/2}` — a **theorem about the local
factors** (the weight filtration). The module verifies `(rad_edge)^{1/2} = |α|` to machine precision, all
5 curves.

So over `𝔽_q` the Euler product gives the edge `q` directly **and** the centre `√q` *via purity of the
local factors* — Euler-borne end to end. This sharpens the answer to M2's question ("can the FE's `μ=1` be
*upgraded* to an Euler-read `μ` distinct from the FE value?"):

> **The upgrade is NOT a different multiplier.** `μ` stays the FE's `1` for the `s↔1−s` similitude (C3a is
> genuinely FE-borne/DH-shared). The Euler-borne datum is a **SEPARATE** object — the edge abscissa `q` —
> whose **square root, via PURITY, sets the centre**. C3b's "Euler-borne radius" is therefore
> **NOT** "set `Re s=½`" in the abstract, but specifically:
>
> **`C3b ⟺` the local Euler factors `{L_p}` are PURE of the right weight** (carry a weight filtration whose
> `H^1` graded piece is pure of weight 1, so the centre is the square root of the edge).
>
> The radius functor is `rad = (·)^{1/2} ∘ (edge-abscissa) : LocFac → 𝔾_m`.

This is the precise C3b-as-representability statement M2b was tasked to produce, and it **names the next
construction**: M4 must build, *by descent from the local `{L_p}`*, a **weight filtration on `ζ`'s local
factors making `H^1` pure of weight 1** — the centre `Re s=½` as `(edge `Re s=1`)^{1/2}` *via an
Euler-sourced purity*, NOT borrowed from the FE.

---

## The DH falsifier (C6), now type-level

The split is sharper than before: **`rad_edge` does not even type-check for DH.** DH has an FE (so
`rad_FE = 1` survives — DH-shared) but **no Euler product**, hence no `{L_p}`, hence `rad_edge`'s domain
`LocFac` is *empty*. The Euler radius functor has no input; the construction *fails to exist at C3b* exactly
as M1/C6 demanded — and now it fails by **domain emptiness**, not by a numeric flip. This is `falsify.py`'s
Euler-borne axis realized as a typing condition on the functor, the cleanest form of C6 yet.

---

## Falsifier verdict (M2b, anchor — not a `ℤ`-candidate)

M2b is a **definitional/anchor** result (it defines C3b as a functor and realizes it in the FF), not a new
`ℤ`-positivity object, so its three-axis verdict is the FF archetype's, on record: **Euler-borne Y**
(`rad_edge` reads the local product), **sees-zeros Y** (purity `(edge)^{1/2}=√q` is where the zeros sit),
**independent N** (purity is Deligne's theorem, = the FF Weil positivity) **→ CIRCULAR over `ℤ`** — expected
and correct, because over `𝔽_q` the Euler product owns the radius via purity. A `radius_functor` registry row
records the new structural fact: *C3b is the purity functor; the upgrade is the edge `q`, not a new `μ`.*

---

## Verdict

`[DEF · anchored vs 𝔽_q]` — **C3b is now written as a representability sub-problem**: the radius datum is
the functor `rad : LocFac → 𝔾_m`, factoring through the local Euler factors. In the FF it is *realized and
functorial* (`rad_edge = q` exact, natural under base change; `(rad_edge)^{1/2} = √q` by Deligne purity).
The decisive refinement of M2's localization: **C3b = the PURITY functor `(·)^{1/2} ∘ (edge-abscissa)` on
the local factors** — the Euler product gives the edge `q` directly and the centre `√q` *via purity*, so
"Euler-borne radius" means "**the local factors are pure of weight 1**". The FE multiplier stays `1` (C3a,
DH-shared); the Euler upgrade is the *separate* edge datum under the purity square root. **Not overclaimed:**
this defines/anchors the functor; the `ℤ` problem is untouched and now reads "construct an Euler-sourced
weight/purity structure on `ζ`'s local factors" (M4). **C6/DH** is type-level: `LocFac` is empty for DH,
so `rad_edge` has no input.
