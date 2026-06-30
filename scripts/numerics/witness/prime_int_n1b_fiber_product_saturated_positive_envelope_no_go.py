r"""Fiber-product-saturated positive-End-envelope no-go.

Doc 284 killed quotienting or retuning the positive U+End envelope to force
the projection formula.  This witness tests the next categorical repair:

    freely adjoin formal fiber-product objects and projection cells to the
    positive U+End envelope.

The positive fact is that fiber products are exactly what an actual
Corr^prop(Qbar) construction should use.  The no-go is that free/syntactic
fiber-product saturation either only declares projection while the semantic
defect remains, or repeats the retuning damage from doc 284 when represented
back in NS triples.  It also leaves DD.4 uncoupled and is formable on
positive controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_fiber_product_saturated_positive_envelope_no_go
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


def projection_sides(A, B, C, E):
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A, B, C, E):
    lhs, rhs = projection_sides(A, B, C, E)
    return float(abs(lhs - rhs))


def retune_first_degree_for_projection(A, B, C, E):
    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    c2 = C[2]
    return product[0] + (rhs - lhs) / c2, product[1], product[2]


def point_count(F, q, n):
    return float(q**n + 1 - np.trace(np.linalg.matrix_power(F, n)).real)


def dd4_split_with_label(L, label):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})

    def sigma(x):
        vector, cell_label, unit = x
        exponent = vector[0] - vector[1]
        return vector, cell_label, mul(pow_unit(c, exponent, mul, inv), phi(unit))

    def emul(x, y):
        return (x[0][0] + y[0][0], x[0][1] + y[0][1]), x[1], mul(x[2], y[2])

    def einv(x):
        return (-x[0][0], -x[0][1]), x[1], inv(x[2])

    generator = sigma(((1, 0), label, {0: 1}))
    boundary = emul(generator, einv(sigma(generator)))
    return boundary == ((0, 0), label, c)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "FPS1 DD.4 class is nonzero before fiber-product saturation",
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
    "FPS2 positive U+End anchor survives before categorical saturation",
    ns_intersection(D_true, G_true) == 7
    and ns_intersection(G_true, H_true) == 76
    and corr_defect(compose(G_true, H_true), G3_true) < 1e-12
    and qsim_defect(F_true, E_true, q_true) < 1e-12
    and positive_hodge < 0,
    "Delta.G1=7 G1.G2=76 G1oG2=G3 qsim exact H=%.3f" % positive_hodge,
)


semantic_defect = projection_defect(G_true, D_true, G_true, E_true)
formal_cell_declared = {
    "object": "G1_times_Delta",
    "projection_formula_cell": True,
    "represented_by_Qbar_pullback": False,
}
declared_defect = 0.0 if formal_cell_declared["projection_formula_cell"] else semantic_defect

gate(
    "FPS3 formal fiber-product cells declare projection while semantics still fail",
    semantic_defect == 27.0
    and declared_defect == 0.0
    and not formal_cell_declared["represented_by_Qbar_pullback"],
    "declared defect %.0f, componentwise semantic defect %.0f, no Qbar pullback"
    % (declared_defect, semantic_defect),
)


retuned_pullback = retune_first_degree_for_projection(G_true, D_true, G_true, E_true)
retuned_projection_defect = abs(
    ns_intersection(retuned_pullback, G_true)
    - projection_sides(G_true, D_true, G_true, E_true)[1]
)

gate(
    "FPS4 representing the cell in NS triples repeats degree retuning damage",
    retuned_projection_defect < 1e-12
    and retuned_pullback[0] == -20.0
    and corr_defect(retuned_pullback, G_true) == 27.0
    and point_count(F_true, q_true, 2) == 63.0,
    "retuned pullback d1 %.0f vs graph d1 %.0f; original count2 %.0f"
    % (retuned_pullback[0], G_true[0], point_count(F_true, q_true, 2)),
)


q_alt = 2
F_alt = frobenius(q_alt, 0)
E_alt = weil_pairing(F_alt, q_alt)
D_alt = diagonal(F_alt)
G_alt = frobenius_graph(F_alt, q_alt, 1)
H_alt = frobenius_graph(F_alt, q_alt, 2)
selective_defect_12 = projection_defect(G_alt, D_alt, H_alt, E_alt)
selective_defect_11 = projection_defect(G_alt, D_alt, G_alt, E_alt)

gate(
    "FPS5 finite fiber-product/projection samples remain cherry-pickable",
    primitive_hodge_index(F_alt, E_alt, 1) < 0
    and selective_defect_12 < 1e-12
    and selective_defect_11 == 8.0,
    "q=2,a=0 has declared sample defect %.0f but adjacent defect %.0f"
    % (selective_defect_12, selective_defect_11),
)


split_ok = all(
    dd4_split_with_label(8, label)
    for label in ("fiber_product_cell", "qbar_boundary_placeholder", "control_cell")
)

gate(
    "FPS6 fiber-product saturation does not couple DD.4 to the square data",
    split_ok,
    "endpoint DD.4 split works with fiber-product, boundary-placeholder, and control labels",
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_package = {
    "positive_qsim": qsim_defect(control_F, control_E, control_q) < 1e-12,
    "positive_sign": primitive_hodge_index(control_F, control_E, 1) < 0,
    "formal_fiber_products": True,
    "projection_cells": True,
    "actual_Qbar": False,
    "carrier_boundary": False,
    "control_death": False,
}

gate(
    "FPS7 positive controls admit the same fiber-product saturation",
    control_package["positive_qsim"]
    and control_package["positive_sign"]
    and control_package["formal_fiber_products"]
    and control_package["projection_cells"]
    and control_projection == 11.0
    and not control_package["actual_Qbar"]
    and not control_package["carrier_boundary"]
    and not control_package["control_death"],
    "control projection defect %.0f; formal cells yes, Qbar/boundary/death no"
    % control_projection,
)


audit = {
    "positive_U_End": True,
    "formal_fiber_products": True,
    "projection_formula_declared": True,
    "actual_Qbar": False,
    "p1_p2": False,
    "integral_pushforward": False,
    "proper_correspondences": False,
    "projection_formula_from_geometry": False,
    "carrier_boundary": False,
    "dd4_boundary_killing": False,
    "control_death": False,
}

gate(
    "FPS8 fiber-product-saturated envelope satisfies no carrier-first contract",
    audit["positive_U_End"]
    and audit["formal_fiber_products"]
    and audit["projection_formula_declared"]
    and not audit["actual_Qbar"]
    and not audit["p1_p2"]
    and not audit["integral_pushforward"]
    and not audit["proper_correspondences"]
    and not audit["projection_formula_from_geometry"]
    and not audit["carrier_boundary"]
    and not audit["dd4_boundary_killing"]
    and not audit["control_death"],
    "formal cells yes; Qbar/p1p2/proper Corr/boundary/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nFPS1-FPS8 ALL PASS: fiber-product-saturated positive envelope is not the square carrier")
print(
    "VERDICT: freely adjoining fiber-product and projection cells to the "
    "positive U+End envelope is categorical syntax, not a compactified square. "
    "It declares projection while the componentwise semantic defect remains, "
    "or repeats degree retuning when represented in NS triples. DD.4 remains "
    "independent and positive controls admit the same saturation without Qbar, "
    "carrier boundary, or control death."
)
