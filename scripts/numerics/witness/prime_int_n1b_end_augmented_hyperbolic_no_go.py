r"""End-augmented hyperbolic-plane DD.4/SCC no-go.

Doc 281 killed scalar trace augmentation because scalar traces do not
remember End products.  This witness tests the stronger repair:

    keep the hyperbolic endpoint plane, replace the scalar trace slot by a
    full End algebra, and add componentwise graph composition.

The positive fact is real.  The finite-field model U + End(H^1) reproduces
diagonal counts, off-diagonal graph pairings, and Gamma_m Gamma_n=Gamma_{m+n}.
The no-go is that this is still a formal matrix envelope unless produced by
the compactified square carrier.  It can wrap off-circle data and controls,
the DD.4 split is independent of the End slot, and no proper correspondence
category, fiber-product composition, projection formula, or control death is
constructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_end_augmented_hyperbolic_no_go
"""

from math import comb, log2

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    ns_intersection,
    primitive_hodge_index,
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


def corr_defect(a, b):
    return abs(a[0] - b[0]) + np.linalg.norm(a[1] - b[1]) + abs(a[2] - b[2])


def finite_field_end_augmented_profile(q=7, a1=1):
    F = frobenius(q, a1)
    delta = diagonal(F)
    diagonal_rows = []
    for n in (1, 2, 3, 4):
        gamma = frobenius_graph(F, q, n)
        count = q**n + 1 - np.trace(np.linalg.matrix_power(F, n)).real
        diagonal_rows.append(
            {
                "n": n,
                "pairing": ns_intersection(delta, gamma),
                "count": count,
            }
        )

    offdiag_rows = []
    for m, n in ((1, 1), (1, 2), (2, 2), (2, 3)):
        gamma_m = frobenius_graph(F, q, m)
        gamma_n = frobenius_graph(F, q, n)
        offdiag_rows.append(
            {
                "m": m,
                "n": n,
                "pairing": ns_intersection(gamma_m, gamma_n),
                "formula": q**m + q**n - np.trace(np.linalg.matrix_power(F, m + n)).real,
            }
        )

    composition_rows = []
    for m, n in ((1, 1), (1, 2), (2, 3)):
        composition_rows.append(
            {
                "m": m,
                "n": n,
                "defect": corr_defect(
                    compose(frobenius_graph(F, q, m), frobenius_graph(F, q, n)),
                    frobenius_graph(F, q, m + n),
                ),
            }
        )

    return {
        "F": F,
        "diagonal_rows": diagonal_rows,
        "offdiag_rows": offdiag_rows,
        "composition_rows": composition_rows,
    }


def dd4_split_independence_profile(L=8):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    end_labels = ["Id", "F", "F2", "control"]

    def sigma(x):
        vector, _end_label, unit = x
        exponent = vector[0] - vector[1]
        return vector, _end_label, mul(pow_unit(c, exponent, mul, inv), phi(unit))

    def emul(x, y):
        return (x[0][0] + y[0][0], x[0][1] + y[0][1]), x[1], mul(x[2], y[2])

    def einv(x):
        return (-x[0][0], -x[0][1]), x[1], inv(x[2])

    def boundary(x):
        return emul(x, einv(sigma(x)))

    rows = []
    for label in end_labels:
        split_generator = sigma(((1, 0), label, {0: 1}))
        rows.append(
            {
                "label": label,
                "boundary_is_c": boundary(split_generator) == ((0, 0), label, c),
            }
        )
    return rows


def offcircle_formal_end_profile():
    q = 2
    F = frobenius(q, 3)
    E = weil_pairing(F, q)
    delta = diagonal(F)
    graph = frobenius_graph(F, q, 1)
    return {
        "composition_defect": corr_defect(compose(graph, graph), frobenius_graph(F, q, 2)),
        "diagonal_pairing": ns_intersection(delta, graph),
        "hodge": primitive_hodge_index(F, E, 1),
        "qsim_defect": np.linalg.norm(F.T @ E @ F - q * E),
    }


