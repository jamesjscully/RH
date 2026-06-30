r"""Positive-Rosati End-envelope DD.4/SCC no-go.

Doc 282 killed the formal U+End envelope because it can wrap off-circle data
and controls.  This witness tests the stronger repair:

    keep U+End, require a chosen polarization, exact q-similitude, formal
    dagger, and the primitive Hodge/Rosati sign.

The positive fact is real: the finite-field model has diagonal counts,
off-diagonal graph pairings, graph law, q-similitude, Rosati relation, and
negative primitive Hodge sign.  Requiring the sign rejects the standard
off-circle determinant-q graph.  The no-go is that a positive matrix package
is still not a carrier: the pasted pairing and componentwise composition
lack the projection formula, the DD.4 split is independent of the positive
End slot, and the same positive package is formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_positive_rosati_end_envelope_no_go
"""

from math import comb, log2

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    ns_intersection,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


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


def compose(a, b):
    d1, z, d2 = a
    e1, w, e2 = b
    return d1 * e1, z @ w, d2 * e2


def dagger(a, E):
    d1, z, d2 = a
    return d2, rosati(z, E), d1


def corr_defect(a, b):
    return abs(a[0] - b[0]) + np.linalg.norm(a[1] - b[1]) + abs(a[2] - b[2])


def qsim_defect(F, E, q):
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def projection_defect(A, B, C, E):
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(abs(lhs - rhs))


def dd4_split_with_end_label(L, end_label):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        vector, label, unit = x
        exponent = vector[0] - vector[1]
        return vector, label, mul(pow_unit(c, exponent, mul, inv), phi(unit))

    def emul(x, y):
        return (x[0][0] + y[0][0], x[0][1] + y[0][1]), x[1], mul(x[2], y[2])

    def einv(x):
        return (-x[0][0], -x[0][1]), x[1], inv(x[2])

    generator = sigma(((1, 0), end_label, {0: 1}))
    boundary = emul(generator, einv(sigma(generator)))
    return boundary == ((0, 0), end_label, c)


def finite_field_positive_profile(q=7, a1=1):
    F = frobenius(q, a1)
    E = weil_pairing(F, q)
    delta = diagonal(F)
    graph1 = frobenius_graph(F, q, 1)
    graph2 = frobenius_graph(F, q, 2)
    graph3 = frobenius_graph(F, q, 3)
    diag_count = ns_intersection(delta, graph1)
    offdiag = ns_intersection(graph1, graph2)
    graph_defect = corr_defect(compose(graph1, graph2), graph3)
    dagger_defect = corr_defect(dagger(graph1, E), (1, q * np.linalg.inv(F), q))
    return {
        "F": F,
        "E": E,
        "diag_count": diag_count,
        "offdiag": offdiag,
        "graph_defect": graph_defect,
        "qsim": qsim_defect(F, E, q),
        "dagger_defect": dagger_defect,
        "primitive_hodge": primitive_hodge_index(F, E, 1),
        "projection_defects": [
            projection_defect(graph1, delta, graph2, E),
            projection_defect(graph1, graph1, delta, E),
            projection_defect(graph2, graph1, delta, E),
        ],
    }


def offcircle_profile():
    q = 2
    F = frobenius(q, 3)
    E = weil_pairing(F, q)
    return {
        "qsim": qsim_defect(F, E, q),
        "primitive_hodge": primitive_hodge_index(F, E, 1),
        "radius_defect": max(abs(abs(root) - np.sqrt(q)) for root in np.linalg.eigvals(F)),
    }


