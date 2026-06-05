# State of the search — honest assessment (2026-06-05)

A step back over everything examined, the convergent finding, and where the genuine frontier is.
This is the "win-win negative" payoff of STRATEGY §7.3, made explicit.

## The convergent finding

**Every analytic route we examined factors through the same missing object** — the arithmetic
`C×C` (Connes–Consani Scaling Site / the surface whose intersection positivity proves RH over
function fields), manifest analytically as *a positivity that is only known to be equivalent to
RH, never independently provable*. The routes and where each lands:

| route | status | lands on |
|---|---|---|
| **Nyman–Beurling / witness** (forward convergence) | dispersing (RH-neutral); descent-trivial | nothing — it's a reformulation |
| **Descent / obstruction calculus** | constant-coeff nerve contractible → `H¹=0` (decoration); obstruction is *metric*, not topological | the metric enrichment (Arakelov) |
| **Jensen / hyperbolicity / metric-Arakelov** | legitimate forcing-structure candidate (fails for DH/Epstein, not Weil-disguise); slack = height of discriminant, super-exp small, GUE energy; grounded in real ζ | **BGS §6.3** (positive Green form for Jensen–discriminant) = RH-hard |
| **Weil positivity / explicit formula** | RH ⟺ it, but only known equivalent (dispersing); our kill-test discriminator | Connes–Consani archimedean trace on the **Scaling Site** `C×C` |

The Jensen/metric route was the one with a real shot — a genuine forcing structure in height
language — and three independent passes (the descent micro-test, the kill-tests, and the real-ζ
grounding) all show it lands on the missing object: the uniform-in-`d` slack bound, the positive
Green form (BGS §6.3), and the archimedean Weil positivity are *the same difficulty wearing
different clothes*. The connective tissue is **potential theory** (log-energy, Green's functions,
equilibrium measures) and the **GUE/semicircle universality** shared by the slack and the zeros.

**Honest reading:** this is strong, structured evidence that **RH is not reachable by analytic
reformulation alone** — it requires the geometric object (the arithmetic surface). That is not a
proof of anything, but it is a real, reusable map: it says where *not* to spend effort
(reformulations, descent topology, bare hyperbolicity) and concentrates the difficulty into one
precise place.

## The de Bruijn–Newman / dynamical route — now examined (`dbn_route.py`)

By the program's own criteria it is the **most promising** route, and a kill-test confirms it is
a genuine RH-content criterion with real reverse force:

- **Kill-test passed.** The heat flow `H_t = e^{−tD²}` realizes complex zeros; `Λ(f)=inf{t:H_t f
  all-real}` satisfies **`Λ>0 ⟺ off-line zeros present`** (verified: all-real → `Λ=0`; one complex
  pair → `Λ=0.16`; `x²+1` → `0.5`; far-off-line → `1.76`, growing with distance off the line). So
  the dBN criterion **fails for DH/Epstein** (off-line zeros ⇒ `Λ>0`).
- **Real reverse force + a real unconditional theorem.** The flow *forces* zeros real; Rodgers–Tao
  proved `Λ≥0` unconditionally — the only theorem of its kind, using **dynamics + zero statistics
  (Montgomery)**, *not* the arithmetic surface. So dBN's hard endpoint is **different** from the
  geometric routes'.
- **Honest catch.** `Λ≥0` is the RH-*independent* direction ("RH barely true if true"); RH is
  `Λ≤0`, open and hard, and the dynamical method gives the wrong-direction bound. Forcing `Λ≤0`
  (controlling the backward flow) is where Rodgers–Tao + Polymath stalled.

**The two genuine frontiers are now distinct and named:** (a) the **missing arithmetic object**
(geometric/analytic routes → positive Green form / Scaling Site `C×C`), and (b) **forcing `Λ≤0`
via dynamics** (dBN). Neither is a reformulation; neither is reachable by relabeling RH.

