# AN-dB — de Branges spaces / the Conrey–Li no-go — verdict: REAL_NOGO (scoped) + CIRCULAR core (2026-06-06)

Mapping the de Branges strategy on the analytic side, against the program's charter
(`analytic-strategies-map.md`) and Theorem B′ (`WRITEUP-geometric-obstruction.md`: the RH-positivity is
not forced by any structural datum — it must come from analysis). This is the ONE place on the analytic
side where a *genuine analytic no-go theorem already exists* (Conrey–Li). Below: the exact statements, an
independent 40-digit verification of the counterexample, the precise scope, and the positivity-source
diagnosis. Discipline: [established]/[partial]/[heuristic].

---

## 1. What de Branges requires (precise) [established]

A **de Branges space** `H(E)` is a reproducing-kernel Hilbert space of entire functions attached to a
**structure function** `E` in the **Hermite–Biehler class** (`|E(z̄)| < |E(z)|` for `Im z > 0`, i.e. no
zeros in the open upper half-plane). Inner product and kernel (Conrey–Li (2.1)–(2.2)):

```
⟨F, G⟩_{H(E)} = ∫_{-∞}^{∞} F(x)Ḡ(x)/|E(x)|² dx,
K(w,z) = [E(z)Ē(w) − Ē(z̄)E(w̄)] / [2πi(w̄ − z)].
```

For ζ take `E(z) = ξ(1 − iz)`, `ξ(s)=s(s−1)π^{−s/2}Γ(s/2)ζ(s)`. Then **RH ⟺ all zeros of `E` lie on
`Im z = −1/2`**, and the functional equation `ξ(s)=ξ(1−s)` becomes `Ē(z̄)=E(z−i)`.

**Key fact (the structural half is FREE):** ζ's `E` DOES satisfy the Hermite–Biehler / Pólya-class
prerequisites. Conrey–Li compute `|E(z)|² = ∏_ρ [(Im ρ + y)² + (Re ρ − x)²]/|ρ|²`, which (using only
`0 < Re ρ < 1`, Hadamard–de la Vallée Poussin 1896) gives `|E(x−iy)| < |E(x+iy)|` for `y>0` and
`|E(x+iy)|` strictly increasing in `y`. So the **membership in the right class is unconditional** — this
is exactly the Step-A / functional-equation datum of Theorem B′, free at every radius.

**De Branges's forcing theorem** (Conrey–Li Theorem 1, "essentially due to de Branges"):

> Let `E` have no real zeros, `|E(z̄)|<|E(z)|` for `Im z>0`, `Ē(z̄)=ε E(z−i)` (`|ε|=1`), and `|E(x+iy)|`
> strictly increasing in `y>0`. **IF** the **strong positivity condition**
>
> **(3.1)   `Im⟨F(z), F(z+i)⟩_{H(E)} ≥ 0`** for every `F∈H(E)` with `F(·+i)∈H(E)`,
>
> THEN the zeros of `E` lie on `Im z = −1/2` (= RH), and `Im{Ē'(w)E(w+i)/2πi} ≥ 0` at every zero `w`.

The companion **Theorem 2** (analytic-function space `F(W)`, `W=1/ξ(1−iz)`): if `Im⟨F, TF⟩_{F(W)} ≥ 0`
(`T: K(w,z)↦K(w+i,z)`), i.e. **(3.3)**, then `W` extends analytically to `Im z > −1/2` and
`Re[W(z)/W(z+i)] ≥ 0` there — i.e. ζ has no zeros with `Re s > 1/2`.

So the **de Branges prerequisite is exactly the positivity hypothesis (3.1) [and/or (3.3)]** — everything
else (class membership, FE, kernel) is unconditional.

## 2. What Conrey–Li refuted, and the EXACT scope [established; verified here to 40 digits]

The conclusion of Theorem 1 includes a **necessary** consequence: `Im{Ē'(w)E(w+i)/2πi} ≥ 0` at *every*
zero `w`. Writing `ρ=1−iw`, this is `Im{Ē'(w)E(w+i)/(2πi)} = −Re{ξ'(ρ)ξ(1+ρ)}`. Conrey–Li exhibit a zero
where it is **negative**, so (3.1) is FALSE for ζ's own space.

**(3.2):** at `ρ = 1/2 + i·111.0295355431696745…` (the 34th zero),
`−ξ'(ρ)ξ(1+ρ) = −5.389100507182945… × 10⁻⁶⁹ < 0`.

**Independent verification (this log), mpmath dps=40:**
```
ξ(ρ)            = −4.5e−51 + 1.1e−81 i   (numerically a zero)
−ξ'(ρ)·ξ(1+ρ)   = −5.389100507182942961…×10⁻⁶⁹  + 6.1e−68 i
Re part         = −5.38910050718294…×10⁻⁶⁹  < 0   ✓ matches Conrey–Li (3.2) exactly
```
(40-digit agreement with their published constant.) Companion refutation of Theorem 2, **(3.4):**
`Im[ξ(1+i·282)/ξ(2+i·282)] = −0.000131957 < 0` ⟹ (3.3) fails. Same for `L(s,χ₄)`.

