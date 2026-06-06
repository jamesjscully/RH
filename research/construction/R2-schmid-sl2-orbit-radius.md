# R2 — Does Schmid's SL(2)-orbit `N` force the RADIUS (N4) or only the FREE parity `(−1)^w`? [DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §0 (categorical/duality, not metric), §2 (the `(p,q)` enrichment).
**Block:** the RESIDUE (AGENDA `## NEXT`, item R2). **Built on:** R1 (`R1-weight-monodromy-residue.md`,
`weight_monodromy_residue.py`) — which pinned the residue to an archimedean nilpotent `N` satisfying four
axioms **(N1)–(N4)** and showed the FF mechanism is `M(N)=W`-with-no-zeros, the obstruction being that
`ℤ/∞` lacks the geometric degeneration `𝔽_q` uses. Also M3b (`(−1)^w` is a sign = the free phase),
K2r-fix (the radius is the scale, orthogonal to every conjugation), M4r (the radius is the sole residue).
**Module:** `scripts/numerics/witness/schmid_sl2_orbit_radius.py`
(run: `python3 -m scripts.numerics.witness.schmid_sl2_orbit_radius`). **Falsifier row added.**

R2's mandate: **Schmid's `SL(2)`-orbit theorem is the ONE place where the archimedean weight-monodromy IS a
theorem** — at a degeneration of a polarized variation of Hodge structure (VHS), the limiting mixed Hodge
structure (LMHS) carries a nilpotent `N` with `M(N)=W` (the relative weight filtration), a genuine
*archimedean-place* theorem (Schmid 1973; the `sl_2`/Hard-Lefschetz primitive decomposition). **The
question:** does Schmid's `N` satisfy R1's **(N4) radius compatibility** (force `|α|=q^{w/2}`, the even
split), or only **(N1)–(N3)** + the free weight parity `(−1)^w`?

---

## The recall — R1's four axioms for the archimedean `N`

- **(N1) NILPOTENT** `N^{w+1}=0` (so `M(N)` exists and is finite).
- **(N2) a `(−1,−1)`-MORPHISM** of the polarized HS, `N(F^p)⊆F^{p−1}`, compatible with the real structure `c`.
- **(N3) `M(N)=W`** — the monodromy filtration centered at `w` coincides with the archimedean weight filtration.
- **(N4) RADIUS COMPATIBILITY** — on `gr^M_k` the archimedean "Frobenius" radius has `|α|=q^{k/2}`, so the
  centre (`k=w`) sits at `|α|=q^{w/2}` = the even split.

R1 established (N1)–(N3) are the **mechanism** (`M(N)=W`-with-no-zeros, FF-anchored exactly); **(N4) is the
residue** (the radius). R2 decides whether Schmid's `N` reaches (N4).

---

## The decisive split (exact) — Schmid gives (N1)–(N3) + parity, NOT (N4) radius

**[1] Schmid's `N` supplies (N1)–(N3) at the archimedean place — a theorem.** For a degenerating polarized
VHS, `N = log(`unipotent monodromy`)` is a `(−1,−1)`-morphism, and the LMHS's weight filtration `W` equals
the monodromy filtration `M(N)` with the Hard-Lefschetz `sl_2` primitive decomposition. Verified the
`sl_2` symmetry (pure Hodge/filtration data, **no zeros, no `q`**) for `N`-Jordan structures `[1,1],[2],
[3],[2,2]` → `M(N)=W` absolute weights `[1,1]`, `[0,2]`, `[−1,1,3]`, `[0,0,2,2]`, all symmetric about `w=1`.

**[2] What the centering DELIVERS is the PARITY (a sign), not the radius (a modulus).** The Weil operator
satisfies `C² = (−1)^w` on `gr^W_w` (verified `=−1` for `w=1`); the graded parities are `(k, (−1)^k)`.
**(N4)'s radius `|α|=q^{k/2}` CANNOT be read off Schmid's `N` alone** (the module returns
`q_available=False`): a real/complex polarized Hodge structure carries **no Frobenius eigenvalue, no base
size `q`** — the radius is an *arithmetic* datum, absent at the archimedean place.

**[3] The parity `(−1)^w` is RADIUS-SILENT (the M3b lesson, made exact).** `q=9` and `q=25` give the SAME
parity `(−1)^w=−1` but DIFFERENT radii `3` vs `5`. Fixing the parity does NOT pin `|α|`: the radius is
ORTHOGONAL to the SL(2)-orbit's phase datum — exactly K2r-fix's orthogonality (reality/phase free, the
radius is the scale `d`).

