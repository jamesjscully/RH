r"""Qbar-shell positive-End-envelope no-go.

Doc 285 killed free fiber-product/projection cells on the positive U+End
envelope.  This witness tests the next stronger shortcut:

    add a named Qbar shell with p1,p2,dQ,Corr^prop,boundary localization,
    and control-death labels, but do not construct the carrier geometry.

The positive fact is that these are the right carrier-first names.  The no-go
is that a name shell can satisfy a naive checklist while the semantic
projection defect, DD.4 obstruction, endpoint-map ambiguity, and control
formability remain.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_shell_positive_envelope_no_go
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


REQUIRED_SLOTS = {
    "endpoint_integrality",
    "degree_maps",
    "rep_NS",
    "diagonal",
    "frobenius_graph",
    "fiber_product_composition",
    "projection_formula",
    "dd4_boundary_killing",
    "rosati_duality",
    "primitive_positive_sign",
    "control_death",
}


def naive_derive_slots(generators):
    """Name-level dependency graph; intentionally accepts declared labels."""

    generators = set(generators)
    slots = set()

    if {"Qbar", "p1", "p2", "integral_cycles", "proper_pushforward"} <= generators:
        slots |= {"endpoint_integrality", "degree_maps"}

    if {"Qbar", "Corr_prop", "integral_cycles", "intersection_pairing"} <= generators:
        slots |= {"rep_NS", "diagonal"}

    if {"Corr_prop", "fiber_products", "Frobenius_graph", "degree_maps"} <= generators | slots:
        slots |= {"frobenius_graph", "fiber_product_composition"}

    if {"Corr_prop", "proper_pushforward", "intersection_pairing", "fiber_product_composition"} <= generators | slots:
        slots.add("projection_formula")

    if {"dQ", "localization_sequence", "dd4_coefficients", "boundary_self_duality"} <= generators:
        slots.add("dd4_boundary_killing")

    if {"duality_functor", "diagonal", "rep_NS", "intersection_pairing"} <= generators | slots:
        slots.add("rosati_duality")

    if {"rosati_duality", "primitive_hodge_index", "frobenius_graph"} <= generators | slots:
        slots.add("primitive_positive_sign")

    if {"Qbar", "p1", "p2", "dQ", "Frobenius_graph", "control_death_guard"} <= generators:
        slots.add("control_death")

    return slots


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


def projection_sides(A, B, C, E):
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A, B, C, E):
    lhs, rhs = projection_sides(A, B, C, E)
    return float(abs(lhs - rhs))


def dd4_split_with_label(L, label):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        vector, shell_label, unit = x
        exponent = vector[0] - vector[1]
        return vector, shell_label, mul(pow_unit(c, exponent, mul, inv), phi(unit))

    def emul(x, y):
        return (x[0][0] + y[0][0], x[0][1] + y[0][1]), x[1], mul(x[2], y[2])

    def einv(x):
        return (-x[0][0], -x[0][1]), x[1], inv(x[2])

    generator = sigma(((1, 0), label, {0: 1}))
    boundary = emul(generator, einv(sigma(generator)))
    return boundary == ((0, 0), label, c)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "QBS1 DD.4 class is nonzero before Qbar-shell naming",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
G_true = frobenius_graph(F_true, q_true, 1)
H_true = frobenius_graph(F_true, q_true, 2)
G3_true = frobenius_graph(F_true, q_true, 3)
positive_hodge = primitive_hodge_index(F_true, E_true, 1)

gate(
    "QBS2 positive U+End finite-field anchor is intact before shelling",
    ns_intersection(D_true, G_true) == 7
    and ns_intersection(G_true, H_true) == 76
    and corr_defect(compose(G_true, H_true), G3_true) < 1e-12
    and qsim_defect(F_true, E_true, q_true) < 1e-12
    and positive_hodge < 0,
    "Delta.G1=7 G1.G2=76 G1oG2=G3 qsim exact H=%.3f" % positive_hodge,
)


shell_generators = {
    "Qbar",
    "Q",
    "dQ",
    "p1",
    "p2",
    "Corr_prop",
    "fiber_products",
    "integral_cycles",
    "proper_pushforward",
    "intersection_pairing",
    "Frobenius_graph",
    "localization_sequence",
    "dd4_coefficients",
    "boundary_self_duality",
    "duality_functor",
    "primitive_hodge_index",
    "control_death_guard",
}
naive_slots = naive_derive_slots(shell_generators)
represented_slots = set()

gate(
    "QBS3 a Qbar shell passes name-level CFC but constructs no slots",
    REQUIRED_SLOTS <= naive_slots and represented_slots == set(),
    "naive slots=%d, represented slots=%d" % (len(naive_slots), len(represented_slots)),
)


semantic_projection = projection_defect(G_true, D_true, G_true, E_true)
shell_declared_projection = True
shell_projection_from_geometry = False

gate(
    "QBS4 shell projection theorem is declared while semantic defect remains",
    shell_declared_projection
    and semantic_projection == 27.0
    and not shell_projection_from_geometry,
    "declared projection yes; semantic defect %.0f; geometry proof no" % semantic_projection,
)


base_c_nonboundary = all(p["c_nonboundary"] and p["res1_c"] == 1 for p in profiles)
shell_declares_boundary_kill = True
shell_boundary_map_constructed = False
split_labels_ok = all(
    dd4_split_with_label(8, label)
    for label in ("qbar_shell_boundary", "declared_localization", "control_shell")
)

gate(
    "QBS5 shell boundary kills DD.4 only by declaration or free split",
    base_c_nonboundary
    and shell_declares_boundary_kill
    and not shell_boundary_map_constructed
    and split_labels_ok,
    "base [c] nonboundary with res1=1; declared boundary/free labels split c",
)


same_total_a = (10, F_true, 1)
same_total_b = (7, F_true, 4)
same_total = same_total_a[0] + same_total_a[2] == same_total_b[0] + same_total_b[2]
same_diagonal = ns_intersection(D_true, same_total_a) == ns_intersection(D_true, same_total_b)
endpoint_probes_differ = same_total_a[0] != same_total_b[0] and same_total_a[2] != same_total_b[2]

gate(
    "QBS6 shell p1,p2 labels do not force carrier-native endpoint maps",
    same_total and same_diagonal and endpoint_probes_differ,
    "(10,F,1) and (7,F,4) have total 11 and Delta pairing 10 but different endpoints",
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_shell_slots = naive_derive_slots(shell_generators)
control_projection = projection_defect(control_G, control_D, control_G, control_E)

gate(
    "QBS7 positive controls admit the same Qbar shell",
    qsim_defect(control_F, control_E, control_q) < 1e-12
    and primitive_hodge_index(control_F, control_E, 1) < 0
    and REQUIRED_SLOTS <= control_shell_slots
    and control_projection == 11.0,
    "control has positive matrix data and naive shell slots; semantic projection defect %.0f"
    % control_projection,
)


audit = {
    "named_Qbar": True,
    "named_p1_p2": True,
    "named_dQ": True,
    "named_Corr_prop": True,
    "actual_Qbar": False,
    "actual_p1_p2": False,
    "proper_pullbacks": False,
    "projection_formula_from_geometry": False,
    "boundary_localization_from_carrier": False,
    "carrier_rosati": False,
    "control_death": False,
}

gate(
    "QBS8 Qbar shell satisfies no construction-grade carrier contract",
    audit["named_Qbar"]
    and audit["named_p1_p2"]
    and audit["named_dQ"]
    and audit["named_Corr_prop"]
    and not audit["actual_Qbar"]
    and not audit["actual_p1_p2"]
    and not audit["proper_pullbacks"]
    and not audit["projection_formula_from_geometry"]
    and not audit["boundary_localization_from_carrier"]
    and not audit["carrier_rosati"]
    and not audit["control_death"],
    "names yes; constructed Qbar/p1p2/pullbacks/boundary/Rosati/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nQBS1-QBS8 ALL PASS: Qbar shell positive envelope is not the square carrier")
print(
    "VERDICT: naming Qbar, p1,p2,dQ,Corr^prop, localization, and control death "
    "around the positive U+End envelope can pass a name-level checklist, but "
    "it constructs no carrier. The projection defect and DD.4 obstruction "
    "remain semantic, endpoint maps are still labels, and positive controls "
    "admit the same shell."
)
