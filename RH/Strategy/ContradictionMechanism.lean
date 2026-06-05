import RH.Witness.Hierarchy

/-!
Abstract contradiction mechanism (real version).

Earlier this theorem was a tautology: it took an `incompatible` hypothesis equal
to its own conclusion and applied it.  It is now a genuine theorem.  Modelling
the forward distances `dist(u, V_N(τ))` as a nonnegative rational sequence, the
two real predicates

  * `ForwardConvergence` — the distances tend to `0`   (RH-equivalent), and
  * `ReverseObstruction` — the distances sit above a positive floor for all `N`,

are logically incompatible; `False` follows from order facts alone (see
`RH/Witness/DistanceSequence.lean`).  Nothing assumes the conclusion.
-/

namespace RH.Strategy

open RH

theorem contradiction_from_forward_and_reverse
    {W : WitnessSystem} {path : WitnessPath W}
    (D : WitnessDistances W path)
    (forward : ForwardConvergence D)
    (reverse : ReverseObstruction D) :
    False :=
  forward_reverse_incompatible D.dist forward reverse

end RH.Strategy
