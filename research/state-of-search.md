# State of the search — a map of RH's resistance (finalized 2026-06-06)

The durable product of this program: an honest, comprehensive map of *why* the Riemann Hypothesis
resists analytic attack, where exactly the irreducible difficulty sits, and which routes are dead
and why. Not a proof. Read with `STRATEGY.md` (the charter) and the dated logs in `research/log/`.

---

## 1. The one-paragraph conclusion

Every route we examined confirms, with increasing precision, the same thing: **the RH content is
the subleading Euler-product / zero-distribution structure of `ζ`, and it is not reachable through
any leading / archimedean / functional-equation / metric / edge reformulation.** Every such
reformulation is either *dispersing* (RH-neutral — it holds for Davenport–Heilbronn, which has the
same functional equation but no Euler product and provable off-line zeros) or it lands on the
*missing arithmetic object* (the surface `C×C` whose intersection positivity proves RH over
function fields, with no analogue over `Spec ℤ`). The two genuine frontiers are research-grade open
problems; we found no fresh finite handle into either.

## 2. The route map

| route | verdict | where it lands |
|---|---|---|
| **Nyman–Beurling / witness** (forward convergence = `d_N→0`) | **dispersing** (RH-neutral; holds for DH); descent-trivial | a reformulation — nothing |
| **Descent / obstruction calculus** (nerve `H¹` of a template cover) | **decoration**: additive families → contractible nerve → `H¹=0`; obstruction is *metric*, not topological | the metric enrichment (Arakelov) |
| **Jensen / hyperbolicity / metric-Arakelov** | genuine forcing-structure *candidate* (fails for DH/Epstein, not Weil-disguise); slack = condition-number = arithmetic **height of the discriminant**, super-exp, GUE energy; grounded in real `ζ` | **BGS §6.3** positive-Green-form obstruction = RH-hard |
| **Weil positivity / explicit formula** | RH `⟺` it, but **only known equivalent** (dispersing); our kill-test discriminator | Connes–Consani archimedean trace on the Scaling Site `C×C` |
| **de Bruijn–Newman / dynamical** | genuine forcing structure with **real reverse force**; `Λ≥0` proved unconditionally (Rodgers–Tao, via dynamics+statistics, *not* the missing object) | **forcing `Λ≤0`** — a distinct RH-hard endpoint |
| **Spectral edge** (deviation `J_{d,n}−H_d` at the Airy edge) | the large edge deviation is **dispersing** — set by the leading functional-equation kernel, independent of the arithmetic (verified `~1e-8`) | a functional-equation feature — no reverse force |

Three independent passes on the **Jensen/metric** route (the descent micro-test, the kill-tests,
the real-`ζ` grounding) all show its frontiers — the uniform-in-`d` slack bound, the positive Green
form (BGS §6.3), the archimedean Weil positivity — are *the same difficulty in different clothes*.

## 3. The Hermite junction — where the routes meet, fully mapped

The Jensen polynomials converge to Hermite (`J_{d,n}→H_d`, GORZ; verified in real `ζ`,
`xi_jensen.py`), and the dBN flow `e^{−tD²}` *generates* Hermite. So the static metric slack and the
dynamic flow are **one Hermite/heat-flow/GUE object**. Three fresh angles (parallel subagents,
`{totally_positive,renormalization,lambda_height}.py`) mapped it:

- **Total positivity** (Angle 1): the right *language* (Pólya-frequency / Aissen–Schoenberg–Whitney,
  dBN as a variation-diminishing TP semigroup) but **not a fresher coordinate** — the slack is
  super-exponential in every TP coordinate too.
- **Renormalization** (Angle 2): the dBN flow acts on the Hermite fixed shape as a **pure dilation**
  `e^{−tD²}H_n=(1+4t)^{n/2}H_n(x/√(1+4t))` — *exactly marginal* (a precise "Λ=0 at the fixed point");
  but no fixed-point recursion — the slack is a marginal `½ d log d` law, spectral-edge controlled.
- **Λ as a height** (Angle 3): the dBN, Weil, and Arakelov-height archimedean terms are **one digamma
  `Γ_ℝ` object** (exact: `2 Re E_Ξ = h₊`) — but it is **shared with Davenport–Heilbronn ⇒ RH-neutral**.

**Conclusion:** the static / archimedean / fixed-shape side of the junction is **fully understood
and fully RH-neutral**. The RH content is the *deviation* from the fixed shape — and (the spectral-
edge pull) that deviation is **largest at the edge but the edge is dispersing** (leading functional-
equation structure); the genuine RH content (the arithmetic) is the **subleading** part, at the
shoulder/bulk, tiny at accessible `(d,n)`.

## 4. The precise location of the difficulty

