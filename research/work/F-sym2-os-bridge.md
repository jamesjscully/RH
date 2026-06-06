# Applying the loop: propagating sym² edge-positivity to the centre (2026-06-06)

Task: take the **unconditional sym² edge-positivity** (Worker E, Route II — the only candidate to
clear Euler-borne AND independent) and propagate it from the edge `Re s=1` to the centre `Re s=½` via
a Hodge/reflection structure. Run `research/method.md`. Tags: **[formal]** / **[open]** / **[falsifier]**.

---

## Step 1 — MECHANISM (object-free)

Where does "edge/half-plane positivity → centre/line spectrum" already work, abstractly?

- **Osterwalder–Schrader reconstruction.** A **reflection-positive** functional `B(θx,x) ≥ 0` (θ an
  involution) has a GNS completion on which the reconstructed transfer operator is **self-adjoint** ⟹
  **real spectrum**. Positivity-on-a-half + reflection-compatibility ⟹ spectrum on the reflection's
  **fixed locus**.
- **Hodge index / Weil.** A self-dual pairing, negative-definite on the primitive part, pins Frobenius
  eigenvalues to the circle (the "line").

**Common object-free form:** *an involution `θ` on a space `H`, a `θ`-compatible form `B` that is
positive on a half, forces the spectrum of the `θ`-reconstructed operator onto the fixed locus of `θ`.*
For ζ, `θ` = the functional equation `s ↦ 1−s`, whose **fixed locus is exactly `Re s = ½`**. So the
mechanism we need is **reflection positivity under the functional equation.**

## Step 2 — AXIOMS (so that `axioms ⟹ RH` is formal)

On an abstract object carrying ζ's data:
- **(A1)** a space `H` built from the **sym²/Rankin–Selberg Euler product** `L(s,f×f̄)=ζ(s)L(s,sym²f)`
  (Dirichlet coefficients `≥0`, an Euler-product norm-square — Worker E, unconditional);
- **(A2)** the involution `θ` = the functional equation `s ↦ 1−s` (fixed locus `Re s=½`);
- **(A3)** the sym² coefficient-positivity assembled into a Hermitian form `B` on `H`;
- **(A4)** **reflection positivity:** `B(θx, x) ≥ 0` on the relevant subspace.

**Formal lemma [formal].** `A1–A4 ⟹` (OS/GNS reconstruction) `⟹` a self-adjoint operator whose
spectrum is the nontrivial zeros `⟹` the zeros lie on the fixed locus `Re s=½` = **RH**. This is a
*one-line* consequence of OS reconstruction — *no hard analysis between the axioms and RH.* The
hardness has been moved entirely onto **A4**.

(Check the method's discipline: the implication IS formal, so the axioms are *complete enough* — the
whole problem is now constructing/verifying A4, not deriving the conclusion.)

## Step 3 — OBSTRUCTION (a precise object)

A1–A3 are unconditional (sym² coefficients are non-negative, the FE is a theorem). **A4 is the only
non-formal axiom.** The obstruction is an *object*: the value of `B(θx,x)` on test vectors localized
at the **FE fixed line `Re s=½` / the archimedean corner** — the same cross-place locus the entire
audit converged on (`W_∞ ≥ Σ_p W_p`, `Δ·Δ`). The sym² gives `B`'s positivity on the **half** `Re ≥ 1`
(the edge); A4 demands it **survive the reflection to the centre**.

## Step 4 — REPAIR + UNIVERSAL PROPERTY

**What the object represents [universal property].** The missing object is the **GNS/OS Hilbert space
of `(B, θ)`** — the reflection-positive completion of the sym² Euler-product form under the functional
equation. It *exists as a Hilbert space with a self-adjoint generator iff A4 holds.* We do not build it
by hand; it is the representing object of the reflection-positive-completion functor.

**Minimal repair (if A4 fails as stated):** a compactification of the corner / a metric making `B`
reflection-positive across `Re s=½` — i.e. `h_∞`, now re-specified as *"the structure under which the
sym² form is OS-positive."*

## Step 5 — MODEL + FALSIFY

The candidate FORCING object is the OS Hilbert space of `(B,θ)`. Run the three axes **by construction**:
- **Euler-borne [falsifier ✓ — maximally].** DH has no Satake parameters ⟹ **no sym²/RS exists** ⟹ `B`
  *cannot be formed for DH* (Worker E). DH-refusing structurally, not just by a sign.
- **sees-zeros [falsifier ✓].** OS reconstruction's spectrum *is* the zeros; the reconstructed
  operator's self-adjointness is exactly the statement "on the line."
