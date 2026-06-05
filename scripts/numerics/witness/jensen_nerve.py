"""Jensen-cover nerve computation (STRATEGY.md §4 + §7.2).

Does the Jensen cert/tail/bridge proof structure have genuine DESCENT TEETH, or is it
descent-trivial like the deleted NB-BD family?

The sharp criterion (STRATEGY §4):
  * constant-coefficient nerve H^1 sees only the TOPOLOGY of the covered region;
  * a pure cert/tail/bridge RECURSION is a TREE -> contractible -> H^1 = 0 (trivial);
  * teeth require (a) SHARED sub-problems (reconvergent cycles -> a DAG, not a tree),
    AND (b) nontrivial SLACK MONODROMY around those cycles -- the metric obstruction,
    i.e. H^1 of the slack-valued certificate sheaf, not the constant sheaf.

This module supplies the apparatus and computes it on several coverage models.  The
real Jensen (degree d, shift n) overlap data plugs into `jensen_dn_cover` once known.

Run:  python3 -m scripts.numerics.witness.jensen_nerve
"""
from __future__ import annotations

import numpy as np

from .descent_test import cech_h1


# ---- coverage models -------------------------------------------------------
def tree_recursion(depth: int):
    """A pure cert/tail/bridge recursion: each bridge splits into (cert, tail, bridge).
    The dependency graph is a TREE -> contractible -> H^1 = 0."""
    edges = []
    nxt = 1
    frontier = [0]
    for _ in range(depth):
        new = []
        for parent in frontier:
            for _child in range(3):          # cert, tail, bridge
                edges.append((parent, nxt))
                new.append(nxt)
                nxt += 1
        frontier = new
    return {"V": nxt, "edges": edges, "H1": cech_h1(nxt, edges)}


def shared_subproblem_dag():
    """A recursion where sub-problems are REUSED across branches (reconvergence):
    two bridges depend on the SAME sub-certificate -> a diamond -> a cycle.
    Each independent diamond contributes 1 to H^1."""
    # 0 -> {1,2};  1 -> 3;  2 -> 3   (diamond 0-1-3-2);  plus a second diamond 3->{4,5}->6
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 6), (5, 6)]
    return {"V": 7, "edges": edges, "H1": cech_h1(7, edges)}


def jensen_dn_cover(degrees=4, kind="strip"):
    """Model the (d, n) certification grid as a cover.
    kind='strip'  : contractible quadrant tiled by overlapping boxes -> H^1 = 0.
    kind='annulus': the same tiling but with an UNCERTIFIED hole (a degree/shift
                    window no single method covers) -> the cover wraps a loop -> H^1 = 1.
    These bracket the real proof: teeth appear iff the certified region is not simply
    connected OR the slack sheaf has monodromy (see slack_monodromy)."""
    # vertices = boxes on a grid; edges = adjacent (overlapping) boxes
    pts = [(d, n) for d in range(degrees) for n in range(degrees)]
    if kind == "annulus":
        pts = [p for p in pts if p != (degrees // 2, degrees // 2)]  # punch a hole
    idx = {p: i for i, p in enumerate(pts)}
    edges = []
    for (d, n), i in idx.items():
        for dd, nn in [(d + 1, n), (d, n + 1)]:
            if (dd, nn) in idx:
                edges.append((i, idx[(dd, nn)]))
    # triangulate each fully-present 2x2 cell via its diagonal (a--e), so the cell is a
    # contractible disk (good cover); without this a filled grid would show spurious loops.
    triangles = []
    for (d, n) in list(idx):
        if all(q in idx for q in [(d, n), (d + 1, n), (d, n + 1), (d + 1, n + 1)]):
            a, b = idx[(d, n)], idx[(d + 1, n)]
            c, e = idx[(d, n + 1)], idx[(d + 1, n + 1)]
            edges.append((a, e))                 # the cell diagonal
            triangles += [(a, b, e), (a, c, e)]
    return {"kind": kind, "V": len(pts), "H1": cech_h1(len(pts), edges, triangles)}


# ---- the metric obstruction: slack monodromy -------------------------------
def slack_monodromy(cycle_ratios):
    """The real (metric) descent obstruction (STRATEGY §3/§4).  Around an overlap
    CYCLE, each edge carries a multiplicative slack ratio r_ij (region i's certified
    margin vs region j's on their overlap).  The local margins reconcile into a global
    certificate iff there exist m_i with m_j/m_i = r_ij on every edge -- i.e. iff the
    product of r_ij around the cycle is 1.  The product is the monodromy = H^1 of the
    slack sheaf; != 1 means the 'no-slack' tightness CANNOT be glued (descent fails)."""
    prod = float(np.prod(cycle_ratios))
    return {"ratios": list(cycle_ratios), "monodromy": prod,
            "reconcilable": abs(prod - 1.0) < 1e-12}


def summary():
    print("Jensen-cover nerve computation (STRATEGY.md §4)\n")

    tr = tree_recursion(depth=3)
    print(f"[pure recursion = tree]      V={tr['V']:3d}  H^1 = {tr['H1']}  -> TRIVIAL "
          "(same fate as NB-BD)")

    dag = shared_subproblem_dag()
    print(f"[shared sub-problems = DAG]  V={dag['V']:3d}  H^1 = {dag['H1']}  -> "
          "cycles (2 diamonds) -> descent-live")

    strip = jensen_dn_cover(kind="strip")
    ann = jensen_dn_cover(kind="annulus")
    print(f"[(d,n) cover, contractible]  V={strip['V']:3d}  H^1 = {strip['H1']}  -> trivial")
    print(f"[(d,n) cover, with a hole]   V={ann['V']:3d}  H^1 = {ann['H1']}  -> descent-live")

    print("\n[slack monodromy = the metric obstruction]")
    ok = slack_monodromy([1.2, 0.8, 1.0 / (1.2 * 0.8)])      # product 1
    bad = slack_monodromy([1.2, 0.8, 1.05])                  # product != 1
    print(f"   reconcilable cycle: product={ok['monodromy']:.4f}  reconcilable={ok['reconcilable']}")
    print(f"   obstructed   cycle: product={bad['monodromy']:.4f}  reconcilable={bad['reconcilable']}")

    print("\nVERDICT / what to check in the REAL Jensen proof")
    print("  * If the proof is a pure cert/tail/bridge recursion (a tree), it is")
    print("    descent-TRIVIAL -- H^1 = 0 -- and descent buys nothing (same as NB-BD).")
    print("  * Teeth require BOTH: (a) sub-certificates REUSED across branches, so the")
    print("    dependency graph has reconvergent cycles (a DAG / a hole in the (d,n)")
    print("    coverage), AND (b) nontrivial SLACK MONODROMY around those cycles -- the")
    print("    product of margin-ratios on overlaps != 1, so the tight margins cannot be")
    print("    globally reconciled.  That monodromy IS the forcing-structure obstruction.")
    print("  NEXT (real data): extract from a Jensen (or interval-subdivision) proof its")
    print("  overlap graph and the per-overlap margin ratios; run cech_h1 for cycles and")
    print("  slack_monodromy for the metric class.  H^1=0 and monodromy=1 everywhere ->")
    print("  descent is dead for RH-shaped proofs (a real negative result).  Otherwise ->")
    print("  the family where an obstruction calculus could actually live.")
    return {"tree": tr["H1"], "dag": dag["H1"], "strip": strip["H1"], "annulus": ann["H1"]}


if __name__ == "__main__":
    summary()
