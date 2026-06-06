# Is an equivariant RH-signed regularization of Δ·Δ possible? — an honest exploration (2026-06-06)

The question the lift obstruction (`lift-obstruction.md`) reduces to: can the diagonal self-
intersection divergence `Δ·Δ = lim_{λ→1} 1/|1−λ| = ∞` be regularized to a **finite, equivariant,
RH-signed** value? This is the heart of the missing object, so §8 discipline is maximal: the goal is
to characterize what is *free*, what is *forced*, and whether equivariance and the RH sign are
compatible, in tension, or equivalent — **not** to manufacture a proof.

## The disentanglement (the main result of the exploration)

"Equivariant RH-signed regularization" silently bundles **two** steps that behave completely
differently:

**Step 1 — regularize the divergence.** This is *possible, equivariantly, with the right sign.*
- The divergence is **logarithmic** (`∫ dλ/|1−λ| ~ log`), so the counterterm ambiguity is **one real
  parameter** `c` (the renormalization scale): `Δ·Δ_reg = −log(1/ε) + c` **[computed]**.
- The bare divergence has **negative sign** (`Δ·Δ ~ −log(1/ε) < 0`) — the **Hodge-index direction**
  (`Δ·Δ ≤ 0`), consistent with `Δ·Δ = 2−2g` at "infinite genus" `g=∞`. The corner is **not fighting
  the RH sign.** Encouraging, and the first genuinely positive structural note in the whole search.
- The principal-value (Weil) regularization is **scale-invariant = equivariant** — no cutoff needed.
  So an equivariant regularization of the *divergence* exists.

**Step 2 — make the resulting form RH-signed (positive).** This is *equivalent to RH.*
- The one free parameter `c` is **consumed by matching the actual `ζ`** (the explicit formula is an
  identity; it fixes the finite part). Equivariance has no preferred scale so it does **not** fix `c`;
  the functional equation `λ↔1/λ` forces the counterterm even; `ζ`-matching then pins `c`.
- Once `c` is fixed by `ζ`, the positivity of the resulting Weil form **is RH** (`weil_form.py`: PSD
  iff the zeros are real). There is **no free knob left** to "choose" the sign.

So the user's target splits cleanly: **the regularization is possible and equivariant with the right-
sign divergence; the RH-positivity of the regularized form is `ζ`'s, and equals RH.** The
divergence-regularization is *necessary* (it defines the intersection theory) but **not where RH
lives** — it is the archimedean corner, which is RH-neutral (the digamma `Γ_ℝ` data, shared with
Davenport–Heilbronn; three prior confirmations).

## Why equivariance is in tension with the RH content (the structural reason)

This is the deeper finding and it explains CC20's retreat to a non-equivariant cutoff:

> **Fully `ℝ₊^*`-equivariant operators are Mellin-diagonal** (multipliers `m(s)` in the spectral/
> Mellin variable `s`, by the spectral theorem for the abelian group `ℝ₊^*`). Their positivity is the
> **pointwise-local** condition `m(s) ≥ 0`, which says nothing about *where the zeros sit*. The RH
> content — the zeros lying on the line — is carried by the **off-diagonal / scale-mixing** coupling
> between the archimedean place and the primes, which is **not** Mellin-diagonal, hence **not
> equivariant.**

Two faces of the same fact:
- the equivariant (diagonal) part of the Weil form is the archimedean digamma — **RH-neutral**;
- the indefiniteness that an off-line zero produces (`weil_form.py`: min eig `−1.49`) lives in the
  **off-diagonal** (prime) structure; a diagonal (equivariant) counterterm cannot remove it without
  changing the diagonal value `f(0)` = the regularized trace = **changing `ζ`**.

So **continuous equivariance forces locality, and locality is RH-neutral.** This is the precise sense
in which the "real-number-like" continuity (`Aut(ℝ_max)=ℝ₊^*`) is the wound: a *discrete* Frobenius
(`𝔽_q`) is compatible with the global Hodge index, but the *continuous* scaling group's equivariant
operators see only local spectral data.

## What would actually force RH equivariantly — and why it's obstructed

The one equivariant object that *would* force RH is an **equivariant self-adjoint generator** of the
scaling flow whose spectrum is the zeros (real spectrum ⟺ zeros on the line). The corner divergence
`1/|1−λ|` — the conformal `−1/(2|u|)` kernel at the fixed point — is **exactly the obstruction to
essential self-adjointness** of that generator (`corner_defect.py`): it needs a self-adjoint
extension, and (CC20) the extension either **breaks equivariance** (the `Λ=1` Sonin cutoff) or does
not pin the spectrum to the line. The polarization that would supply the missing positivity is an
**equivariant positive Green form** for the diagonal — the **BGS §6.3** object, which **can genuinely
fail to exist.**

## Verdict (honest)

An equivariant RH-signed regularization is **possible if and only if RH is true** — not more
reachable, not less:

- **Not obstructed by a no-go.** A regularization exists, it is equivariant, the counterterm
  freedom is finite (one scale), and the divergence's sign is *correct* (Hodge/negative). Nothing
  forbids the object.
- **Not forced by any free choice.** The one parameter is consumed by `ζ`-matching; the resulting
  sign is `ζ`'s, i.e. RH. The genuine missing ingredient is the **equivariant positive Green form /
  self-adjoint extension** (the polarization) — BGS §6.3-open — and continuous equivariance makes it
  hard precisely because equivariant data is Mellin-local = RH-neutral.

**What the exploration genuinely bought:** it separated a *solved* sub-problem (regularize the
divergence — equivariant, finite, right sign) from the *RH-equivalent* one (the regularized form's
positivity), located the irreducible obstruction in the **off-diagonal / non-equivariant** coupling,
and surfaced one structurally encouraging fact — **the corner divergence carries the Hodge-index sign,
so the geometry is not pushing against RH.** That is a real, honest clarification, and it is the
boundary of what computation can establish without constructing the polarization.
