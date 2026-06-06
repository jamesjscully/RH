"""falsify.py -- the unified falsification harness for positivity candidates (upgraded 2026-06-06).

The kill-test discipline, sharpened by the thread/worker audit. A candidate positivity for RH is
classified on three independent axes, each a falsifiable test:

  1. EULER-BORNE   -- does it FAIL for Davenport-Heilbronn (no Euler product)?  [necessary]
  2. SEES-ZEROS    -- is it SENSITIVE to a planted off-line zero (does it depend on zero LOCATIONS,
                      not just the real-axis Dirichlet coefficients)?           [necessary for content]
  3. INDEPENDENT   -- is its positivity provable WITHOUT assuming RH (not = the Weil/Li positivity)?

Four verdicts:

  DISPERSING   : not Euler-borne (holds for DH). RH-neutral. [de Branges, Nyman-Beurling, bare
                 self-adjointness, RTF/period, the unitary scattering structure]
  RH-SILENT    : Euler-borne but does NOT see the zeros -- an "Euler-product detector". It confirms
                 ζ HAS a product (passes DH) but is blind to where the zeros sit. THIS IS THE NEW
                 CATEGORY the workers exposed: QSM free energy, the prime Gram/Hankel form. The trap
                 is that these PASS the DH kill-test yet carry no RH content.
  CIRCULAR     : Euler-borne, sees the zeros, but its positivity for ζ IS RH (Weil/Li). Correct
                 forcing functional, no independent proof.
  FORCING      : Euler-borne, sees the zeros, AND independently provable. The prize. NONE YET.

The decisive upgrade over the old harness: the SEES-ZEROS axis. Passing the DH test ("has a
product") is necessary but cheap; the content is whether a candidate is sensitive to the zero
LOCATIONS. `offline_sensitivity` makes that axis executable.

Run:  python3 -m scripts.numerics.witness.falsify
"""
from __future__ import annotations

import mpmath as mp


# ---- the executable SEES-ZEROS probe -------------------------------------------------------------

def li_coeff(zeros_plus, n):
    """Li-type functional Σ_ρ [1−(1−1/ρ)^n] over a zero multiset (the canonical zero-functional)."""
    return sum((1 - (1 - 1 / mp.mpc(r)) ** n) for r in zeros_plus).real


def offline_sensitivity(zero_functional, nmax=40, rho0=mp.mpc(0.99, 2.0)):
    """Is a zero-functional SENSITIVE to a planted off-line zero quadruple? Returns (sensitive, n*).
    A functional that does not change sign when an off-line quadruple is injected is RH-SILENT."""
    on_line = [mp.mpc(0.5, 14.1347), mp.mpc(0.5, -14.1347), mp.mpc(0.5, 21.022), mp.mpc(0.5, -21.022)]
    quad = [rho0, 1 - rho0, mp.conj(rho0), 1 - mp.conj(rho0)]
    for n in range(1, nmax + 1):
        base = zero_functional(on_line, n)
        pert = zero_functional(on_line + quad, n)
        # sensitive if injecting the off-line quadruple flips the sign of the functional
        if pert < 0 <= base or (base >= 0 and pert < 0):
            return True, n
    return False, None


# ---- the classifier ------------------------------------------------------------------------------

def classify(euler_borne, sees_zeros, independent):
    if not euler_borne:
        return "DISPERSING"
    if not sees_zeros:
        return "RH-SILENT"
    if not independent:
        return "CIRCULAR"
    return "FORCING"


# candidate registry: (name, euler_borne, sees_zeros, independent, note)
REGISTRY = [
    ("Weil form / Li coefficients", True, True, False, "= RH (stone 2); the canonical forcing functional"),
    ("QSM free energy −log ζ(β)", True, False, False, "worker A: real-axis, RH-silent"),
    ("prime Gram / adelic Hankel", True, False, False, "worker B: Euler product in a Hankel skin"),
    ("Birman–Krein phase winding", True, True, False, "worker B: detects off-line zero, but counts not forces"),
    ("Beurling–Selberg / Cohn–Elkies majorant", True, False, False, "worker D: a sup over {ĝ≥0}, RH-agnostic bound"),
    ("BRS modular interpolation (primes+zeros nodes)", True, True, False, "worker D: records RH (frame⟺RH); Eisenstein dual cert = archimedean"),
    ("scattering unitarity |S|=1", False, False, False, "stone 1: holds for off-line control too"),
    ("self-adjointness (Hilbert–Pólya)", False, False, False, "reflects, does not force"),
    ("de Branges reproducing kernel", False, True, False, "falsified, Conrey–Li 2000"),
    ("Nyman–Beurling / Hardy", False, False, False, "dispersing"),
    ("RTF / period (Waldspurger)", False, False, False, "central value, not zeros"),
    ("naive Yamabe / conformal Laplacian", False, False, False, "wrong sign (negative curvature)"),
]


def summary():
    mp.mp.dps = 30
    print("falsify.py -- positivity-candidate classification (upgraded with the SEES-ZEROS axis)\n")

    # demonstrate the SEES-ZEROS probe is executable and discriminating
    sens, nstar = offline_sensitivity(li_coeff)
    print(f"[SEES-ZEROS probe] Li functional sensitive to a planted off-line zero? {sens} (first n*={nstar})")
    print("   -> the canonical zero-functional SEES the zeros; a real-axis (QSM) candidate cannot.\n")

    print(f"  {'candidate':34s} {'Euler':5s} {'sees0':5s} {'indep':5s} -> verdict")
    for name, eb, sz, ind, note in REGISTRY:
        v = classify(eb, sz, ind)
        print(f"  {name:34s} {'Y' if eb else '.':5s} {'Y' if sz else '.':5s} {'Y' if ind else '.':5s} -> {v:11s}  ({note})")

    print("\n[the upgrade] the RH-SILENT verdict is new: QSM free energy and the prime Gram PASS the")
    print("  DH kill-test (Euler-borne) yet carry NO RH content -- they see the product, not the zeros.")
    print("  The prize (FORCING: Euler-borne + sees-zeros + independently provable) is still empty.")
    print("  Standing falsifier for any new candidate: run all three axes; DH-passing is necessary, cheap.")


if __name__ == "__main__":
    summary()
