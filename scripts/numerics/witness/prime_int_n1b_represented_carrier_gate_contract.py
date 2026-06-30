r"""Represented-carrier gate contract for End(S^2/Z).

This is a construction-spec witness, not a no-go theorem and not a proof of
RH.  It upgrades the carrier-first checklist after the Qbar-shell no-go:
slot names count only when backed by represented object/map/cycle/pullback/
boundary evidence.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_represented_carrier_gate_contract
"""

from math import comb, log2

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    ns_intersection,
    offcircle_plant,
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
    "carrier_object",
    "endpoint_maps",
    "integral_rep_NS",
    "diagonal",
    "frobenius_graph",
    "proper_composition",
    "projection_formula",
    "dd4_boundary_killing",
    "rosati_duality",
    "primitive_positive_sign",
    "control_death",
}


VISIBLE_FF_SLOTS = {
    "carrier_object",
    "endpoint_maps",
    "integral_rep_NS",
    "diagonal",
    "frobenius_graph",
    "proper_composition",
    "rosati_duality",
    "primitive_positive_sign",
}


def represented_slots(evidence):
    """Only represented evidence counts; declared names alone are ignored."""

    evidence = set(evidence)
    slots = set()

    if {"object_actual", "open_actual", "boundary_actual"} <= evidence:
        slots.add("carrier_object")

    if {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"} <= evidence:
        slots.add("endpoint_maps")

    if {"cycle_lattice_actual", "intersection_form_actual", "rep_functor_actual"} <= evidence:
        slots.add("integral_rep_NS")

    if {"diagonal_cycle_actual", "integral_rep_NS"} <= evidence | slots:
        slots.add("diagonal")

    if {"frobenius_graph_cycle_actual", "endpoint_maps", "integral_rep_NS"} <= evidence | slots:
        slots.add("frobenius_graph")

    if {"proper_pullbacks_actual", "fiber_product_composition_proved"} <= evidence:
        slots.add("proper_composition")

    if {
        "proper_pushforward_actual",
        "proper_pullbacks_actual",
        "projection_formula_proved",
        "intersection_form_actual",
    } <= evidence:
        slots.add("projection_formula")

    if {
        "boundary_map_actual",
        "localization_exact_actual",
        "dd4_class_mapped_to_zero",
        "self_dual_boundary_actual",
    } <= evidence:
        slots.add("dd4_boundary_killing")

    if {"duality_functor_actual", "duality_involutive_proved", "rosati_evaluation_proved"} <= evidence:
        slots.add("rosati_duality")

    if {"rosati_duality", "primitive_sign_proved", "frobenius_graph"} <= evidence | slots:
        slots.add("primitive_positive_sign")

    if {"control_instantiation_impossible", "control_death_at_formation_proved"} <= evidence:
        slots.add("control_death")

    return slots


def declared_slots(names):
    """Name-level checklist used only to show what no longer counts."""
    names = set(names)
    slots = set()

    if {"Qbar", "Q", "dQ"} <= names:
        slots.add("carrier_object")
    if {"p1", "p2"} <= names:
        slots.add("endpoint_maps")
    if {"rep_NS", "intersection"} <= names:
        slots.add("integral_rep_NS")
    if "Delta" in names:
        slots.add("diagonal")
    if "Gamma" in names:
        slots.add("frobenius_graph")
    if {"Corr_prop", "fiber_products"} <= names:
        slots.add("proper_composition")
    if "projection_formula" in names:
        slots.add("projection_formula")
    if {"dQ", "localization", "dd4_kill"} <= names:
        slots.add("dd4_boundary_killing")
    if "Rosati" in names:
        slots.add("rosati_duality")
    if "primitive_positive_sign" in names:
        slots.add("primitive_positive_sign")
    if "control_death" in names:
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


def projection_defect(A, B, C, E):
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(abs(lhs - rhs))


shell_names = {
    "Qbar",
    "Q",
    "dQ",
    "p1",
    "p2",
    "rep_NS",
    "intersection",
    "Delta",
    "Gamma",
    "Corr_prop",
    "fiber_products",
    "projection_formula",
    "localization",
    "dd4_kill",
    "Rosati",
    "primitive_positive_sign",
    "control_death",
}
shell_evidence = set()
shell_declared = declared_slots(shell_names)
shell_represented = represented_slots(shell_evidence)

gate(
    "RCG1 represented-carrier gate rejects name-level Qbar shells",
    REQUIRED_SLOTS <= shell_declared and shell_represented == set(),
    "declared slots=%d represented slots=%d" % (len(shell_declared), len(shell_represented)),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
G1 = frobenius_graph(F_true, q_true, 1)
G2 = frobenius_graph(F_true, q_true, 2)
G3 = frobenius_graph(F_true, q_true, 3)
graph_law = compose(G1, G2)
on_index = primitive_hodge_index(F_true, E_true, 1)
F_off, E_off = offcircle_plant(q_true, 1.5)
off_index = primitive_hodge_index(F_off, E_off, 1)

ff_visible_evidence = {
    "object_actual",
    "open_actual",
    "boundary_actual",
    "p1_map_actual",
    "p2_map_actual",
    "proper_pushforward_actual",
    "cycle_lattice_actual",
    "intersection_form_actual",
    "rep_functor_actual",
    "diagonal_cycle_actual",
    "frobenius_graph_cycle_actual",
    "proper_pullbacks_actual",
    "fiber_product_composition_proved",
    "duality_functor_actual",
    "duality_involutive_proved",
    "rosati_evaluation_proved",
    "primitive_sign_proved",
}
ff_visible_slots = represented_slots(ff_visible_evidence)
ff_counts_ok = (
    ns_intersection(D_true, G1) == 7
    and ns_intersection(D_true, G2) == 63
    and ns_intersection(D_true, G3) == 364
)
graph_ok = graph_law[0] == G3[0] and np.array_equal(graph_law[1], G3[1]) and graph_law[2] == G3[2]

gate(
    "RCG2 finite-field model is accepted only for represented visible slots",
    VISIBLE_FF_SLOTS <= ff_visible_slots
    and "projection_formula" not in ff_visible_slots
    and "dd4_boundary_killing" not in ff_visible_slots
    and "control_death" not in ff_visible_slots
    and ff_counts_ok
    and graph_ok
    and on_index < 0
    and off_index > 0,
    "visible slots=%s; counts n=1,2,3 ok; H_on=%.3f H_off=%.3f"
    % (",".join(sorted(ff_visible_slots)), on_index, off_index),
)


semantic_projection = projection_defect(G1, D_true, G1, E_true)
declared_projection_evidence = {"projection_formula_declared"}
proper_projection_evidence = {
    "proper_pushforward_actual",
    "proper_pullbacks_actual",
    "projection_formula_proved",
    "intersection_form_actual",
}

gate(
    "RCG3 projection requires represented push-pull proof",
    "projection_formula" not in represented_slots(declared_projection_evidence)
    and "projection_formula" in represented_slots(proper_projection_evidence)
    and semantic_projection == 27.0,
    "declared projection rejected; proper push-pull evidence accepted; semantic defect %.0f"
    % semantic_projection,
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
free_split_evidence = {"torsor_splitter_declared", "chosen_coboundary"}
boundary_evidence = {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
}

gate(
    "RCG4 DD.4 killing requires represented carrier boundary map",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles)
    and "dd4_boundary_killing" not in represented_slots(free_split_evidence)
    and "dd4_boundary_killing" in represented_slots(boundary_evidence),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


same_total_a = (10, F_true, 1)
same_total_b = (7, F_true, 4)
same_total = same_total_a[0] + same_total_a[2] == same_total_b[0] + same_total_b[2]
same_diagonal = ns_intersection(D_true, same_total_a) == ns_intersection(D_true, same_total_b)
endpoint_probes_differ = same_total_a[0] != same_total_b[0] and same_total_a[2] != same_total_b[2]

gate(
    "RCG5 endpoint maps require represented p1,p2 pushforwards",
    "endpoint_maps" not in represented_slots({"p1_declared", "p2_declared", "total_degree_decoder"})
    and "endpoint_maps"
    in represented_slots({"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"})
    and same_total
    and same_diagonal
    and endpoint_probes_differ,
    "(10,F,1) and (7,F,4) share total/Delta pairing but differ at endpoints",
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_declared_evidence = shell_names | {"positive_qsim_declared"}
control_death_evidence = {"control_instantiation_impossible", "control_death_at_formation_proved"}

gate(
    "RCG6 control death must be formation failure, not a named guard",
    "control_death" in declared_slots(control_declared_evidence)
    and "control_death" not in represented_slots(control_declared_evidence)
    and "control_death" in represented_slots(control_death_evidence)
    and control_projection == 11.0,
    "declared guard rejected; formation death evidence accepted; control defect %.0f"
    % control_projection,
)


complete_evidence = {
    "object_actual",
    "open_actual",
    "boundary_actual",
    "p1_map_actual",
    "p2_map_actual",
    "proper_pushforward_actual",
    "cycle_lattice_actual",
    "intersection_form_actual",
    "rep_functor_actual",
    "diagonal_cycle_actual",
    "frobenius_graph_cycle_actual",
    "proper_pullbacks_actual",
    "fiber_product_composition_proved",
    "projection_formula_proved",
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
    "duality_functor_actual",
    "duality_involutive_proved",
    "rosati_evaluation_proved",
    "primitive_sign_proved",
    "control_instantiation_impossible",
    "control_death_at_formation_proved",
}
essential_witnesses = {
    "object_actual",
    "p1_map_actual",
    "proper_pullbacks_actual",
    "boundary_map_actual",
    "duality_functor_actual",
    "control_instantiation_impossible",
}
complete_slots = represented_slots(complete_evidence)
single_deletion_failures = [
    token for token in sorted(essential_witnesses) if not REQUIRED_SLOTS <= represented_slots(complete_evidence - {token})
]

gate(
    "RCG7 complete represented evidence is necessary slotwise",
    REQUIRED_SLOTS <= complete_slots and single_deletion_failures == sorted(essential_witnesses),
    "complete slots=%d; essential deletions fail=%s"
    % (len(complete_slots), ",".join(single_deletion_failures)),
)


zeta_evidence_now = set()

gate(
    "RCG8 this is a gate, not yet the zeta carrier",
    not REQUIRED_SLOTS <= represented_slots(zeta_evidence_now),
    "over Z the represented carrier evidence remains absent",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nRCG1-RCG8 ALL PASS: represented-carrier gate pinned")
print(
    "VERDICT: carrier-first names now count only with represented evidence. "
    "Finite-field data fills the visible model slots, but the zeta-side "
    "carrier still needs actual Qbar, p1,p2, proper pullbacks, boundary "
    "localization, Rosati, and control-death proofs."
)
