# PA — transporting the radius through the `q→1` (𝔽₁) degeneration: is the archimedean radius the `q→1` TANGENT (a SPEED) of the 𝔽_q radius `q^{w/2}`, not its VALUE? [ATTACK · coherence-checked vs 𝔽_q · DEAD_END / CIRCULAR]

2026-06-06. Module: inline mpmath 40dps (this log). Anchors on R3b-BC (`q→1` value-tracking), R8 (type table), R10 (count-vs-radius split). 47th `falsify.py` consideration, DISPERSING-by-design (terminus-characterizer, Euler-silent).

## The mandate / the new angle

R3b-BC tracked the **VALUE** `q^{w/2} → 1` as `q→1` and concluded "the radius evaporates" — a trivial collapse to the point (𝔽₁). This attack asks the sharper question the value-collapse leaves open:

> The radius `q^{w/2}` is a *function of `q`*. Its value at `q=1` is trivially `1`. But the **`q→1` TANGENT / logarithmic derivative** `d/dq[q^{w/2}]|_{q=1} = w/2` is FINITE and nonzero. **Is the archimedean radius the RATE at which `q^{w/2}` departs from `1` — a SPEED, not a cardinality?** This would be a genuinely NEW type evading R8's table (continuum / length / index — none a cardinality), because a *speed* is none of those.

## What got computed (exact, mpmath 40dps)

**[1] The tangent is finite and recovers `w/2` (= the even-split exponent).**
`q^{w/2} = e^{(w/2)·h}`, `h = log q → 0` as `q→1`. Then
`d/dq[q^{w/2}]|_{q=1} = d/dh[e^{(w/2)h}]|_{h=0} = w/2`.
Computed: `w=0 → 0`, `w=1 → 0.5`, `w=2 → 1.0`. The tangent equals **`w/2 = Re s`** exactly. So the value collapses (`→1`) while the **slope is finite (`w/2`)** — the angle's premise (b) is numerically real: there IS a finite renormalized datum at `q=1`.

**[2] The tangent SEES off-circle (it is sensitive to non-purity) — but only as a READOUT.**
A non-pure eigenvalue `|α| = q^{w/2+ε}` (off-line zero, `Re s = w/2+ε`) has tangent `w/2+ε`. Computed: `ε=0 → 0.5`, `ε=0.3 → 0.8`, `ε=−0.2 → 0.3`. So the tangent **distinguishes pure from non-pure** — it changes when the zero moves off the line.

**BUT** the tangent of `q^{Re s}` at `q=1` **is `Re s` identically**: it is a *faithful readout* of the exponent `Re s`, NOT a *forcing* of `Re s = 1/2`. It tells you WHERE the zero is (you must already know `Re s` to build the family `q ↦ q^{Re s}`); it does not constrain it. This is the count/location axis, not the radius/purity axis.

**[3] The new "type" FAILS to be new — the tangent is the EXPONENT in disguise = the abscissa coordinate the scaling site already marks FOR FREE.**
The tangent `w/2` is a dimensionless slope, and dimensionally it is `Re s` — the FE/Haar self-dual axis `1/2 = the even split`, which **R3 (scaling site) already marks freely, DH-shared.** The radius is the *modulus bound* `|α| = q^{w/2}` (eigenvalues lie ON the circle of that radius); the exponent `w/2` is available the instant you *write* `q^{w/2}`. Differentiating `q^{w/2}` and getting `w/2` adds **no purity** — it re-expresses the already-present exponent as a slope. A SPEED here is just the EXPONENT, which is the COUNT/LOCATION axis (`Re s`), not the radius. So the count-vs-radius split (R10) **RE-COUPLES**: the tangent reads the location exponent, never forces it to `1/2`.

## The anchor check (decisive) — does the tangent recover `q^{1/2}` on 𝔽_q WITHOUT assuming the zeros? **FAIL (circular as a forcing).**

The tangent CONSTRUCTION **consumes** the family `q ↦ |α(q)| = q^{w/2}` and returns its slope `w/2`. To build that family you must already supply the modulus `q^{w/2}` at each `q` — which over 𝔽_q is **Weil II / purity**, the radius as INPUT (the constant field under the curve). The tangent **does not produce `q^{1/2}`; it consumes the whole curve `q ↦ q^{1/2}` and returns `1/2`.** The radius is assumed to build the curve.

Worse, the germ is **not arithmetically available**: at `q=1`, `1^{anything}=1`, so the value at the arithmetic place alone determines nothing (computed: exponents `1/2` and `0.8` give identical value `1` at `q=1`). The tangent needs the germ of `q ↦ |α(q)|` in a *neighborhood* of `q=1` — i.e. the whole 𝔽_q family for `q` near `1`. But there is **no 𝔽_q for `q<2`**, and `Spec ℤ` is a single 𝔽₁ point, **not a `q`-interval**: the tangent direction `h = log q` is exactly the missing infinitesimal neighborhood that 𝔽₁-geometry does not supply. (This is the same R8 fact from the derivative angle: "`Spec ℤ` has no constant field" ⟹ no `q`-deformation ⟹ no germ to differentiate.)

