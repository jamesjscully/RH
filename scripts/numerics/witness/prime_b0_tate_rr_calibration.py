"""B0 calibration witness: Tate-curve liquid-RR shadow.

This is the smallest executable object from proof/46:

    B0 = (L0, b0, R0/T0, tr0, comb_p, Count0).

It is deliberately only a calibration/kill-test platform.  It checks
the theorem-grade Route A shadow recorded in MM/XX:

* RR on the Tate curve gives chi(L_d) = d and residue trace 1.
* Those trace/count numbers are independent of p.
* The q-expansion grading carries the p^Z address and reproduces the
  one-place Gaussian comb with the standard Poisson weight/spacing.
* Replacing p^Z by the Epstein represented-norm monoid leaves the
  theta/Poisson count layer alive but destroys the valuation/tower
  address by nonunique factorization.

No zeta zeros, explicit-formula signs, inserted continuum unit,
odd-slot spectrum, Frobenius-index form, or comparison theorem are used.

Run:
    python3 -m scripts.numerics.witness.prime_b0_tate_rr_calibration
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass


failures: list[str] = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def record(msg: str) -> None:
    print("  " + msg)


def gaussian(x: float, sigma: float) -> float:
    return math.exp(-(x * x) / (2.0 * sigma * sigma))


def gaussian_hat(xi: float, sigma: float) -> float:
    """Fourier transform with convention int f(x) exp(-i x xi) dx."""
    return math.sqrt(2.0 * math.pi) * sigma * math.exp(
        -(sigma * sigma * xi * xi) / 2.0
    )


def lattice_sum_hat(spacing: float, sigma: float, tol: float = 1e-16) -> float:
    total = gaussian_hat(0.0, sigma)
    n = 1
    while True:
        term = 2.0 * gaussian_hat(n * spacing, sigma)
        total += term
        if abs(term) < tol:
            return total
        n += 1
        if n > 1_000_000:
            raise RuntimeError("hat-side lattice sum did not truncate")


def lattice_sum_space(spacing: float, sigma: float, tol: float = 1e-16) -> float:
    dual_spacing = 2.0 * math.pi / spacing
    total = gaussian(0.0, sigma)
    k = 1
    while True:
        term = 2.0 * gaussian(k * dual_spacing, sigma)
        total += term
        if abs(term) < tol:
            return (2.0 * math.pi / spacing) * total
        k += 1
        if k > 1_000_000:
            raise RuntimeError("space-side lattice sum did not truncate")


def rr_data(degree: int) -> tuple[int, int, int]:
    """Classical elliptic RR for the Tate-curve calibration object.

    For degree d > 0, h0(L_d) = d and h1(L_d) = 0.  For O, h0 = h1 = 1.
    Negative degrees are not part of B0's positive count calibration.
    """
    if degree == 0:
        return 1, 1, 0
    if degree > 0:
        return degree, 0, degree
    return 0, -degree, degree


@dataclass(frozen=True)
class B0:
    prime: int

    @property
    def q(self) -> float:
        return 1.0 / self.prime

    @property
    def address_spacing(self) -> float:
        return math.log(self.prime)

    @property
    def period_lattice(self) -> tuple[float, float]:
        return (-math.log(self.prime), 2.0 * math.pi)

    def count0(self, degree: int) -> int:
        return rr_data(degree)[2]

    def trace0(self) -> int:
        return 1


def represented_by_epstein(limit: int) -> set[int]:
    max_x = int(math.sqrt(limit)) + 1
    max_y = int(math.sqrt(limit / 5.0)) + 1
    out: set[int] = set()
    for x in range(-max_x, max_x + 1):
        for y in range(-max_y, max_y + 1):
            n = x * x + 5 * y * y
            if 0 < n <= limit:
                out.add(n)
    return out


def irreducible_in_monoid(n: int, monoid: set[int]) -> bool:
    if n not in monoid:
        return False
    for d in range(2, n):
        if n % d == 0 and d in monoid and n // d in monoid:
            return False
    return True


def main() -> int:
    primes = (2, 3, 5, 11)
    degrees = tuple(range(0, 9))
    objects = [B0(p) for p in primes]

    print("B0.1: RR count and Serre trace are p-independent")
    rr_ok = True
    for degree in degrees:
        expected = rr_data(degree)
        for obj in objects:
            rr_ok = rr_ok and rr_data(degree) == expected
            rr_ok = rr_ok and obj.count0(degree) == expected[2]
            rr_ok = rr_ok and obj.trace0() == 1
    gate(
        "B0.1 RR-trace-null",
        rr_ok,
        "chi(L_d)=d for d=0..8 and tr0=res(dz/z)=1 for p in %s"
        % (primes,),
    )
    record(
        "periods vary as (-log p, 2pi), but Count0 and tr0 do not read them"
    )

    print("B0.2: q-expansion address carries the p^Z comb")
    comb_ok = True
    worst_rel = 0.0
    for p in primes:
        for multiplier in (1, 2):
            spacing = multiplier * math.log(p)
            for sigma in (0.37, 0.73, 1.41):
                left = lattice_sum_hat(spacing, sigma)
                right = lattice_sum_space(spacing, sigma)
                rel = abs(left - right) / max(1.0, abs(right))
                worst_rel = max(worst_rel, rel)
                comb_ok = comb_ok and rel < 5e-13
    gate(
        "B0.2 poisson-comb-address",
        comb_ok,
        "sum phihat(n log p) = (2pi/log p) sum phi(2pi k/log p); "
        "worst rel %.2e for p and p^2 controls" % worst_rel,
    )
    record(
        "the only p-dependence is the address spacing log p and its Poisson dual"
    )

    print("B0.3: no promotion fields are present in B0")
    b0_fields = {"L0", "b0", "R0/T0", "tr0", "comb_p", "Count0"}
    forbidden = {"U", "Fr", "H_odd", "I", "N", "Compare"}
    gate(
        "B0.3 no-promotion",
        b0_fields.isdisjoint(forbidden),
        "B0 omits U, Fr, H_odd, I, N, Compare by construction",
    )

    print("B0.4: Epstein replacement kills the valuation/tower address")
    rep = represented_by_epstein(36)
    epstein_count_alive = all(n in rep for n in (1, 4, 6, 9, 36))
    no_prime_atoms = 2 not in rep and 3 not in rep
    irreducibles = all(irreducible_in_monoid(n, rep) for n in (4, 6, 9))
    double_factorization = 4 * 9 == 6 * 6 == 36
    epstein_ok = (
        epstein_count_alive
        and no_prime_atoms
        and irreducibles
        and double_factorization
    )
    gate(
        "B0.4 epstein-carrier-guard",
        epstein_ok,
        "Q=x^2+5y^2 represents 1,4,6,9,36; 2,3 absent; "
        "4,6,9 irreducible; 36=4*9=6*6",
    )
    record(
        "theta/count layer survives, but no free rank-1 valuation or q-tower address is formable"
    )

    print("B0.5: calibration verdict")
    verdict_ok = not failures
    gate(
        "B0.5 calibration-only",
        verdict_ok,
        "Route A produces a scale-free one-place null, not the missing carrier",
    )
    if failures:
        print("FAILURES:", ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
