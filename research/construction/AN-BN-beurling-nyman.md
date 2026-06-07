# AN-BN — the Beurling–Nyman criterion (analytic strategy map, 2026-06-06)

**Strategy (BN).** Beurling (1955) / Nyman (1950): RH ⟺ the indicator `1_{(0,1)}` lies in the
`L²(0,1)`-closure of `span{ρ_θ : 0<θ≤1}`, `ρ_θ(x)={θ/x}−θ{1/x}` (dilated fractional parts).
Báez-Duarte (2003) refinement: it suffices to use `θ=1/n`, `n∈ℕ` — the discrete span
`span{ {1/(nx)} }` — and frees the criterion from Hardy-space invariant-subspace theory.

**Equivalent analytic form (the load-bearing object).** [Bettin–Conrey–Farmer 2012, eq. as in
arXiv lineage; established]
> `d_N² := inf_{A_N} (1/2π) ∫_{−∞}^{∞} |1 − ζ(½+it)·A_N(½+it)|² dt/(¼+t²)`,
> infimum over Dirichlet polynomials `A_N(s)=Σ_{n≤N} a_n n^{−s}`.
> **RH ⟺ `lim_{N→∞} d_N² = 0`.**

So the prerequisite is an **approximation**: `1` is `L²`-approximable by `ζ·(Dirichlet poly)` against
the measure `dt/(¼+t²)` — equivalently `dist(1, span)=0`. This is a *genuine reformulation* of RH as a
concrete functional-analysis question; it is **not** circular in the trivial sense (it does not write
"RH ⟺ RH"); it *moves* RH to an `L²` density problem. The question is what kind of road it is.

---

## 1. Prerequisite classification: UNCONSTRUCTED (open), not contradictory, not circular-trivial

**(a) Not CONTRADICTORY.** `d_N` is monotone non-increasing in `N` (the spans nest) and bounded below
by `0`. Nothing forbids `d_N→0`; indeed under RH it is a *theorem* that `d_N→0`, with the Balazard–de
Roton upper bound `d_N² ≪ (loglog N)^{5/2+ε}/√(log N)` [conditional on RH; established]. There is no
analogue of Conrey–Li here: the BN prerequisite is not provably impossible. It is **the correct
equivalence** — see (d).

**(b) The distance formula — what is *unconditionally* known.** [Báez-Duarte–Balazard–Landreau–Saias
2000–05; Burnol; established]
> `liminf_{N→∞} d_N² · log N ≥ Σ_{Re(ρ)=½} m(ρ)²/|ρ|²`,
> the sum **restricted to the distinct zeros `ρ` of `ζ` on the critical line**, `m(ρ)` the multiplicity.

And the **conjectured sharp asymptotic** [BDBLS, expected; heuristic/partial]:
> `d_N² ~ (1/log N) · Σ_{Re(ρ)=½} m(ρ)²/|ρ|²`,
> which under RH (+simplicity) equals `(2+γ−log 4π)/log N` (since `Σ_{Re ρ=½} m(ρ)²/|ρ|² = 2+γ−log 4π`
> under RH). Bettin–Conrey–Farmer **prove** this asymptotic *assuming RH* plus a mild bound
> `Σ_{|Im ρ|≤T} 1/|ζ'(ρ)|² ≪ T^{3/2−δ}` [established, conditional].

**The decisive reading of the formula.** The unconditional lower bound sums **only over on-line zeros**.
It does NOT include off-line zeros and does NOT bound `d_N` *above*. So:
- the known distance formula tells you the on-line zeros *obstruct* faster-than-`1/log N` decay;
- it says **nothing** that forces `d_N→0`. To prove `d_N→0` you must *construct* Dirichlet polynomials
  `A_N` whose error beats the contribution of any putative off-line zeros — i.e. you must build an
  approximant that the off-line zeros do not block. **No such construction exists.**
The formula therefore **re-encodes** RH at the zeros but supplies **no mechanism** to reach `d_N=0`.

**(c) Not CIRCULAR-as-positivity.** Crucially, BN is **not a positivity criterion at all**. There is no
quadratic form `Q≥0`, no Weil sum `Σ_ρ ĥ(ρ)≥0`. RH is encoded as a **distance = 0** (an approximation),
not as a **form ≥ 0**. Hence the unifying question of `WRITEUP-geometric-obstruction.md` / Theorem B′
("does it supply the RH-positivity from a new analytic source, or reduce to Weil positivity?") is, for
BN, **orthogonal**: BN does not traffic in positivity. It neither supplies a new analytic positivity nor
reduces to Weil positivity — `positivity_source = NONE`. This is itself diagnostic: BN cannot be the
vehicle for "supplying the positivity Theorem B′ says no structure forces," because it carries no
positivity to supply. What it carries is an *approximation* whose obstruction is the off-line zeros.

