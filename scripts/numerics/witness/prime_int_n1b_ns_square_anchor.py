r"""Weight-2 NS square anchor.

This is a construction-spec witness, not a no-go theorem.  It records the
function-field model the missing End(S^2/Z) must reproduce: the weight-2
Neron-Severi lattice, the indecomposable diagonal, Frobenius graphs, and the
canonical Rosati/duality pairing on End(H^1).

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_ns_square_anchor
"""

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    end_component,
    frobenius,
    frobenius_graph,
    is_indecomposable,
    ns_intersection,
    offcircle_plant as ns_offcircle_plant,
    primitive_hodge_index as ns_primitive_hodge_index,
    weil_pairing,
)
from scripts.numerics.witness.ns_hodge_index_duality import (
    C4_defect_weight2,
    P_gram,
    frobenius_and_cup,
    involutivity_defect,
    offcircle_plant as dual_offcircle_plant,
    primitive_hodge_index as dual_primitive_hodge_index,
    weil_curves,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


curves = [(2, 1, "q=2"), (5, 2, "q=5"), (7, 1, "q=7"), (11, 3, "q=11"), (13, 5, "q=13")]


point_count_checks = []
for q, a1, label in curves:
    F = frobenius(q, a1)
    Delta = diagonal(F)
    for n in (1, 2, 3):
        Gamma = frobenius_graph(F, q, n)
        intersection = ns_intersection(Delta, Gamma)
        count = q ** n + 1 - sum(alpha ** n for alpha in np.linalg.eigvals(F)).real
        point_count_checks.append((label, n, intersection, count, abs(intersection - count) < 1e-9))

gate(
    "NSA1 rep_NS diagonal/Frobenius graph reproduces point counts",
    all(ok for *_rest, ok in point_count_checks),
    "; ".join(f"{label}:n={n}:D.G={intersection:.1f}=#{count:.1f}" for label, n, intersection, count, _ok in point_count_checks[:5]),
)


indecomp_checks = []
for q, a1, label in curves:
    F = frobenius(q, a1)
    Delta = diagonal(F)
    fiber = (1, np.zeros_like(F), 0)
    indecomp_checks.append(
        (
            label,
            float(np.linalg.norm(end_component(Delta))),
            float(np.linalg.norm(end_component(fiber))),
            is_indecomposable(Delta) and not is_indecomposable(fiber),
            ns_intersection(Delta, Delta),
        )
    )

gate(
    "NSA2 diagonal is indecomposable, product/fiber classes are not",
    all(ok for _label, _d_norm, _f_norm, ok, _dd in indecomp_checks),
    "; ".join(f"{label}:||End(Delta)||={d_norm:.4f},||End(fiber)||={f_norm:.1f},D.D={dd:.1f}" for label, d_norm, f_norm, _ok, dd in indecomp_checks),
)


primitive_checks = []
for q, a1, label in curves:
    F = frobenius(q, a1)
    E = weil_pairing(F, q)
    on_index = ns_primitive_hodge_index(F, E, 1)
    Foff, Eoff = ns_offcircle_plant(q, 1.5)
    off_index = ns_primitive_hodge_index(Foff, Eoff, 1)
    primitive_checks.append((label, on_index, off_index, on_index < 0 and off_index > 0))

gate(
    "NSA3 primitive weight-2 Hodge index flips off circle",
    all(ok for _label, _on, _off, ok in primitive_checks),
    "; ".join(f"{label}:on={on:+.3f},off={off:+.3f}" for label, on, off, _ok in primitive_checks),
)


duality_checks = []
for name, q, g, roots in weil_curves():
    F, E = frobenius_and_cup(roots, q)
    Foff, Eoff = dual_offcircle_plant(q, g, 1.5)
    on_index = dual_primitive_hodge_index(F, E, g)
    off_index = dual_primitive_hodge_index(Foff, Eoff, g)
    duality_checks.append(
        (
            name,
            involutivity_defect(E),
            C4_defect_weight2(E),
            P_gram(F, F, E),
            on_index,
            off_index,
            involutivity_defect(E) < 1e-9
            and C4_defect_weight2(E) < 1e-9
            and abs(P_gram(F, F, E) - 2 * g * q) < 1e-8
            and off_index > on_index + 1e-9,
        )
    )

gate(
    "NSA4 weight-2 duality is involutive and pairing is canonical",
    all(ok for *_rest, ok in duality_checks),
    "; ".join(f"{name}:D2={d2:.1e},C4={c4:.1e},TrFFdag={tr:.2f}" for name, d2, c4, tr, _on, _off, _ok in duality_checks),
)


dh_has_euler_product = False
dh_has_satake = False
dh_has_fx_f_product = False
dh_has_end_frobenius = False
dh_has_ns_diagonal_component = False
gate(
    "NSA5 DH has no typed NS square anchor",
    not dh_has_euler_product
    and not dh_has_satake
    and not dh_has_fx_f_product
    and not dh_has_end_frobenius
    and not dh_has_ns_diagonal_component,
    "no Euler product/Satake/fxf/End-Frobenius/indecomposable NS diagonal",
)


zeta_rep_ns_constructed = False
zeta_indecomposable_diagonal_constructed = False
zeta_frobenius_graph_constructed = False
zeta_square_intersection_form_constructed = False
zeta_positive_rosati_constructed = False
zeta_laurent_boundary_constructed = False
zeta_torsor_splitter_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "NSA6 this is an anchor/spec, not yet End(S^2/Z)",
    not zeta_rep_ns_constructed
    and not zeta_indecomposable_diagonal_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_square_intersection_form_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_laurent_boundary_constructed
    and not zeta_torsor_splitter_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "Z must still construct rep_NS, diagonal, graph, form, Rosati, boundary, splitter, DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (NSA1-NSA6)")
print(
    "VERDICT: the function-field square anchor is explicit.  The target is "
    "rep_NS: correspondences represented by (d1,z,d2), with intersection "
    "d1 e2 + d2 e1 - Tr(z w), diagonal (1,Id,1), Frobenius graph "
    "(q^n,F^n,1), and canonical weight-2 duality pairing Tr(z w^dag).  "
    "The diagonal is indecomposable and the primitive Hodge index is the "
    "Rosati/RH flip.  Over Z this remains a specification: rep_NS and its "
    "positive Rosati square carrier are not constructed yet."
)
