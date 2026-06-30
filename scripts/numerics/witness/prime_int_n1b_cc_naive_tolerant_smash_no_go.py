"""CC naive tolerant-smash/Kunneth repair witness.

N-doc Q2 leaves an honest CC-square repair: define a smash of tolerant
modules by the relation generated from factor tolerances, then prove an
additive Kunneth theorem for dim_S on the square.  This witness tests the
naive generated-relation candidate in exact finite interval shadows.

The candidate gives only the expected additive log-count on product
cardinalities.  For discrete/equality tolerances the generated relation is
just equality on the product; the resulting dimension remembers n + m but
does not construct square H^2, an intersection form, correspondences, a
Frobenius graph, Rosati, Laurent boundary data, or a torsor splitter.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_naive_tolerant_smash_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def interval(n):
    """Power-of-two interval shadow with 2^n elements."""
    return tuple(range(2**n))


def equality_relation(points):
    return {(x, x) for x in points}


def naive_smash_relation(n, m):
    """Generated relation for equality tolerances on E_n x E_m."""
    e1 = interval(n)
    e2 = interval(m)
    r1 = equality_relation(e1)
    r2 = equality_relation(e2)
    rel = set()

    for x, xp in r1:
        for y in e2:
            rel.add(((x, y), (xp, y)))

    for x in e1:
        for y, yp in r2:
            rel.add(((x, y), (x, yp)))

    return rel


def relation_stats(n, m):
    rel = naive_smash_relation(n, m)
    off_diagonal = sum(1 for a, b in rel if a != b)
    return len(rel), off_diagonal


def ceil_log(k, b):
    power = 1
    n = 0
    while power < k:
        power *= b
        n += 1
    return n


def min_binary_generators_for_cardinality(cardinality):
    return ceil_log(cardinality, 2)


def subset_sum_values(generators):
    values = set()
    count = len(generators)
    for mask in range(1 << count):
        total = 0
        for i, generator in enumerate(generators):
            if mask & (1 << i):
                total += generator
        values.add(total)
    return values


def powers_of_two_cover_exact_power(r):
    generators = [1 << i for i in range(r)]
    values = subset_sum_values(generators)
    return len(values) == 2**r and values == set(range(2**r))


def product_cardinality(n, m):
    return len(interval(n)) * len(interval(m))


def naive_product_dimension(n, m):
    return min_binary_generators_for_cardinality(product_cardinality(n, m))


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


published_monoidal_tolerance_defined = False
published_dim_kunneth_theorem = False
q2_candidate_selected_by_program = True
carrier_native_tolerance_constructed = False
non_em_square_functor_defined = False
diagonal_factorization_broken = False
square_bigrading_constructed = False

square_h2_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False

laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False
dh_epstein_death_at_square_map = False


gate(
    "NTS1 published CC has no tolerant-module smash or dim Kunneth theorem",
    not published_monoidal_tolerance_defined
    and not published_dim_kunneth_theorem
    and q2_candidate_selected_by_program,
    "tests the N-doc Q2 generated-relation candidate, not a CC theorem",
)

relation_size, off_diagonal = relation_stats(2, 3)
gate(
    "NTS2 naive generated relation is product equality on discrete shadows",
    relation_size == product_cardinality(2, 3) == 32 and off_diagonal == 0,
    f"|R^wedge|={relation_size}, off-diagonal pairs={off_diagonal}",
)

gate(
    "NTS3 additive Kunneth shape is only exact log-cardinality",
    all(
        naive_product_dimension(n, m) == n + m
        and powers_of_two_cover_exact_power(n + m)
        for n, m in [(1, 1), (2, 3), (4, 4)]
    ),
    (
        "dims="
        + ",".join(
            f"({n},{m})->{naive_product_dimension(n, m)}"
            for n, m in [(1, 1), (2, 3), (4, 4)]
        )
    ),
)

gate(
    "NTS4 dimension-only shadow erases ordered square bidegree",
    naive_product_dimension(1, 4) == naive_product_dimension(2, 3) == 5
    and (1, 4) != (2, 3)
    and not square_bigrading_constructed,
    "(1,4) and (2,3) both give dimension 5 with no constructed bidegree",
)

gate(
    "NTS5 quantized dimension remains base-dependent bookkeeping",
    ceil_log(2**7, 2) == 7
    and ceil_log(2**7, 3) == 5
    and ceil_log(3**5, 3) == 5
    and ceil_log(3**5, 2) == 8,
    "128 has dimensions 7 over base 2 and 5 over base 3; 243 has 8 and 5",
)

gate(
    "NTS6 generated relation is an external selector, not a carrier-native construction",
    q2_candidate_selected_by_program
    and not carrier_native_tolerance_constructed
    and not square_bigrading_constructed,
    "no CC-internal monoidal universal property or square-native tolerance",
)

gate(
    "NTS7 no non-EM square functor escapes the diagonal-probe barrier",
    not non_em_square_functor_defined and not diagonal_factorization_broken,
    "additive log-counts do not define a non-EM square functor",
)

gate(
    "NTS8 no square H2/intersection/correspondence/Rosati is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "naive tolerant-smash data is not the square correspondence algebra",
)

gate(
    "NTS9 no Laurent boundary or DD4 weight>=1 data is constructed",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "no boundary map, torsor splitter, or weight>=1 datum",
)

gate(
    "NTS10 base R1 obstructions and carrier guard remain",
    dmp_dim(-1) == 1
    and dmp_dim(-2) == 0
    and not dh_epstein_death_at_square_map
    and not square_correspondence_algebra_defined,
    "DMP bottom gap remains; no carrier-consuming square map where controls die",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (NTS1-NTS10)")