**This is a PROOF, not a numerical heuristic.** A single zero `w` with `Im{Ē'(w)E(w+i)/2πi}<0`
*contradicts* the necessary conclusion of Theorem 1; hence its hypothesis (3.1) is provably false for
`E=ξ(1−iz)`. (It happens to be exhibited by a computation, but the logic is a strict contradiction, not a
sampling.) **[established — REAL_NOGO for this hypothesis.]**

### Scope — what is and is NOT closed

- **CLOSED (REAL_NOGO):** de Branges's **specific strong positivity hypotheses (3.1)/(3.3)** — the
  *particular* conditions from his 1986–1994 papers that he used to deduce RH — are **provably not
  satisfied** by the canonical zeta/`L`-spaces `H(ξ(1−iz))`, `F(1/ξ(1−iz))`. The tool, *as he applied
  it*, is inadequate (Wikipedia/Conrey–Li: "his tools are therefore inadequate to address the problems in
  question").
- **NOT CLOSED (the honest limit):** Conrey–Li do **not** assert de Branges's mathematics is wrong, only
  the conclusions. They refute *one specific sufficient condition*, not the *entire* idea of building a
  de Branges/canonical-system model of ζ. A **weaker** de Branges approach — a different `E`, a different
  positivity, a chain of subspaces, or the canonical-system / Krein-string reformulation — is **not**
  killed by Conrey–Li. (de Branges's later preprints do not even cite them; the gap recurs but is not
  *the same* refuted inequality.)

**So the Conrey–Li no-go is REAL but NARROW:** it forecloses the *literal* de Branges positivity for ζ,
not the de Branges *framework*. It closes a labelled door, not the corridor.

## 3. Positivity source — does de Branges supply a NEW analytic source, or reduce to Weil? [established/partial]

**Reduces to Weil — REDUCES_TO_WEIL.** The de Branges inner product on `H(ξ(1−iz))` **is the Weil
explicit-formula pairing**. This is the Lagarias coincidence [THM, "naturally coincident", Lagarias,
*Hilbert Spaces of Entire Functions and Dirichlet L-Functions*, 2006; cf. Burnol]:

> the de Branges norm of `H(E)` and the **Weil Hermitian form** (the spectral side of the explicit
> formula) are naturally coincident; the de Branges space *encodes the explicit formula in its scalar
> product*, with its elements as the explicit-formula test functions.

Consequence: the de Branges positivity `⟨F,F⟩ ≥ 0` is, after this identification, **the Weil positivity
`W(f)=Σ_ρ f̂(ρ) ≥ 0` rewritten in reproducing-kernel language** — the SAME functional the charter audits
as CIRCULAR. The strong condition (3.1) `Im⟨F,F(·+i)⟩≥0` is a *shifted/skew* strengthening of that same
Weil pairing; it does not import any estimate, operator, or measure from outside the explicit formula.
There is **no independent analytic input** (no constructed self-adjoint operator with the spectrum, no
measure-positivity, no Euler-product estimate). De Branges's positivity is the structural duality pairing
of the FE — exactly the datum Theorem B′ proves underdetermines the signature — packaged as a Hilbert
norm. **It supplies Step A (the kernel, the FE) and *asserts* Step B (positivity) as a hypothesis; it
does not derive Step B.**

This explains *why* Conrey–Li could refute it so cleanly: a positivity that is the Weil form in disguise
is positive **iff RH**; de Branges's extra condition (3.1) is in fact *stronger* than RH-positivity (it
demands the skewed `Im⟨F,F(·+i)⟩≥0`), so it **over-proves** — it would force RH *and more*, and the
"more" is exactly what fails (the `10⁻⁶⁹` sign). The program's own tracker already records this:
"de Branges reproducing-kernel — **over-proves** — falsified (Conrey–Li 2000)"
(`positivity-program.md` §C; `stone3.md` graveyard).

## 4. Anchor (function field) + DH [established/partial]

**Anchor [partial].** The de Branges / canonical-system formalism IS the spectral-theoretic skeleton that
works in the model cases: a Krein string / canonical system whose `E` has all zeros on a line is exactly
the **self-adjoint (Hilbert–Pólya) realisation**, and over **function fields** the analogue is genuine —
the zeros are Frobenius eigenvalues on `H¹`, a finite-dim self-adjoint (unitarizable) datum, and the
de Branges positivity there is a **theorem** (it is Weil's Hodge-index positivity, which holds because of
the finite ground — Theorem A). So the de Branges positivity has a function-field analogue and there it is
**non-vacuous and true** — but it is true *because of the finite-ground geometry*, the very input ℚ lacks
at `∞`. Over ℚ the same positivity is precisely the unforced Step B. The de Branges machine transports the
*statement* but not the *proof* across the char-p → char-0 divide — consistent with the geometric writeup.

