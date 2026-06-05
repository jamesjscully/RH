"""P1 -- certify the slack constant via the exact Hermite discriminant (STRATEGY §8).

The slack rho(d) is the condition number = 1/dist to the discriminant variety in the
Bombieri-Weyl metric (Pardo-Pardo).  P1 pins its constant rigorously.  Certified result:

  disc(H_n) = 2^{3 n(n-1)/2} * prod_{k=1}^{n} k^k        (EXACT; verified n=2..N)
  log|disc(H_n)| = (3/2) n(n-1) ln2 + sum_{k=1}^n k ln k
  log|disc(H_n)| / n^2  ->  (1/2) ln n + ( (3/2) ln2 - 1/4 )

The (1/2) ln n term is the SEMICIRCLE (GUE) log-energy -- the same universality as the zeros'
pair correlation.  The (3/2) ln2 is the exact 2-power STRUCTURAL CONSTANT of the discriminant
-- the recognizable constant the BW-metric slack rate (~1.04) reflects.

Honest scope: the discriminant (the energy/height) is pinned exactly.  The slack *distance*
inherits the (3/2)ln2 from the 2-power but its exact constant also carries the gradient /
conditioning factor of the discriminant variety -- the remaining sub-step (P1b).  Everything
here is exact integer / closed-form arithmetic (no floats on the spine), per §8.

Run:  python3 -m scripts.numerics.witness.jensen_p1
"""
from __future__ import annotations

from math import comb, log

from flint import fmpz_poly, fmpq


def _hermites(N):
    Hs = [fmpz_poly([1]), fmpz_poly([0, 2])]
    x2 = fmpz_poly([0, 2])
    for n in range(1, N):
        Hs.append(x2 * Hs[n] - 2 * n * Hs[n - 1])
    return Hs


def hermite_discriminant(n: int, Hs=None) -> int:
    """Exact integer discriminant of the physicists' Hermite polynomial H_n,
    via disc = (-1)^{n(n-1)/2} Res(H_n, H_n') / lc(H_n)."""
    if Hs is None:
        Hs = _hermites(n + 1)
    H = Hs[n]
    R = H.resultant(H.derivative())
    lc = int(H.leading_coefficient())
    return (-1) ** (n * (n - 1) // 2) * int(R) // lc


def closed_form(n: int) -> int:
    """2^{3 n(n-1)/2} * prod_{k=1}^{n} k^k."""
    prod = 1
    for k in range(1, n + 1):
        prod *= k ** k
    return (2 ** (3 * n * (n - 1) // 2)) * prod


def bw_norm_sq(n: int, Hs=None) -> fmpq:
    """Exact ||H_n||^2 in the Bombieri-Weyl metric: sum a_k^2 / C(n,k)."""
    if Hs is None:
        Hs = _hermites(n + 1)
    s = fmpq(0)
    for k, c in enumerate(Hs[n].coeffs()):
        ak = int(c)
        if ak:
            s += fmpq(ak * ak, comb(n, k))
    return s


def verify_closed_form(N: int = 12):
    """Certified: disc(H_n) == 2^{3n(n-1)/2} prod k^k for all n<=N (exact integers)."""
    Hs = _hermites(N + 1)
    return all(hermite_discriminant(n, Hs) == closed_form(n) for n in range(2, N + 1))


def summary(N: int = 20):
    ok = verify_closed_form(min(N, 12))
    print("P1 -- certify the slack constant via the exact Hermite discriminant\n")
    print(f"[certified] disc(H_n) = 2^(3n(n-1)/2) * prod k^k  exact for n<=12: {ok}")
    c = 1.5 * log(2)
    print(f"[certified] log|disc(H_n)| = (3/2)n(n-1)ln2 + sum_k k ln k")
    print(f"            -> log|disc|/n^2 -> (1/2)ln n + ((3/2)ln2 - 1/4),  (3/2)ln2 = {c:.6f}\n")
    Hs = _hermites(N + 1)
    print(" n | log|disc|/n^2 |  (1/2)ln n + (3/2 ln2 - 1/4) | 2-power frac (3/2 ln2 part)")
    for n in range(4, N + 1, 4):
        ld = log(abs(hermite_discriminant(n, Hs)))
        pred = 0.5 * log(n) + c - 0.25
        two_power = 1.5 * n * (n - 1) * log(2)
        print(f"{n:2d} |   {ld / n**2:8.4f}    |        {pred:8.4f}             |  {two_power / ld:6.3f}")
    print("\n[interpretation]")
    print("  * The (1/2)ln n energy is the SEMICIRCLE / GUE log-energy (zeros' universality).")
    print("  * The (3/2)ln2 is the EXACT 2-power structural constant -- the recognizable")
    print("    constant the BW-metric slack rate (~1.04) reflects.  Discriminant = the energy,")
    print("    pinned exactly.")
    print("  * P1b (next): the slack DISTANCE to the discriminant variety also carries the")
    print("    gradient/conditioning factor; certify it (two-sided, via certified roots and")
    print("    H_n' values) to pin the slack constant itself.")
    return {"closed_form_ok": ok, "two_power_const": c}


if __name__ == "__main__":
    summary()
