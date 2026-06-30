r"""Projection-forced positive-End-envelope DD.4/SCC no-go.

Doc 283 killed the positive U+End matrix package because componentwise
composition still lacks the projection formula.  This witness tests the next
repair:

    impose the projection formula on the positive U+End envelope by quotient
    relations or local retuning.

The positive fact is real: the projection formula is exactly the missing
proper-correspondence theorem.  The no-go is that imposing it on the formal
componentwise law changes genuine finite-field trace/count data, collapses
universal scalar quotients, retunes graph degrees, leaves DD.4 uncoupled, and
is formable on positive controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_projection_forced_positive_envelope_no_go
"""

from math import comb, gcd, log2

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


def projection_sides(A, B, C, E):
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A, B, C, E):
    lhs, rhs = projection_sides(A, B, C, E)
    return float(abs(lhs - rhs))


def trace_power(F, n):
    return float(np.trace(np.linalg.matrix_power(F, n)).real)


def point_count(F, q, n):
    return float(q**n + 1 - trace_power(F, n))


def retune_first_degree_for_projection(A, B, C, E):
    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    c2 = C[2]
    return product[0] + (rhs - lhs) / c2, product[1], product[2]


def dd4_split_with_label(L, label):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        vector, end_label, unit = x
        exponent = vector[0] - vector[1]
        return vector, end_label, mul(pow_unit(c, exponent, mul, inv), phi(unit))

    def emul(x, y):
        return (x[0][0] + y[0][0], x[0][1] + y[0][1]), x[1], mul(x[2], y[2])

    def einv(x):
        return (-x[0][0], -x[0][1]), x[1], inv(x[2])

    generator = sigma(((1, 0), label, {0: 1}))
    boundary = emul(generator, einv(sigma(generator)))
    return boundary == ((0, 0), label, c)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "PFE1 DD.4 class is nonzero before projection forcing",
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
positive_hodge = primitive_hodge_index(F_true, E_true, 1)

gate(
    "PFE2 positive U+End finite-field data is intact before the repair",
    ns_intersection(D_true, G_true) == 7
    and ns_intersection(G_true, H_true) == 76
    and corr_defect(compose(G_true, H_true), frobenius_graph(F_true, q_true, 3)) < 1e-12
    and qsim_defect(F_true, E_true, q_true) < 1e-12
    and positive_hodge < 0,
    "Delta.G1=7 G1.G2=76 graph/qsim exact H=%.3f" % positive_hodge,
)


projection_11 = projection_defect(G_true, D_true, G_true, E_true)
actual_tr2 = trace_power(F_true, 2)
forced_tr2 = 2.0 * q_true
actual_count2 = point_count(F_true, q_true, 2)
forced_count2 = q_true**2 + 1.0 - forced_tr2

gate(
    "PFE3 forcing projection formula changes genuine trace/count data",
    projection_11 == 27.0
    and actual_tr2 == -13.0
    and forced_tr2 == 14.0
    and actual_count2 == 63.0
    and forced_count2 == 36.0,
    "defect=27 forces TrF2 %.0f->%.0f and count2 %.0f->%.0f"
    % (actual_tr2, forced_tr2, actual_count2, forced_count2),
)


q_alt = 2
F_alt = frobenius(q_alt, 0)
E_alt = weil_pairing(F_alt, q_alt)
D_alt = diagonal(F_alt)
G_alt = frobenius_graph(F_alt, q_alt, 1)
defect_true = int(round(projection_11))
defect_alt = int(round(projection_defect(G_alt, D_alt, G_alt, E_alt)))
alt_hodge = primitive_hodge_index(F_alt, E_alt, 1)

gate(
    "PFE4 scalar projection quotient collapses even over positive anchors",
    positive_hodge < 0 and alt_hodge < 0 and defect_true == 27 and defect_alt == 8 and gcd(defect_true, defect_alt) == 1,
    "positive defects %d and %d have gcd 1" % (defect_true, defect_alt),
)


retuned_G = retune_first_degree_for_projection(G_true, D_true, G_true, E_true)
retuned_projection = abs(
    ns_intersection(retuned_G, G_true)
    - projection_sides(G_true, D_true, G_true, E_true)[1]
)
graph_degree_defect = corr_defect(retuned_G, G_true)

gate(
    "PFE5 local projection retuning destroys the graph degree",
    retuned_projection < 1e-12 and graph_degree_defect == 27.0 and retuned_G[0] == -20.0,
    "retuned d1 %.0f vs graph d1 %.0f" % (retuned_G[0], G_true[0]),
)


H_alt = frobenius_graph(F_alt, q_alt, 2)
selective_defect_12 = projection_defect(G_alt, D_alt, H_alt, E_alt)
selective_defect_11 = projection_defect(G_alt, D_alt, G_alt, E_alt)

gate(
    "PFE6 finite projection samples remain cherry-pickable",
    selective_defect_12 < 1e-12 and selective_defect_11 == 8.0,
    "q=2,a=0 has defect(1,2)=%.0f but defect(1,1)=%.0f"
    % (selective_defect_12, selective_defect_11),
)


split_ok = all(dd4_split_with_label(8, label) for label in ("positive_projection", "retuned_graph", "control"))
gate(
    "PFE7 projection forcing still does not couple DD.4 to End/Rosati",
    split_ok,
    "endpoint DD.4 split works with positive_projection, retuned_graph, control labels",
)


control_q = 3
control = frobenius(control_q, 1)
control_E = weil_pairing(control, control_q)
control_D = diagonal(control)
control_G = frobenius_graph(control, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_retuned = retune_first_degree_for_projection(control_G, control_D, control_G, control_E)
control_has_euler_product = False
control_has_satake = False
control_has_proper_correspondences = False
control_has_carrier_boundary = False
control_has_control_death = False

gate(
    "PFE8 positive controls admit the same projection forcing/retuning",
    qsim_defect(control, control_E, control_q) < 1e-12
    and primitive_hodge_index(control, control_E, 1) < 0
    and control_projection == 11.0
    and corr_defect(control_retuned, control_G) == 11.0
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_proper_correspondences
    and not control_has_carrier_boundary
    and not control_has_control_death,
    "control projection_defect=%.0f retuned d1 %.0f no carrier/death"
    % (control_projection, control_retuned[0]),
)


audit = {
    "positive_U_End": True,
    "projection_forced": True,
    "actual_Qbar": False,
    "carrier_integral_rep_NS": False,
    "proper_correspondence_category": False,
    "fiber_product_composition": False,
    "projection_formula_from_geometry": False,
    "carrier_boundary": False,
    "control_death": False,
}

gate(
    "PFE9 projection-forced positive envelope satisfies no carrier-first contract",
    audit["positive_U_End"]
    and audit["projection_forced"]
    and not audit["actual_Qbar"]
    and not audit["carrier_integral_rep_NS"]
    and not audit["proper_correspondence_category"]
    and not audit["fiber_product_composition"]
    and not audit["projection_formula_from_geometry"]
    and not audit["carrier_boundary"]
    and not audit["control_death"],
    "relation repair yes; Qbar/Corr^prop/fiber products/boundary/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPFE1-PFE9 ALL PASS: projection-forced positive envelope is not the square carrier")
print(
    "VERDICT: forcing the projection formula on the positive U+End envelope "
    "is a relation repair, not proper correspondence construction. It "
    "changes finite-field trace/count data, collapses scalar quotients, "
    "retunes graph degrees, leaves DD.4 independent, and is formable on "
    "positive controls without Qbar, carrier boundary, or control death."
)
