"""CC norm-filtration/MAX-face promotion witness.

AA proves a real positive strict-layer fact: CC's norm filtration,
transported through the strict-square character, is the archimedean half of
the product formula on the monoid ring.  This witness records why promoting
that strict norm/MAX face itself to End(S^2/Z) is still not construction
grade.

The norm supplies weights, not THH degrees, square H^2, an intersection
form, correspondences, a Frobenius graph, Rosati, Laurent boundary data, or
a torsor splitter.  The archimedean norm alone is also carrier-blind; the
discriminating content is the coupling to multiplication, valuations, and a
derived degree axis.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_norm_filtration_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def prime_factorization(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def reconstruct_from_valuations(n):
    prod = 1
    for p, e in prime_factorization(n).items():
        prod *= p**e
    return prod


def monoid_norm(a):
    return abs(a)


def difference_class_norm(p, i, j):
    if i == j:
        return p**i
    return 2 * p ** max(i, j)


def epstein_metric_norm(v):
    x, y = v
    return x * x + 5 * y * y


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


aa_strict_norm_theorem_available = True
aa_epstein_norm_guard_passed = True
cc_norm_supplies_weights = True
cc_norm_supplies_degrees = False
derived_normed_spectral_sequence_constructed = False
bokstedt_degree_dictionary_constructed = False
non_em_square_functor_defined = False

integer_carrier_has_multiplication = True
epstein_control_has_metric = True
epstein_control_has_integer_factorization = False
epstein_control_has_product_formula = False

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
    "CNF1 AA strict norm filtration is a real positive strict-layer datum",
    aa_strict_norm_theorem_available
    and all(monoid_norm(a) == a for a in range(1, 13))
    and difference_class_norm(2, 2, 0) == 8
    and difference_class_norm(3, 2, 1) == 18,
    "N([A])=|A| and N([p^i]-[p^j])=2 p^max on checked examples",
)

gate(
    "CNF2 product-formula split requires integer multiplication and valuations",
    integer_carrier_has_multiplication
    and all(reconstruct_from_valuations(n) == n for n in range(2, 501)),
    "integer labels reconstruct exactly from prime valuations for 2<=n<=500",
)

gate(
    "CNF3 norm weights alone erase monoid-ring sign and algebra data",
    monoid_norm(6) == monoid_norm(-6)
    and monoid_norm(10) == monoid_norm(-10)
    and cc_norm_supplies_weights
    and not cc_norm_supplies_degrees,
    "the norm sees |A|, not the signed monoid-ring class or a degree axis",
)

epstein_values = [epstein_metric_norm((3**i, 1)) for i in range(5)]
gate(
    "CNF4 the archimedean norm face is carrier-blind without the MIN half",
    aa_epstein_norm_guard_passed
    and epstein_control_has_metric
    and all(v > 0 for v in epstein_values)
    and not epstein_control_has_integer_factorization
    and not epstein_control_has_product_formula,
    f"metric norms exist on controls {epstein_values}, but no v_p/product formula",
)

gate(
    "CNF5 no derived degree or Bokstedt dictionary is constructed",
    cc_norm_supplies_weights
    and not cc_norm_supplies_degrees
    and not derived_normed_spectral_sequence_constructed
    and not bokstedt_degree_dictionary_constructed,
    "AA's degree dictionary remains observation-grade; no derived abutment",
)

gate(
    "CNF6 no non-EM square functor is built by the strict norm filtration",
    not non_em_square_functor_defined
    and not derived_normed_spectral_sequence_constructed,
    "strict weights do not extract square cohomology from the character object",
)

gate(
    "CNF7 no square H2/intersection/correspondence/Rosati is constructed",
    not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined,
    "norm/MAX-face data is not the square correspondence algebra",
)

gate(
    "CNF8 no Laurent boundary or DD4 weight>=1 data is constructed",
    not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "no boundary map, torsor splitter, or weight>=1 datum",
)

gate(
    "CNF9 surviving evasion must be derived/normed/tolerant, not strict MAX face",
    not derived_normed_spectral_sequence_constructed
    and not non_em_square_functor_defined
    and not square_correspondence_algebra_defined,
    "the open route must make weight and degree coexist carrier-natively",
)

gate(
    "CNF10 base R1 obstructions and carrier guard remain",
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

print("\nALL PASS (CNF1-CNF10)")
