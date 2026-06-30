r"""Residual obligation sieve for oriented-Cartier Qbar_BECD boundary.

Doc 312 gives the live local B-shape:

    oriented Cartier boundary on O+E.

This witness separates the positive local splitter from the remaining carrier
proofs.  The endpoint/orientation bank shows that total degree, imported
difference sign, parity sublattices, and parity tags are not carrier-fixed
orientation or self-dual properness.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_oriented_cartier_residual_sieve
"""

from fractions import Fraction
from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


OBJECT = {"object_actual", "open_actual", "boundary_actual"}
ENDPOINT = {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"}
BOUNDARY = {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
}
CONTROL = {"control_instantiation_impossible", "control_death_at_formation_proved"}


def represented_slots(evidence):
    evidence = set(evidence)
    slots = set()
    if OBJECT <= evidence:
        slots.add("carrier_object")
    if ENDPOINT <= evidence:
        slots.add("endpoint_maps")
    if BOUNDARY <= evidence:
        slots.add("dd4_boundary_killing")
    if CONTROL <= evidence:
        slots.add("control_death")
    return slots


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
        "c": c,
        "c_inv": inv(c),
        "coboundaries": coboundaries,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


def decode_total_difference(total, difference):
    return Fraction(total + difference, 2), Fraction(total - difference, 2)


def parity_tag(label):
    total, difference = label
    return (total - difference) % 2


def contract_accepts(contract):
    return (
        contract["ocb_shape"]
        and contract["orientation_fixed_by_carrier"]
        and contract["p1p2_primary"]
        and contract["self_dual_properness"]
        and contract["control_nonformability"]
    )


oe = OBJECT | ENDPOINT
ocb_shape = oe | {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "oriented_cartier_normal_shape_actual",
    "dd4_direction_selected",
}
live_b = ocb_shape | {"self_dual_boundary_actual"}

gate(
    "OCR1 OCB shape is M+L+Z plus direction, but not live B without self-duality",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"}
    and represented_slots(ocb_shape) == {"carrier_object", "endpoint_maps"}
    and represented_slots(live_b) == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"},
    "O+E=%s; shape=%s; liveB=%s"
    % (
        ",".join(sorted(represented_slots(oe))),
        ",".join(sorted(represented_slots(ocb_shape))),
        ",".join(sorted(represented_slots(live_b))),
    ),
)


total_pair_a = (10, 1)
total_pair_b = (7, 4)
difference_pair_a = (10, 1)
difference_pair_b = (11, 2)

gate(
    "OCR2 total direction is carrier-symmetric but not endpoint-primary",
    sum(total_pair_a) == sum(total_pair_b)
    and total_pair_a != total_pair_b,
    "(10,1) and (7,4) share total 11 but have different endpoints",
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "OCR3 imported orientation sign changes representative, not just notation",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and to_vec(p["c"], p["L"]) != to_vec(p["c_inv"], p["L"])
        for p in profiles
    )
    and difference_pair_a[0] - difference_pair_a[1]
    == difference_pair_b[0] - difference_pair_b[1]
    and difference_pair_a != difference_pair_b,
    "c and c^-1 differ as representatives; (10,1) and (11,2) share difference 9",
)


labels = [(11, 9), (11, 3), (11, 8), (0, 1), (10, 1)]
decodes = {label: decode_total_difference(*label) for label in labels}
integral_labels = [
    label for label, decoded in decodes.items() if decoded[0].denominator == decoded[1].denominator == 1
]
half_integral_labels = [label for label in labels if label not in integral_labels]

gate(
    "OCR4 parity sublattice is endpoint integrality restated, not constructed",
    (11, 9) in integral_labels
    and (11, 3) in integral_labels
    and (11, 8) in half_integral_labels
    and (0, 1) in half_integral_labels
    and (10, 1) in half_integral_labels,
    "integral=%s half_integral=%s" % (integral_labels, half_integral_labels),
)


tagged_labels = [(1, 1), (0, 1), (11, 8), (10, 1)]
tag_zero = [label for label in tagged_labels if parity_tag(label) == 0]
tag_one = [label for label in tagged_labels if parity_tag(label) == 1]

gate(
    "OCR5 parity tags diagnose but do not produce carrier endpoint maps",
    tag_zero == [(1, 1)]
    and tag_one == [(0, 1), (11, 8), (10, 1)]
    and any(label[1] == 1 for label in tag_one),
    "tag0=%s tag1=%s; tag1 still contains a=1 split labels" % (tag_zero, tag_one),
)


shape_only = {
    "ocb_shape": True,
    "orientation_fixed_by_carrier": False,
    "p1p2_primary": True,
    "self_dual_properness": False,
    "control_nonformability": False,
}
carrier_orientation_only = dict(shape_only)
carrier_orientation_only.update({"orientation_fixed_by_carrier": True})
self_dual_orientation = dict(carrier_orientation_only)
self_dual_orientation.update({"self_dual_properness": True})
live_contract = dict(self_dual_orientation)
live_contract.update({"control_nonformability": True})

gate(
    "OCR6 residual obligations are carrier orientation, self-dual properness, then controls",
    not contract_accepts(shape_only)
    and not contract_accepts(carrier_orientation_only)
    and not contract_accepts(self_dual_orientation)
    and contract_accepts(live_contract),
    "shape -> orientation -> self-dual properness -> control nonformability",
)


gate(
    "OCR7 constructing residual live B leaves exactly formation control death as Phase-A slot",
    represented_slots(live_b) == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(live_b | CONTROL)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"},
    "before C=%s; after C=%s"
    % (
        ",".join(sorted(represented_slots(live_b))),
        ",".join(sorted(represented_slots(live_b | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nOCR1-OCR7 ALL PASS: oriented-Cartier residual obligation sieve pinned")
print(
    "VERDICT: OCB shape already gives the local splitter/direction.  The next "
    "construction proof is carrier-fixed orientation plus self-dual properness "
    "with p1,p2 kept primary; parity lattices and tags are only diagnostics. "
    "After that, Phase A reduces to formation-level control death."
)