So **ANCHOR = FAIL** in the load-bearing sense: the tangent recovers `w/2` only by differentiating a family whose radius is already Weil-II input, and the germ does not exist over ℤ.

## The DH check — does it fail to exist for DH? **PASS, but for the trivial Frobenius reason.**

DH has no Euler product ⟹ no Frobenius ⟹ no `q`-family `q ↦ |α(q)|` ⟹ the tangent is **UNPOSABLE** for DH (no curve to differentiate, no 𝔽_q-deformation of a non-motivic L-function). This passes the DH kill-test, but for the *same* reason every Frobenius-based object passes: there is no `q`-family to begin with. It is not a *new* DH-discrimination — it inherits the Euler-product one.

## Verdict — DEAD_END (and CIRCULAR as a forcing)

> **[ATTACK · PA verdict].** The `q→1` tangent `d/dq[q^{w/2}]|_{q=1} = w/2` is finite (the value collapses, the slope survives — premise (b) of the angle is real), and it is sensitive to off-circle eigenvalues. But it is a **READOUT of the exponent `Re s`, not a FORCING of `Re s=1/2`**: the tangent of `q^{Re s}` is `Re s` identically. The "SPEED, not cardinality" reframing **fails to escape R8's type obstruction** because the speed IS the exponent `w/2` = the even-split / FE-fixed abscissa coordinate the scaling site (R3) already marks FOR FREE, DH-shared — it is the COUNT/LOCATION axis, not the radius/purity axis. The count-vs-radius split (R10) **RE-COUPLES**: differentiating `q^{w/2}` returns the location exponent and adds no purity. **Anchor FAILS as a forcing** — the tangent consumes the radius `q^{w/2}` (Weil-II input) to return `w/2`, and the germ at `q=1` is not arithmetically available (no 𝔽_q for `q<2`; `Spec ℤ` is a single 𝔽₁ point, not a `q`-interval — the same "no constant field" fact, now blocking the differentiation direction). **DH passes** (unposable, no `q`-family) but only via the inherited Euler-product reason.

So `q^{1/2}` as `q→1` does NOT (b) survive as a renormalized finite `1/2` carrying the radius; it survives as the finite slope `w/2` carrying only the **exponent** — option (a) collapse-to-trivial *for the radius*, with the surviving finite datum being the already-free location coordinate, not a new type.

## Falsifier verdict (PA — terminus-characterizer, Euler-silent by design)

- **EULER-BORNE — NO on this pass, by design.** Type-checks the tangent's content; not a standalone ℤ-positivity. DH structural verdict sharp: no Euler product ⟹ no `q`-family ⟹ tangent unposable.
- **SEES-ZEROS — YES (as a readout).** The tangent `w/2+ε` changes when the zero moves off the line — but it *reads* `Re s`, does not force it.
- **INDEPENDENT — NO.** The radius the tangent would mark is `Re s=1/2` = the even split = purity = the FE-fixed DH-shared axis; pinning the readout `w/2+ε` to `1/2` is RH.

→ **DISPERSING-by-design** (terminus-characterizer, Euler-silent like R1–R10). Confirms the count-vs-radius split (R10) and the type obstruction (R8) from the **`q→1` derivative** direction: the surviving finite `q→1` datum (the slope `w/2`) is the **location exponent**, not the radius — the speed is the abscissa coordinate, already free.

**Ladder `DH < ζ < FF`.** DH: no Frobenius ⟹ no `q`-family ⟹ tangent unposable. ζ: the `q→1` value `→1` (R3b-BC), the tangent `→ w/2` finite but `= Re s` (the free even-split axis); no germ at `q=1` (𝔽₁ point, not interval). FF: the family `q ↦ q^{w/2}` exists (𝔽_q, integer prime-power `q`), its tangent is `w/2` — but the family's radius is Weil-II INPUT, so the tangent *consumes* the radius rather than producing it.

**Not overclaimed.** This decides the **tangent/speed** reframing of the `q→1` transport (finite slope YES, but it is the exponent/location, not the radius, and it consumes the radius as input). It does NOT prove no future `q→1`-renormalized invariant could carry purity. It pins the residue from the derivative angle: **the missing datum is a `q`-deformation germ at `q=1` carrying the MODULUS BOUND (not the exponent)** — exactly the 𝔽₁ neighborhood `Spec ℤ` lacks (R8's "no constant field," now as "no `q`-interval to differentiate").
