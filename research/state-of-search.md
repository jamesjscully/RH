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

## The one underexplored route — de Bruijn–Newman / dynamical

Conspicuously, one route is **not** in the table because we have not pushed it, and by the
program's own criteria it is the **most promising**:

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

No proof, and our work says plainly why none is near: every reformulation route lands on the
missing arithmetic object. What we *have* is valuable and honest: a precise graveyard map, a
fully-grounded metric/Arakelov candidate with its exact RH-hard endpoint (BGS §6.3) and a
certified energy constant tied to GUE universality, a reusable kill-test + nerve + height toolkit,
and a clear identification of the one route worth examining next (dBN dynamics). The verifiability
discipline (§8) held throughout — it caught and retracted two of my own over-claims (the `(3/2)ln2`
slack constant, the exponential slack rate). That is the program working as intended.
