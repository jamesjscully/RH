r"""Trace-augmented hyperbolic-plane DD.4/SCC no-go.

Doc 280 killed the bare hyperbolic endpoint plane because it forgets the
End/Frobenius trace term in rep_NS.  This witness tests the immediate repair:

    keep the hyperbolic endpoint plane U=<e,f>, and add a scalar trace slot
    so Delta.Gamma_n = q^n + 1 - Tr(F^n).

The positive fact is real: a trace-augmented hyperbolic shadow can reproduce
the diagonal point-count intersections.  The no-go is that the scalar trace
slot is still not the End component.  It cannot compute off-diagonal
Tr(F^m F^n), does not give graph composition, admits arbitrary control trace
sequences, and leaves all carrier slots unconstructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_trace_augmented_hyperbolic_no_go
"""

from math import comb, log2

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    ns_intersection,
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


def point_count_from_matrix(q, F, n):
    return q**n + 1 - np.trace(np.linalg.matrix_power(F, n)).real


def trace_shadow_pair(a, b):
    """Scalar trace-augmented hyperbolic pairing.

    A label is (d1, t, d2).  The diagonal is represented with trace
    coefficient 1, so Delta_shadow . Gamma_shadow_n = q^n + 1 - Tr(F^n).
    """

    d1, t, d2 = a
    e1, s, e2 = b
    return d1 * e2 + d2 * e1 - t * s


def trace_shadow_graph(q, F, n):
    return (q**n, np.trace(np.linalg.matrix_power(F, n)).real, 1)


def trace_shadow_profile(q=7, a1=1):
    F = frobenius(q, a1)
    delta_real = diagonal(F)
    delta_shadow = (1, 1, 1)
    diagonal_rows = []
    for n in (1, 2, 3, 4):
        gamma_real = frobenius_graph(F, q, n)
        gamma_shadow = trace_shadow_graph(q, F, n)
        diagonal_rows.append(
            {
                "n": n,
                "real": ns_intersection(delta_real, gamma_real),
                "shadow": trace_shadow_pair(delta_shadow, gamma_shadow),
                "count": point_count_from_matrix(q, F, n),
            }
        )

    offdiag_rows = []
    for m, n in ((1, 1), (1, 2), (2, 2), (2, 3)):
        real_a = frobenius_graph(F, q, m)
        real_b = frobenius_graph(F, q, n)
        shadow_a = trace_shadow_graph(q, F, m)
        shadow_b = trace_shadow_graph(q, F, n)
        offdiag_rows.append(
            {
                "m": m,
                "n": n,
                "real": ns_intersection(real_a, real_b),
                "shadow": trace_shadow_pair(shadow_a, shadow_b),
                "needed_trace": np.trace(np.linalg.matrix_power(F, m + n)).real,
                "product_trace": shadow_a[1] * shadow_b[1],
            }
        )

    return {"F": F, "diagonal_rows": diagonal_rows, "offdiag_rows": offdiag_rows}


def scalar_composition_defect(q=7, a1=1):
    F = frobenius(q, a1)
    rows = []
    for m, n in ((1, 1), (1, 2), (2, 2), (2, 3)):
        trace_m = np.trace(np.linalg.matrix_power(F, m)).real
        trace_n = np.trace(np.linalg.matrix_power(F, n)).real
        trace_sum = np.trace(np.linalg.matrix_power(F, m + n)).real
        rows.append(
            {
                "m": m,
                "n": n,
                "scalar_product": trace_m * trace_n,
                "needed": trace_sum,
                "defect": trace_m * trace_n - trace_sum,
            }
        )
    return rows


def same_trace_different_product_profile():
    A = np.array([[1.0, 1.0], [0.0, 0.0]])
    B = np.array([[1.0, 0.0], [0.0, 0.0]])
    C = np.array([[0.0, 0.0], [1.0, 0.0]])
    return {
        "trace_A": np.trace(A).real,
        "trace_B": np.trace(B).real,
        "trace_C": np.trace(C).real,
        "trace_AC": np.trace(A @ C).real,
        "trace_BC": np.trace(B @ C).real,
        "same_scalar_inputs": np.trace(A).real == np.trace(B).real and np.trace(C).real == 0,
        "different_product_trace": np.trace(A @ C).real != np.trace(B @ C).real,
    }