**(d) Why it is genuinely the correct equivalence (the generalized criterion).** [de Roton 2004–06,
Nikolski; established] The BN density for a Dirichlet series is equivalent to the **absence of zeros in
the open half-plane `Re(s)>½`** (the Beurling half-plane form), which by the functional equation is RH.
The generalized criterion links `L²`-density to the localization of zeros in half-planes `Re(s)>σ₀`.
This means BN is a **faithful** equivalence: a Dirichlet series *with* a zero in `Re(s)>½` *fails* the
density. The criterion sees the zero locations correctly. (Contrast the *forward numerical witness*
`d_N→0` computed to finite `N`, which is RH-neutral as a finite computation — see §3.)

**Verdict on prerequisite:** **UNCONSTRUCTED.** The missing object is a **family of Dirichlet
polynomials `A_N(s)` with an unconditional error estimate `d_N²→0`** — equivalently a constructive proof
that `1` is in the closure of the span. It is open, not contradictory, not RH-restated-trivially.

---

## 2. Positivity source: NONE (BN is an approximation, not a positivity)

`WRITEUP-geometric-obstruction.md` Theorem B′: the RH-positivity (`F†=F̄`, the `(d,0)` signature) is not
forced by any structural datum; a proof must supply it from analysis. **BN does not address this axis.**
- There is no operator, no measure-positivity, no form `≥0`.
- The only "positivity-flavoured" object in the vicinity is Burnol's lower bound, which is a *sum of
  positive terms over on-line zeros* `Σ m(ρ)²/|ρ|² > 0` — but that is an **obstruction lower bound**
  (it bounds `d_N` *below*, i.e. it is the wrong direction: large positivity = *bad*, it keeps `d_N`
  from decaying), not an RH-forcing positivity.
- So BN does **not** reduce to the circular Weil positivity (it never invokes it), and it does **not**
  supply a new analytic positivity. **`positivity_source = NONE`.**

This is the honest separation from the audit wall: BN is a *different shape* of reduction (approximation,
not positivity). It does not hit the Weil-positivity circularity that `weil_form.py` /
`operator_domination.py` documented — because it is not a positivity reformulation. Its open object is an
**estimate / construction**, not a sign.

---

## 3. DH (the litmus): PASS — BN is Euler-borne and DH-refusing (correcting the prior repo framing)

**Prior repo framing was imprecise.** `positivity-program.md` §C and `state-of-search.md` list
"Nyman–Beurling / Hardy" as *"holds for DH ⟹ dispersing."* That verdict applies to the **forward
numerical witness** (computing `d_N` to finite `N` and watching it shrink — a finite computation that is
RH-neutral and looks the same for ζ and DH at finite `N`). It does **not** apply to the **criterion** as
an equivalence.

**The criterion correctly fails for DH.** [established, via the generalized criterion] Davenport–Heilbronn
`f_DH` has the same `Γ_ℝ` functional equation but **has zeros with `Re(s)>½`** (off the line, in the
half-plane). By de Roton/Nikolski's generalized BN criterion, the `L²`-density holds **iff** there are no
zeros in `Re(s)>½`. DH *has* such zeros, so the BN density **FAILS for DH** — i.e. `dist(1,span_DH)>0`.
The criterion *discriminates* ζ from DH at the level of zero locations.

Where does the Euler product enter? It does not enter `f_DH` (no Euler product, off-line zeros), and the
BN density consequently fails for `f_DH`. The discriminator is precisely the **half-plane zero-freeness**,
which for ζ is supplied by — and only by — the prime/Euler structure (a Dirichlet series with off-line
zeros, like DH, breaks density). So **DH = PASS** (the criterion fails for DH exactly as a faithful RH
equivalence must). This is a *correction*: BN-as-criterion is **not** dispersing; BN-as-finite-witness is.

The reason this never advanced the program: BN converts RH into an *equally hard* approximation problem
with **no new handle** — the off-line zeros that BN must rule out are the same ones RH is about, and BN
gives no estimate to rule them out. It is faithful but inert.

---

## 4. Anchor (function field): the analytic content is a THEOREM there, hence vacuous as a lever

