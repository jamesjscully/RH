# Stone one of the lift: the conformal scattering operator S(s) — 2026-06-06

First concrete construction step of `research/the-lift-program.md` (`scripts/numerics/witness/
scattering.py`). Built `S(s) = Λ(2s-1)/Λ(2s)`, `Λ(s)=π^{-s/2}Γ(s/2)ζ(s)` — the cusp/Eisenstein
scattering matrix of `PSL(2,ℤ)\ℍ` (Lax–Phillips), the concrete realization of the program's
"conformal-boundary scattering operator whose resonances are the zeros."

## What was built and verified

1. **Resonances = zeros [verified].** `S(s)` has simple poles at `s = ρ/2` (zeros of `Λ(2s)`). Under
   RH, `ρ = ½+iγ ⟹` resonance at `Re s = ¼`. **RH ⟺ all scattering resonances on `Re s = ¼`.**
2. **Unitary on the line [verified].** `|S(½+it)| = 1`, `S(s)S(1-s)=1` — to 1e-30. This is the
   conservation / self-adjointness condition, and it uses **only the functional equation**.

## The kill-test result (the honest, load-bearing finding)

Planted an off-line zero quadruple preserving the functional equation (the RH-false / DH situation):
- **unitarity is unchanged** (`|S_offline(½+it)| = 1`) — so the unitary/self-adjoint **structure is
  RH-NEUTRAL**; it holds verbatim for an RH-false function;
- the off-line zero produces an **off-line resonance** (`Re s = 0.4 ≠ ¼`).

So `S(s)` faithfully **reflects** the zeros as resonances but does **not force** them onto the line.
This is the **Lax–Phillips obstruction, made precise in our framework**: self-adjointness/unitarity is
necessary but RH-neutral. (It also re-confirms, from a new direction, that the archimedean/FE data is
RH-neutral — fourth independent confirmation.)

## Where this leaves the program — stone two

The RH content is isolated to the **forcing**: a positivity that *pins* the scattering resonances to
`Re s = ¼`, which the off-line-zero function must **fail**. It must be **Euler-product-borne** (the only
thing ζ has that the RH-false function lacks). Two routes for stone two:

- **(Weil bridge)** via Birman–Krein, the derivative of the scattering phase `d/dt arg S(½+it)` is the
  spectral density; the resonance-pinning positivity is the **Weil positivity** in scattering language
  — connecting to `weil_form.py` (already a demonstrated RH-detector). Honest caveat: same hard core.
- **(Conformal-geometric, the program's bet)** the genuinely new tool: a **conformal positivity**
  (GJMS / Yamabe-type, the positivity of the conformally-covariant boundary operator built from the
  metric `h_∞` on the canonical) that forces the resonances — the angle Lax–Phillips lacked.

Stone two is: **build the Euler-product-borne forcing functional on `S(s)` and verify it pins ζ's
resonances while failing for the off-line-zero / DH control.** The kill-test scaffold is already in
place (`S_offline`), so stone two is immediately falsifiable.
