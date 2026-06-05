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

1. **Forcing-structure search via the obstruction calculus** (§3): enumerate *structured*
   template families, compute each limit obstruction, kill-test it (§5), and check it is not
   Weil-positivity-in-disguise.
2. **Jensen-cover nerve computation** (`jensen_nerve.py`): does the Jensen cert/tail/bridge
   structure have descent teeth (shared sub-problems + slack monodromy) or is it a tree
   (trivial, same fate as NB-BD)?
3. **Win-win framing.** Either a structured family's limit obstruction is a *provable*
   forcing structure (→ a real step toward RH), or every analytic family converges to a
   dispersing equivalence — strong evidence that all analytic obstructions factor through the
   missing `𝔽₁` object. The negative result is itself worth proving.

## 8. References (load-bearing)

- **Farmer** — criteria for RH-equivalences; Jensen polynomials disperse information.
- **Bombieri** — Weil positivity; **Li (1997)**, **Bombieri–Lagarias (1999)** — Li coefficients.
- **Griffin–Ono–Rolen–Zagier (2019)** and **GORTTW** — Jensen hyperbolicity (and its dispersion).
- **Rodgers–Tao (2020)** — de Bruijn–Newman `Λ ≥ 0`.
- **Weil (1948)**, **Deligne (1974)** — RH over function fields (cohomological forcing structure).
- **Connes**, **Deninger**, `𝔽₁` geometry — attempts to build the missing arithmetic site.
- **de Branges**; **Conrey–Li (2000)** — a forcing structure, and its falsification.
- **Davenport–Heilbronn (1936)**; **Potter–Titchmarsh (1935)** / **Epstein** — the kill-test objects.
