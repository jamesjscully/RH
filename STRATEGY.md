# Strategy — the anti-futility charter

**This file is the single source of truth.** It supersedes and replaces the deleted
`research-program.md`, `research/tracker.md`, and `research/forward-theorem.md`. Its job
is to stop this project from drifting back into futility. Read it before proposing work.

The historical record of *why* things were abandoned lives in `research/log/` — keep those;
they are the immune memory.

---

## 0. The one lesson: reverse force / forcing structure

Most exact criteria for RH are **information-dispersing equivalences** (Farmer): they are
equivalent to RH without being a *route* to it. The mechanical tell is the
**Davenport–Heilbronn function** — a ζ-type functional equation, no Euler product,
provably off-line zeros. Any criterion that holds for DH is RH-neutral.

> A route is viable only if it carries a **forcing structure** (≡ a "bridge with reverse
> force"): a property **provable on its own terms** that **forces** the zeros onto the
> line — not merely a statement equivalent to their being there.

Equivalence is not leverage. An `iff` with RH cannot be easier than RH. Only a forcing
structure breaks that symmetry.

## 1. The forcing-structure catalog (the only known templates)

| template | forcing agent | status |
|---|---|---|
| **spectral** (Hilbert–Pólya) | self-adjointness | operator unconstructed; circles back to positivity |
| **positivity** (Weil) | positive-definite pairing | number fields: only known *equivalent* → dispersing |
| **cohomological** (function fields; Weil 1948 / Deligne 1974) | Frobenius eigenvalues + Poincaré duality + intersection positivity | **proven** — but the object (a surface over `𝔽_q`) has no `ℤ`-analogue |
| **dynamical** (de Bruijn–Newman) | heat-flow monotonicity | Rodgers–Tao 2020: `Λ ≥ 0` unconditional; `RH ⟺ Λ ≤ 0`. Reverse force in **one** direction only |
| **hyperbolicity / Laguerre–Pólya** (Jensen) | real-rootedness preservation | provable results are **dispersing** (Farmer): `RH up to height T → hyperbolicity for d ≤ T²`; unconditional fixed-degree needs `n ≥ c·e^d`. No reverse force |

Common thread: **a forcing structure is a provable, preserved positivity.** The number-field
gap is precisely that the object which would make the positivity *provable* (the arithmetic
surface) does not exist — this is the `𝔽₁` / Connes / Deninger problem. Every number-field
attack is, at bottom, an attempt to manufacture that object.

## 2. Autopsy: why the witness / Nyman–Beurling program was futile (deleted)

- `forward = RH` (Ge 2019 / Wei–Wu 2022); the reverse direction is trivial; the
  Hilbert/Gram geometry is **RH-neutral** (holds for DH). It is a dispersing reformulation
  with **no reverse force** — exactly the failure mode the project's own founding instinct
  (anti-dispersion / kill-tests) was built to reject.
- The **descent micro-test** confirmed it structurally: the explicit-formula/NB-BD family is
  *additive* in the primes → its cover is a chain → contractible nerve → `H¹ = 0` → the
  obstruction is cohomologically trivial and collapses to the (unprovable, dispersing) Weil
  positivity. Descent is **decoration** there.
- **Deleted** as futility: `hardy.py`, `forward_bound.py`, `power_test.py`, the entire Lean
  witness/Hardy/Strategy apparatus, `research-program.md`, `forward-theorem.md`, the forward
  workstreams. Do not reconstruct them.

## 3. The reframe: obstruction → forcing structure

Obstruction theory is the one "impossibility" methodology that *constructs*: a vanishing
obstruction class **is** existence. So:

> Organize would-be proofs as a **functorial family of templates**; compute the **limit
> obstruction**; its **marginal vanishing is the forcing structure.**

Two non-negotiable requirements (drop either and it's vacuous):

1. **Metric enrichment.** The obstruction must be the **slack itself** (a real number, ≤ 1
   by a whisker), not a qualitative cohomology class. Lawvere-cost / graded enrichment;
   the analytic seed is pro-étale → condensed mathematics (descent that remembers norms).
   "No slack" = the obstruction vanishes *marginally* — i.e. `Λ = 0`.
2. **Functorial organization.** Obstructions must cohere along refinement maps into a limit
   object. A scattered pile of futility lemmas is a graveyard, not a calculus.

## 4. The descent nerve criterion (the cheap structural gate)

A descent/obstruction calculus has *teeth* on a template family **iff the nerve of its cover
has nontrivial `H¹`** — iff the pieces overlap in **cycles**.

- **Additive / nested** families (explicit formula, prime cutoff, NB-BD truncations) →
  chain/tree nerve → `H¹ = 0` → **decoration**.
- **Overlapping-bridge** families (Jensen degree/shift boxes, interval subdivisions) →
  potentially `H¹ ≠ 0` → **descent-live**.

**The real subtlety (where the obstruction actually lives).** Constant-coefficient nerve `H¹`
only sees the *topology* of the covered region (contractible → 0), and a pure cert/tail/bridge
**recursion is a tree** (contractible → `H¹ = 0`). The genuine descent obstruction is `H¹`
with the **certificate sheaf** (slack-valued) as coefficients, which can be nonzero via
**monodromy** even over a contractible base. So teeth require **shared sub-problems**
(reconvergent cycles, a DAG not a tree) **and** nontrivial **slack monodromy** around them.
This is the same metric enrichment from §3, arrived at independently.

Tool: `scripts/numerics/witness/descent_test.py` (`cech_h1`), `jensen_nerve.py`.

## 5. The kill-test discipline (gates every candidate must pass)

A candidate forcing structure / bridge is admitted only if it:

1. **fails for Davenport–Heilbronn** (no Euler product) — `explicit_formula.py`;
2. **fails for the Epstein second wall** (product-bearing yet RH-false) — `second_wall.py`;
3. **respects Weil/Li positivity** (≥ 0 for ζ, detects DH's off-line zeros) — `li_positivity.py`;
4. **is not descent-trivial** (its cover's nerve has `H¹ ≠ 0`) — `descent_test.py`;
5. **is not a known dispersing equivalence** (not Weil-positivity-in-disguise);
6. is not falsified the way **de Branges** was by **Conrey–Li (2000)** — i.e. its mechanism
   must not over-prove.

`harness.py` runs gates 1–4 on demand.

## 6. DO NOT (the futility attractors)

- Do not grind NB-BD / forward convergence / Gram or distance bounds.
- Do not prove more RH-equivalent reformulations — they hold for DH.
- Do not prove Jensen hyperbolicity bounds — dispersing (Farmer).
- Do not mistake the harness **defending** a candidate for progress; the harness exists to
  **kill** dispersing candidates and drive a search.
- Do not adopt a categorical / descent framing **without the metric enrichment** — bare
  category theory abstracts away the only hard part (the slack).
- Do not formalize ahead of the math. Lean was premature; the witness formalization is
  deleted. Re-introduce a formal substrate only when there is a certified obstruction or
  forcing-structure theorem worth checking.

## 7. The live work

0. **THE ACTIVE THREAD — the spectral edge** (`research/spectral-edge.md`;
   `research/state-of-search.md`). The Hermite junction is now mapped: its static/archimedean
   side is understood **and RH-neutral** (the dBN flow is a pure dilation on the Hermite fixed
   shape = exactly marginal; the fixed shape's archimedean energy is the shared digamma `Γ_ℝ`
   factor, identical for ξ and Davenport–Heilbronn ⇒ dispersing; the slack is super-exponential
   in every coordinate). So the RH content is in the **deviation from the fixed shape** —
   *transverse* to the marginal flow, at the **spectral edge (Tracy–Widom/Airy)**, on the
   dynamical/Euler-product side. **Precise question:** does the edge fluctuation of `J_{d,n} − H_d`
   admit a one-sided (`Λ≥0`-compatible) bound under the dBN flow, uniform in `d`? **First pull:**
   resolve edge-vs-bulk on the *real* ξ data (the BW height is edge-dominated but root collision
   is bulk — §8 says verify, don't assume).

1. **Forcing-structure search via the obstruction calculus** (§3): enumerate *structured*
   template families, compute each limit obstruction, kill-test it (§5), and check it is not
   Weil-positivity-in-disguise.
2. **Jensen path — resolved on real data** (`jensen_nerve.py`, `jensen_real.py`;
   log `2026-06-05-jensen-real.md`). A *correct* Jensen proof has filled diamonds →
   constant-coefficient `H¹ = 0` → **descent topology is decoration here too**. The real
   obstruction is **metric**: the Hermite stability radius `ρ(d) ~ e^{−1.22 d}` (computed) —
   the slack vanishes exponentially. The forcing-structure question, made precise: can the
   `ζ^{(2n)}(½)` asymptotic error be driven below `ρ(d)` **uniformly in `d`**? RH-hard exactly
   where `ρ(d) → 0`. **Live target:** a certified uniform-in-`d` error-vs-`ρ(d)` bound — the
   metric enrichment (§3), not the topology.

3. **Metric/Arakelov direction** (`research/metric-arakelov-probe.md`). The slack is
   potential-theoretic, and potential theory *is* the archimedean place of Arakelov geometry —
   so Option 1 ("metric replaces topology") already exists (Arakelov heights, the Connes–Consani
   tropical arithmetic site, Berkovich/condensed analytic geometry). Computed bridge:
   `log(1/ρ(d)) ~ 1.22 d` is **a height** (linear), while the bare Hermite discriminant grows
   like `d² log d` (the **semicircle = GUE-universal** log-energy) — i.e. the slack is the
   condition-number = **arithmetic height of the discriminant variety**. Next: P2 (is the rate
   GUE-universal?) and P4 (recast "error-height ≤ slack-height uniformly in `d`" as an
   arithmetic-Hodge-index positivity, then kill-test it). Honest caveat: the forcing endpoints
   (positive Green forms, archimedean Weil positivity, Connes–Consani) are RH-hard open; the
   one cheap, novel, computable thing is the Jensen-slack ↔ height bridge.
4. **Win-win framing.** Either a structured family's limit obstruction is a *provable*
   forcing structure (→ a real step toward RH), or every analytic family converges to a
   dispersing equivalence — strong evidence that all analytic obstructions factor through the
   missing `𝔽₁` object. The negative result is itself worth proving.

## 8. Verifiability commitment (formal backpressure)

Exploratory research is informal and numeric by necessity — but the project commits to a
**verifiable path**, so we cannot fool ourselves. Backpressure applied *now*, before any
formalization:

- **Certified, not floating.** Every numeric claim is a python-flint ball-arithmetic
  enclosure (a certified interval), never a bare float.
- **Exact structure.** Every structural claim (nerve `H¹`, slack monodromy, ranks) is exact
  linear algebra over `ℤ/ℚ`, not a numerical threshold.
- **Gated.** Every candidate runs the kill-test gates (§5) and the descent criterion (§4).
- **No "proved" without a certificate.** A claim is established only as a certified
  inequality or (later) a checked proof — never as "the numerics look right."

**Commit trigger.** The moment exploration yields a concrete candidate that passes all
kill-tests *and* carries a non-trivial descent obstruction (the first genuine
forcing-structure candidate), **re-introduce a formal substrate** (Lean, or a proof-checked
certificate format) and migrate the spine into it before building further. Formalizing
earlier is premature (§6); formalizing never is self-deception. This is the pre-commitment
that forbids both — once exploratory research concludes, the path becomes verifiable.

## 9. References (load-bearing)

- **Farmer** — criteria for RH-equivalences; Jensen polynomials disperse information.
- **Bombieri** — Weil positivity; **Li (1997)**, **Bombieri–Lagarias (1999)** — Li coefficients.
- **Griffin–Ono–Rolen–Zagier (2019)** and **GORTTW** — Jensen hyperbolicity (and its dispersion).
- **Rodgers–Tao (2020)** — de Bruijn–Newman `Λ ≥ 0`.
- **Weil (1948)**, **Deligne (1974)** — RH over function fields (cohomological forcing structure).
- **Connes**, **Deninger**, `𝔽₁` geometry — attempts to build the missing arithmetic site.
- **de Branges**; **Conrey–Li (2000)** — a forcing structure, and its falsification.
- **Davenport–Heilbronn (1936)**; **Potter–Titchmarsh (1935)** / **Epstein** — the kill-test objects.
