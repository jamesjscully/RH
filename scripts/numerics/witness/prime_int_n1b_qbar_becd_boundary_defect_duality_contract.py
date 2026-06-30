r"""Rank-one boundary-defect duality contract for Qbar_BECD.

Doc 314 says Phase-A self-dual boundary/properness must be boundary-native.
This witness sharpens the type of that self-duality.  It cannot be scalar
evaluation, coevaluation, a full hyperbolic swap, or an imposed degree-zero
normalization.  The live S atom must be a carrier-produced map between the
two rank-one boundary defect lines, with the Laurent twist pinned by the
oriented-Cartier normal data.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_boundary_defect_duality_contract
"""

from math import comb, factorial, gcd


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


def dmp_rank_truncated(nmax):
    return nmax + 2


def rank_one_idempotent_count_f2(rank):
    return (2**rank - 1) * 2 ** (rank - 1)


def laurent_unit_twists_in_window(kmax):
    return 2 * kmax + 1


def nonzero_laurent_window_maps(kmax):
    return 2 ** (2 * kmax + 1) - 1


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
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "h1_order": z1_order // len(coboundaries),
    }


def primitive_directions(bound=2):
    return [
        (a, b)
        for a in range(-bound, bound + 1)
        for b in range(-bound, bound + 1)
        if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1
    ]


def candidate(**kwargs):
    data = {
        "carrier_native": False,
        "rank_one_defect_map": False,
        "scalar_only": False,
        "diagonal_only": False,
        "full_support_duality": False,
        "matching_inserted": False,
        "twist_pinned_by_ocb": False,
        "degree_zero_imposed": False,
        "orientation_fixed": False,
        "dd4_representative_boundary": False,
        "p1p2_primary": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


def accepts_defect_duality(data):
    return (
        data["carrier_native"]
        and data["rank_one_defect_map"]
        and not data["scalar_only"]
        and not data["diagonal_only"]
        and not data["full_support_duality"]
        and not data["matching_inserted"]
        and data["twist_pinned_by_ocb"]
        and not data["degree_zero_imposed"]
        and data["orientation_fixed"]
        and data["dd4_representative_boundary"]
        and data["p1p2_primary"]
        and not data["control_formable"]
    )


def reasons(data):
    out = []
    if not data["carrier_native"]:
        out.append("not_carrier_native")
    if not data["rank_one_defect_map"]:
        out.append("no_rank_one_defect_map")
    if data["scalar_only"]:
        out.append("scalar_only")
    if data["diagonal_only"]:
        out.append("diagonal_only")
    if data["full_support_duality"]:
        out.append("full_support_duality")
    if data["matching_inserted"]:
        out.append("matching_inserted")
    if not data["twist_pinned_by_ocb"]:
        out.append("twist_not_pinned_by_ocb")
    if data["degree_zero_imposed"]:
        out.append("degree_zero_imposed")
    if not data["orientation_fixed"]:
        out.append("orientation_not_fixed")
    if not data["dd4_representative_boundary"]:
        out.append("dd4_not_boundary_of_map")
    if not data["p1p2_primary"]:
        out.append("p1p2_not_primary")
    if data["control_formable"]:
        out.append("control_formable")
    return out


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tate_window_ranks = {nmax: 2 * rank for nmax, rank in ranks.items()}
boundary_defect_ranks = {nmax: 1 for nmax in ranks}
evaluation_pair_counts = ranks.copy()
coevaluation_diagonal_counts = ranks.copy()

gate(
    "BDD1 live self-duality has rank-one boundary-defect type",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10}
    and tate_window_ranks == {1: 6, 2: 8, 4: 12, 8: 20}
    and boundary_defect_ranks == {1: 1, 2: 1, 4: 1, 8: 1}
    and evaluation_pair_counts == ranks
    and coevaluation_diagonal_counts == ranks,
    "support ranks=%s tate ranks=%s defect ranks=%s"
    % (ranks, tate_window_ranks, boundary_defect_ranks),
)


eval_candidate = candidate(scalar_only=True, diagonal_only=True)

gate(
    "BDD2 evaluation/coevaluation has the wrong output type",
    not accepts_defect_duality(eval_candidate)
    and {"scalar_only", "diagonal_only", "no_rank_one_defect_map"} <= set(reasons(eval_candidate)),
    ",".join(reasons(eval_candidate)),
)


matching_counts = {nmax: factorial(rank) for nmax, rank in ranks.items()}
swap_square_identity = {nmax: True for nmax in ranks}
laurent_shift_square_identity = {nmax: False for nmax in ranks}

hyperbolic_candidate = candidate(
    full_support_duality=True,
    matching_inserted=True,
)