Over `𝔽_q(C)` the zeta is `Z(T)=P(T)/((1−T)(1−qT))`, `P` a polynomial of degree `2g`; RH = all
`|α_j|=√q`. The Beurling–Nyman analogue is a density/approximation in an `L²` of the relevant adelic /
Tate space. **But over the function field the relevant `1` is automatically in the closed span**: the BN
density is equivalent to the zero-freeness in the half-plane, which is **Weil's theorem** — the finite
ground forces it (Hodge index). So the function-field BN criterion is **satisfied as a corollary of a
proven theorem**: its analytic content there is a *consequence*, not an independent mechanism. The
approximation is achievable over `𝔽_q(C)` precisely *because* the zeros are already known to be on the
line — the construction of the approximants is downstream of the geometric positivity, not a substitute
for it. **Anchor verdict: the FF analogue exists and is a theorem there, hence vacuous as a transferable
lever** — it inherits, it does not supply. (Same shape as Weil/Li positivity row in the §4.2 table: over
`𝔽_q` it is a theorem; the content is the finite ground, absent at `∞`.)

This sharpens the classification: BN's open object over `ℚ` (the construction of `A_N` with `d_N→0`) is,
over `𝔽_q`, *handed to you by the geometric positivity Theorem A says `ℚ` lacks at `∞`*. So BN does not
route around the obstruction; it sits downstream of it.

---

## 5. Honest standing: the most concrete *live* analytic road, but inert (no new handle)

- **Most concrete?** Yes — BN/Báez-Duarte is the single most *concrete* analytic reformulation of RH: a
  literal `L²` approximation by explicit elementary functions (`{1/(nx)}`), with a known distance
  formula. It is the cleanest "open functional-analysis problem ⟺ RH."
- **Live?** As a *road*, only formally. The reduction is faithful (it sees DH, §3) and unconstructed
  (§1), so it is an OPEN_ROAD in the strict sense — but it is **inert**: the missing object (an `A_N`
  construction with an unconditional `d_N→0` estimate) is *not easier* than RH and carries no new
  analytic input. The distance formula re-expresses the obstruction at the off-line zeros without
  supplying any estimate to remove them. There is no positivity, no operator, no measure — nothing for
  Theorem B′'s "supply the positivity from analysis" to grip.
- **Comparison to the genuine live edge.** The program's live levers (QSM free energy thread 5; the
  Euler/Hecke cross-place coupling `W_∞≥Σ_p W_p`, threads 0/4/E) are *positivity* objects with a
  candidate Euler-borne, DH-refusing, sees-zeros source. BN is a *different category*: an approximation
  whose only content is "rule out the off-line zeros," with no mechanism offered. It is the most
  concrete *statement*, not the most promising *handle*.

**One line.** BN is a faithful, concrete, **UNCONSTRUCTED** analytic reformulation (RH ⟺ `dist(1,span)=0`
⟺ no zeros in `Re s>½`); it correctly **fails for DH** (DH=PASS); but it carries **no positivity** (so it
neither supplies a new analytic positivity nor reduces to Weil — `NONE`), its distance formula only
**re-encodes** the off-line-zero obstruction, and over function fields its content is a **theorem**
downstream of the very finite-ground positivity `ℚ` lacks at `∞`. The precise missing object: **an
explicit family `A_N(s)=Σ_{n≤N}a_n n^{−s}` with an unconditional estimate `(1/2π)∫|1−ζA_N(½+it)|²
dt/(¼+t²) → 0`** — equally hard as RH, with no new analytic source.

**Verdict: OPEN_ROAD (faithful, concrete, but inert — no positivity source). prerequisite =
UNCONSTRUCTED. positivity_source = NONE. DH = PASS.**

---

## References
- B. Nyman, *On some groups and semigroups of translations*, thesis, Uppsala (1950).
- A. Beurling, *A closure problem related to the Riemann zeta-function*, PNAS 41 (1955).
- L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*,
  arXiv:math/0202141; *A class of invariant unitary operators*, Adv. Math. (2003).
- L. Báez-Duarte, M. Balazard, B. Landreau, E. Saias, *Notes sur la fonction ζ de Riemann, 3*,
  Adv. Math. 149 (2000); the lower bound `liminf d_N² log N ≥ Σ_{Re ρ=½} 1/|ρ|²`.
- M. Balazard, E. Saias, M. Yor, *Notes sur la fonction ζ de Riemann, 2*, Adv. Math. 143 (1999).
- J.-F. Burnol, improvement to multiplicity-weighted `Σ m(ρ)²/|ρ|²`.
- S. Bettin, J. B. Conrey, D. W. Farmer, *An optimal choice of Dirichlet polynomials for the
  Nyman–Beurling criterion*, Proc. Steklov Inst. Math. 280 (2013) — the `d_N²` integral, eq. (1),
  Theorem 1 (`d_N² ~ (2+γ−log4π)/log N` under RH + mild `1/|ζ'(ρ)|²` bound).
- A. de Roton, *Généralisation du critère de Beurling–Nyman pour l'hypothèse de Riemann*,
  C. R. Acad. Sci. (2004) / Trans. AMS — density ⟺ half-plane zero-freeness; N. Nikolski, prior.
