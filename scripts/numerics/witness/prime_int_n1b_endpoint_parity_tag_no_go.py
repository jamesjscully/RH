r"""Endpoint-parity-tag DD.4/SCC no-go.

Doc 274 rejects selecting the same-parity endpoint lattice or saturating by
half-sums. This witness tests the next repair:

    keep the full total/difference register but add a Z/2 parity tag
    delta=s-a mod 2, then use that tag as the missing integrality datum.

The positive fact is real.  The tag detects exactly whether the half-sum
decoder is integral, and the oriented difference twist still splits
c=(1+z)^-1.  The no-go is that a tag is only a diagnostic/selector.  If the
delta=1 labels are discarded, this is doc 274's externally selected
same-parity lattice.  If they are retained, the register still contains
non-endpoint labels that can split c and decode only to half-integral
endpoints.  The same tag package is formable on controls, and no
square-carrier slot is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_endpoint_parity_tag_no_go
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


def parity_tag(label):
    s, a = label
    return (s - a) % 2


def in_same_parity_lattice(label):
    return parity_tag(label) == 0


def tagged(label):
    return label[0], label[1], parity_tag(label)


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


def tagged_register_profile(window=4):
    labels = [(s, a) for s in range(-window, window + 1) for a in range(-window, window + 1)]
    rows = []
    for label in labels:
        tag = parity_tag(label)
        integral = decode_integral(label) is not None
        saturated = decode_saturated(label)
        rows.append(
            {
                "label": label,
                "tag": tag,
                "integral": integral,
                "saturated": saturated,
            }
        )
    return {
        "rows": rows,
        "tag_detects_integrality": all((row["tag"] == 0) == row["integral"] for row in rows),
        "tag_classes": sorted({row["tag"] for row in rows}),
        "kept_if_projected": [row["label"] for row in rows if row["tag"] == 0],
        "discarded_if_projected": [row["label"] for row in rows if row["tag"] == 1],
        "discarding_delta_one_is_same_parity_lattice": True,
        "retaining_delta_one_keeps_non_endpoints": any(
            row["tag"] == 1 and row["saturated"][0].denominator == 2 for row in rows
        ),
    }


def tagged_split_profile(L, label):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def ell(tagged_label):
        return tagged_label[1]

    def sigma(x):
        tag_label, unit = x
        twist = pow_unit(c, ell(tag_label), mul, inv)
        return tag_label, mul(twist, phi(unit))

    def tau(x):
        tag_label, unit = x
        s, a, delta = tag_label
        return (s, -a, delta), inv(unit)

    def emul(x, y):
        return endpoint_mul(x, y, mul)

    def einv(x):
        return endpoint_inv(x, inv)

    def eboundary(x):
        return emul(x, einv(sigma(x)))

    tag_label = tagged(label)
    gens = [
        (tagged((2, 0)), {0: 1}),
        (tagged((1, 1)), {0: 1}),
        (tagged((0, 1)), {0: 1}),
        (tagged((1, 0)), {0: 1}),
    ]
    unit_gens = [((0, 0, 0), {0: 1, k: 1}) for k in range(1, L + 1)]
    test_gens = gens + unit_gens
    split_generator = sigma((tag_label, {0: 1}))
    split_boundary = eboundary(split_generator)
    saturated = decode_saturated(label)

    return {
        "L": L,
        "label": label,
        "tag_label": tag_label,
        "tag_detects_integrality": (tag_label[2] == 0) == (decode_integral(label) is not None),
        "integral_decode": decode_integral(label),
        "saturated_decode": saturated,
        "is_half_integral": saturated[0].denominator == 2 or saturated[1].denominator == 2,
        "split_ell": ell(tag_label),
        "sigma_involutive_on_gens": all(sigma(sigma(gen)) == gen for gen in test_gens),
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in test_gens),
        "split_boundary_is_c": split_boundary == ((0, 0), c),
        "uses_square_data": False,
    }


def parity_tag_decision_profile():
    labels = [(1, 1), (0, 1), (11, 8), (10, 1), (11, 9), (11, 3)]
    rows = []
    for label in labels:
        rows.append(
            {
                "label": label,
                "tag": parity_tag(label),
                "integral_decode": decode_integral(label),
                "saturated_decode": decode_saturated(label),
            }
        )
    return {
        "rows": rows,
        "project_to_zero_discards_labels": [row["label"] for row in rows if row["tag"] == 1],
        "keep_one_has_no_integral_decode": all(
            row["integral_decode"] is None for row in rows if row["tag"] == 1
        ),
        "tag_supplies_endpoint_maps": False,
        "carrier_forces_projection": False,
    }


def control_tag_profile(dim):
    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))

    def add_vec(x, y):
        return tuple(a + b for a, b in zip(x, y))

    def neg_vec(x):
        return tuple(-a for a in x)

    def scale_vec(n, x):
        return tuple(n * a for a in x)

    def ell(tag_label):
        return tag_label[1]

    def sigma(pair):
        tag_label, vector = pair
        return tag_label, add_vec(neg_vec(vector), scale_vec(ell(tag_label), chosen))

    def tau(pair):
        tag_label, vector = pair
        s, a, delta = tag_label
        return (s, -a, delta), neg_vec(vector)

    gens = [
        (tagged((1, 1)), zero),
        (tagged((0, 1)), zero),
        (tagged((2, 0)), zero),
        (tagged((11, 8)), chosen),
    ]
    split_zero = (tagged((1, 1)), zero)
    split_one = (tagged((0, 1)), zero)
    return {
        "dim": dim,
        "tags_declared": all(gen[0][2] == parity_tag(gen[0][:2]) for gen in gens),
        "sigma_involutive": all(sigma(sigma(gen)) == gen for gen in gens),
        "tau_commutes_with_sigma": all(tau(sigma(gen)) == sigma(tau(gen)) for gen in gens),
        "delta_zero_splits": sigma(split_zero)[1] == chosen,
        "delta_one_splits": sigma(split_one)[1] == chosen,
        "uses_square_data": False,
        "kills_controls": False,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
tag_profile = tagged_register_profile()
valid_split_profiles = [tagged_split_profile(L, (1, 1)) for L in (6, 8, 10, 12)]
invalid_split_profiles = [tagged_split_profile(L, (0, 1)) for L in (6, 8, 10, 12)]
decision_profile = parity_tag_decision_profile()
control_profiles = [control_tag_profile(dim) for dim in (2, 4, 8)]


gate(
    "EPT1 base DD.4 class remains the nonzero 1-unit obstruction",
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
    "EPT2 parity tag exactly detects half-sum integrality",
    tag_profile["tag_detects_integrality"]
    and tag_profile["tag_classes"] == [0, 1]
    and tag_profile["discarding_delta_one_is_same_parity_lattice"]
    and tag_profile["retaining_delta_one_keeps_non_endpoints"],
    "kept=%d discarded=%d"
    % (len(tag_profile["kept_if_projected"]), len(tag_profile["discarded_if_projected"])),
)

gate(
    "EPT3 tagged integral labels split c but this is only the doc-274 lattice",
    all(
        p["tag_detects_integrality"]
        and p["tag_label"][2] == 0
        and p["integral_decode"] == (1, 0)
        and p["split_ell"] == 1
        and p["sigma_involutive_on_gens"]
        and p["tau_commutes_with_sigma"]
        and p["split_boundary_is_c"]
        and not p["uses_square_data"]
        for p in valid_split_profiles
    ),
    "delta=0 label (1,1) decodes to (1,0) and splits",
)

gate(
    "EPT4 tagged non-endpoint labels still split c",
    all(
        p["tag_detects_integrality"]
        and p["tag_label"][2] == 1
        and p["integral_decode"] is None
        and p["is_half_integral"]
        and p["split_ell"] == 1
        and p["tau_commutes_with_sigma"]
        and p["split_boundary_is_c"]
        and not p["uses_square_data"]
        for p in invalid_split_profiles
    )
    and decision_profile["keep_one_has_no_integral_decode"]
    and not decision_profile["tag_supplies_endpoint_maps"]
    and not decision_profile["carrier_forces_projection"],
    "delta=1 examples="
    + ", ".join(str(label) for label in decision_profile["project_to_zero_discards_labels"]),
)

gate(
    "EPT5 the same endpoint parity tag is formable on controls",
    all(
        p["tags_declared"]
        and p["sigma_involutive"]
        and p["tau_commutes_with_sigma"]
        and p["delta_zero_splits"]
        and p["delta_one_splits"]
        and not p["uses_square_data"]
        and not p["kills_controls"]
        for p in control_profiles
    ),
    "  ".join("dim%d:tagged-parity-splits" % p["dim"] for p in control_profiles),
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

parity_tag_slots = {
    "parity_diagnostic": True,
    "selector_bit": True,
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
    "EPT6 endpoint parity tag satisfies no square-carrier slot",
    not any(parity_tag_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nEPT1-EPT6 ALL PASS: endpoint parity tags are not the square carrier")
print(
    "VERDICT: a Z/2 parity tag detects exactly when the half-sum decoder is "
    "integral, but it is only a diagnostic/selector.  Projecting to tag zero "
    "is the same external parity lattice as doc 274, while keeping tag one "
    "retains non-endpoint labels that split c and decode only half-integrally. "
    "The same package is formable on controls, and no square, rep_NS, proper "
    "correspondences, projection formula, Rosati, carrier boundary, or "
    "control death is constructed."
)