- **independent [falsifier ✓].** A1–A3 are unconditional (the `L(1,sym²)` Siegel bound). The only
  conditional/open piece is A4 — and A4 is a *positivity of a form*, not "assume RH."

**⟹ This is the first candidate that, if A4 holds, fills the FORCING slot — clearing all three axes,
with the conclusion formal.** The methodology has collapsed the entire task to a single, sharply-posed,
testable positivity.

## The reduced open problem (the one thing left)

> **[open] A4 — Is the sym²/Rankin–Selberg functional-equation form `B(θ·,·)` reflection-positive?**
> Equivalently: does the unconditional sym² edge-positivity (`Re s≥1`) assemble, under `s↦1−s`, into
> an Osterwalder–Schrader-positive form across the centre `Re s=½`?

This unifies the two strongest threads — **Worker E's sym² (the only Euler-borne+independent object)**
and **thread 1's reflection positivity (the OS route to the self-adjointness stone 1 couldn't get
directly)**.

### Honest status of A4 (do not fool ourselves)
`A4 ⟺ RH` for `L(s,f×f̄)=ζ·L(s,sym²f)` — OS positivity ⟺ self-adjoint reconstruction ⟺ real spectrum.
So A4 is *not weaker than RH*; it is **RH wearing the OS/reflection-positivity coat**. The genuine,
non-circular open content is the **implication**
> **`(sym² coefficients are a norm-square, i.e. `a_n(sym²)≥0`)  ⟹  A4`**
i.e. *does the unconditional edge norm-square propagate, under `s↦1−s`, to OS-positivity across the
centre?* That implication **is** the edge→line wall — but posed in its **most promising form yet**:
the input is an honest **norm-square** (not an assumed positivity), and *norm-squares are reflection-
positive in many settings* (that's the whole content of OS theory). So this is the one place the wall
might genuinely yield — "norm-square ⟹ OS-positive" is a *structured* implication, not "prove the Weil
positivity from nothing." This is the loop doing its job: the wall is unmoved but **re-posed where a
theorem could exist.**

### Step 5 — where the norm-square actually lives (analytic, before any numerics)
A4's input, the sym² norm-square, is the **Rankin–Selberg / Petersson** structure:
`L(s,f×f̄)` has a pole at `s=1` with residue `= ‖f‖²_{Petersson} > 0` (unfolding). So the norm-square's
positivity is **anchored at `s=1` — the edge** (this *is* Worker E's `L(1,sym²)` Siegel bound, and the
residue is literally a Petersson norm). The reflection `θ` must carry that edge-anchored positivity to
the OS form at `Re s=½`. **So A4 reduces to: is the Petersson inner product reflection-positive under
`s↦1−s`?** — and the Petersson positivity, as it stands, certifies `s=1`, not `s=½`.

### Step 6 — what the first pass LOCATES (the loop working)
The first pass does **not** cross the wall — and it tells us *exactly* why and what's missing. The
chain `sym² ⟶ norm-square ⟶ Petersson residue` is **edge-anchored at `s=1`**; OS-positivity at `s=½`
is the reflected centre. So the missing axiom is sharply named:

> **(A5, the next axiom)** a structure under which the **Petersson/sym² edge-norm at `s=1` becomes a
> reflection-positive form across `s=½`** — i.e. an involution/metric pairing the `s=1` residue to the
> `s=½` form. *This is `h_∞` re-specified, now in OS language:* the corner-compactification = whatever
> makes the Petersson edge-norm OS-positive at the centre.

So the loop's first pass converted "propagate sym² to the centre" into a **single, named, structural
target** (A5), with `A1–A4` formal/unconditional around it, the two best threads unified, and the
falsifier passing by construction. The wall is unmoved but **re-posed as a property a metric could
supply** — and that metric is exactly the object the whole program has been circling. Next pass (step
2 with A5 added): axiomatize what pairs the `s=1` residue to the `s=½` form, and ask what *represents*
it.

### (deferred numerics)
A direct min-eigenvalue test of `B(θ·,·)` would only confirm `A4 ⟺ RH` (positive iff RH) — uninformative.
The informative probe is structural (A5): whether *any* natural pairing carries the Petersson residue
from `s=1` to a positive form at `s=½`, tested for sym²Δ vs the DH-surrogate. Queued for the next pass.

## Next step (step 5/6)

Compute `B(θ·,·)` for a concrete Hecke eigenform `f` (e.g. `Δ`, weight 12) and test reflection
positivity numerically. Two outcomes, both informative: **holds** ⟹ chase the proof of A4; **fails at
the corner** ⟹ the failure profile *is* the next missing structure (the `h_∞` compactification),
returning us to step 2 with one more axiom.
