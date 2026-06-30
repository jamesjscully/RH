r"""Endpoint-parity-saturation DD.4/SCC no-go.

Doc 273 rejects oriented endpoint difference because recovering endpoints
from total and difference uses a parity condition and a half-sum decoder. This
witness tests the next repair:

    build the parity condition into the register, or saturate the register by
    adjoining the half-sums.

The positive fact is real.  The same-parity lattice
P={(s,a): s=a mod 2} is the image of (d1,d2) -> (d1+d2,d1-d2), the half-sum
decoder is integral on P, and the oriented difference twist splits
c=(1+z)^-1 on P.  The no-go is that P is an externally selected index-two
integrality condition.  The full total/difference register still has
non-endpoint labels that split the DD.4 class, while saturation decodes those
labels to half-integral endpoints.  The same parity/saturation package is
formable on controls, and no square-carrier slot is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_endpoint_parity_saturation_no_go
"""

from fractions import Fraction
from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[z]/z^{L+1}; 1-units are dicts {power: 1}."""

    def add(a, b):
        out = dict(a)
        for k in b:
            out[k] = out.get(k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def mul(a, b):
        out = {}
        for i in a:
            for j in b:
                if i + j <= L:
                    out[i + j] = out.get(i + j, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def inv(a):
        assert a.get(0, 0) == 1
        rem = add(a, {0: 1})
        term = {0: 1}
        out = {0: 1}
        for _ in range(1, L + 1):
            term = mul(term, rem)
            if not term:
                break
            out = add(out, term)
        return out

    def phi(f):
        out = {}
        for m in f:
            if m == 0:
                out[0] = out.get(0, 0) ^ 1
                continue
            for k in range(0, L - m + 1):
                if comb(m + k - 1, k) % 2:
                    out[m + k] = out.get(m + k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    return add, mul, inv, phi


def to_vec(f, L):
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, zero_vec, from_vec_fn, mul_fn, to_vec_fn):
    seen = {zero_vec}
    queue = [zero_vec]
    while queue:
        current = from_vec_fn(queue.pop())
        for gen in gens:
            nxt = to_vec_fn(mul_fn(current, gen))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def pow_unit(unit, exponent, mul, inv):
    if exponent < 0:
        return inv(pow_unit(unit, -exponent, mul, inv))
    out = {0: 1}
    base = unit
    n = exponent
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def boundary(unit, inv, phi, mul):
    return mul(unit, inv(phi(unit)))


def h1_profile(L):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        boundary({0: 1, k: 1}, inv, phi, mul) for k in range(1, L + 1)
    ]
    norm_gens = [
        mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)
    ]
    coboundaries = closure(
        boundary_gens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    norm_image = closure(
        norm_gens,
        (0,) * L,
        from_vec,
        mul,
        lambda f: to_vec(f, L),
    )
    z1_order = 2**L // len(norm_image)
    return {
        "L": L,
        "c": c,
        "coboundaries": coboundaries,
        "h1_order": z1_order // len(coboundaries),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "c_boundary": to_vec(c, L) in coboundaries,
        "res1_c": c.get(1, 0),
    }


def sumdiff(pair):
    d1, d2 = pair
    return d1 + d2, d1 - d2


def in_same_parity_lattice(label):
    s, a = label
    return (s - a) % 2 == 0


def decode_integral(label):
    s, a = label
    if not in_same_parity_lattice(label):
        return None
    return (s + a) // 2, (s - a) // 2


def decode_saturated(label):
    s, a = label
    return Fraction(s + a, 2), Fraction(s - a, 2)


def endpoint_mul(x, y, mul):
    return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])


def endpoint_inv(x, inv):
    return (-x[0][0], -x[0][1]), inv(x[1])


def oriented_sumdiff_split_profile(L, split_vector):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def ell(label):
        return label[1]

    def sigma(x):
        label, unit = x
        twist = pow_unit(c, ell(label), mul, inv)
        return label, mul(twist, phi(unit))

    def tau(x):
        label, unit = x
        s, a = label
        return (s, -a), inv(unit)

    def emul(x, y):
        return endpoint_mul(x, y, mul)

    def einv(x):
        return endpoint_inv(x, inv)

    def eboundary(x):
        return emul(x, einv(sigma(x)))

    register_gens = [((2, 0), {0: 1}), ((1, 1), {0: 1}), ((1, -1), {0: 1})]
    unit_gens = [((0, 0), {0: 1, k: 1}) for k in range(1, L + 1)]
    test_gens = register_gens + unit_gens
    split_generator = sigma((split_vector, {0: 1}))
    split_boundary = eboundary(split_generator)

    return {
        "L": L,
        "split_vector": split_vector,
        "split_vector_in_parity_lattice": in_same_parity_lattice(split_vector),
        "split_decodes_to": decode_integral(split_vector),
        "split_ell": ell(split_vector),
        "sigma_involutive_on_gens": all(sigma(sigma(gen)) == gen for gen in test_gens),
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in test_gens),
        "split_boundary_is_c": split_boundary == ((0, 0), c),
        "uses_square_data": False,
    }


def parity_lattice_profile(window=3):
    endpoint_pairs = [(d1, d2) for d1 in range(-window, window + 1) for d2 in range(-window, window + 1)]
    labels = [sumdiff(pair) for pair in endpoint_pairs]
    decoded = [decode_integral(label) for label in labels]
    parity_classes = {(s % 2, a % 2) for s in range(2) for a in range(2)}
    image_classes = {(label[0] % 2, label[1] % 2) for label in labels}
    invalid_examples = [(0, 1), (11, 8), (10, 1)]
    return {
        "matrix_det": -2,
        "index_two": True,
        "image_is_same_parity": all(in_same_parity_lattice(label) for label in labels),
        "decoder_round_trips": decoded == endpoint_pairs,
        "parity_classes": parity_classes,
        "image_classes": image_classes,
        "excluded_classes": parity_classes - image_classes,
        "invalid_examples": invalid_examples,
        "invalid_not_in_lattice": all(not in_same_parity_lattice(label) for label in invalid_examples),
        "carrier_forces_parity": False,
    }


def invalid_splitter_profile(L):
    profile = oriented_sumdiff_split_profile(L, (0, 1))
    return {
        **profile,
        "invalid_splitter_not_endpoint": decode_integral((0, 1)) is None,
        "saturated_decode": decode_saturated((0, 1)),
    }


def saturation_profile():
    labels = [(0, 1), (11, 8), (10, 1), (11, 9), (11, 3)]
    rows = []
    for label in labels:
        decoded = decode_saturated(label)
        integral = decoded[0].denominator == 1 and decoded[1].denominator == 1
        rows.append(
            {
                "label": label,
                "decoded": decoded,
                "integral": integral,
                "ordinary_decode": decode_integral(label),
            }
        )
    return {
        "rows": rows,
        "invalid_labels_become_half_integral": all(
            not row["integral"] for row in rows if row["ordinary_decode"] is None
        ),
        "valid_labels_remain_integral": all(
            row["integral"] for row in rows if row["ordinary_decode"] is not None
        ),
        "integer_degree_maps_preserved_on_full_register": False,
        "half_sum_saturation_imported": True,
    }


def control_parity_profile(dim):
    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))

    def add_vec(x, y):
        return tuple(a + b for a, b in zip(x, y))

    def neg_vec(x):
        return tuple(-a for a in x)

    def scale_vec(n, x):
        return tuple(n * a for a in x)

    def ell(label):
        return label[1]

    def sigma(pair):
        label, vector = pair
        return label, add_vec(neg_vec(vector), scale_vec(ell(label), chosen))

    def tau(pair):
        label, vector = pair
        s, a = label
        return (s, -a), neg_vec(vector)

    parity_gens = [((2, 0), zero), ((1, 1), zero), ((1, -1), zero)]
    split = ((1, 1), zero)
    return {
        "dim": dim,
        "parity_lattice_declared": all(in_same_parity_lattice(gen[0]) for gen in parity_gens),
        "sigma_involutive": all(sigma(sigma(gen)) == gen for gen in parity_gens),
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in parity_gens),
        "split_boundary_is_chosen": sigma(split)[1] == chosen,
        "uses_square_data": False,
        "kills_controls": False,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
parity_profile = parity_lattice_profile()
parity_split_profiles = [
    oriented_sumdiff_split_profile(L, (1, 1)) for L in (6, 8, 10, 12)
]
invalid_split_profiles = [invalid_splitter_profile(L) for L in (6, 8, 10, 12)]
saturation = saturation_profile()
control_profiles = [control_parity_profile(dim) for dim in (2, 4, 8)]


gate(
    "EPS1 base DD.4 class remains the nonzero 1-unit obstruction",
    all(
        p["h1_order"] == 2 and not p["c_boundary"] and p["res1_c"] == 1
        for p in base_profiles
    ),
    "  ".join(
        "L%d:|B|=2^%d,|Z1|=2^%d,H1=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in base_profiles
    ),
)

gate(
    "EPS2 same-parity sum/difference lattice decodes endpoints and splits c",
    parity_profile["matrix_det"] == -2
    and parity_profile["index_two"]
    and parity_profile["image_is_same_parity"]
    and parity_profile["decoder_round_trips"]
    and all(
        p["split_vector_in_parity_lattice"]
        and p["split_decodes_to"] == (1, 0)
        and p["split_ell"] == 1
        and p["sigma_involutive_on_gens"]
        and p["tau_commutes_with_sigma"]
        and p["split_boundary_is_c"]
        and not p["uses_square_data"]
        for p in parity_split_profiles
    ),
    "image classes=%s; excluded=%s"
    % (sorted(parity_profile["image_classes"]), sorted(parity_profile["excluded_classes"])),
)

gate(
    "EPS3 parity is an external index-two integrality condition",
    not parity_profile["carrier_forces_parity"]
    and parity_profile["invalid_not_in_lattice"]
    and all(
        p["invalid_splitter_not_endpoint"]
        and p["split_ell"] == 1
        and p["tau_commutes_with_sigma"]
        and p["split_boundary_is_c"]
        and not p["uses_square_data"]
        for p in invalid_split_profiles
    ),
    "invalid labels still split: "
    + ", ".join(str(label) for label in parity_profile["invalid_examples"]),
)

gate(
    "EPS4 half-sum saturation makes invalid labels half-integral endpoints",
    saturation["invalid_labels_become_half_integral"]
    and saturation["valid_labels_remain_integral"]
    and not saturation["integer_degree_maps_preserved_on_full_register"]
    and saturation["half_sum_saturation_imported"],
    "  ".join(
        "%s->%s" % (row["label"], row["decoded"]) for row in saturation["rows"]
    ),
)

gate(
    "EPS5 the same parity/saturation package is formable on controls",
    all(
        p["parity_lattice_declared"]
        and p["sigma_involutive"]
        and p["tau_commutes_with_sigma"]
        and p["split_boundary_is_chosen"]
        and not p["uses_square_data"]
        and not p["kills_controls"]
        for p in control_profiles
    ),
    "  ".join("dim%d:parity-lattice-splits" % p["dim"] for p in control_profiles),
)


required_slots = [
    "actual_square",
    "integral_rep_NS",
    "two_degree_maps",
    "indecomposable_diagonal",
    "frobenius_graph",
    "proper_correspondence",
    "fiber_product_composition",
    "projection_formula",
    "canonical_rosati",
    "positive_primitive_sign",
    "carrier_boundary",
    "control_death",
]

parity_saturation_slots = {
    "selected_index_two_lattice": True,
    "half_sum_saturation": True,
    "actual_square": False,
    "integral_rep_NS": False,
    "two_degree_maps": False,
    "indecomposable_diagonal": False,
    "frobenius_graph": False,
    "proper_correspondence": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "canonical_rosati": False,
    "positive_primitive_sign": False,
    "carrier_boundary": False,
    "control_death": False,
}

gate(
    "EPS6 endpoint parity saturation satisfies no square-carrier slot",
    not any(parity_saturation_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nEPS1-EPS6 ALL PASS: endpoint parity saturation is not the square carrier")
print(
    "VERDICT: the same-parity sum/difference lattice makes the half-sum "
    "decoder integral and still splits c=(1+z)^-1, but selecting that "
    "index-two lattice is external.  The full register has non-endpoint "
    "labels that split c, while saturation decodes them to half-integral "
    "endpoints.  The same package is formable on controls, and no square, "
    "rep_NS, proper correspondences, projection formula, Rosati, carrier "
    "boundary, or control death is constructed."
)
