r"""Carrier-first categorical square contract for End(S^2/Z).

This is a construction-spec witness, not a no-go theorem and not a proof of
RH.  It records the admissible categorical route after the square-carrier
contract: category theory may organize the construction only after a specific
compactified square supplies the maps, boundary, correspondences, and duality.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_carrier_first_categorical_square_contract
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


def derive_slots(generators):
    """Finite dependency graph for the carrier-first categorical contract."""

    generators = set(generators)
    slots = set()

    if {
        "compactified_square",
        "p1",
        "p2",
        "integral_cycles",
        "proper_pushforward",
    } <= generators:
        slots |= {"endpoint_integrality", "degree_maps"}

    if {
        "compactified_square",
        "proper_correspondence_category",
        "integral_cycles",
        "intersection_pairing",
    } <= generators:
        slots |= {"rep_NS", "diagonal"}

    if {
        "proper_correspondence_category",
        "fiber_products",
        "frobenius_hecke_graph",
        "degree_maps",
    } <= generators | slots:
        slots |= {"frobenius_graph", "fiber_product_composition"}

    if {
        "proper_correspondence_category",
        "proper_pushforward",
        "intersection_pairing",
        "fiber_product_composition",
    } <= generators | slots:
        slots.add("projection_formula")

    if {
        "boundary",
        "localization_sequence",
        "dd4_coefficients",
        "self_dual_boundary",
    } <= generators:
        slots.add("dd4_boundary_killing")

    if {
        "duality_functor",
        "diagonal",
        "rep_NS",
        "intersection_pairing",
    } <= generators | slots:
        slots.add("rosati_duality")

    if {
        "rosati_duality",
        "primitive_hodge_index",
        "frobenius_graph",
    } <= generators | slots:
        slots.add("primitive_positive_sign")

    if {
        "compactified_square",
        "p1",
        "p2",
        "boundary",
        "frobenius_hecke_graph",
        "control_death_guard",
    } <= generators:
        slots.add("control_death")

    return slots


carrier_first_generators = {
    "compactified_square",
    "open_square",
    "boundary",
    "p1",
    "p2",
    "proper_correspondence_category",
    "fiber_products",
    "integral_cycles",
    "proper_pushforward",
    "intersection_pairing",
    "frobenius_hecke_graph",
    "localization_sequence",
    "dd4_coefficients",
    "self_dual_boundary",
    "duality_functor",
    "primitive_hodge_index",
    "control_death_guard",
}

carrier_first_slots = derive_slots(carrier_first_generators)

gate(
    "CFC1 one carrier-first datum derives the square slots together",
    REQUIRED_SLOTS <= carrier_first_slots,
    "derived: " + ", ".join(sorted(carrier_first_slots)),
)


def compose(a, b):
    d1, z, d2 = a
    e1, w, e2 = b
    return d1 * e1, z @ w, d2 * e2


F7 = frobenius(7, 1)
Delta7 = diagonal(F7)
graph_checks = []
for n in (1, 2, 3):
    Gamma = frobenius_graph(F7, 7, n)
    intersection = ns_intersection(Delta7, Gamma)
    count = 7**n + 1 - sum(alpha**n for alpha in np.linalg.eigvals(F7)).real
    graph_checks.append((n, intersection, count, abs(intersection - count) < 1e-9))

G1 = frobenius_graph(F7, 7, 1)
G2 = frobenius_graph(F7, 7, 2)
G3 = frobenius_graph(F7, 7, 3)
composition_ok = (
    compose(G1, G2)[0] == G3[0]
    and np.array_equal(compose(G1, G2)[1], G3[1])
    and compose(G1, G2)[2] == G3[2]
)

E7 = weil_pairing(F7, 7)
on_index = primitive_hodge_index(F7, E7, 1)
Foff, Eoff = offcircle_plant(7, 1.5)
off_index = primitive_hodge_index(Foff, Eoff, 1)

gate(
    "CFC2 finite-field model realizes graph, composition, and Rosati sign",
    all(row[-1] for row in graph_checks)
    and composition_ok
    and on_index < 0
    and off_index > 0,
    "; ".join(f"n={n}:D.G={intersection:.1f}=#{count:.1f}" for n, intersection, count, _ in graph_checks)
    + f"; G1oG2=G3:{composition_ok}; H_on={on_index:+.3f},H_off={off_index:+.3f}",
)


def make(L):
    """Arithmetic in F_2[z]/z^(L+1); unit polynomials are dicts {power: 1}."""

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
    bgens = [mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)]
    coboundaries = closure(bgens, L, mul)
    ngens = [mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)]
    norm_image = closure(ngens, L, mul)
    z1_order = 2**L // len(norm_image)
    h1_order = z1_order // len(coboundaries)
    return {
        "L": L,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "h1_order": h1_order,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "res1_c": c.get(1, 0),
    }


dd4_profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
free_splitter_slots = derive_slots({"torsor_splitter"})
carrier_boundary_slots = derive_slots(
    {
        "boundary",
        "localization_sequence",
        "dd4_coefficients",
        "self_dual_boundary",
    }
)

gate(
    "CFC3 DD.4 must be killed by carrier boundary, not free splitting",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in dd4_profiles)
    and "dd4_boundary_killing" in carrier_boundary_slots
    and "dd4_boundary_killing" not in free_splitter_slots,
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in dd4_profiles
    ),
)


shortcuts = {
    "generic_spans": {
        "span_bicategory",
        "profunctors",
        "pullback_composition",
        "adjoints",
        "beck_chevalley",
        "traces",
    },
    "formal_triples": {
        "symbolic_degree_labels",
        "componentwise_composition",
        "declared_delta",
        "declared_graph_law",
    },
    "free_dd4_splitter": {
        "torsor_splitter",
        "coefficient_extension",
        "chosen_coboundary",
    },
    "control_profile": {
        "trace_window",
        "declared_projection_formula",
        "declared_positive_pairing",
    },
}

shortcut_slots = {name: derive_slots(gens) for name, gens in shortcuts.items()}

gate(
    "CFC4 generic categorical shortcuts do not instantiate the carrier",
    all(not REQUIRED_SLOTS <= slots for slots in shortcut_slots.values())
    and all("endpoint_integrality" not in slots for slots in shortcut_slots.values())
    and all("control_death" not in slots for slots in shortcut_slots.values()),
    "; ".join(f"{name}:{len(slots)} slots" for name, slots in shortcut_slots.items()),
)


required_generators = {
    "compactified_square",
    "boundary",
    "p1",
    "p2",
    "proper_correspondence_category",
    "fiber_products",
    "integral_cycles",
    "proper_pushforward",
    "intersection_pairing",
    "frobenius_hecke_graph",
    "localization_sequence",
    "duality_functor",
    "control_death_guard",
}

candidate_generators = {
    "carrier_first_square": carrier_first_generators,
    "generic_spans": shortcuts["generic_spans"],
    "formal_triples": shortcuts["formal_triples"],
    "free_dd4_splitter": shortcuts["free_dd4_splitter"],
    "control_profile": shortcuts["control_profile"],
}

admissible = {
    name: required_generators <= gens for name, gens in candidate_generators.items()
}

gate(
    "CFC5 the universal-property filter rejects wild-goose routes early",
    admissible == {
        "carrier_first_square": True,
        "generic_spans": False,
        "formal_triples": False,
        "free_dd4_splitter": False,
        "control_profile": False,
    },
    ", ".join(f"{name}={value}" for name, value in admissible.items()),
)


control_formation = derive_slots(shortcuts["control_profile"])

gate(
    "CFC6 control death is a formation condition",
    not control_formation
    and "control_death" in carrier_first_slots
    and "frobenius_graph" in carrier_first_slots,
    "controls may declare traces/forms, but without square maps and boundary they derive no carrier slots",
)


zeta_constructed_generators = set()

gate(
    "CFC7 this is a categorical contract, not yet End(S^2/Z)",
    not REQUIRED_SLOTS <= derive_slots(zeta_constructed_generators),
    "over Z the compactified square carrier and its structural generators remain to be constructed",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nCFC1-CFC7 ALL PASS: carrier-first categorical square contract pinned")
print(
    "VERDICT: the categorical route is admitted only as a carrier-first construction. "
    "The square object must supply compactification, boundary localization, two maps, "
    "proper correspondences, integral cycles, graph composition, duality/Rosati, and "
    "control death together. Generic spans, symbolic triple laws, and free DD.4 "
    "splitters remain shortcut languages until those generators exist."
)