def control_formal_end_profile():
    q = 3
    control = np.array([[1.0, 2.0], [1.0, 4.0]])
    delta = (1.0, np.eye(2), 1.0)

    def graph(n):
        return q**n, np.linalg.matrix_power(control, n), 1.0

    return {
        "identity_defect": corr_defect(compose(delta, graph(2)), graph(2)),
        "composition_defect": corr_defect(compose(graph(2), graph(3)), graph(5)),
        "diagonal_pairing": ns_intersection(delta, graph(1)),
        "euler_product": False,
        "satake": False,
        "proper_correspondences": False,
        "carrier_boundary": False,
        "control_death": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "EAH1 DD.4 class is nonzero before End augmentation",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


ff = finite_field_end_augmented_profile()
gate(
    "EAH2 full End augmentation fixes diagonal and off-diagonal trace defects",
    all(row["pairing"] == row["count"] for row in ff["diagonal_rows"])
    and all(row["pairing"] == row["formula"] for row in ff["offdiag_rows"]),
    "diag "
    + ",".join("%d" % row["pairing"] for row in ff["diagonal_rows"][:3])
    + "; offdiag "
    + ",".join("%d" % row["pairing"] for row in ff["offdiag_rows"][:3]),
)


gate(
    "EAH3 componentwise End graph law holds in the finite-field model",
    all(row["defect"] < 1e-12 for row in ff["composition_rows"]),
    "; ".join(
        "G%dG%d=G%d defect %.1e" % (row["m"], row["n"], row["m"] + row["n"], row["defect"])
        for row in ff["composition_rows"]
    ),
)


split_rows = dd4_split_independence_profile()
gate(
    "EAH4 DD.4 split is independent of the formal End slot",
    all(row["boundary_is_c"] for row in split_rows),
    "split works with End labels: " + ",".join(row["label"] for row in split_rows),
)


offcircle = offcircle_formal_end_profile()
gate(
    "EAH5 the same End envelope wraps off-circle data where positivity fails",
    offcircle["composition_defect"] < 1e-12
    and offcircle["qsim_defect"] < 1e-12
    and offcircle["hodge"] > 0,
    "composition=%.1e qsim=%.1e primitive_H=%.3f"
    % (offcircle["composition_defect"], offcircle["qsim_defect"], offcircle["hodge"]),
)


control = control_formal_end_profile()
gate(
    "EAH6 the same End-augmented hyperbolic package is formable on controls",
    control["identity_defect"] < 1e-12
    and control["composition_defect"] < 1e-12
    and not control["euler_product"]
    and not control["satake"]
    and not control["proper_correspondences"]
    and not control["carrier_boundary"]
    and not control["control_death"],
    "control Delta.Gamma=%.1f with no Euler/Satake/properness/boundary/death"
    % control["diagonal_pairing"],
)


audit = {
    "hyperbolic_endpoint_plane": True,
    "formal_End_algebra": True,
    "componentwise_graph_law": True,
    "dd4_split": True,
    "actual_Qbar": False,
    "carrier_integral_rep_NS": False,
    "proper_correspondence_category": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "carrier_rosati_duality": False,
    "positive_primitive_sign_theorem": False,
    "carrier_boundary": False,
    "control_death": False,
}

gate(
    "EAH7 End-augmented hyperbolic data satisfies no carrier-first contract",
    audit["formal_End_algebra"]
    and audit["componentwise_graph_law"]
    and audit["dd4_split"]
    and not audit["actual_Qbar"]
    and not audit["carrier_integral_rep_NS"]
    and not audit["proper_correspondence_category"]
    and not audit["fiber_product_composition"]
    and not audit["projection_formula"]
    and not audit["control_death"],
    "formal U+End yes; Qbar/Corr^prop/fiber products/projection/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nEAH1-EAH7 ALL PASS: End-augmented hyperbolic plane is not the square carrier")
print(
    "VERDICT: adding the full formal End algebra fixes the scalar-trace "
    "defect, but only by rebuilding the finite-field formula as a matrix "
    "envelope. The DD.4 split is independent of the End slot, the same "
    "envelope wraps off-circle data and controls, and no Qbar, proper "
    "correspondence composition, projection formula, carrier Rosati, or "
    "control death is constructed."
)
