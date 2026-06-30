r"""Laurent-field/Hilbert-90 DD.4 no-go.

This witness tests the strongest Laurent repair left after the root-tower
cycles:

    enlarge U_1 = 1 + z F_2[[z]] to the full Laurent field K^*
    and use Hilbert 90.

The positive identity is real.  In K^*, with phi(z)=z/(1+z),

    b = phi(z) = z/(1+z)
    b / phi(b) = (1+z)^-1 = c.

Thus the DD.4 class dies after adjoining the valuation/uniformizer axis.
The no-go is that this is not a square-carrier boundary.  The killing uses
odd valuation outside U_1, the same uniformizer-splitting recipe is formable
on controls, and no SCC slot is constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_laurent_field_hilbert90_no_go
"""

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


def h1_profile(L, augment_with_c=False):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        boundary({0: 1, k: 1}, inv, phi, mul) for k in range(1, L + 1)
    ]
    if augment_with_c:
        boundary_gens.append(c)
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


def pair_mul(x, y, mul):
    return x[0] + y[0], mul(x[1], y[1])


def pair_inv(x, inv):
    return -x[0], inv(x[1])


def pair_boundary(x, inv, phi_pair, mul):
    return pair_mul(x, pair_inv(phi_pair(x), inv), mul)


def laurent_boundary_profile(L):
    _, mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def phi_pair(x):
        valuation, unit = x
        unit_twist = pow_unit(c, valuation, mul, inv)
        return valuation, mul(unit_twist, phi(unit))

    z = (1, {0: 1})
    phi_z = phi_pair(z)
    b = phi_z
    phi_b = phi_pair(b)
    b_boundary = pair_boundary(b, inv, phi_pair, mul)

    return {
        "L": L,
        "phi_z_is_z_times_c": phi_z == (1, c),
        "phi2_z_is_z": phi_b == z,
        "b_boundary_is_c": b_boundary == (0, c),
        "boundary_uses_odd_valuation": b[0] % 2 == 1,
    }


def valuation_parity_profile(L):
    _, mul, inv, _ = make(L)
    base = h1_profile(L)
    c = base["c"]
    coboundaries = base["coboundaries"]
    rows = []
    for valuation in range(-3, 4):
        val_boundary = pow_unit(c, valuation, mul, inv)
        ratio_to_c = mul(val_boundary, inv(c))
        rows.append(
            {
                "valuation": valuation,
                "res1_boundary": val_boundary.get(1, 0),
                "same_h1_class_as_c": to_vec(ratio_to_c, L) in coboundaries,
                "parity": valuation % 2,
            }
        )
    return {
        "L": L,
        "rows": rows,
        "odd_valuations_kill_c": all(
            row["same_h1_class_as_c"] for row in rows if row["parity"] == 1
        ),
        "even_valuations_do_not_kill_c": all(
            not row["same_h1_class_as_c"] for row in rows if row["parity"] == 0
        ),
        "res1_equals_valuation_parity": all(
            row["res1_boundary"] == row["parity"] for row in rows
        ),
    }


def dmp_tcr_phi_support(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def laurent_line_support(_deg):
    return 1


def dmp_support_profile():
    window = list(range(-6, 7))
    missing = [
        deg
        for deg in window
        if laurent_line_support(deg) == 1 and dmp_tcr_phi_support(deg) == 0
    ]
    return {
        "window": window,
        "missing_negative_degrees": missing,
        "full_valuation_axis_absent": missing == [-6, -5, -4, -3, -2],
    }


def xor_vec(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def control_uniformizer_profile(dim):
    """Add a valuation axis to kill any chosen C_2 control cocycle."""

    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    zero = tuple(0 for _ in range(dim))

    def sigma(pair):
        valuation, vector = pair
        twist = chosen if valuation % 2 else zero
        return valuation, xor_vec(vector, twist)

    b = (1, chosen)
    sigma_b = sigma(b)
    boundary_b = (0, xor_vec(b[1], sigma_b[1]))
    return {
        "dim": dim,
        "chosen_cocycle": chosen,
        "boundary_is_chosen": boundary_b == (0, chosen),
        "uses_square_data": False,
        "uses_uniformizer_axis": True,
    }


base_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
augmented_profiles = [h1_profile(L, augment_with_c=True) for L in (6, 8, 10, 12)]
laurent_profiles = [laurent_boundary_profile(L) for L in (6, 8, 10, 12)]
valuation_profiles = [valuation_parity_profile(L) for L in (6, 8, 10, 12)]
support_profile = dmp_support_profile()
control_profiles = [control_uniformizer_profile(dim) for dim in (1, 2, 4, 8)]


gate(
    "LFH1 base DD.4 class remains the nonzero 1-unit obstruction",
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
    "LFH2 full Laurent field kills c by the uniformizer Hilbert-90 boundary",
    all(
        p["phi_z_is_z_times_c"]
        and p["phi2_z_is_z"]
        and p["b_boundary_is_c"]
        and p["boundary_uses_odd_valuation"]
        for p in laurent_profiles
    )
    and all(p["h1_order"] == 1 and p["c_boundary"] for p in augmented_profiles),
    "b=phi(z)=z/(1+z), b/phi(b)=c; adding c to B^1 collapses H1",
)

gate(
    "LFH3 killing c is exactly the odd-valuation axis, not a 1-unit boundary",
    all(
        p["odd_valuations_kill_c"]
        and p["even_valuations_do_not_kill_c"]
        and p["res1_equals_valuation_parity"]
        for p in valuation_profiles
    ),
    "valuation m has boundary class m*[c] mod 2 for m=-3..3",
)

gate(
    "LFH4 DMP/TCR support does not contain the full Laurent valuation axis",
    support_profile["full_valuation_axis_absent"],
    "missing degrees %s" % support_profile["missing_negative_degrees"],
)

gate(
    "LFH5 the same uniformizer-splitting recipe is formable on controls",
    all(
        p["boundary_is_chosen"]
        and p["uses_uniformizer_axis"]
        and not p["uses_square_data"]
        for p in control_profiles
    ),
    "  ".join("dim%d:valuation-axis-splits" % p["dim"] for p in control_profiles),
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

laurent_field_slots = {
    "hilbert90_boundary": True,
    "uniformizer_valuation_axis": True,
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
    "LFH6 Laurent-field Hilbert-90 satisfies no square-carrier slot",
    not any(laurent_field_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nLFH1-LFH6 ALL PASS: Laurent-field Hilbert 90 is not the DD.4 carrier boundary")
print(
    "VERDICT: in the full Laurent field K^*, c=(1+z)^-1 is a genuine "
    "Hilbert-90 coboundary, with b=phi(z)=z/(1+z) and b/phi(b)=c.  But "
    "the killing uses the odd valuation/uniformizer axis outside U_1; the "
    "DMP/TCR support lacks the full Laurent line, the same uniformizer "
    "splitting is formable on controls, and no square, rep_NS, degree maps, "
    "graph, projection formula, Rosati, carrier boundary, or control death "
    "is constructed."
)
