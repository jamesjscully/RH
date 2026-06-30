"""ku square / Adams graph shadow promotion witness.

The connective ku square is one of the strongest positive shadows in the
bank: THH(ku) has amplitude 2, an even torsion ladder

    |T_{2w}| = lcm(1..w+1) / (w(w+1)),

and the pi_*-level Adams graph shadow has weight-w piece Z/|k-l|.  This
is surface-like and genuinely arithmetic at the count level.

This witness records why promoting that shadow itself to End(S^2/Z) is not
construction-grade.  The determinant/properness scheme is not fixed, the
full Adams-twisted THH correspondence algebra is not computed, integral
structured Adams operations are not constructed, and no compactified
arithmetic square with H2/intersection/Frobenius graph/positive Rosati or
Laurent boundary data is built.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_ku_square_adams_shadow_no_go
"""

import math

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def lcm_upto(n):
    out = 1
    for k in range(1, n + 1):
        out = out * k // math.gcd(out, k)
    return out


def ku_torsion_order(w):
    """Lee/I-doc ladder: |T_{2w}| = lcm(1..w+1)/(w(w+1))."""
    return lcm_upto(w + 1) // (w * (w + 1))


def graph_shadow_order(k, l, w):
    g = 0
    for i in range(1, w + 1):
        g = math.gcd(g, k**i - l**i)
    return abs(g)


def vp(n, p):
    if n == 0:
        return None
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def ku_log_sum(wmax):
    return math.fsum(math.log(ku_torsion_order(w)) for w in range(1, wmax + 1))


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


ku_surface_like_amplitude_banked = True
ku_h0_excess_seen = True
ku_h1_free_seen = True
ku_h2_torsion_seen = True
ku_torsion_even_degree = True
adams_pi_star_graph_shadow_seen = True
p_complete_adams_family_seen = True
p_complete_family_group_like = True

determinant_scheme_fixed = False
regularized_diagonal_constant_computed = False
compactified_arithmetic_square_constructed = False
properness_duality_constructed = False
full_twisted_thh_computed = False
integral_structured_adams_maps_constructed = False
ff_bidegree_frobenius_graph_constructed = False

square_h2_as_arithmetic_cohomology_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False

laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False

dh_epstein_lack_ku_ring = True
dh_epstein_death_at_end_s2z_square_map = False


low_table = {4: 3, 5: 2, 6: 10, 7: 15, 8: 35, 9: 28, 10: 252}
gate(
    "KAS1 ku square amplitude-2 torsion ladder is real",
    ku_surface_like_amplitude_banked
    and ku_h0_excess_seen
    and ku_h1_free_seen
    and ku_h2_torsion_seen
    and all(ku_torsion_order(w) == v for w, v in low_table.items())
    and all(lcm_upto(w + 1) % (w * (w + 1)) == 0 for w in range(1, 150)),
    "H0/H1/H2 shadow banked; |T_2w| low table and divisibility checked",
)


gate(
    "KAS2 positive even-degree H2 shadow is not yet a Rosati form",
    ku_torsion_even_degree
    and all((2 * w) % 2 == 0 for w in range(1, 150))
    and all(ku_torsion_order(w) >= 1 for w in range(1, 150))
    and not positive_rosati_defined
    and not square_intersection_form_defined,
    "all checked torsion degrees are even and positive-count, but no pairing",
)


ok_graph = True
for k in range(2, 18):
    for l in range(1, k):
        for w in (1, 2, 3, 5, 10, 30, 60):
            if graph_shadow_order(k, l, w) != k - l:
                ok_graph = False

gate(
    "KAS3 Adams HH0 graph shadow has exact Z/|k-l| weight pieces",
    adams_pi_star_graph_shadow_seen and ok_graph,
    "gcd_{i<=w}(k^i-l^i)=|k-l| for k,l<=17 and sampled weights",
)


ok_lte = True
p = 5
alpha = 1 + p
modulus = p**35
running = 1
for w in range(1, 501):
    running = (running * alpha) % modulus
    if vp((running - 1) % modulus, p) != 1 + vp(w, p):
        ok_lte = False

gate(
    "KAS4 p-complete Adams family is group-like, not FF bidegree data",
    p_complete_adams_family_seen
    and p_complete_family_group_like
    and ok_lte
    and not integral_structured_adams_maps_constructed
    and not ff_bidegree_frobenius_graph_constructed,
    "wild p-complete LTE ladder checked; integral maps and (1,q) graphs absent",
)


s50 = ku_log_sum(50)
s200 = ku_log_sum(200)
s500 = ku_log_sum(500)
gate(
    "KAS5 determinant/properness scheme is still unfixed",
    s50 < s200 < s500
    and not determinant_scheme_fixed
    and not regularized_diagonal_constant_computed
    and not compactified_arithmetic_square_constructed
    and not properness_duality_constructed,
    f"partial log sums grow {s50:.3f} < {s200:.3f} < {s500:.3f}; no D_ku constant",
)


gate(
    "KAS6 full Adams-twisted THH correspondence algebra is not computed",
    adams_pi_star_graph_shadow_seen
    and not full_twisted_thh_computed
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined,
    "HH0/pi_* graph counts are shadows; no full twisted THH End algebra",
)


gate(
    "KAS7 no compactified square H2/intersection/correspondence/Rosati is built",
    not square_h2_as_arithmetic_cohomology_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "ku has surface-like torsion, not the compactified arithmetic square",
)


gate(
    "KAS8 no Laurent boundary, torsor splitter, or DD4 weight>=1 datum is built",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "the ku shadow does not supply R1 boundary/torsor data",
)


gate(
    "KAS9 carrier guard is only ku-specific, not an End(S^2/Z) construction",
    dh_epstein_lack_ku_ring
    and not dh_epstein_death_at_end_s2z_square_map
    and not compactified_arithmetic_square_constructed,
    "DH/Epstein cannot form ku THH, but no S^2/Z square map is constructed",
)


gate(
    "KAS10 base R1 obstructions remain open",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not positive_rosati_defined,
    "DMP bottom gap remains; R1 needs a carrier-native boundary/correspondence",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (KAS1-KAS10)")
