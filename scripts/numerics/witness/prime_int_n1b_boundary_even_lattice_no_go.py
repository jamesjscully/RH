r"""Boundary-even-lattice parity DD.4/SCC no-go.

Doc 278 left a precise defect: oriented boundary incidence gives the
difference direction, but total plus difference decodes endpoints integrally
only on the same-parity sublattice.  This witness tests the next repair:
claim that a boundary intersection/even-lattice condition forces that parity.

The positive fact is real: the quadratic parity q=s^2-a^2 is even exactly on
the same-parity total/difference lattice, where half-sum decoding is integral
and the DD.4 split works.  The no-go is that this is still an index-two
selector unless the square carrier constructs the lattice, rep_NS, graph,
Rosati, and control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_boundary_even_lattice_no_go
"""

from fractions import Fraction
from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[z]/z^(L+1); 1-units are dicts {power: 1}."""

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

    return mul, inv, phi


def to_vec(f, L):
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, L, mul):
    seen = {(0,) * L}
    queue = [(0,) * L]
    while queue:
        current = from_vec(queue.pop())
        for gen in gens:
            nxt = to_vec(mul(current, gen), L)
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


def h1_profile(L):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)
    ]
    norm_gens = [
        mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)
    ]
    coboundaries = closure(boundary_gens, L, mul)
    norm_image = closure(norm_gens, L, mul)
    z1_order = 2**L // len(norm_image)
    return {
        "L": L,
        "c": c,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


def same_parity(label):
    s, a = label
    return (s - a) % 2 == 0


def boundary_quadratic_even(label):
    s, a = label
    return (s * s - a * a) % 2 == 0


def decode(label):
    s, a = label
    return Fraction(s + a, 2), Fraction(s - a, 2)


def parity_lattice_profile(window=4):
    labels = [(s, a) for s in range(-window, window + 1) for a in range(-window, window + 1)]
    rows = []
    for label in labels:
        decoded = decode(label)
        integral = decoded[0].denominator == 1 and decoded[1].denominator == 1
        rows.append(
            {
                "label": label,
                "same_parity": same_parity(label),
                "quadratic_even": boundary_quadratic_even(label),
                "integral": integral,
            }
        )
    selected = [row["label"] for row in rows if row["quadratic_even"]]
    rejected = [row["label"] for row in rows if not row["quadratic_even"]]
    return {
        "rows": rows,
        "quadratic_even_equals_same_parity": all(
            row["quadratic_even"] == row["same_parity"] for row in rows
        ),
        "quadratic_even_equals_integral_decode": all(
            row["quadratic_even"] == row["integral"] for row in rows
        ),
        "selected_count": len(selected),
        "rejected_count": len(rejected),
        "rejected_examples": [(0, 1), (11, 8), (10, 1)],
    }


def split_profile(L, label):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        (s, a), unit = x
        return (s, a), mul(pow_unit(c, a, mul, inv), phi(unit))

    def emul(x, y):
        return (x[0][0] + y[0][0], x[0][1] + y[0][1]), mul(x[1], y[1])

    def einv(x):
        return (-x[0][0], -x[0][1]), inv(x[1])

    generator = sigma((label, {0: 1}))
    boundary = emul(generator, einv(sigma(generator)))
    return {
        "label": label,
        "quadratic_even": boundary_quadratic_even(label),
        "integral_decode": decode(label),
        "boundary_is_c": boundary == ((0, 0), c),
    }


def mod2_selector_profile():
    classes = [(0, 0), (0, 1), (1, 0), (1, 1)]
    selectors = {
        "s=a": lambda s, a: (s + a) % 2 == 0,
        "s=0": lambda s, a: s % 2 == 0,
        "a=0": lambda s, a: a % 2 == 0,
    }
    return {
        name: [cls for cls in classes if pred(*cls)] for name, pred in selectors.items()
    }


def saturation_profile():
    invalid = [(0, 1), (11, 8), (10, 1)]
    return [
        {
            "label": label,
            "decoded": decode(label),
            "half_integral": decode(label)[0].denominator == 2
            or decode(label)[1].denominator == 2,
        }
        for label in invalid
    ]


def control_even_lattice_profile(dim):
    return {
        "dim": dim,
        "boundary_quadratic": True,
        "same_parity_selector": True,
        "dd4_split": True,
        "actual_square": False,
        "rep_NS": False,
        "frobenius_graph": False,
        "rosati": False,
        "control_death": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "BEL1 DD.4 class is nonzero before boundary parity selection",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


parity = parity_lattice_profile()
gate(
    "BEL2 boundary quadratic evenness is exactly same-parity decoding",
    parity["quadratic_even_equals_same_parity"]
    and parity["quadratic_even_equals_integral_decode"]
    and parity["selected_count"] == 41
    and parity["rejected_count"] == 40,
    f"selected={parity['selected_count']} rejected={parity['rejected_count']} in window",
)


valid_splits = [split_profile(L, (1, 1)) for L in (6, 8, 10, 12)]
gate(
    "BEL3 the even boundary lattice decodes endpoints and splits c",
    all(p["quadratic_even"] and p["boundary_is_c"] for p in valid_splits),
    "(s,a)=(1,1) is even, decodes to (1,0), and splits c",
)


invalid_splits = [split_profile(8, label) for label in parity["rejected_examples"]]
gate(
    "BEL4 excluded labels still split on the full register",
    all((not p["quadratic_even"]) for p in invalid_splits)
    and invalid_splits[0]["boundary_is_c"]
    and all(
        p["integral_decode"][0].denominator == 2 or p["integral_decode"][1].denominator == 2
        for p in invalid_splits
    ),
    "excluded labels: " + ", ".join(str(p["label"]) for p in invalid_splits),
)


selectors = mod2_selector_profile()
gate(
    "BEL5 mod-2 evenness is a selector among index-two boundary lattices",
    selectors["s=a"] == [(0, 0), (1, 1)]
    and selectors["s=0"] == [(0, 0), (0, 1)]
    and selectors["a=0"] == [(0, 0), (1, 0)],
    str(selectors),
)


saturation = saturation_profile()
gate(
    "BEL6 saturating the full boundary lattice makes half-integral endpoints",
    all(row["half_integral"] for row in saturation),
    "; ".join(f"{row['label']}->{row['decoded']}" for row in saturation),
)


controls = [control_even_lattice_profile(dim) for dim in (2, 4, 8)]
gate(
    "BEL7 the same even-lattice parity package is formable on controls",
    all(
        p["boundary_quadratic"]
        and p["same_parity_selector"]
        and p["dd4_split"]
        and not p["actual_square"]
        and not p["control_death"]
        for p in controls
    ),
    "control dimensions: " + ",".join(str(p["dim"]) for p in controls),
)


boundary_even_slots = {
    "boundary_quadratic": True,
    "same_parity_lattice": True,
    "dd4_split": True,
    "actual_square": False,
    "integral_rep_NS": False,
    "two_carrier_degree_maps": False,
    "proper_correspondence_category": False,
    "fiber_product_composition": False,
    "frobenius_graph": False,
    "projection_formula": False,
    "rosati_duality": False,
    "positive_primitive_sign": False,
    "control_death": False,
}

gate(
    "BEL8 boundary evenness satisfies no square-carrier contract",
    boundary_even_slots["dd4_split"]
    and not boundary_even_slots["actual_square"]
    and not boundary_even_slots["integral_rep_NS"]
    and not boundary_even_slots["frobenius_graph"]
    and not boundary_even_slots["rosati_duality"]
    and not boundary_even_slots["control_death"],
    "parity split yes; rep_NS/graph/composition/Rosati/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBEL1-BEL8 ALL PASS: boundary even lattice is not the square carrier")
print(
    "VERDICT: boundary evenness can package the same-parity condition needed "
    "for total/difference decoding, but without a carrier-native lattice theorem "
    "it is still an index-two selector. It does not construct rep_NS, graph "
    "composition, Rosati, projection, or control death."
)