**…but they share one structure.** The heat flow `e^{−tD²}` *generates the Hermite polynomials*
(`H_d` = heat-evolved monomials), and the Jensen polynomials converge to exactly those `H_d`
(GORZ; verified in real ζ, `xi_jensen.py`). So the **metric/Arakelov slack** (= the Hermite
discriminant, P1a) and the **dBN dynamics** are the *same Hermite / heat-flow / GUE object* seen
two ways — the slack is the *static* discriminant of the heat-flow fixed shape, the dBN flow is its
*dynamic* version. The two frontiers are not independent; they meet at the Hermite/semicircle
universality that also governs the zeros' pair correlation. If there is a non-obvious move left, it
is most likely *here* — at the junction where the static height and the dynamic flow are the same
object.

### (historical note — the original "underexplored" framing)
Before the kill-test the dBN route looked simply most-promising; the analysis above confirms it is
a genuine forcing structure but with its own RH-hard endpoint (`Λ≤0`).

- **Real reverse force.** The dBN heat flow `H_t` (a first-order log-gas on the zeros) *forces*
  zeros real for `t ≥ Λ`. This is a genuine dynamical forcing structure, not a reformulation.
- **Recent unconditional progress.** Rodgers–Tao (2020) proved `Λ ≥ 0` — a real theorem about
  RH, the only one of its kind, `RH ⟺ Λ ≤ 0`.
- **It may not factor through the missing object.** Rodgers–Tao use the *dynamics* + the actual
  zero statistics (Montgomery pair correlation), **not** the arithmetic surface. So the dBN route
  is structurally different from all four above — it might offer a handle the reformulations
  cannot.

The honest caveat: the RH direction (`Λ ≤ 0`) is still open and hard, and `Λ ≥ 0` is the
"RH-independent" direction (so dBN may yet be Farmer-dispersing in the same way). But it is the
genuine gap in our analysis and the route with the best track record. **Next:** kill-test the dBN
criterion (does the flow detect off-line zeros — DH/Epstein?), analyze whether its reverse force is
real or dispersing, and locate its specific hard endpoint. That is the honestly-highest-value
unexamined direction.

## Bottom line

No proof, and our work says plainly why none is near: every **reformulation** route lands on the
missing arithmetic object, and the one **dynamical** route (dBN) has its own distinct RH-hard
endpoint (forcing `Λ≤0`). What we *have* is valuable and honest:

- a precise **graveyard map** — which routes are dispersing/decoration and why;
- a fully-grounded **metric/Arakelov candidate** with its exact RH-hard endpoint (BGS §6.3) and a
  certified energy constant `(3/2)ln2 + ½ln n` tied to **GUE universality**;
- the dBN route **examined**: a genuine forcing structure with real reverse force, a real
  unconditional theorem (`Λ≥0`), and a hard endpoint *not* through the missing object;
- the observation that the **two frontiers meet at the Hermite/heat-flow/GUE structure** — the
  static slack (Hermite discriminant) and the dynamic flow are one object — which is the most
  likely place a non-obvious move hides;
- a reusable **kill-test + nerve + height + dynamics toolkit**, all grounded in real ζ.

The verifiability discipline (§8) held throughout — it caught and retracted two of my own
over-claims (the `(3/2)ln2` slack constant; the exponential slack rate). That is the program
working as intended: an honest map of a hard problem, not a false summit.

## Suggested next moves (for whoever picks this up)

1. **The Hermite junction** (highest-leverage, novel): make precise the identity "static slack =
   discriminant of the heat-flow fixed shape; dBN flow = its dynamic version," and ask whether the
   dynamics give a bound on the *slack's* evolution that the static height cannot — i.e. whether the
   flow controls the uniform-in-`d` slack. This is the one place the two hard endpoints might
   collapse to one tractable one.
2. **dBN `Λ≤0` sub-pieces** — the genuine frontier with the best track record (Rodgers–Tao, Polymath).
3. Treat the geometric endpoint (positive Green form / `C×C`) as the *literature* frontier (Connes–
   Consani, Arakelov), not a computation — it is the arithmetic-geometry open problem.
