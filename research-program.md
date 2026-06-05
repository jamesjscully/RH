# Research Program Spec: A Quantitative Witness-Constraint Route to RH

> **Status note.** The live work breakdown, status, and discipline live in
> [`research/tracker.md`](research/tracker.md), which is the source of truth. This
> file holds the corrected *strategy and mathematics*. An earlier version of this
> document mislocated the difficulty of RH (it named reverse visibility the central
> bottleneck and treated forward convergence as bookkeeping). That framing has been
> inverted here; see [§9](#9-corrected-contradiction-mechanism) and
> [§13](#13-known-risks).

## 1. Mission

The goal is an **unconditional** proof of the Riemann hypothesis. Not a conditional
framework, a numerical scheme, a reformulation, or a collection of analogies.

The central thesis — stated carefully, because the naive version is a trap:

> RH should be attacked through witness systems whose finite truncations make the
> **forward (approximation) problem** carry genuine **arithmetic / Euler-product**
> content, while a cheap **reverse oracle** and the **explicit formula** keep the
> search from proving things that are false or merely RH-equivalent.

The naive version — "forward approximation and reverse obstruction meet in the same
finite coordinates and contradict an off-line zero" — is *true but inert*. As shown in
§9, the reverse obstruction is a lower bound on the very quantity the forward side must
drive to zero; there is no independent "gap" to win. The real content is entirely on
the forward/arithmetic side.

## 2. Guiding principle

Many exact criteria for RH are known. **Almost all of them are RH-neutral
reformulations**: a criterion phrased in Hilbert geometry (Gram matrices, kernels,
closures) typically holds verbatim for the **Davenport–Heilbronn function**, which has
a ζ-type functional equation but **no Euler product** and **provably has off-line
zeros**. A criterion or lemma is on the critical path to RH **only if it fails for
Davenport–Heilbronn** — i.e. only if the Euler product is load-bearing in it.

This is the program's governing test. It does two jobs at once:
- it rejects **false** statements (anything that "proves" RH for DH is false), and
- it rejects **circular** statements (anything that holds for DH is RH-neutral and
  cannot, by itself, be progress).

The second failure mode — proving true-but-RH-equivalent statements and mistaking them
for progress — is the dominant way a program like this wastes years. The DH test is
the mechanical guard against it.

## 3. Primitive object

A quantitative witness-constraint system

\[
\mathfrak W =
(\Theta,\theta_c,\{\mathcal H_\theta\},\{C_\theta\},
\{V_N(\theta)\},\{D_\theta\},\{Q_{N,\theta}\},
\{L_{N,\theta}\},T).
\]

Components: parameter space `Θ`, critical parameter `θ_c`, ambient Hilbert spaces
`H_θ`, target constraint `C_θ`, finite witness spaces `V_N(θ)`, dual/extremal data
`D_θ`, finite quadratic forms `Q_{N,θ}`, explicit loss terms `L_{N,θ}`, transports `T`.

The finite witness spaces are generated from effectively presented arithmetic data
(typically Dirichlet polynomials with prescribed coefficients), so that the **choice of
coefficients** is where Euler-product information is injected. This is deliberate: the
geometry is neutral; the coefficients are not.

## 4. Core hierarchy

A graded hierarchy, to keep the class non-vacuous: **E** (exact critical theorem
`⟺ RH`), **F** (off-critical forward theorem yielding genuine zero-free/positivity
consequences), **C** (finite compression: Gram matrices, tail/conditioning ledgers),
**D** (explicit dual/extremal machinery), **R** (same-coordinate reverse *detection* —
now understood as a cheap oracle, not the hard part), **S** (scale-stable coupling),
**P** (certified positivity backend).

The immediate target is one E/F/C system in the base class with a **load-bearing
Euler-product mechanism in the F layer**, validated against the DH barrier.

## 5. Base class

The proof spine lives in the **Hardy-module / weighted-deformation** class. Two avatars.

### 5.1. Critical Hardy avatar

In the disk model (Ghosh–Kremnizer–Noor–Santos 2024; Noor 2019), with the corrected
normalization,

\[
h_k(z) = \frac1k\,\frac{1}{1-z}\,
\log\!\left(\frac{1+z+\cdots+z^{k-1}}{k}\right),
\qquad k\ge 2,
\]

the critical exact theorem is

\[
\mathrm{RH}\iff 1\in\overline{\operatorname{span}\{h_k:k\ge 2\}}^{\,H^2(\mathbb D)}.
\]

(The leading `1/k` was missing in the earlier draft.) This is a Hardy-space
repackaging of the Báez-Duarte strengthening of Nyman–Beurling, and inherits its
quantitative theory (§6).

### 5.2. Half-plane module avatar

For `Ω_τ = {Re s > τ}`, `τ > 1/2`, set

\[
\phi_\tau(s)=\frac{s-1}{s^2}\zeta(s),\qquad u(s)=\frac{s-1}{s^2},
\]

(the factor `(s−1)/s²` kills the pole at `s=1` and supplies the decay that puts `u` and
`φ_τ D_N` into `H²(Ω_τ)`; note `ζ` itself is **not** in `H²` of a half-plane). The
finite module witness spaces are `V_N(τ) = {φ_τ D_N : D_N(s)=Σ_{n≤N} a_n n^{−s}}`.

**Exact criterion (Ge 2019; Wei–Wu 2022).** For `1/2 ≤ τ < 1`,
`ζ` is zero-free in `Ω_τ ⟺ closure Ran(M_{φ_τ}) = H²(Ω_τ) ⟺ dist(u, closure V(τ)) = 0`.
The `τ=1/2` case is `RH ⟺ Ran(M_φ)` dense. (The disk half-plane analogue, GKNS Thm 4.8,
is only one-directional.)

Zeros become annihilators: if `ρ ∈ Ω_τ` is a zero of `ζ`, every element of `V_N(τ)`
vanishes at `ρ`, for every `N`. **This is the entire reverse mechanism, and it is
trivial** (§8, Barrier Oracle).

### 5.3. Transport requirement

The two avatars must be connected by explicit Mellin/Cayley transports carrying
quantitative norm comparison for forward error, conditioning, truncation, and losses.
Qualitative equivalence is not enough.

## 6. Quantitative invariants

Track for every system: forward error `E_{N,θ} = dist_{H_θ}(C_θ, V_N(θ))`; forward
frontier `σ_N(θ)` (the actual zero-free/positivity consequence); the reverse oracle
value `G` (the trivial evaluation bound, §8); conditioning `κ_{N,θ}`; loss budget
`L_{N,θ,T}`.

**Quantitative reality of the forward error** (this is the binding constraint):
- `E → 0` along `τ ↓ 1/2` is **equivalent to RH**; no unconditional rate is known.
- Unconditional lower bound (Burnol 2002): `d_N² ≥ (Σ_ρ m(ρ)²/|ρ|² + o(1))/log N`.
- Best **conditional** upper bound (Balazard–de Roton 2008):
  `d_N² ≪ (log N)^{−1/2+o(1)}`.
- Optimal coefficients lock onto Möbius: `a_n → −μ(n)` (Báez-Duarte). **This is where
  the Euler product lives.**

There is no "signal-to-slack ratio `G − L − E`" to engineer positive: `G ≤ E`
automatically for any `τ < β`, so the inequality is consistent for free and never
yields a contradiction. The earlier §6.7 framing is withdrawn.

## 7. Resolution scales (scope correction)

The earlier "two scales of reverse visibility" (`δ_T`, `ν_{N,θ}`, `R_θ(N)`) addressed
whether a finite level can *resolve* a zero. **For the half-plane multiplier
construction this is a non-issue**: the zero sits in `V_N(τ)` exactly, for every `N`,
so detection is free and `N`-uniform. Resolution scales are a real concern only in the
Báez-Duarte *dilation* model, where witnesses do not carry the zero as a common factor.
Do not import that machinery into the module avatar without a specific quantitative
purpose.

## 8. Central components

### 8.1. Theorem A — Finite compression with explicit losses *(necessary bookkeeping)*

Prove the explicit Gram representation

\[
\operatorname{dist}_{H^2(\Omega_\tau)}(u,V_N(\tau))^2
= \|u\|^2 - b_{N,\tau}^*G_{N,\tau}^{-1}b_{N,\tau} + \operatorname{Err}_{N,\tau},
\]

with explicit entries, target vector, certified tail error, and condition-number
estimates `κ(G_{N,τ})` as `τ ↓ 1/2`. This is RH-neutral but real: it fixes the
coordinates everything else uses, and `κ` is a genuine input to the harness.

### 8.2. The Barrier Oracle — same-coordinate reverse detection *(cheap guardrail, not a bottleneck)*

For a hypothetical zero `ρ = β + iT` and fixed `τ ∈ (1/2, β)`,

\[
\operatorname{dist}(u,V_N(\tau)) \;\ge\; \frac{|u(\rho)|}{\|k_\rho^{(\tau)}\|}
\;=\; \frac{|u(\rho)|}{\sqrt{1/(2(\beta-\tau))}} \;\sim\; \frac{1}{T}\sqrt{2(\beta-\tau)} \;>\;0,
\qquad\text{for all }N,
\]

since `k_ρ^{(τ)} ⟂ V_N(τ)` at every level. This is exact, classical, and `N`-uniform.
Its role is **not** to be part of the proof; it is the reverse half of the harness
(§10) — the cheap necessary condition that any forward construction must respect, and
the demonstration that the spine is otherwise DH-blind. No projected packets, jets, or
resolution functions are needed for this.

### 8.3. Theorem F — Forward / arithmetic theorem *(the actual bottleneck = RH)*

Construct, **unconditionally and using the Euler product**, bounded-`H²(Ω_τ)`-norm
Möbius approximants `φ_τ M_N` (`M_N = Σ_{n≤N} μ(n) n^{−s}`) with
`dist(u, V_N(τ)) → 0` along a path `τ ↓ 1/2`. By §5.2 this is exactly "ζ zero-free in
`Re s > 1/2`" = RH. There is no separate "coupled-path theorem"; the coupling *is* this
statement. The required content is an arithmetic mechanism that **fails for DH**. All
real effort concentrates here.

## 9. Corrected contradiction mechanism

Assume RH fails: a zero `ρ = β + iT`, `β > 1/2`. For any fixed `τ ∈ (1/2, β)` the
Barrier Oracle gives `dist(u, V_N(τ)) ≥ c(ρ,τ) > 0` for all `N` — done, no path needed.
So the *reverse* direction is immediate and contributes nothing hard.

The proof therefore reduces to a single statement: **prove `dist(u, V_N(τ)) → 0`
unconditionally along some `τ ↓ 1/2`.** That alone implies RH (it contradicts the
oracle for every hypothetical zero). It is not a coupling problem; it is RH, and it is
unprovable by the RH-neutral geometry alone. The program's entire job is to supply the
missing **Euler-product mechanism** that makes this forward convergence unconditional,
with the harness (§10) preventing circular or DH-blind detours.

## 10. The refutation harness *(replaces "reverse visibility as proof")*

Every candidate forward lemma passes four cheap *evaluations* before we invest in a
proof. Full spec in [`research/tracker.md` §2](research/tracker.md). In brief:

1. **Barrier battery** — does the conclusion survive for Davenport–Heilbronn / a
   planted-zero "fake ζ"? A pass exposes falsity or Euler-product blindness.
2. **RH-content tag** — does it constrain `Θ = sup{Re ρ}`? If not, it is RH-neutral.
3. **In-coordinate necessary conditions** — Möbius locking (`a_n → −μ(n)`), Burnol
   lower bound, conditioning sanity.
4. **Finite explicit-formula consistency** — a truncated Weil-positivity check (an
   exact identity coupling zeros and primes; non-circular; DH-discriminating).

## 11. Power test (mandatory go/no-go)

Before aiming at RH, demonstrate the machinery can **unconditionally reprove a known
result** — the classical zero-free region, a zero-density estimate `N(σ,T)`, or
Littlewood's `M_N → 1/ζ` for `Re s > 1`. If it cannot reprove even the classical
zero-free region, it has demonstrated **zero proving power toward RH**, and the
strategy must be reassessed rather than elaborated. This is the cheapest possible
falsification of the whole program.

## 12. Standards for progress

Counts as progress: a finite Gram formula with controlled error; a conditioning
estimate; a forward construction whose coefficients provably lock onto `−μ(n)`; a lemma
that **provably fails for DH** (Euler product load-bearing); an unconditional reproof of
a known result (Power Test); a rigorous obstruction theorem; a finite explicit-formula
positivity bound tied to witness coordinates.

Does **not** count: another RH-equivalent criterion; any statement that holds for DH;
qualitative transport without loss control; density in a non-critical topology;
positivity analogies without an explicit intertwiner; numerics without certified
inequalities.

## 13. Known risks

### 13.1. The bottleneck is the forward theorem, and it is RH

The hard part is **not** the reverse theorem (which is trivial, §8.2). It is the
unconditional **forward/arithmetic** convergence (§8.3), which is literally RH. The
program is acceptable only insofar as it supplies a genuinely new Euler-product
mechanism for forward convergence and produces intermediate **unconditional** results
(Power Test, obstruction theorems) along the way. If it cannot, it is an elaborate
restatement of RH.

### 13.2. Circularity / RH-neutrality *(top risk)*

The dominant failure mode is proving true-but-RH-equivalent statements. Mechanical
guard: the DH test (a statement holds for DH ⟺ it is RH-neutral or false).

### 13.3. DH-blindness

The Hilbert-geometry spine uses no Euler product and is therefore DH-blind. Every
critical-path lemma must fail Check 1 for DH; if it passes, it is off the path.

### 13.4. Conditioning blow-up

As `τ ↓ 1/2`, `G_{N,τ}` may become ill-conditioned. Keep `κ` as a Check-3 input.

### 13.5. Misallocation of effort

Avoid lavishing structure on the neutral geometry and the easy reverse oracle. Budget
effort by §1's thesis: the forward/arithmetic side is the whole problem.

## 14. Development ethic

Theorem-first. Every abstraction must produce a finite inequality, a norm estimate, a
lower bound, a transport estimate, a conditioning estimate, a limit theorem, or an
obstruction theorem — **and must fail for Davenport–Heilbronn if it claims to be on the
critical path.**

## 15. Strategic endpoint

The program succeeds if it proves, **unconditionally and with a load-bearing
Euler-product mechanism**, that there is a Hardy-module witness system and a path
`(N_m, τ_m)`, `τ_m ↓ 1/2`, with `dist(u, V_{N_m}(τ_m)) → 0`. By Ge / Wei–Wu this is RH.
Every intermediate deliverable is judged by whether it moves an **unconditional**
frontier and whether it **fails for DH**.

## Appendix A. Established inputs

- **A.1 Nyman–Beurling–Báez-Duarte closure.** `RH ⟺ d_N → 0` (Báez-Duarte 2003).
  Optimal coefficients `~ −μ(n) n^{−ε}`. Unconditional lower bound (Burnol 2002)
  `d_N² ≳ (Σ_ρ m(ρ)²/|ρ|²)/log N`; conditional upper (Balazard–de Roton 2008)
  `≪ (log N)^{−1/2+o(1)}`. **No unconditional rate to 0 is known.**
- **A.2 Disk Hardy criterion.** GKNS 2024 / Noor 2019: `RH ⟺ 1 ∈ closure span{h_k}`
  in `H²(D)` (iff at the disk; one-way in the half-plane).
- **A.3 Half-plane module/range criterion.** Ge 2019 (operator criterion
  `RH ⟺ Ran M_φ` dense) and Wei–Wu 2022 (closure-of-range characterization,
  bounded-norm Dirichlet form). The forward theorem the program leans on.
- **A.4 Dual/biorthogonal infrastructure.** Toeplitz/de Branges–Rovnyak machinery —
  useful for the (cheap) oracle, not the bottleneck.
- **A.5 Weighted/off-critical deformations.** Define the forward frontier `σ(τ)`; note
  it gets stuck at `Θ = sup{Re ρ}`, and `Θ = 1/2 ⟺ RH`.
- **A.6 Arithmetic locking *(primary, not secondary)*.** Coefficient limits force the
  Möbius function. This is the only non-RH-neutral content; it is where the Euler
  product enters. Treat as central, not as a side track.
- **A.7 Explicit-formula / positivity *(primary backpressure oracle)*.** The Weil
  explicit formula couples zeros and primes as an exact identity; finite truncations
  give cheap necessary inequalities (harness Check 4). Promoted from secondary backend.
- **A.8 Barrier objects.** Davenport–Heilbronn (func. eq., no Euler product, off-line
  zeros incl. `Re s > 1`; Davenport–Heilbronn 1936, Bombieri–Ghosh 2011, Bian–Hejhal
  2007); planted-zero "fake ζ"; truncated Euler products. The litmus tests of §2.

## Appendix B. First milestones

Concrete enough to fail. (Statuses tracked in `research/tracker.md` §4.)

- **B.1 Refutation harness** — the test-object battery (ζ, DH, planted-zero ζ,
  truncated Euler product) and the four checks. *Do first.*
- **B.2 DH-blindness demonstration** — run the spine's evaluation obstruction against
  DH and confirm it cannot distinguish DH from ζ. First real result.
- **B.3 Finite Gram notebook** — closed forms for `G_{N,τ}`, `b_{N,τ}`; `κ(G_{N,τ})`
  as `τ ↓ 1/2`; numerics for small/medium `N`.
- **B.4 Power-test attempt** — try to unconditionally reprove the classical zero-free
  region (or `M_N → 1/ζ` for `Re s > 1`) in the witness language.
- **B.5 Forward mechanism scoping** — identify exactly where the Euler product must
  enter to make forward convergence unconditional (must fail for DH).

## Appendix C. Working rules

1. Every abstraction must produce a finite inequality, transport estimate, reverse
   bound, or obstruction theorem.
2. Every finite theorem states its topology and norm.
3. Every transport states its losses.
4. **Every critical-path lemma must fail for Davenport–Heilbronn.** If it holds for DH,
   it is RH-neutral or false — label it a shadow result and keep it off the spine.
5. Every limiting statement specifies the coupling of `N`, `θ`, `T` (note `T` is fixed
   for the existence argument).
6. Prefer unconditional intermediate results; a conditional construction is a shadow
   model, kept out of the spine.
7. Convert failed attempts into obstruction theorems.