**DH [established — FAIL, i.e. RH-neutral].** Davenport–Heilbronn has the **same** `Γ_ℝ`-archimedean data
and a functional equation, so it admits a Hermite–Biehler structure function `E_{DH}` and a de Branges
space — but its zeros are **off-line**, so its (3.1) fails *for the same structural reason* and there is no
positivity to be had. The de Branges *framework* does not distinguish ζ from DH at the level of class
membership / kernel (both are HB, both have FE). The discrimination, if any, sits in whether the Weil/de
Branges form is `≥0` — which is exactly the Euler-product-borne content the program has shown is the sole
discriminator. De Branges's positivity, being the Weil form, is **DH-neutral as a structure** and only
DH-distinguishing *at the value/sign level* (= the wall). Verdict on the DH axis: **the de Branges
positivity passes the kill-test only insofar as it IS the Weil positivity** — no new DH-refusing lever.
[established that the framework is HB-shared with DH; the sign-level discrimination is the circular Weil
content.]

## 5. The missing object (if any) — and why this is mostly CIRCULAR not OPEN

The de Branges *specific* hypothesis is **CONTRADICTORY** (REAL_NOGO, §2). The de Branges *framework*,
stripped to a live road, would need: **a structure function `E` (or a chain / canonical system) for which
the de Branges positivity is supplied by an analytic source OTHER than the explicit-formula pairing it
coincides with** — e.g. a constructed canonical system / Krein string whose Hamiltonian `H(t)⪰0` is built
from the primes and whose spectral measure forces the zeros real *without* assuming the Weil form `≥0`.
That object is **not constructed**, and crucially it is the *same* missing object the rest of the audit
names — a positive Hamiltonian / measure built from the Euler product (a Hilbert–Pólya operator with an
honest construction). De Branges does not supply it; he supplies the kernel (Step A) and *posits* the
positivity (Step B). So the de Branges road, where not contradictory, **collapses onto the HP/Weil missing
object** — it is not an independent open road.

## 6. Verdict

- **Prerequisite:** de Branges's strong positivity hypothesis (3.1) `Im⟨F,F(·+i)⟩_{H(E)}≥0` (and (3.3)).
- **Prerequisite status: CONTRADICTORY** for the specific de Branges conditions on `H(ξ(1−iz))` —
  **provably false** (Conrey–Li, verified here to 40 digits). The narrowly-scoped REAL_NOGO.
- **Positivity source: REDUCES_TO_WEIL.** By Lagarias, the de Branges norm = the Weil Hermitian form; the
  de Branges positivity is the Weil positivity in reproducing-kernel clothing, with no independent
  analytic input. The specific (3.1) is *stronger* than RH-positivity, which is why it **over-proves** and
  is refutable.
- **Anchor:** function-field analogue exists and the positivity is a *theorem* there (finite ground);
  vacuous-of-proof over ℚ.
- **DH:** the framework is Hermite–Biehler-shared with DH (RH-neutral as structure); only the
  circular-Weil sign content discriminates. FAIL on the kill-test as an *independent* lever.
- **Overall verdict: REAL_NOGO** (the de Branges *specific positivity* is provably contradictory for ζ) —
  **with the honest scope that the underlying positivity is CIRCULAR (= Weil), and the residual de Branges
  *framework* is not killed but reduces to the same unconstructed HP/Euler-borne object.**

> **How much of the analytic side does Conrey–Li actually close?** Honestly: **one labelled door, not the
> corridor.** It is the unique *genuine analytic no-go* on the analytic side — a hard theorem that de
> Branges's *named* positivity conditions fail for ζ. But it closes them precisely *because they are the
> Weil positivity over-asserted*; it does **not** close (i) a different/weaker de Branges or canonical-
> system model, (ii) Hilbert–Pólya as analysis, (iii) the construction of an Euler-borne positive
> Hamiltonian. The de Branges no-go is real, sharp, and **narrow**: it removes the illusion that the
> reproducing-kernel framework *forces* positivity for free — confirming Theorem B′ from the analytic side
> (the kernel/FE is free; the positivity is the unforced, and here *false-as-stated*, extra).

## References
- J. B. Conrey, X.-J. Li, *A note on some positivity conditions related to zeta- and L-functions*, IMRN
  2000 no. 18, 929–940 (arXiv:math/9812166). Theorems 1–2; counterexamples (3.2)=`−5.389…×10⁻⁶⁹<0`,
  (3.4)=`−0.000131957<0`. **Counterexample (3.2) reproduced here independently to 40 digits.**
- L. de Branges, *The Riemann hypothesis for Hilbert spaces of entire functions*, and his 1986–1994 papers
  (the source of the refuted positivity conditions).
- J. C. Lagarias, *Hilbert Spaces of Entire Functions and Dirichlet L-Functions*, in *Frontiers in Number
  Theory, Physics, and Geometry I* (2006): the de Branges norm = the Weil Hermitian form (naturally
  coincident) — the basis of the REDUCES_TO_WEIL diagnosis.
- Cross-refs: `research/WRITEUP-geometric-obstruction.md` (Thm B′, Thm A); `research/positivity-program.md`
  §C (graveyard: "de Branges — over-proves — falsified"); `research/log/2026-06-06-stone3.md` (graveyard).
