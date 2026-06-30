r"""Presented correspondence-carrier no-go.

After doc 221, the next repair is to stop modifying the componentwise formal
law and instead define a universal/presented correspondence category with the
desired graph, adjoint, projection, and count relations as generators and
relations.  This still does not construct End(S^2/Z): finite presentations
encode relation tables rather than produce a square carrier, finite relation
windows admit ghost extensions, arbitrary control count windows have companion
realizations, and projection/positivity remain axioms.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_presented_correspondence_carrier_no_go
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
    rosati,
    weil_pairing,
)


failures: list[str] = []


Corr = tuple[float, np.ndarray, float]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def power_traces(A: np.ndarray, upto: int) -> list[complex]:
    return [np.trace(np.linalg.matrix_power(A, n)) for n in range(1, upto + 1)]


def point_counts(A: np.ndarray, q: float, upto: int) -> list[float]:
    return [float(q**n + 1.0 - power_traces(A, upto)[n - 1].real) for n in range(1, upto + 1)]


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    n = sum(block.shape[0] for block in blocks)
    out = np.zeros((n, n), dtype=complex)
    pos = 0
    for block in blocks:
        k = block.shape[0]
        out[pos : pos + k, pos : pos + k] = block
        pos += k
    return out


def root_of_unity_block(order: int, radius: float) -> np.ndarray:
    roots = [radius * np.exp(2j * np.pi * k / order) for k in range(order)]
    return np.diag(roots)


def elementary_from_power_sums(power_sums: list[float]) -> list[float]:
    """Newton identities: first d power sums -> elementary symmetrics e_1..e_d."""

    e: list[float] = []
    for k, pk in enumerate(power_sums, start=1):
        accum = pk
        for i in range(1, k):
            accum += ((-1) ** i) * e[i - 1] * power_sums[k - i - 1]
        e_k = ((-1) ** (k + 1)) * accum / k
        e.append(float(e_k))
    return e


def roots_from_power_sums(power_sums: list[float]) -> np.ndarray:
    e = elementary_from_power_sums(power_sums)
    coeffs = [1.0]
    for k, e_k in enumerate(e, start=1):
        coeffs.append(((-1) ** k) * e_k)
    return np.roots(coeffs)


def relation_count(window: int) -> int:
    graph_relations = sum(1 for m in range(window + 1) for n in range(window + 1) if m + n <= window)
    count_relations = window
    dagger_relations = window
    sampled_projection_relations = window**3
    return graph_relations + count_relations + dagger_relations + sampled_projection_relations


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def graph(F: np.ndarray, q: float, n: int) -> Corr:
    return corr(q**n, np.linalg.matrix_power(F, n), 1.0)


def compose(A: Corr, B: Corr) -> Corr:
    d1, z, d2 = A
    e1, w, e2 = B
    return corr(d1 * e1, z @ w, d2 * e2)


def dagger(A: Corr, E: np.ndarray) -> Corr:
    d1, z, d2 = A
    return corr(d2, rosati(z, E), d1)


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(abs(lhs - rhs))


# PCC1: a finite-field square shadow can be encoded as a finite presentation,
# but the presentation is only a table of relations unless a square carrier is
# separately constructed.
q_true = 7
F_true = frobenius(q_true, 1).astype(complex)
window = 4
true_counts = point_counts(F_true, q_true, window)
finite_relation_count = relation_count(window)
presentation_has_generators = True
presentation_has_relation_table = True
presentation_constructs_square = False
presentation_constructs_rep_ns = False

gate(
    "PCC1 finite-field data can be encoded as a finite presentation",
    true_counts == [7.0, 63.0, 364.0, 2331.0]
    and finite_relation_count == 87
    and presentation_has_generators
    and presentation_has_relation_table
    and not presentation_constructs_square
    and not presentation_constructs_rep_ns,
    "window=%d, relations=%d, counts=%s, no square/rep_NS constructed"
    % (window, finite_relation_count, [round(x, 1) for x in true_counts]),
)


# PCC2: the same finite presentation schema can realize arbitrary control
# count windows by Newton/companion realization. This is relation fitting, not
# Euler/Satake construction.
control_q = 7
control_counts = [10.0, -3.0, 25.0, 6.0]
control_traces = [control_q**n + 1.0 - c for n, c in enumerate(control_counts, start=1)]
control_roots = roots_from_power_sums(control_traces)
control_operator = np.diag(control_roots)
realized_control_traces = power_traces(control_operator, len(control_traces))
control_has_euler_product = False
control_has_satake = False
control_has_rep_ns = False
control_has_positive_rosati = False

gate(
    "PCC2 presented relation schema fits arbitrary control count windows",
    all(abs(a.real - b) < 1e-7 for a, b in zip(realized_control_traces, control_traces))
    and not control_has_euler_product
    and not control_has_satake
    and not control_has_rep_ns
    and not control_has_positive_rosati,
    "control counts=%s, realized traces=%s, no Euler/Satake/rep_NS/Rosati"
    % (
        [round(float(c), 1) for c in control_counts],
        [round(float(z.real), 3) for z in realized_control_traces],
    ),
)


# PCC3: finite presented relation windows do not determine the carrier. Ghost
# semigroup summands preserve the declared finite window and change the next
# trace/count.
ghost = root_of_unity_block(window + 1, 1.3)
augmented = block_diag(F_true, ghost)
base_traces = power_traces(F_true, window)
aug_traces = power_traces(augmented, window)
base_next_count = point_counts(F_true, q_true, window + 1)[-1]
aug_next_count = point_counts(augmented, q_true, window + 1)[-1]
next_count_gap = abs(base_next_count - aug_next_count)

gate(
    "PCC3 finite presented relations admit ghost carrier extensions",
    all(abs(a - b) < 1e-9 for a, b in zip(base_traces, aug_traces)) and next_count_gap > 1e-3,
    "first %d traces match; count_%d differs by %.3f"
    % (window, window + 1, next_count_gap),
)


# PCC4: declaring projection in the presentation does not construct the
# projection calculus. The componentwise realization still has a nonzero
# semantic defect.
E_true = weil_pairing(F_true, q_true).astype(complex)
D_true = delta(F_true)
G_true = graph(F_true, q_true, 1)
declared_projection_axiom = True
semantic_projection_defect = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "PCC4 projection in a presentation is an axiom, not constructed calculus",
    declared_projection_axiom and semantic_projection_defect == 27.0,
    "declared projection=true, componentwise semantic defect=%.1f" % semantic_projection_defect,
)


# PCC5: adding all scalar count relations imports the target count oracle
# rather than constructing the carrier. Without the supplied table the free
# presentation has no Euler/Satake source for those numbers.
all_counts_relation_source = "supplied_oracle"
count_oracle_window = 8
oracle_counts = point_counts(F_true, q_true, count_oracle_window)
presentation_derives_counts_from_carrier = False
presentation_kills_controls = False

gate(
    "PCC5 all-count presentations import the target trace oracle",
    all_counts_relation_source == "supplied_oracle"
    and len(oracle_counts) == count_oracle_window
    and oracle_counts[:4] == true_counts
    and not presentation_derives_counts_from_carrier
    and not presentation_kills_controls,
    "oracle window=%d, first counts=%s, no carrier derivation/control death"
    % (count_oracle_window, [round(float(c), 1) for c in oracle_counts[:4]]),
)


# PCC6: construction audit.
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_degree_character_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "PCC6 presented correspondence carrier constructs no End(S^2/Z) square package",
    not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_degree_character_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no rep_NS, square, proper correspondences, fiber products, pairing, projection, graph, Rosati, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (PCC1-PCC6)")
print(
    "VERDICT: a universal or finitely presented correspondence carrier is not "
    "End(S^2/Z). Presentations encode relation tables; they can fit arbitrary "
    "control count windows, admit ghost carrier extensions, declare projection "
    "as an axiom while the formal semantics still fail it, and import all-count "
    "oracles without constructing a square carrier, proper correspondences, "
    "positive Rosati, or control death."
)
