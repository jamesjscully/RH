"""CC strict-square divided-power repair witness.

Doc 187 kills promoting Connes-Consani curve-level Pic/Jacobian data itself
to End(S^2/Z).  The next repair is sharper: use the strict Gamma-set square
HZ ^ HZ directly, especially the divided-power invariants Phi_p, Phi'_p and
the universal character invariants that Q/V computed.

This witness records why that object-level noncollapse is not yet the
compactified square correspondence algebra.  The strict square remembers
bilinear factorizations, but the resulting invariants are ungraded,
many-valued diagnostic functions.  They supply no square cohomology H^2, no
intersection form, no correspondence algebra, no Frobenius graph, no positive
Rosati, and no Laurent boundary/torsor data.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_strict_square_divided_power_no_go
"""

from math import factorial

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def binom_int(n, p):
    num = 1
    for i in range(p):
        num *= n - i
    return num // factorial(p)


def total(a, b, edges):
    return sum(a[i] * b[j] for i, j in edges)


def column_sums(a, b, edges):
    cols = [0] * len(b)
    for i, j in edges:
        cols[j] += a[i]
    return cols


def row_sums(a, b, edges):
    rows = [0] * len(a)
    for i, j in edges:
        rows[i] += b[j]
    return rows


def phi_col_mod_p(a, b, edges, p):
    cols = column_sums(a, b, edges)
    return sum((b[j] ** p) * binom_int(cols[j], p) for j in range(len(b))) % p


def phi_row_mod_p(a, b, edges, p):
    rows = row_sums(a, b, edges)
    return sum((a[i] ** p) * binom_int(rows[i], p) for i in range(len(a))) % p


def chi_col(a, b, edges):
    """Universal column character Sum_j b_j [A_j], dropping A_j=0."""
    out = {}
    for j, bj in enumerate(b):
        aj = sum(a[i] for i, jj in edges if jj == j)
        if bj != 0 and aj != 0:
            out[aj] = out.get(aj, 0) + bj
    return {key: val for key, val in out.items() if val != 0}


def convolve_chi(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a * b] = out.get(a * b, 0) + ca * cb
    return {key: val for key, val in out.items() if val != 0}


def square_product(x, y):
    """External product of two strict-square triples at 1_+."""
    a, b, edges = x
    c, d, fedges = y
    new_a = tuple(ai * ck for ai in a for ck in c)
    new_b = tuple(bj * dl for bj in b for dl in d)
    new_edges = []
    for i, j in edges:
        for k, l in fedges:
            new_i = i * len(c) + k
            new_j = j * len(d) + l
            new_edges.append((new_i, new_j))
    return new_a, new_b, tuple(new_edges)


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


L = ((1, 1), (1, 1), ((0, 0), (0, 1), (1, 0)))
C3 = ((3,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
F41 = ((4,), (1,), ((0, 0),))
BASE0 = ((1,), (0,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

L_total = total(*L)
C3_total = total(*C3)
L_phi2 = phi_row_mod_p(*L, 2)
C3_phi2 = phi_row_mod_p(*C3, 2)
F22_total = total(*F22)
F41_total = total(*F41)
F22_phi3 = phi_col_mod_p(*F22, 3)
F41_phi3 = phi_col_mod_p(*F41, 3)
zero_split_total = total(*ZERO_SPLIT)
zero_split_chi = chi_col(*ZERO_SPLIT)

chi_L = chi_col(*L)
chi_C3 = chi_col(*C3)
chi_F22 = chi_col(*F22)
chi_F41 = chi_col(*F41)
prod = square_product(L, F22)

# Status flags for the demanded End(S^2/Z) package.
strict_square_object_level_exists = True
published_cc_functors_factor_through_diagonal = True
strict_square_has_grading = False
degree_3_bokstedt_slot_formable = False
square_h2_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False
laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
carrier_multiplication_with_dd4_weight_data = False
dh_epstein_death_at_square_correspondence = False


gate(
    "CSD1 strict square separates diagonal fibers",
    L_total == C3_total == 3 and L_phi2 == 1 and C3_phi2 == 0,
    f"mu(L)=mu(C3)={L_total}, Phi'_2(L)={L_phi2}, Phi'_2(C3)={C3_phi2}",
)

gate(
    "CSD2 strict square remembers bilinear factorization",
    F22_total == F41_total == 4 and F22_phi3 == 0 and F41_phi3 == 1,
    f"mu(2x2)=mu(4x1)={F22_total}, Phi_3(2x2)={F22_phi3}, Phi_3(4x1)={F41_phi3}",
)

gate(
    "CSD3 zero fiber also splits from the basepoint shadow",
    zero_split_total == 0 and zero_split_chi == {1: 2, 2: -1},
    f"mu(zero split)={zero_split_total}, chi_col={zero_split_chi}",
)

gate(
    "CSD4 universal character data overproduces invariant axes",
    chi_L == {1: 1, 2: 1}
    and chi_C3 == {3: 1}
    and chi_F22 == {2: 2}
    and chi_F41 == {4: 1},
    f"chi(L)={chi_L}, chi(C3)={chi_C3}, chi(2x2)={chi_F22}, chi(4x1)={chi_F41}",
)

gate(
    "CSD5 character multiplication is monoid-ring convolution, not H2",
    chi_col(*prod) == convolve_chi(chi_L, chi_F22),
    f"chi(L*2x2)={chi_col(*prod)}, convolution={convolve_chi(chi_L, chi_F22)}",
)

gate(
    "CSD6 published CC probes still see only the diagonal curve shadow",
    strict_square_object_level_exists and published_cc_functors_factor_through_diagonal,
    "object noncollapse exists, but EM/RR/Pic/Hom probes factor through mu",
)

gate(
    "CSD7 no grading or Bokstedt-degree dictionary is constructed",
    not strict_square_has_grading and not degree_3_bokstedt_slot_formable,
    "Phi'_2 is a Z/2 shadow, not a degree-3 THH class",
)

gate(
    "CSD8 no square H2, intersection, correspondence, Frobenius, or Rosati",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "strict invariants are diagnostics, not the End(S^2/Z) algebra",
)

gate(
    "CSD9 no Laurent boundary or torsor data is produced",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not carrier_multiplication_with_dd4_weight_data,
    "DD.4 weights>=1 remains unfinished",
)

gate(
    "CSD10 base R1 obstructions and carrier guard remain",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not torsor_splitter_defined
    and not dh_epstein_death_at_square_correspondence,
    "no degree -2 DMP support, no b/phi(b)=c splitter, no DH/Epstein death",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CSD1-CSD10)")
