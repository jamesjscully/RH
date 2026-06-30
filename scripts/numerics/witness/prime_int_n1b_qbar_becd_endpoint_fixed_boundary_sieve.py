r"""Endpoint-fixed DD.4 boundary sieve for the Qbar_BECD frontier.

Doc 309 made the endpoint+boundary probe decisive.  Doc 289 already ran the
naive CC/CxC product version of that probe: product projections can be granted
as endpoint maps, but product normal crossings do not produce the actual
DD.4-killing boundary/localization map.

This witness records the sharpened live branch:

    keep O+E on the CC/CxC product line,
    solve B = boundary map + exact localization + DD.4 zero + self-duality,
    then test C = formation-level control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_endpoint_fixed_boundary_sieve
"""

from itertools import combinations
from math import comb, gcd, log2


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

object_evidence = {"object_actual", "open_actual", "boundary_actual"}
endpoint_evidence = {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"}
control_evidence = {"control_instantiation_impossible", "control_death_at_formation_proved"}

BOUNDARY_ATOMS = {
    "map": {"boundary_map_actual"},
    "exact": {"localization_exact_actual"},
    "zero": {"dd4_class_mapped_to_zero"},
    "selfdual": {"self_dual_boundary_actual"},
}


def represented_slots(evidence):
    evidence = set(evidence)
    slots = set()

    if object_evidence <= evidence:
        slots.add("carrier_object")
    if endpoint_evidence <= evidence:
        slots.add("endpoint_maps")
    if set().union(*BOUNDARY_ATOMS.values()) <= evidence:
        slots.add("dd4_boundary_killing")
    if control_evidence <= evidence:
        slots.add("control_death")

    return slots


def boundary_branch_names():
    names = list(BOUNDARY_ATOMS)
    for size in range(len(names) + 1):
        for combo in combinations(names, size):
            yield combo


def boundary_branch_evidence(combo):
    evidence = set()
    for name in combo:
        evidence |= BOUNDARY_ATOMS[name]
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


cc_cxc_object = object_evidence | {
    "duality_functor_actual",
    "duality_involutive_proved",
}
cc_cxc_product_endpoints = cc_cxc_object | endpoint_evidence
product_boundary_shape = cc_cxc_product_endpoints | {
    "product_boundary_shape_actual",
    "normal_crossing_boundary_actual",
    "boundary_direction_family_actual",
}
declared_boundary = product_boundary_shape | {
    "boundary_map_declared",
    "localization_exact_declared",
    "dd4_class_mapped_to_zero_declared",
    "self_dual_boundary_declared",
}
actual_boundary = cc_cxc_product_endpoints | set().union(*BOUNDARY_ATOMS.values())


gate(
    "BDS1 doc-289 product probe fixes the live line at O+E, not E+B",
    represented_slots(cc_cxc_product_endpoints) == {"carrier_object", "endpoint_maps"}
    and represented_slots(product_boundary_shape) == {"carrier_object", "endpoint_maps"},
    "product endpoints slots=%s; product boundary-shape slots=%s"
    % (
        ",".join(sorted(represented_slots(cc_cxc_product_endpoints))),
        ",".join(sorted(represented_slots(product_boundary_shape))),
    ),
)


primitive_directions = [
    (a, b)
    for a in range(-2, 3)
    for b in range(-2, 3)
    if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1
]

gate(
    "BDS2 product normal crossings expose directions but select no DD.4 map",
    len(primitive_directions) == 16
    and "dd4_boundary_killing" not in represented_slots(product_boundary_shape),
    "primitive directions in [-2,2]^2=%d" % len(primitive_directions),
)


branches = {
    combo: represented_slots(cc_cxc_product_endpoints | boundary_branch_evidence(combo))
    for combo in boundary_branch_names()
}
complete_boundary_branches = [
    branch_label(combo) for combo, slots in branches.items() if "dd4_boundary_killing" in slots
]

gate(
    "BDS3 the endpoint-fixed boundary problem is a 16-branch atom sieve",
    len(branches) == 16
    and complete_boundary_branches == ["map+exact+zero+selfdual"],
    "branches=%d complete=%s" % (len(branches), ",".join(complete_boundary_branches)),
)


full_combo = ("map", "exact", "zero", "selfdual")
single_deletions = {}
for name in full_combo:
    reduced = tuple(part for part in full_combo if part != name)
    single_deletions[name] = branches[reduced]

gate(
    "BDS4 every boundary atom is necessary for represented DD.4 killing",
    all("dd4_boundary_killing" not in slots for slots in single_deletions.values()),
    "; ".join(
        "%s-deleted:%s" % (name, ",".join(sorted(slots)))
        for name, slots in single_deletions.items()
    ),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "BDS5 without the actual zero map the DD.4 class remains nonzero",
    all(
        p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1
        for p in profiles
    )
    and "dd4_boundary_killing" not in branches[("map", "exact", "selfdual")],
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


gate(
    "BDS6 map+exact+zero without self-duality is still not Phase-A boundary",
    "dd4_boundary_killing" not in branches[("map", "exact", "zero")]
    and represented_slots(actual_boundary - {"self_dual_boundary_actual"})
    == {"carrier_object", "endpoint_maps"},
    "self-dual boundary/properness is an atom, not decoration",
)


gate(
    "BDS7 declared boundary localization does not count as represented B",
    represented_slots(declared_boundary) == {"carrier_object", "endpoint_maps"}
    and "dd4_boundary_killing" not in represented_slots(declared_boundary),
    "declared slots=%s" % ",".join(sorted(represented_slots(declared_boundary))),
)


actual_boundary_slots = represented_slots(actual_boundary)
phase_a_after_boundary = PHASE_A_SLOTS - actual_boundary_slots

gate(
    "BDS8 actual B would leave exactly formation-level control death",
    actual_boundary_slots == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and phase_a_after_boundary == {"control_death"},
    "O+E+B slots=%s missing=%s"
    % (",".join(sorted(actual_boundary_slots)), ",".join(sorted(phase_a_after_boundary))),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBDS1-BDS8 ALL PASS: endpoint-fixed DD.4 boundary sieve pinned")
print(
    "VERDICT: do not repeat the product E+B probe.  Product endpoints give the "
    "O+E line; product boundary shape does not give B.  The next construction "
    "target is the actual boundary map, exact localization, DD.4-zero image, "
    "and self-dual boundary/properness data together."
)
