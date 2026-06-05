# Open Questions

Live questions under the corrected architecture ([`tracker.md`](tracker.md)). The
former "reverse visibility" questions are largely resolved (the reverse bound is the
trivial `N`-uniform evaluation bound) or dropped (resolution `R_τ(N)`).

## Critical path (forward / arithmetic)

1. **Where exactly must the Euler product enter** to make forward convergence
   unconditional? (Any candidate mechanism must *fail* for Davenport–Heilbronn.)
2. What is the stall point of the Balazard–de Roton conditional upper bound
   `d_N² ≪ (log N)^{−1/2+o(1)}`, and can the witness machinery move an *unconditional*
   frontier there?
3. Do the extremal forward coefficients provably lock onto `−μ(n)` in the half-plane
   module avatar (not just the BD avatar)?

## Power test

4. Which known unconditional result is the best first target — the classical zero-free
   region, a zero-density estimate `N(σ,T)`, or `M_N → 1/ζ` for `Re s > 1`?
5. Can the machinery reprove it **unconditionally**? (If not even the classical
   zero-free region, the program lacks demonstrated proving power.)

## Refutation harness

6. Minimal faithful numerical model of Davenport–Heilbronn and a planted-zero "fake ζ"
   for the battery (env: Python only, no scipy/mpmath yet).
7. What finite truncation of the Weil explicit formula gives a usable, DH-discriminating
   positivity check?

## Finite compression (bookkeeping)

8. Exact `H²(Ω_τ)` norm convention; is `u ∈ H²(Ω_τ)` uniform as `τ ↓ 1/2`?
9. Exact Gram entries for `‖φ_τ D_N‖²` and the conditioning growth of `G_{N,τ}`.

## Foundational / Lean

10. Add Mathlib now, or after the first analytic target is concrete? (Needed for a real
    Theorem A.)
11. How to rewrite the contradiction theorem so it derives `False` from the evaluation
    obstruction rather than assuming incompatibility?