**[4] FF cross-check — why over `𝔽_q` the radius IS forced (the extra factor named).** Over `𝔽_q` the SAME
Schmid `N` exists (a degenerating family of curves), and the radius `q^{w/2}` IS forced — but **only because
the `ℓ`-adic/crystalline realization adds an ARITHMETIC FROBENIUS supplying `q`** (centre radii `2,3,5` for
`q=4,9,25`, from the Frobenius, NOT from Schmid's `N`). The Hodge/SL(2) data is *identical* between `𝔽_q`
and `∞`; the extra ingredient `𝔽_q` has and `∞` LACKS is the **base size `q`**. So over `𝔽_q`: *Schmid's `N`
+ arithmetic Frobenius TOGETHER* force the even split — the SL(2)-orbit gives `M(N)=W` (parity), the
Frobenius supplies `q` (radius). At infinity the second factor is missing.

---

## Verdict — the M3b lesson RECURS (phase free, radius residual)

> **[DEF · R2 verdict].** Schmid's `SL(2)`-orbit theorem delivers **(N1),(N2),(N3) at the archimedean
> place** — a genuine archimedean weight-monodromy theorem — and its centering supplies the **weight parity
> `(−1)^w`** (the phase/reality, M3b's free datum). It does **NOT** supply **(N4), the radius `|α|=q^{w/2}`**:
> a polarized real/complex Hodge structure carries no Frobenius eigenvalue, no base size `q`. Over `𝔽_q` the
> radius is forced by the `ℓ`-adic Frobenius (the EXTRA factor), not by Schmid's `N`. **The SL(2)-orbit gives
> the parity for FREE and leaves the RADIUS exactly where M3b/M4r/K2r-fix left it: the residual, arithmetic
> datum.**

**The residue, re-sharpened by R2:** the missing archimedean `N` must carry **MORE than Schmid's
Hodge-theoretic `N`** — it must couple the `(p,q)`-grading to an **arithmetic SCALE `q` at infinity**. Schmid
gives the `(p,q)` centering; the open object is the `q` (the archimedean Frobenius scale). This is the
precise reason the expected outcome (M3b's lesson) recurs: the SL(2)-orbit lives entirely in the
DH-SHARED archimedean Hodge data, which is phase-only.

---

## Falsifier verdict (R2 — characterization/anchor, not a `ℤ`-candidate)

- **Euler-borne N on this pass** — the SL(2)-orbit / Hodge data is **Euler-SILENT**: it is exactly the
  **DH-SHARED archimedean structure** (DH has the same `Γ`-factor / archimedean Hodge type), so Schmid's `N`
  exists for DH too and is radius-silent for both. The **sharp DH verdict**: Schmid's `N` is DH-shared, hence
  **cannot be the discriminator** — (N4)'s `q` is the only DH-distinguishing datum, and Schmid does not carry it.
- **sees-zeros Y** — only via (N4), which Schmid lacks.
- **independent N** — `M(N)=W ⟹` purity over the FF.

→ the SL(2)-orbit is the **PHASE half** (free, DH-shared, radius-silent); the radius is NOT here. Consistent
with the standing wall (phase free, radius residual). Registered as `euler_borne=False` (a characterization
that LOCATES the radius outside the archimedean Hodge data), with the structural DH ladder `DH=ζ` *on the
SL(2)-orbit datum* (both share it) `< FF` (which adds the arithmetic Frobenius).

---

## Verdict

`[DEF · coherence-checked vs 𝔽_q]` — **Schmid's `SL(2)`-orbit `N` supplies (N1)–(N3) at the archimedean
place (a genuine archimedean weight-monodromy theorem) and the free weight parity `(−1)^w`, but NOT (N4),
the radius** — verified exactly: the `sl_2` symmetry of `M(N)=W` is pure filtration data (no `q`); the
parity is a sign, radius-silent (`q=9` vs `q=25`, same parity, different radius); over `𝔽_q` the radius is
forced by the *arithmetic Frobenius*, the factor `∞` lacks. **Not overclaimed:** this decides the R2
question (Schmid = parity, not radius) and does not build the radius-carrying `N`. **Successor named:** R3 —
the Connes–Consani scaling site / absolute Frobenius is the candidate to supply the missing *arithmetic
scale `q` at infinity*; the success criterion (sharpened from R1's): does the scaling generator's `N` carry
the **radius (N4)**, or — like Schmid's — only the parity? R2 isolates precisely what R3 must provide: not
another `(p,q)` centering (free, DH-shared) but an **archimedean base size `q`** coupling the grading to a
modulus.
