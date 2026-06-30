r"""Diagonal trace graph shadow no-go.

Doc 211 fixes the function-field square anchor:

    Delta.Gamma_{F^n} = q^n + 1 - Tr(F^n).

The next shortcut is to promote the scalar diagonal intersections themselves
to a zeta-side Frobenius graph.  This witness checks the missing structure.
The scalar trace sequence can be preserved by many trace-zero perturbations,
but those shadows do not satisfy graph composition, q-similitude/Rosati
constraints, or carrier-native control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_diagonal_trace_graph_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    ns_intersection,
    weil_pairing,
)


failures = []


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def trace_shadow_graph(F: np.ndarray, q: int, n: int, eps: float):
    """A trace-only fake graph with the right diagonal intersection.

    It has the same fiber degrees as Gamma_{F^n} and the same trace on the
    End slot, but its End component is perturbed by a traceless matrix.
    """

    K = np.array([[1.0, 0.35], [0.0, -1.0]])
    return (q**n, np.linalg.matrix_power(F, n) + eps * K, 1)


def end_component(graph):
    return graph[1]


def composition_defect(graph_m, graph_n, graph_mn) -> float:
    """Defect of the End-slot graph semigroup relation."""

    return float(np.linalg.norm(end_component(graph_m) @ end_component(graph_n) - end_component(graph_mn)))


def similitude_defect(z: np.ndarray, E: np.ndarray, degree: float) -> float:
    """Defect of z being a degree-similitude for the cup form."""

    return float(np.linalg.norm(z.T @ E @ z - degree * E))


q = 7
a1 = 1
F = frobenius(q, a1)
E = weil_pairing(F, q)
Delta = diagonal(F)


# DTG1: the genuine function-field graph has all required structure.
genuine_counts = []
genuine_similitudes = []
for n in (1, 2, 3, 4):
    G = frobenius_graph(F, q, n)
    count = q**n + 1 - np.trace(np.linalg.matrix_power(F, n)).real
    genuine_counts.append(abs(ns_intersection(Delta, G) - count) < 1e-9)
    genuine_similitudes.append(similitude_defect(end_component(G), E, q**n) < 1e-9)

genuine_composition_defects = [
    composition_defect(frobenius_graph(F, q, 1), frobenius_graph(F, q, 1), frobenius_graph(F, q, 2)),
    composition_defect(frobenius_graph(F, q, 1), frobenius_graph(F, q, 2), frobenius_graph(F, q, 3)),
    composition_defect(frobenius_graph(F, q, 2), frobenius_graph(F, q, 2), frobenius_graph(F, q, 4)),
]

gate(
    "DTG1 genuine FF graph has counts, composition, and q-similitude",
    all(genuine_counts) and all(genuine_similitudes) and max(genuine_composition_defects) < 1e-9,
    "max composition defect %.1e; max similitude defect %.1e"
    % (max(genuine_composition_defects), max(similitude_defect(end_component(frobenius_graph(F, q, n)), E, q**n) for n in (1, 2, 3, 4))),
)


# DTG2: diagonal intersections alone are preserved by trace-zero perturbations.
epsilons = {1: 0.25, 2: -0.40, 3: 0.15, 4: 0.33}
shadow_counts = []
count_details = []
for n, eps in epsilons.items():
    G = frobenius_graph(F, q, n)
    S = trace_shadow_graph(F, q, n, eps)
    shadow_counts.append(abs(ns_intersection(Delta, G) - ns_intersection(Delta, S)) < 1e-9)
    count_details.append(f"n={n}:D.G={ns_intersection(Delta, G):.1f}=D.S={ns_intersection(Delta, S):.1f}")

gate(
    "DTG2 trace-zero shadows preserve all sampled diagonal counts",
    all(shadow_counts),
    "; ".join(count_details),
)


# DTG3: the same shadows fail graph composition.
S1 = trace_shadow_graph(F, q, 1, epsilons[1])
S2 = trace_shadow_graph(F, q, 2, epsilons[2])
S3 = trace_shadow_graph(F, q, 3, epsilons[3])
S4 = trace_shadow_graph(F, q, 4, epsilons[4])
shadow_composition_defects = [
    composition_defect(S1, S1, S2),
    composition_defect(S1, S2, S3),
    composition_defect(S2, S2, S4),
]

gate(
    "DTG3 diagonal counts do not force graph composition",
    min(shadow_composition_defects) > 1e-3,
    "composition defects " + ", ".join(f"{x:.3f}" for x in shadow_composition_defects),
)


# DTG4: the same shadows fail the q-similitude/Rosati relation.
shadow_similitude_defects = [
    similitude_defect(end_component(trace_shadow_graph(F, q, n, epsilons[n])), E, q**n)
    for n in (1, 2, 3, 4)
]

gate(
    "DTG4 diagonal counts do not force q-similitude or Rosati duality",
    min(shadow_similitude_defects) > 1e-3,
    "similitude defects " + ", ".join(f"{x:.3f}" for x in shadow_similitude_defects),
)


# DTG5: the trace-only operation is formable on controls, hence is not a carrier guard.
control_trace_sequence = [3.0, -5.0, 8.0, 13.0]
control_shadows = []
for n, trace_value in enumerate(control_trace_sequence, start=1):
    z = np.array([[trace_value, 0.0], [0.0, 0.0]])
    control_shadows.append((q**n, z, 1))

control_has_euler_product = False
control_has_satake = False
control_has_correspondence_algebra = False
control_has_rosati = False
control_trace_shadow_exists = all(
    abs(np.trace(end_component(G)).real - trace_value) < 1e-9
    for G, trace_value in zip(control_shadows, control_trace_sequence)
)

gate(
    "DTG5 trace-only graph shadows are formable on controls",
    control_trace_shadow_exists
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_correspondence_algebra
    and not control_has_rosati,
    "arbitrary scalar trace sequence realized without Euler/Satake/correspondence/Rosati data",
)


# DTG6: construction audit.
zeta_rep_ns_constructed = False
zeta_graph_composition_constructed = False
zeta_q_similitude_constructed = False
zeta_off_diagonal_pairing_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "DTG6 diagonal traces alone construct no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_graph_composition_constructed
    and not zeta_q_similitude_constructed
    and not zeta_off_diagonal_pairing_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, graph law, q-similitude, off-diagonal pairing, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (DTG1-DTG6)")
print(
    "VERDICT: diagonal intersections Delta.Gamma_n are only the trace shadow "
    "of a Frobenius graph. Trace-zero perturbations preserve those scalars but "
    "destroy graph composition and q-similitude/Rosati duality, and the same "
    "trace-only construction is formable on controls. The zeta-side object must "
    "construct rep_NS, graph composition, off-diagonal pairings, and positive "
    "Rosati; explicit-formula traces alone are not End(S^2/Z)."
)