Stripped to the line: the leading / archimedean / functional-equation / edge structure is
**dispersing** — confirmed in *three independent places*: the shared digamma `Γ_ℝ` factor (Angle 3),
the descent triviality, and the dispersing edge. The RH content is the **subleading Euler-product /
zero-distribution structure** — the part that distinguishes RH-true `ζ` from RH-false DH/Epstein. It
is exactly the content of **Weil positivity** (only-known-equivalent) and the **missing arithmetic
object** (BGS §6.3 / the Scaling Site `C×C`). It is asymptotic / not finitely accessible (the dBN
sequence flow shows finite Jensen polynomials are robustly hyperbolic; criticality is the
`(d,n)→∞` limit, consistent with GORZ's `n ≳ e^d`).

## 5. The two genuine frontiers (both RH-hard, open)

> **The missing object is now characterized precisely** — `research/literature/the-missing-object.md`
> (synthesis) and the three deep-dives (`arakelov-arithmetic-surface.md`,
> `connes-consani-scaling-site.md`, `deninger-spectral-cohomology.md`), plus its computable analytic
> shadow (`weil_form.py`: the Weil form is the demonstrated RH-detector). All three programs build the
> object's points, Frobenius flow, and Lefschetz/trace identity, and converge on the **same
> irreducible gap**: the **`H¹` on the square `S²` (the arithmetic `C×C`) carrying the zeros — and
> its intersection positivity (`= RH`) — does not exist**, and (BGS §6.3) cannot hold for formal
> reasons, so a genuine geometry over `Spec ℤ` (`𝔽₁`) is required.


1. **The missing arithmetic object** — the geometric/analytic routes all land here: a positive Green
   form (BGS §6.3) / the archimedean Weil positivity / the intersection positivity on `C×C`. This is
   the `𝔽₁` / Connes–Consani / Deninger program — the deepest open problem in the subject.
2. **Forcing `Λ ≤ 0`** (de Bruijn–Newman) — distinct, dynamical, the best track record
   (Rodgers–Tao proved the *opposite* direction `Λ≥0`; Polymath). Uses zero statistics, not the
   missing object. Controlling the backward flow is open.

## 6. What the program produced

- **A precise graveyard map** (§2–§4): which routes disperse / are decoration, and why — reusable to
  avoid re-walking them.
- **Reusable, kill-test-disciplined tooling**, all grounded in real `ζ`: the kill-tests
  (`explicit_formula.py`, `li_positivity.py`, `second_wall.py` — DH wall, Epstein wall, Weil/Li
  positivity); the descent nerve criterion (`descent_test.py`); the height machinery
  (`jensen_p1.py`, `jensen_p1b.py`); the dynamics (`dbn_route.py`, `xi_jensen.py`); the harness
  (`harness.py`).
- **Clean exact results banked:** `disc(H_n)=2^{3n(n−1)/2}∏kᵏ` with energy `(3/2)ln2 + ½ln n`
  (semicircle/GUE), certified (P1a); the pure-dilation identity (Angle 2B); the archimedean digamma
  unification `2 Re E_Ξ = h₊` (Angle 3); the Epstein second wall (`ζ_K=ζ·L`, RH-false constituents).
- **The verifiability discipline (§8) held** — it caught and retracted **three** of my own
  over-claims: the `(3/2)ln2` slack constant, the exponential slack rate, and the "polynomial dBN
  margin" (which was the heat flow on the polynomial, not the dBN sequence flow on `Ξ`). The honest
  map is the result, not a false summit.

## 7. Do-not-revisit (the dead ends, with the reason)

- Re-encoding RH as an approximation/closure/positivity criterion — **dispersing** (holds for DH).
- Descent *topology* on additive template families — **decoration** (`H¹=0`); the obstruction is metric.
- Bare Jensen hyperbolicity, or the static BW slack as if RH-relevant — the slack is partly a
  height-metric artifact; the *physical* margin is milder, and neither bridges to `Λ`.
- The archimedean / functional-equation / `Γ_ℝ` / spectral-edge structure — **RH-neutral** (shared
  with DH), in three independent confirmations.
- Heat flow on the Jensen *polynomial* mistaken for the dBN flow on `Ξ` (the correct dBN flow is the
  *sequence* flow `γ→γ_t`, `xi_jensen.jensen_sequence_flowed`).

## 8. If someone picks this up

There is **no fresh finite handle** left in our toolkit. Genuine progress requires engaging one of
the two §5 frontiers as the research problem it is:
- the missing object — a *literature/theory* frontier (Connes–Consani Scaling Site, Arakelov
  positivity, `𝔽₁`), not a computation;
- `Λ≤0` — the dynamical frontier (Rodgers–Tao, Polymath), where zero-statistics control of the
  backward flow is the open question.

The reusable contribution is the map and the discipline: any new candidate must pass the kill-tests
(fail for DH **and** Epstein, not be Weil-positivity-in-disguise, carry the subleading Euler-product
content, not be dispersing/edge/archimedean), or it is already in the graveyard above.