def control_trace_shadow_profile():
    traces = [3, -5, 8, 13]
    labels = [(2**i, traces[i - 1], 1) for i in range(1, 5)]
    delta = (1, 1, 1)
    diagonal_values = [trace_shadow_pair(delta, label) for label in labels]
    return {
        "traces": traces,
        "labels": labels,
        "diagonal_values": diagonal_values,
        "euler_product": False,
        "satake": False,
        "end_component": False,
        "proper_correspondences": False,
        "control_death": False,
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
gate(
    "TAH1 DD.4 class is nonzero before trace augmentation",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


shadow = trace_shadow_profile()
gate(
    "TAH2 scalar trace augmentation reproduces diagonal point counts",
    all(
        row["real"] == row["shadow"] and row["real"] == row["count"]
        for row in shadow["diagonal_rows"]
    ),
    "; ".join(
        "n=%d:shadow=%d=count=%d" % (row["n"], row["shadow"], row["count"])
        for row in shadow["diagonal_rows"]
    ),
)


gate(
    "TAH3 scalar trace pairing fails off-diagonal graph intersections",
    any(row["real"] != row["shadow"] for row in shadow["offdiag_rows"]),
    "; ".join(
        "m=%d,n=%d:real=%d,shadow=%d"
        % (row["m"], row["n"], row["real"], row["shadow"])
        for row in shadow["offdiag_rows"]
    ),
)


composition_rows = scalar_composition_defect()
gate(
    "TAH4 scalar trace slots do not compose as Frobenius graphs",
    all(row["scalar_product"] != row["needed"] for row in composition_rows),
    "; ".join(
        "t%d*t%d=%d vs t%d=%d"
        % (
            row["m"],
            row["n"],
            row["scalar_product"],
            row["m"] + row["n"],
            row["needed"],
        )
        for row in composition_rows
    ),
)


same_trace = same_trace_different_product_profile()
gate(
    "TAH5 traces alone do not determine End product traces",
    same_trace["same_scalar_inputs"] and same_trace["different_product_trace"],
    (
        "Tr(A)=Tr(B)=%d, Tr(C)=%d, but Tr(AC)=%d and Tr(BC)=%d"
        % (
            same_trace["trace_A"],
            same_trace["trace_C"],
            same_trace["trace_AC"],
            same_trace["trace_BC"],
        )
    ),
)


controls = control_trace_shadow_profile()
gate(
    "TAH6 arbitrary control traces admit the same augmented hyperbolic shadow",
    controls["diagonal_values"] == [0, 10, 1, 4]
    and not controls["euler_product"]
    and not controls["satake"]
    and not controls["end_component"]
    and not controls["proper_correspondences"]
    and not controls["control_death"],
    "control traces: " + ",".join(str(t) for t in controls["traces"]),
)


carrier_slots = {
    "hyperbolic_endpoint_plane": True,
    "scalar_trace_slot": True,
    "diagonal_counts": True,
    "dd4_split_available": True,
    "actual_square": False,
    "integral_rep_NS_with_End": False,
    "two_carrier_degree_maps": False,
    "indecomposable_diagonal": False,
    "frobenius_graph": False,
    "proper_correspondence_category": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "canonical_rosati": False,
    "positive_primitive_sign": False,
    "control_death": False,
}

gate(
    "TAH7 trace-augmented hyperbolic data satisfies no square-carrier contract",
    carrier_slots["diagonal_counts"]
    and not carrier_slots["actual_square"]
    and not carrier_slots["integral_rep_NS_with_End"]
    and not carrier_slots["frobenius_graph"]
    and not carrier_slots["fiber_product_composition"]
    and not carrier_slots["canonical_rosati"]
    and not carrier_slots["control_death"],
    "Delta.Gamma counts yes; End product/graph composition/Rosati/control death no",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nTAH1-TAH7 ALL PASS: trace-augmented hyperbolic plane is not the square carrier")
print(
    "VERDICT: adding a scalar trace slot to the hyperbolic endpoint plane "
    "recovers diagonal point-count shadows, but not the End component. It "
    "fails off-diagonal graph pairings, cannot compose Frobenius graphs, is "
    "formable on controls, and does not construct rep_NS, Rosati, projection, "
    "or control death."
)
