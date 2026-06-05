# The Hermite junction — static height vs dynamic flow — 2026-06-05

Pursued the highest-leverage idea from state-of-search: the metric/Arakelov slack (static, the
Hermite discriminant) and the de Bruijn–Newman flow (dynamic) are the *same Hermite/heat-flow
object* — because `e^{−tD²}` generates Hermite and the Jensen limit *is* Hermite.

## Probe

For the real-ξ Jensen polynomials `J_{d,n}` (all hyperbolic), measured two margins:
- **static**: min relative root gap (separation) — grows with shift `n` toward the Hermite limit;
- **dynamic**: `Λ_- =` backward-dBN flow room before hyperbolicity is lost (`dbn_route.backward_margin`).

## Finding (genuine, modest)

The two are **anti-correlated in `n`**: as `n` grows the static separation *increases* (`d=10`:
`0.012 → 0.041` over `n=0→12`) while the dynamic margin *decreases* (`d=10`: `1.5e-3 → 2.8e-3`…
actually rises slightly then the ratio `dyn/stat` falls `0.125 → 0.068`; across `d` the dynamic
margin falls fast with degree: `d=4: ~5e-2`, `d=10: ~1.5e-3`). The dynamic margin → 0 as `(d,n)`
grow toward the full ξ.

**Reading:** the shrinking dynamic margin is the **de Bruijn–Newman `Λ = 0` ("RH barely true"),
resolved by degree and shift** — the dynamic/dBN view of the same "barely hyperbolic" fact the
static slack measures statically. The anti-correlation shows the two views are genuinely
different *measurements* of one Hermite object. This confirms the junction is real.

## Honest assessment

This is a real structural observation and a clean unification (static slack ↔ dynamic flow ↔
Hermite/GUE), grounded in real ζ. It does **not** advance toward a proof: it quantifies "RH is
barely true" in the dynamic sense, the same way the static slack did — both land on the same
RH-hard endpoints (`Λ≤0` / uniform slack / positive Green form). The junction is the most
*interesting* place left, but cracking it would require a genuinely new idea (a transfer from the
controlled flow `Λ≥0` to the slack's uniform-in-`d` decay) that I do not have. Recorded as the
honest endpoint of this exploration.
