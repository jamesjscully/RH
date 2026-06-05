"""Kill-test gates (STRATEGY.md §5).

A candidate forcing structure / bridge is admitted only if it passes these
*anti-dispersion* gates.  They are cheap evaluations, not proofs, and their job is to
KILL information-dispersing candidates -- not to defend one.  The governing tell:
a statement is RH-neutral (dispersing) if it holds for Davenport-Heilbronn.

  Gate 1  DH discrimination     -- prime side != Lambda for DH (explicit_formula)
  Gate 2  Epstein second wall   -- product-bearing yet RH-false (second_wall)
  Gate 3  Weil/Li positivity    -- >=0 for zeta, detects DH off-line zeros (li_positivity)
  Gate 4  not descent-trivial   -- the cover's nerve has H^1 != 0 (descent_test)

Run:  python3 -m scripts.numerics.witness.harness
"""
from __future__ import annotations


def gate1_dh_discrimination(M: int = 30):
    from . import explicit_formula as EF
    return EF.weil_positivity_check(M)


def gate2_epstein_wall():
    from . import second_wall as SW
    return SW.summary()


def gate3_weil_li_positivity():
    from . import li_positivity as LP
    return LP.summary(quick=True)


def gate4_descent_nontrivial():
    from . import descent_test as DT
    return DT.nerve_examples()


def _report():
    print("=" * 72)
    print("KILL-TEST GATES (anti-dispersion).  A candidate must FAIL for DH/Epstein,")
    print("respect Weil positivity, and not be descent-trivial.  See STRATEGY.md §5.")
    print("=" * 72)

    print("\n[Gate 1] DH discrimination (prime side of -Z'/Z)")
    g1 = gate1_dh_discrimination()
    print("  zeta prime side == von Mangoldt:", g1["zeta_prime_side_equals_vonMangoldt"])
    print("  DH prime side has negative coeffs:", g1["DH_prime_side_has_negative_coeffs"])
    print("  -> the Euler-product signature separates zeta from DH (FAILS for DH): good.")

    print("\n[Gate 2] Epstein second wall (Euler product yet RH-false)")
    gate2_epstein_wall()

    print("\n[Gate 3] Weil / Li positivity")
    gate3_weil_li_positivity()

    print("\n[Gate 4] Descent non-triviality (nerve H^1)")
    g4 = gate4_descent_nontrivial()
    print("  chain / additive cover (e.g. NB-BD truncation):  H^1 =", g4["chain_nested_cover"],
          "-> DECORATION (kill)")
    print("  overlap-cycle cover (e.g. Jensen boxes):         H^1 =", g4["loop_4box"],
          "-> descent-live")
    print("  CRITERION: a candidate is descent-trivial unless its cover's nerve has H^1 != 0.")
    print("=" * 72)


if __name__ == "__main__":
    _report()
