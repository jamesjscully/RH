# dBN anchor — where forcing `Λ≤0` stalls, and is it the same wall? (2026-06-06)

**Item** (AGENDA NEXT #1, with #4 folded in). Map exactly where the dynamical route stalls: be
precise about Rodgers–Tao's mechanism and why it gives `Λ≥0` not `Λ≤0`; decide whether the
obstruction to `Λ≤0` (=RH) is the SAME cross-place coupling `W_∞≥Σ_p W_p` as the static routes, or a
genuinely distinct dynamical endpoint; and run the kill-test on the GUE/pair-correlation lever.

Module: `scripts/numerics/witness/dbn_anchor.py` (+ 1 `falsify.py` row). Builds on `dbn_route.py`.

## The mechanism (Q1), stated precisely [THM, Rodgers–Tao 2018, arXiv:1801.05914, Forum Math Pi 2020]

`H_t = e^{-tD²}xi`; `Λ(xi)=inf{t : H_t all-real}`; de Bruijn–Newman: **RH ⟺ Λ≤0**. RT prove
**Λ≥0 unconditionally**, by **contradiction**:
- Assume `Λ<0` (= RH with a strict spectral margin).
- Over `(Λ,0]` the zeros `x_j(t)` flow under the repulsive log-gas ODE
  `d/dt x_j = −2 Σ_{k≠j} 1/(x_k−x_j)` (Csordas–Smith–Varga dynamics). `Λ<0` forces
  **convergence to local equilibrium**: gaps equalize, so at `t=0` the zeros must locally look like
  an **arithmetic progression** (uniform spacing → global mean).
- **Contradiction via Montgomery pair correlation**: zeta's true zeros (`t=0`) have **GUE-type**
  pair correlation `1−(sin πu/πu)²` — level repulsion *with oscillation*, NOT the rigid
  picket-fence AP that equilibrium would force. Hence `Λ<0` is impossible ⟹ `Λ≥0`.
  (Source: Tao's blog 2018-01-19; abstract confirms the proof uses **dynamics + pair-correlation
  statistics**, NO Euler product / arithmetic surface.)

**Why `≥` not `≤`** [the load-bearing asymmetry]. RT derive the contradiction from a property the
zeros DO have (GUE rigidity being *incompatible with equilibrium*): a **lower bound on disorder** —
"the zeros are too repulsive to have equilibrated, so the flow can't have run far backward" ⟹ `Λ` not
very negative ⟹ `Λ≥0`. RH is `Λ≤0`: **no complex zero pair exists at `t=0`** — a statement about zero
**locations** (the imaginary part), which a **2-point statistic cannot see** (a single off-line pair
is measure-zero in pair correlation). This is the **same modulus(statistics)/phase(location) split**
that closed the static forms (DONE #25–#28): `≥` is a bulk/statistics(=modulus) bound; `≤`=RH is a
per-zero location(=`sign Im`/phase) bound.

## What I made executable (`dbn_anchor.py`)

**[Q1] forward/backward asymmetry — COMPUTED, monotone.** The root variance (log-gas spread) is
monotone in flow time: `Var(roots)` at `t=−.02,−.01,0,+.01,+.02 = 2.500, 2.580, 2.660, 2.740, 2.820`.
**Forward DISPERSES** (`dVar=+0.16`), **backward CONTRACTS** (`dVar=−0.16`). RT exploit the backward
contraction→equilibrium; **forward flow has NO Lyapunov purchase on reality** — there is no monotone
functional pushing a stray complex pair back onto `ℝ`, so the `≤` direction gets no forcing.

**[Q2] does the flow EVADE the Sylvester inertia-lock?** YES — a genuinely distinct finding. The heat
semigroup `e^{-tD²}` is NOT a `*`-congruence `Tᵀ(·)T` of a fixed form (which Sylvester locked in
every static route); it is a 1-param group acting on the **polynomial/zeros** and **CHANGES the count
of real roots**. COMPUTED: a config with one complex pair (`all_real=False`) becomes all-real after
flow (`all_real=True`, `Λ=0.186`). So on the **inertia axis** the dynamical branch is genuinely
different from the closed static family — it is not inertia-locked.

**[Q4] DECISIVE KILL-TEST — is the GUE/pair-correlation lever Euler-borne or universal?** The RT
contradiction needs "zeta's zeros are repulsive/rigid, not AP-equilibrium". The input supplying that
is **GUE level repulsion**. COMPUTED small-gap depletion `P(gap<0.25·mean)`:
- **GUE (no Euler product, pure Hermitian random matrix): `0.020`**
- Poisson (uncorrelated): `0.220`
- AP / equilibrium: `0.000`

GUE (NO Euler product) shows the level repulsion the argument relies on (~11× depletion vs Poisson),
**identical to what the contradiction needs**. So the lever is the **universality class**, shared with
non-zeta spectra — **NOT a zeta-intrinsic Euler-borne lever** ⟹ **RH-silent on the Euler axis**.
(Lit. corroboration: DH off-line zeros have "essentially different" statistics, but the GUE INPUT
itself is universal, shared with random matrices that have no Euler product.)

## Verdict [computed + THM-flavored]

- **Λ sees zeros** YES (`Λ>0 ⟺ off-line pair`, `dbn_route.py`).
- **The flow ESCAPES the Sylvester inertia-lock** YES — genuinely distinct on the inertia/congruence
  axis (a 1-param semigroup, not a congruence; changes the real-root count). **This is the one place
  the dynamical branch is structurally NEW.**
- **BUT the only UNCONDITIONAL handle (RT) gives `Λ≥0`, the WRONG direction, and its lever (GUE/
  Montgomery pair correlation) is UNIVERSAL, NOT Euler-borne.** falsify.py classifies the lever
  **DISPERSING** (not Euler-borne).
- **The `Λ≤0` endpoint reduces to the SAME wall**: forbidding a single off-line pair = per-zero
  location/phase control = `W_∞≥Σ_p W_p` read dynamically. The forward/backward asymmetry IS the
  modulus/phase split. **29th confirmation of the standing cross-place coupling**, now from the
  dynamical side.

**Net.** The dynamical branch is genuinely distinct on the **inertia axis** (it is not Sylvester-
locked — a real, honest finding the static-route audit could not have produced), but it does **not**
provide a new Euler-borne lever: the only unconditional input (GUE pair correlation) is universal
(RH-silent) and points the wrong direction (`≥`), and the `Λ≤0` direction needs exactly the per-zero
location control the wall withholds. **The route is not a reformulation of the static wall (different
endpoint on inertia), but it stalls at the SAME place** for the SAME reason: no Euler-borne object
controls zero *locations*. What RT do NOT supply — and what a genuinely new attack would need — is a
**flow functional built from `Λ(n)` (the Euler data) that is monotone toward reality** (a dynamical
`W_∞≥Σ_p W_p`). That is the precise open object the dBN branch leaves.

## Honest subtleties
- The variance/Sylvester demos use small synthetic polynomials (the dBN flow is exact on polynomials;
  the structural point — semigroup changes real-root count, forward disperses — is robust and exact).
- The GUE depletion is a coarse 2-point discriminator (small-gap fraction), not the full sine-kernel
  form factor; but the load-bearing fact (GUE-without-Euler-product carries the repulsion the RT
  contradiction needs, `0.020` vs Poisson `0.220`) is unambiguous and matches the literature.
- The `Λ≥0`/`Λ≤0` asymmetry and the GUE-universality are [THM]/literature; the executable parts are
  the monotone variance, the real-root-count flip (Sylvester evasion), and the GUE depletion numbers.

## Sources
- Rodgers, Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914 (Forum Math Pi 8, 2020).
- T. Tao, blog 2018-01-19 (mechanism, the AP-equilibrium contradiction, forward/backward asymmetry).
- Montgomery, *The pair correlation of zeros of the zeta function* (GUE pair correlation).
- Davenport–Heilbronn off-line zeros have "essentially different" statistics (web-search corroboration).