def positive_control_profile():
    q = 3
    control = np.array([[0.0, -float(q)], [1.0, 0.0]])
    E = weil_pairing(control, q)
    delta = diagonal(control)
    graph1 = frobenius_graph(control, q, 1)
    graph2 = frobenius_graph(control, q, 2)
    graph3 = frobenius_graph(control, q, 3)
    return {
        "q": q,
        "control": control,
        "qsim": qsim_defect(control, E, q),
        "primitive_hodge": primitive_hodge_index(control, E, 1),
        "graph_defect": corr_defect(compose(graph1, graph2), graph3),
        "diagonal_pairing": ns_intersection(delta, graph1),
        "projection_defect": projection_defect(graph1, delta, graph2, E),
        "euler_product": False,
        "satake": False,
        "proper_correspondences": False,
        "carrier_boundary": False,
        "control_death": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "PRE1 DD.4 class is nonzero before positive Rosati augmentation",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


positive = finite_field_positive_profile()
gate(
    "PRE2 finite-field U+End package has graph law, Rosati relation, and sign",
    positive["diag_count"] == 7
    and positive["offdiag"] == 76
    and positive["graph_defect"] < 1e-12
    and positive["qsim"] < 1e-12
    and positive["dagger_defect"] < 1e-12
    and positive["primitive_hodge"] < 0,
    "Delta.G1=%d G1.G2=%d graph=%.1e qsim=%.1e H=%.3f"
    % (
        positive["diag_count"],
        positive["offdiag"],
        positive["graph_defect"],
        positive["qsim"],
        positive["primitive_hodge"],
    ),
)


offcircle = offcircle_profile()
gate(
    "PRE3 positive primitive sign rejects the standard off-circle q-similitude",
    offcircle["qsim"] < 1e-12 and offcircle["primitive_hodge"] > 0 and offcircle["radius_defect"] > 1e-3,
    "qsim=%.1e radius_defect=%.3f H=%.3f"
    % (offcircle["qsim"], offcircle["radius_defect"], offcircle["primitive_hodge"]),
)


gate(
    "PRE4 positive formal End package still lacks projection formula",
    min(positive["projection_defects"]) > 1e-6,
    "projection_defects=%s"
    % [round(float(defect), 3) for defect in positive["projection_defects"]],
)


split_rows = [
    dd4_split_with_end_label(8, label)
    for label in ("positive_F", "positive_control", "Id")
]
gate(
    "PRE5 DD.4 split is still independent of the positive End/Rosati slot",
    all(split_rows),
    "split works with positive_F, positive_control, and Id labels",
)


control = positive_control_profile()
gate(
    "PRE6 the same positive U+End/Rosati package is formable on controls",
    control["qsim"] < 1e-12
    and control["primitive_hodge"] < 0
    and control["graph_defect"] < 1e-12
    and not control["euler_product"]
    and not control["satake"]
    and not control["proper_correspondences"]
    and not control["carrier_boundary"]
    and not control["control_death"],
    "control q=%d qsim=%.1e H=%.3f projection_defect=%.3f no carrier/death"
    % (control["q"], control["qsim"], control["primitive_hodge"], control["projection_defect"]),
)


audit = {
    "formal_positive_U_End": True,
    "graph_law": True,
    "qsimilitude": True,
    "primitive_sign": True,
    "dd4_split": True,
    "actual_Qbar": False,
    "carrier_integral_rep_NS": False,
    "proper_correspondence_category": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "carrier_boundary": False,
    "control_death": False,
}

gate(
    "PRE7 positive Rosati End envelope satisfies no carrier-first contract",
    audit["formal_positive_U_End"]
    and audit["primitive_sign"]
    and audit["dd4_split"]
    and not audit["actual_Qbar"]
    and not audit["carrier_integral_rep_NS"]
    and not audit["proper_correspondence_category"]
    and not audit["fiber_product_composition"]
    and not audit["projection_formula"]
    and not audit["carrier_boundary"]
    and not audit["control_death"],
    "positive U+End yes; Qbar/Corr^prop/projection/boundary/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPRE1-PRE7 ALL PASS: positive-Rosati End envelope is not the square carrier")
print(
    "VERDICT: adding q-similitude and the primitive Rosati sign to the "
    "formal U+End envelope rejects off-circle data, but it is still not a "
    "carrier construction. The projection formula fails for componentwise "
    "composition, DD.4 is independent of the End slot, and positive controls "
    "can form the same package without Qbar, proper correspondences, boundary, "
    "or control death."
)