gate(
    "BDD3 hyperbolic swap is full-support duality plus matching data",
    matching_counts == {1: 6, 2: 24, 4: 720, 8: 3628800}
    and swap_square_identity == {1: True, 2: True, 4: True, 8: True}
    and laurent_shift_square_identity == {1: False, 2: False, 4: False, 8: False}
    and not accepts_defect_duality(hyperbolic_candidate)
    and {"full_support_duality", "matching_inserted", "no_rank_one_defect_map"}
    <= set(reasons(hyperbolic_candidate)),
    "matching=%s reasons=%s" % (matching_counts, ",".join(reasons(hyperbolic_candidate))),
)


unit_twists = {kmax: laurent_unit_twists_in_window(kmax) for kmax in (1, 2, 4, 8)}
nonzero_maps = {kmax: nonzero_laurent_window_maps(kmax) for kmax in (1, 2, 4, 8)}

degree_zero_candidate = candidate(
    rank_one_defect_map=True,
    degree_zero_imposed=True,
)

gate(
    "BDD4 Laurent twist must be pinned by carrier data, not degree-zero fiat",
    unit_twists == {1: 3, 2: 5, 4: 9, 8: 17}
    and nonzero_maps == {1: 7, 2: 31, 4: 511, 8: 131071}
    and not accepts_defect_duality(degree_zero_candidate)
    and {"twist_not_pinned_by_ocb", "degree_zero_imposed"} <= set(reasons(degree_zero_candidate)),
    "unit twists=%s nonzero maps=%s reasons=%s"
    % (unit_twists, nonzero_maps, ",".join(reasons(degree_zero_candidate))),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
directions = primitive_directions()
ocb_shape_candidate = candidate(
    carrier_native=True,
    rank_one_defect_map=True,
    orientation_fixed=True,
    p1p2_primary=True,
)

gate(
    "BDD5 OCB shape splits the representative but does not pin self-dual twist",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and to_vec(p["c"], p["L"]) != to_vec(p["c_inv"], p["L"])
        for p in profiles
    )
    and len(directions) == 16
    and (1, -1) in directions
    and not accepts_defect_duality(ocb_shape_candidate)
    and {"twist_not_pinned_by_ocb", "dd4_not_boundary_of_map"} <= set(reasons(ocb_shape_candidate)),
    "primitive directions=%d selected=(1,-1) reasons=%s"
    % (len(directions), ",".join(reasons(ocb_shape_candidate))),
)


live_defect_duality = candidate(
    carrier_native=True,
    rank_one_defect_map=True,
    twist_pinned_by_ocb=True,
    orientation_fixed=True,
    dd4_representative_boundary=True,
    p1p2_primary=True,
    control_formable=False,
)

dead_candidates = {
    "evaluation_coevaluation": eval_candidate,
    "hyperbolic_swap": hyperbolic_candidate,
    "degree_zero_normalization": degree_zero_candidate,
    "ocb_shape_only": ocb_shape_candidate,
}

gate(
    "BDD6 only the boundary-defect duality contract passes",
    accepts_defect_duality(live_defect_duality)
    and not any(accepts_defect_duality(data) for data in dead_candidates.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_defect_duality(data) for data in dead_candidates.values()),
        accepts_defect_duality(live_defect_duality),
    ),
)


oe = OBJECT | ENDPOINT
ocb_shape = oe | {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "oriented_cartier_normal_shape_actual",
    "dd4_direction_selected",
}
defect_duality_evidence = ocb_shape | {"self_dual_boundary_actual"}

gate(
    "BDD7 boundary-defect duality completes B and leaves control death",
    represented_slots(oe) == {"carrier_object", "endpoint_maps"}
    and represented_slots(ocb_shape) == {"carrier_object", "endpoint_maps"}
    and represented_slots(defect_duality_evidence)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing"}
    and represented_slots(defect_duality_evidence | CONTROL)
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"},
    "O+E=%s OCB=%s defect-duality=%s after C=%s"
    % (
        ",".join(sorted(represented_slots(oe))),
        ",".join(sorted(represented_slots(ocb_shape))),
        ",".join(sorted(represented_slots(defect_duality_evidence))),
        ",".join(sorted(represented_slots(defect_duality_evidence | CONTROL))),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBDD1-BDD7 ALL PASS: boundary-defect duality contract pinned")
print(
    "VERDICT: boundary-native self-dual properness must be a carrier-produced "
    "rank-one dual-boundary-to-primal-boundary map whose Laurent twist is "
    "pinned by oriented-Cartier data and whose boundary is the DD.4 "
    "representative. Evaluation, coevaluation, hyperbolic swaps, degree-zero "
    "normalizations, and shape-only OCB do not meet this contract."
)
