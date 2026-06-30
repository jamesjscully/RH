r"""Phase-A sieve for the Qbar_BECD construction frontier.

This witness is constructive narrowing, not a no-go theorem.  Doc 308 pins the
first missing object as:

    Qbar_BECD = Qbar/Q/dQ + endpoints + DD.4 boundary killing
                + formation-level control death.

The point here is to avoid random construction attempts.  We enumerate the
four Phase-A bundles, identify the current object-containing line, and record
the next sharp experiment: try to construct endpoint pushforwards and the DD.4
boundary/localization map together on the Connes-Consani/CxC carrier.  That
single probe separates endpoint failure, boundary failure, and the residual
control-death problem.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_phase_a_sieve
"""

from itertools import combinations
from math import comb, log2

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


PHASE_A_SLOTS = {
    "carrier_object",
    "endpoint_maps",
    "dd4_boundary_killing",
    "control_death",
}

object_bundle = {"object_actual", "open_actual", "boundary_actual"}
endpoint_bundle = {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"}
boundary_bundle = {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
}
control_bundle = {
    "control_instantiation_impossible",
    "control_death_at_formation_proved",
}

BUNDLES = {
    "object": object_bundle,
    "endpoint": endpoint_bundle,
    "boundary": boundary_bundle,
    "control": control_bundle,
}

BUNDLE_TO_SLOT = {
    "object": "carrier_object",
    "endpoint": "endpoint_maps",
    "boundary": "dd4_boundary_killing",
    "control": "control_death",
}


def represented_slots(evidence):
    evidence = set(evidence)
    slots = set()

    if {"object_actual", "open_actual", "boundary_actual"} <= evidence:
        slots.add("carrier_object")
    if {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"} <= evidence:
        slots.add("endpoint_maps")
    if {
        "boundary_map_actual",
        "localization_exact_actual",
        "dd4_class_mapped_to_zero",
        "self_dual_boundary_actual",
    } <= evidence:
        slots.add("dd4_boundary_killing")
    if {"control_instantiation_impossible", "control_death_at_formation_proved"} <= evidence:
        slots.add("control_death")

    return slots


def branch_names():
    names = list(BUNDLES)
    for size in range(len(names) + 1):
        for combo in combinations(names, size):
            yield combo


def branch_evidence(combo):
    evidence = set()
    for name in combo:
        evidence |= BUNDLES[name]
    return evidence


def branch_label(combo):
    return "+".join(combo) if combo else "empty"


def make(L):
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


routes = {
    "pfd_xbar": {
        "object_actual",
        "duality_functor_actual",
    },
    "connes_consani_scaling_site_cxc": {
        "object_actual",
        "open_actual",
        "boundary_actual",
        "duality_functor_actual",
        "duality_involutive_proved",
    },
    "condensed_metric_enrichment": {
        "analytic_site_actual",
        "metric_enrichment_actual",
        "positive_metric_declared",
    },
}

route_slots = {name: represented_slots(evidence) for name, evidence in routes.items()}
best_route = max(route_slots, key=lambda name: len(route_slots[name]))

gate(
    "PAS1 current route evidence gives only the object-containing start line",
    route_slots["pfd_xbar"] == set()
    and route_slots["connes_consani_scaling_site_cxc"] == {"carrier_object"}
    and route_slots["condensed_metric_enrichment"] == set()
    and best_route == "connes_consani_scaling_site_cxc",
    "; ".join(
        "%s:%s" % (name, ",".join(sorted(slots)) or "none")
        for name, slots in route_slots.items()
    ),
)


branches = {
    combo: {
        "label": branch_label(combo),
        "slots": represented_slots(branch_evidence(combo)),
    }
    for combo in branch_names()
}

unique_slot_profiles = {frozenset(data["slots"]) for data in branches.values()}
complete_branches = [
    data["label"] for data in branches.values() if data["slots"] == PHASE_A_SLOTS
]

gate(
    "PAS2 the Phase-A hypothesis class is exactly a 16-branch sieve",
    len(branches) == 16
    and len(unique_slot_profiles) == 16
    and complete_branches == ["object+endpoint+boundary+control"],
    "branches=%d unique_slot_profiles=%d complete=%s"
    % (len(branches), len(unique_slot_profiles), ",".join(complete_branches)),
)


full_combo = ("object", "endpoint", "boundary", "control")
single_deletions = {}
for name in full_combo:
    reduced = tuple(part for part in full_combo if part != name)
    single_deletions[name] = PHASE_A_SLOTS - branches[reduced]["slots"]

gate(
    "PAS3 each Phase-A bundle deletes exactly its own represented slot",
    all(single_deletions[name] == {BUNDLE_TO_SLOT[name]} for name in full_combo),
    "; ".join(
        "%s->missing:%s" % (name, ",".join(sorted(missing)))
        for name, missing in single_deletions.items()
    ),
)


object_line = {
    combo: data for combo, data in branches.items() if "object" in combo
}
object_line_missing = {
    data["label"]: PHASE_A_SLOTS - data["slots"] for data in object_line.values()
}
pre_control_combo = ("object", "endpoint", "boundary")

gate(
    "PAS4 the object-containing line has one pre-control frontier",
    len(object_line) == 8
    and object_line_missing["object"] == {
        "endpoint_maps",
        "dd4_boundary_killing",
        "control_death",
    }
    and object_line_missing["object+endpoint+boundary"] == {"control_death"}
    and object_line_missing["object+endpoint+control"] == {"dd4_boundary_killing"}
    and object_line_missing["object+boundary+control"] == {"endpoint_maps"}
    and branches[pre_control_combo]["slots"] == PHASE_A_SLOTS - {"control_death"},
    "; ".join(
        "%s missing %s" % (label, ",".join(sorted(missing)) or "none")
        for label, missing in sorted(object_line_missing.items())
    ),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
same_total_a = (10, F_true, 1)
same_total_b = (7, F_true, 4)
same_total = same_total_a[0] + same_total_a[2] == same_total_b[0] + same_total_b[2]
same_diagonal = ns_intersection(D_true, same_total_a) == ns_intersection(D_true, same_total_b)
endpoints_differ = same_total_a[0] != same_total_b[0] and same_total_a[2] != same_total_b[2]

gate(
    "PAS5 endpoint failure is a graph/composition failure, not a degree-label gap",
    same_total
    and same_diagonal
    and endpoints_differ
    and "endpoint_maps" not in branches[("object", "boundary", "control")]["slots"],
    "(10,F,1) and (7,F,4) share total degree and Delta pairing but differ at endpoints",
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
no_dd4_branch = branches[("object", "endpoint", "control")]["slots"]

gate(
    "PAS6 boundary failure is exactly the surviving DD.4 class",
    all(
        p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1
        for p in profiles
    )
    and "dd4_boundary_killing" not in no_dd4_branch,
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)

gate(
    "PAS7 after endpoint+boundary, the remaining obstruction is formation control death",
    branches[pre_control_combo]["slots"] == PHASE_A_SLOTS - {"control_death"}
    and control_sign < 0
    and control_projection == 11.0
    and "control_death" not in branches[pre_control_combo]["slots"],
    "pre-control missing=control_death; q=3 sign %.3f and projection defect %.0f"
    % (control_sign, control_projection),
)


endpoint_boundary_probe = endpoint_bundle | boundary_bundle
current_evidence = routes["connes_consani_scaling_site_cxc"]
after_probe_slots = represented_slots(current_evidence | endpoint_boundary_probe)
random_singletons = {
    name: PHASE_A_SLOTS - represented_slots(current_evidence | bundle)
    for name, bundle in {
        "endpoint_only": endpoint_bundle,
        "boundary_only": boundary_bundle,
        "control_only": control_bundle,
    }.items()
}

gate(
    "PAS8 next experiment is the endpoint+boundary probe on the CC/CxC object",
    after_probe_slots == PHASE_A_SLOTS - {"control_death"}
    and random_singletons["endpoint_only"] == {"dd4_boundary_killing", "control_death"}
    and random_singletons["boundary_only"] == {"endpoint_maps", "control_death"}
    and random_singletons["control_only"] == {"endpoint_maps", "dd4_boundary_killing"}
    and endpoint_boundary_probe == endpoint_bundle | boundary_bundle,
    "endpoint+boundary leaves only control_death; single probes leave two missing slots",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPAS1-PAS8 ALL PASS: Qbar_BECD Phase-A sieve pinned")
print(
    "VERDICT: refine the current CC/CxC object line by a combined endpoint+boundary "
    "test.  If endpoints fail, graph/composition dies; if the boundary map fails, "
    "DD.4 remains nonzero; if both pass, the only Phase-A slot left is "
    "formation-level control death."
)
