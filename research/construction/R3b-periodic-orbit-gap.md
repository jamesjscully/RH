# R3b — Does DISCRETIZING the scaling (periodic orbits, period `log p`) supply the arithmetic base size `q` (N4), or only the EDGE/length? [DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §0 (categorical/duality, not metric), Pillar A (the `𝔽₁` base = Connes–Consani).
**Block:** the RESIDUE (AGENDA `## NEXT`, item R3b). **Built on:** R3 (`R3-connes-consani-scaling-radius.md`, `scaling_site_radius.py`) — which PROVED the CONTINUOUS scaling site marks the FE/Haar self-dual axis `1/2` (DH-shared, free) but NOT the arithmetic `q`, and **CONVERTED the residue** from "an `ℝ_{>0}^×`-grading" (the scaling HAS one) to **"a DISCRETE / GAPPED refinement carrying a finite base size at `∞`"** (the archimedean analogue of `|𝔽_q|` finite). Also M4r (the radius is not a function of the determinant/edge; the product/edge assembles, the individual radius does not).
**Module:** `scripts/numerics/witness/periodic_orbit_gap.py` (run: `python3 -m scripts.numerics.witness.periodic_orbit_gap`). **Falsifier row added (38th wall confirmation).**

R3b's mandate: R3 named the residue as a **discrete gap at `∞`**. R3b tests the ONE natural archimedean discretization the Connes program offers — the scaling flow's **PERIODIC ORBITS** (in Connes' trace formula / the scaling site, `Spec ℤ` appears as the set of periodic orbits, one per prime `p`, of length `log p`; the orbit `C_p = ℝ_{>0}^× / p^ℤ`, a circle of circumference `log p`, with discrete holonomy `p^ℤ`). **The question:** is the per-orbit period `log p` (or the holonomy `p^ℤ`) the discrete gap supplying a per-place arithmetic base size — forcing `|α| = p^{w/2}` on `C_p` — or, like the continuous scaling, does the orbit supply only a *length* (the edge), with the radix `p` entering only through the arithmetic (Euler) input?

---

## The decisive split (exact mpmath 40dps, FF-anchored)

**[A] The periodic orbit `C_p = ℝ_{>0}^× / p^ℤ` IS a genuine discrete refinement — the gap R3 asked for EXISTS at the orbit level.**
The holonomy group is the **DISCRETE `p^ℤ`** (not the continuum), the primitive period is `log p`, and the Frobenius-at-`p` is the **marked generator** `t ↦ p·t`. Verified: the holonomy spectrum `{p^n}` is gapped (constant ratio `p`). Unlike the bare continuous scaling (homogeneous, no marked point, R3's `marked_q_exists = False`), the ORBIT carries a discrete marked generator. **The discrete refinement R3 named EXISTS.**

**[B] BUT the marked size `p` is the ARITHMETIC LENGTH SPECTRUM (the Euler input), not an archimedean datum the flow produces.**
The orbit length spectrum `{log p : p prime}` IS the prime-length spectrum: the radix recovered as `exp(log p) = p` is the SAME prime `p` the Euler factor `(1−p^{−s})^{−1}` carries (verified). The archimedean scaling flow `t ↦ λt` is the SAME continuous flow for all `λ`; the orbits `C_p` are **labelled BY the primes** (the arithmetic input), not produced by the flow. So the discreteness/gap at `C_p` is **Euler-SOURCED**, not archimedean-sourced. **Davenport–Heilbronn** has non-multiplicative coefficients `a_n` (`a_2 a_3 = 0.91 ≠ 0.5 = a_6`), so there is NO prime-orbit decomposition / no multiplicative length spectrum `{log p}` closed under the orbit structure — the periodic-orbit gap **FAILS to exist for DH** at the multiplicativity step.

**[C] The FF anchor — `𝔽_q(C)` has ONE shared ground field `q`; `ℤ`'s radices differ, no single archimedean base.**
Over `𝔽_q(C)` the periodic orbits are the **closed points `x`**, length `deg(x)·log q`, with the base size `q` the **SAME `q` for every orbit** (one global ground field `𝔽_q`); the per-point datum is only `deg(x)`. Over `ℤ` the would-be orbits `C_p` have radix `p` **DIFFERING per prime** (all distinct) — there is NO single ground-field `q`. The "base size at `∞`" R3 sought would be a **SINGLE archimedean scale** uniformizing all the `p`'s (the `q→1` / `𝔽₁` base), and that single uniformizing scale is **NOT in the per-prime length data** — the length spectrum gives a gap PER prime, not one shared archimedean `q`.

**[D] The decisive pin — the orbit length `log p` is the EDGE; the radius is the SEPARATE residue (M4r, one level deeper).**
The orbit length `log p` sets the orbit **circumference = the EDGE datum** (the determinant `|αβ| = p^{k−1}` / the abscissa `log p`). The **RADIUS `|α| = p^{w/2}`** on the orbit's `H^1(C_p)` is the SEPARATE even-split / purity condition. A plant off the even split (`|α'| = r·p^{w/2}`, `|β'| = p^{w/2}/r`) has the SAME orbit length `log p` AND the SAME edge/determinant but a DIFFERENT radius (verified `length_pins_radius = False`, all primes). **So the length does NOT pin the radius** — exactly M4r's split (the product/length assembles, the individual radius does not), now localized to the orbit.

---

## Verdict — discretizing RECOVERS a gap, but it is the EULER INPUT / the EDGE, not a new archimedean radius

> **[DEF · R3b verdict].** The periodic orbits `C_p = ℝ_{>0}^× / p^ℤ` DO carry a discrete gap (the marked holonomy `p^ℤ`, the primitive period `log p`) — **the discrete refinement R3 named EXISTS.** BUT the gap it supplies is the **PRIME LENGTH SPECTRUM `{log p}` = the EULER input itself** (the radix `p` at `C_p` is the SAME `p` as the Euler factor), NOT an archimedean datum the flow produces; and it is the **EDGE datum** (the orbit length/circumference = the determinant/abscissa), NOT the per-orbit RADIUS `|α| = p^{w/2}` (the even split on `H^1(C_p)` = purity). Over `𝔽_q(C)` ONE ground-field `q` serves all orbits (per-point datum = `deg(x)` only); over `ℤ` the radices differ and the single archimedean base (`q→1` / `𝔽₁`) R3 sought is NOT in the length data.

**The advance over R3 (genuine, on the FALSIFIER axis).** R3's scaling-`1/2` was DISPERSING (DH-shared). **R3b's periodic-orbit gap is the FIRST scaling-side datum that MOVES to genuinely Euler-borne** (the length spectrum `{log p}` is multiplicative ⟹ DH fails at multiplicativity). The discretization crosses the DH line — but it lands on the **EDGE** (RH-SILENT), not the radius. So R3b lands on **M4r's wall ONE LEVEL DEEPER**: the periodic-orbit discretization is Euler-borne and supplies the EDGE/length, but the RADIUS is the SAME residue, now localized to "the Frobenius/monodromy eigenvalues ON the orbit cohomology `H^1(C_p)` lie at `|α| = p^{w/2}`" = the orbit even split = purity = RH — which needs R1's archimedean `N` (N4) ON the orbit, still absent.

---

## Falsifier verdict (R3b — characterization/anchor, not a `ℤ`-candidate)

- **Euler-borne YES** (on the EDGE/length half) — the orbit length spectrum `{log p}` is multiplicative ⟹ DH FAILS at multiplicativity (no prime-orbit decomposition, no length spectrum closed under the orbit structure). **The first scaling-side datum that moves from DH-shared (R3) to genuinely Euler-borne** — real progress on the falsifier axis.
- **sees-zeros NO** — the orbit LENGTH is the EDGE, RADIUS-SILENT: a plant off the even split has the SAME length (M4r: the product/length assembles, the individual radius does not).
- **independent NO** — the radius `= even split = purity = RH`.

→ classifier verdict **RH-SILENT** (Euler-borne, but blind to the zero locations through the length). The periodic-orbit gap is the **EDGE half** (Euler-borne, the length/determinant); the RADIUS is the residue. **M4r's split RECURS at the orbit level.** Registered as the **38th wall confirmation**.

---

## Verdict

`[DEF · coherence-checked vs 𝔽_q]` — **discretizing the scaling (the periodic orbits `C_p = ℝ_{>0}^×/p^ℤ`, period `log p`) RECOVERS the discrete gap R3 named, but it is the EULER input itself (the prime length spectrum `{log p}`) / the EDGE (the orbit length = the determinant/abscissa), NOT a new archimedean radius.** The discretization crosses the DH line (Euler-borne, the first scaling-side datum to do so) but lands on the edge (RH-silent), not the radius — M4r's split one level deeper. **Not overclaimed:** R3b decides the periodic-orbit question (it gives the Euler-borne length/edge, not the archimedean radix `q`) and re-localizes the residue to **"the Frobenius eigenvalues ON `H^1(C_p)` lie at `|α| = p^{w/2}`"** = the orbit even split = purity. **Successor:** R4 (the EXISTENCE/construction of R1's archimedean `N` (N4) ON the periodic orbit `C_p` — does any degeneration / limiting structure supply an `N` with `M(N) = W` forcing the orbit radius `p^{w/2}`, or is its non-existence over `ℤ` the precisely-located obstruction?), now with the orbit as the concrete locus and the EDGE (the length) Euler-assembled for free.
