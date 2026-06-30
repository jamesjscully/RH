r"""Internal effectivity-domain contract for Qbar_BECD.

Doc 323 says the first generator must be a represented Euler/effectivity
domain with native prime-power towers.  This witness sharpens "represented":
the effectivity domain has to be an internal stratum of the same Qbar_BECD
object/map/cycle package that types endpoints, boundary, pushforwards, graph,
Rosati, count/degree data, and control death.  External prime monoids,
valuation registers, pair codecs, local Euler-factor stacks, and declared
domain IDs do not count.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_internal_effectivity_domain_contract
"""

from __future__ import annotations


failures: list[str] = []

INTERNAL_DOMAIN = "D_Qbar_BECD_eff"
ATOMS = {
    "effectivity_domain",
    "endpoint",
    "boundary",
    "pushforward",
    "graph",
    "rosati",
    "count_degree",
    "control_death",
}
REQUIRED_DOMAIN_EDGES = {
    ("effectivity_domain", "endpoint"),
    ("endpoint", "boundary"),
    ("boundary", "pushforward"),
    ("pushforward", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
    ("rosati", "control_death"),
    ("control_death", "effectivity_domain"),
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def valuation_depth(n: int, p: int) -> int | None:
    depth = 0
    while n > 1 and n % p == 0:
        n //= p
        depth += 1
    if n != 1:
        return None
    return depth


def prime_power_tower(p: int, length: int) -> list[int]:
    return [p**k for k in range(length)]


def connected(atoms: set[str], edges: set[tuple[str, str]]) -> bool:
    if not atoms:
        return False
    adjacency = {atom: set() for atom in atoms}
    for left, right in edges:
        if left in atoms and right in atoms:
            adjacency[left].add(right)
            adjacency[right].add(left)
    seen = set()
    stack = [next(iter(atoms))]
    while stack:
        atom = stack.pop()
        if atom in seen:
            continue
        seen.add(atom)
        stack.extend(adjacency[atom] - seen)
    return seen == atoms


def q_value(x: int, y: int) -> int:
    return x * x + 5 * y * y


def represented_values(limit: int) -> set[int]:
    bound = int(limit**0.5) + 1
    vals = set()
    for x in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            value = q_value(x, y)
            if 0 < value <= limit:
                vals.add(value)
    return vals


def irreducibles_in_monoid(values: set[int], limit: int) -> set[int]:
    irreducibles = set()
    for n in sorted(v for v in values if v > 1):
        reducible = False
        for a in values:
            if a <= 1 or n % a:
                continue
            b = n // a
            if b in values and b > 1:
                reducible = True
                break
        if not reducible and n <= limit:
            irreducibles.add(n)
    return irreducibles


def irreducible_factorizations(n: int, irreducibles: set[int]) -> set[tuple[int, ...]]:
    facts: set[tuple[int, ...]] = set()

    def rec(remaining: int, start: int, acc: list[int]) -> None:
        if remaining == 1:
            facts.add(tuple(acc))
            return
        for p in sorted(irreducibles):
            if p < start or remaining % p:
                continue
            rec(remaining // p, p, acc + [p])

    rec(n, 2, [])
    return facts


def endpoint_pair_code(left: int, right: int) -> int:
    return (2**left) * (3**right)


def all_atom_domains(domain_id: str) -> dict[str, str]:
    return {atom: domain_id for atom in ATOMS}


def source(**kwargs):
    data = {
        "carrier_native": False,
        "represented_object_maps_cycles": False,
        "internal_effectivity_stratum_actual": False,
        "domain_generated_by_qbar_object": False,
        "prime_power_towers_internal": False,
        "valuation_depth_internal": False,
        "euler_address_internal": False,
        "cartier_effectivity_strata_native": False,
        "strata_specialization_maps_native": False,
        "endpoint_pushforward_typed_by_internal_domain": False,
        "boundary_localization_typed_by_internal_domain": False,
        "graph_composition_typed_by_internal_domain": False,
        "rosati_typed_by_internal_domain": False,
        "count_degree_typed_by_internal_domain": False,
        "controls_undefined_at_internal_domain": False,
        "epstein_undefined_at_internal_domain": False,
        "theta_shadow_only_downstream": False,
        "non_split_domain_atom_graph": False,
        "domain_id": None,
        "atom_domains": {},
        "domain_edges": set(),
        "external_prime_monoid": False,
        "free_commutative_prime_monoid": False,
        "valuation_register": False,
        "degree_pair_codec": False,
        "endpoint_register": False,
        "local_euler_factor_only": False,
        "finite_prime_sample": False,
        "declared_internal_domain": False,
        "represented_norm_shadow_promoted": False,
        "semantic_euler_label": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_object_maps_cycles", "object_maps_cycles_not_represented"),
    ("internal_effectivity_stratum_actual", "internal_stratum_not_actual"),
    ("domain_generated_by_qbar_object", "domain_not_generated_by_qbar_object"),
    ("prime_power_towers_internal", "prime_power_towers_not_internal"),
    ("valuation_depth_internal", "valuation_depth_not_internal"),
    ("euler_address_internal", "euler_address_not_internal"),
    ("cartier_effectivity_strata_native", "cartier_strata_not_native"),
    ("strata_specialization_maps_native", "strata_specialization_not_native"),
    (
        "endpoint_pushforward_typed_by_internal_domain",
        "endpoint_pushforward_not_typed_by_internal_domain",
    ),
    (
        "boundary_localization_typed_by_internal_domain",
        "boundary_localization_not_typed_by_internal_domain",
    ),
    (
        "graph_composition_typed_by_internal_domain",
        "graph_composition_not_typed_by_internal_domain",
    ),
    ("rosati_typed_by_internal_domain", "rosati_not_typed_by_internal_domain"),
    (
        "count_degree_typed_by_internal_domain",
        "count_degree_not_typed_by_internal_domain",
    ),
    (
        "controls_undefined_at_internal_domain",
        "controls_not_undefined_at_internal_domain",
    ),
    ("epstein_undefined_at_internal_domain", "epstein_not_undefined_at_internal_domain"),
    ("theta_shadow_only_downstream", "theta_shadow_not_downstream_only"),
    ("non_split_domain_atom_graph", "domain_atom_graph_split"),
)

BANNED = (
    ("external_prime_monoid", "external_prime_monoid"),
    ("free_commutative_prime_monoid", "free_commutative_prime_monoid"),
    ("valuation_register", "valuation_register"),
    ("degree_pair_codec", "degree_pair_codec"),
    ("endpoint_register", "endpoint_register"),
    ("local_euler_factor_only", "local_euler_factor_only"),
    ("finite_prime_sample", "finite_prime_sample"),
    ("declared_internal_domain", "declared_internal_domain"),
    ("represented_norm_shadow_promoted", "represented_norm_shadow_promoted"),
    ("semantic_euler_label", "semantic_euler_label"),
    ("control_formable", "control_formable"),
)


def same_internal_domain(data) -> bool:
    return data["domain_id"] == INTERNAL_DOMAIN and all(
        data["atom_domains"].get(atom) == INTERNAL_DOMAIN for atom in ATOMS
    )


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    edges = set(data["domain_edges"])
    if not same_internal_domain(data):
        out.append("atom_domains_not_same_internal_stratum")
    if not connected(ATOMS, edges):
        out.append("domain_atom_graph_not_connected")
    if not REQUIRED_DOMAIN_EDGES <= edges:
        out.append("required_domain_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_internal_domain(data) -> bool:
    edges = set(data["domain_edges"])
    return (
        all(data[key] for key, _ in REQUIRED)
        and same_internal_domain(data)
        and connected(ATOMS, edges)
        and REQUIRED_DOMAIN_EDGES <= edges
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_object_maps_cycles=True,
        internal_effectivity_stratum_actual=True,
        domain_generated_by_qbar_object=True,
        prime_power_towers_internal=True,
        valuation_depth_internal=True,
        euler_address_internal=True,
        cartier_effectivity_strata_native=True,
        strata_specialization_maps_native=True,
        endpoint_pushforward_typed_by_internal_domain=True,
        boundary_localization_typed_by_internal_domain=True,
        graph_composition_typed_by_internal_domain=True,
        rosati_typed_by_internal_domain=True,
        count_degree_typed_by_internal_domain=True,
        controls_undefined_at_internal_domain=True,
        epstein_undefined_at_internal_domain=True,
        theta_shadow_only_downstream=True,
        non_split_domain_atom_graph=True,
        domain_id=INTERNAL_DOMAIN,
        atom_domains=all_atom_domains(INTERNAL_DOMAIN),
        domain_edges=set(REQUIRED_DOMAIN_EDGES),
        control_formable=False,
    )
    data.update(kwargs)
    return data


split_domains = live_source(
    atom_domains={
        "effectivity_domain": INTERNAL_DOMAIN,
        "endpoint": "D_endpoint_register",
        "boundary": INTERNAL_DOMAIN,
        "pushforward": INTERNAL_DOMAIN,
        "graph": INTERNAL_DOMAIN,
        "rosati": INTERNAL_DOMAIN,
        "count_degree": INTERNAL_DOMAIN,
        "control_death": INTERNAL_DOMAIN,
    }
)

gate(
    "IED1 every atom must be typed by the same internal stratum",
    accepts_internal_domain(live_source())
    and not accepts_internal_domain(split_domains)
    and "atom_domains_not_same_internal_stratum" in reasons(split_domains),
    ",".join(reasons(split_domains)),
)


tower = prime_power_tower(2, 7)
depths = [valuation_depth(n, 2) for n in tower]
external_prime_monoid = live_source(
    carrier_native=False,
    represented_object_maps_cycles=False,
    internal_effectivity_stratum_actual=False,
    domain_generated_by_qbar_object=False,
    prime_power_towers_internal=False,
    valuation_depth_internal=False,
    euler_address_internal=False,
    cartier_effectivity_strata_native=False,
    strata_specialization_maps_native=False,
    endpoint_pushforward_typed_by_internal_domain=False,
    boundary_localization_typed_by_internal_domain=False,
    graph_composition_typed_by_internal_domain=False,
    rosati_typed_by_internal_domain=False,
    count_degree_typed_by_internal_domain=False,
    controls_undefined_at_internal_domain=False,
    domain_id="N_primes",
    atom_domains=all_atom_domains("N_primes"),
    domain_edges=set(),
    external_prime_monoid=True,
    free_commutative_prime_monoid=True,
    control_formable=True,
)

gate(
    "IED2 external prime monoid has towers but no internal Qbar stratum",
    tower == [1, 2, 4, 8, 16, 32, 64]
    and depths == [0, 1, 2, 3, 4, 5, 6]
    and not accepts_internal_domain(external_prime_monoid)
    and {
        "object_maps_cycles_not_represented",
        "internal_stratum_not_actual",
        "domain_not_generated_by_qbar_object",
        "atom_domains_not_same_internal_stratum",
        "external_prime_monoid",
        "free_commutative_prime_monoid",
        "control_formable",
    }
    <= set(reasons(external_prime_monoid)),
    "tower=%s depths=%s reasons=%s"
    % (tower, depths, ",".join(reasons(external_prime_monoid))),
)


pair_window = {(a, b): endpoint_pair_code(a, b) for a in range(4) for b in range(4)}
codec_labels_distinct = len(set(pair_window.values())) == len(pair_window)
codec = live_source(
    internal_effectivity_stratum_actual=False,
    domain_generated_by_qbar_object=False,
    prime_power_towers_internal=False,
    valuation_depth_internal=False,
    euler_address_internal=False,
    endpoint_pushforward_typed_by_internal_domain=False,
    count_degree_typed_by_internal_domain=False,
    domain_id="N_pair_code",
    atom_domains=all_atom_domains("N_pair_code"),
    degree_pair_codec=True,
    control_formable=True,
)

gate(
    "IED3 prime-power pair codecs are labels, not internal domain strata",
    codec_labels_distinct
    and pair_window[(1, 0)] == 2
    and pair_window[(0, 1)] == 3
    and not accepts_internal_domain(codec)
    and {
        "internal_stratum_not_actual",
        "domain_not_generated_by_qbar_object",
        "prime_power_towers_not_internal",
        "endpoint_pushforward_not_typed_by_internal_domain",
        "degree_pair_codec",
        "control_formable",
    }
    <= set(reasons(codec)),
    "labels=%d reasons=%s" % (len(set(pair_window.values())), ",".join(reasons(codec))),
)


directions = {(1, 0), (0, 1), (1, 1), (1, -1), (2, 1)}
register = live_source(
    internal_effectivity_stratum_actual=False,
    domain_generated_by_qbar_object=False,
    cartier_effectivity_strata_native=False,
    strata_specialization_maps_native=False,
    boundary_localization_typed_by_internal_domain=False,
    domain_id="Z2_endpoint_register",
    atom_domains=all_atom_domains("Z2_endpoint_register"),
    valuation_register=True,
    endpoint_register=True,
    control_formable=True,
)

gate(
    "IED4 endpoint valuation registers choose boundary direction externally",
    len(directions) == 5
    and (1, 0) in directions
    and (0, 1) in directions
    and not accepts_internal_domain(register)
    and {
        "internal_stratum_not_actual",
        "domain_not_generated_by_qbar_object",
        "cartier_strata_not_native",
        "boundary_localization_not_typed_by_internal_domain",
        "valuation_register",
        "endpoint_register",
        "control_formable",
    }
    <= set(reasons(register)),
    "directions=%s reasons=%s" % (sorted(directions), ",".join(reasons(register))),
)


local_domains = {
    "effectivity_domain": "prod_local_Dp",
    "endpoint": "D_2",
    "boundary": "D_3",
    "pushforward": "D_3",
    "graph": "D_5",
    "rosati": "D_5",
    "count_degree": "D_7",
    "control_death": "posthoc_filter",
}
local_euler_stack = live_source(
    non_split_domain_atom_graph=False,
    domain_id="prod_local_Dp",
    atom_domains=local_domains,
    local_euler_factor_only=True,
    finite_prime_sample=True,
    control_formable=True,
)

gate(
    "IED5 local Euler-factor stacks split the domain across atoms",
    not accepts_internal_domain(local_euler_stack)
    and {
        "domain_atom_graph_split",
        "atom_domains_not_same_internal_stratum",
        "local_euler_factor_only",
        "finite_prime_sample",
        "control_formable",
    }
    <= set(reasons(local_euler_stack)),
    ",".join(reasons(local_euler_stack)),
)


cartier_strata = [
    {"domain": INTERNAL_DOMAIN, "value": 2**k, "depth": k, "p1_degree": 2**k, "p2_degree": 1}
    for k in range(6)
]
specialization_edges = [
    (cartier_strata[k]["value"], cartier_strata[k + 1]["value"])
    for k in range(len(cartier_strata) - 1)
]
cartier_candidate = live_source()

gate(
    "IED6 accepted shape is an internal Cartier/effectivity stratum tower",
    accepts_internal_domain(cartier_candidate)
    and [row["depth"] for row in cartier_strata] == [0, 1, 2, 3, 4, 5]
    and [row["value"] for row in cartier_strata] == [1, 2, 4, 8, 16, 32]
    and all(isinstance(row["p1_degree"], int) and row["p2_degree"] == 1 for row in cartier_strata)
    and specialization_edges == [(1, 2), (2, 4), (4, 8), (8, 16), (16, 32)],
    "strata=%s edges=%s" % (cartier_strata, specialization_edges),
)


rq = represented_values(36)
irreducibles = irreducibles_in_monoid(rq, 36)
fact36 = irreducible_factorizations(36, irreducibles)
epstein_shadow = live_source(
    internal_effectivity_stratum_actual=False,
    domain_generated_by_qbar_object=False,
    prime_power_towers_internal=False,
    valuation_depth_internal=False,
    euler_address_internal=False,
    epstein_undefined_at_internal_domain=False,
    domain_id="Epstein_norm_shadow",
    atom_domains=all_atom_domains("Epstein_norm_shadow"),
    represented_norm_shadow_promoted=True,
    control_formable=True,
)

gate(
    "IED7 Epstein norm shadows remain downstream, not the internal domain",
    {1, 4, 6, 9, 36} <= rq
    and {(4, 9), (6, 6)} <= fact36
    and not accepts_internal_domain(epstein_shadow)
    and {
        "internal_stratum_not_actual",
        "domain_not_generated_by_qbar_object",
        "prime_power_towers_not_internal",
        "epstein_not_undefined_at_internal_domain",
        "represented_norm_shadow_promoted",
        "control_formable",
    }
    <= set(reasons(epstein_shadow)),
    "fact36=%s reasons=%s" % (sorted(fact36), ",".join(reasons(epstein_shadow))),
)


formal_control_shadow = {
    "formal_graph_law": True,
    "formal_rosati_shadow": True,
    "formal_count_shadow": True,
}
control_package = live_source(
    carrier_native=False,
    represented_object_maps_cycles=False,
    internal_effectivity_stratum_actual=False,
    domain_generated_by_qbar_object=False,
    controls_undefined_at_internal_domain=False,
    domain_id="formal_control",
    atom_domains=all_atom_domains("formal_control"),
    semantic_euler_label=True,
    control_formable=True,
)

gate(
    "IED8 controls may have formal shadows but no internal effectivity domain",
    all(formal_control_shadow.values())
    and not accepts_internal_domain(control_package)
    and {
        "not_carrier_native",
        "object_maps_cycles_not_represented",
        "internal_stratum_not_actual",
        "controls_not_undefined_at_internal_domain",
        "semantic_euler_label",
        "control_formable",
    }
    <= set(reasons(control_package)),
    ",".join(reasons(control_package)),
)


declared_internal = live_source(
    represented_object_maps_cycles=False,
    internal_effectivity_stratum_actual=False,
    domain_generated_by_qbar_object=False,
    cartier_effectivity_strata_native=False,
    declared_internal_domain=True,
)

gate(
    "IED9 declared internal domain IDs without represented strata are rejected",
    same_internal_domain(declared_internal)
    and not accepts_internal_domain(declared_internal)
    and {
        "object_maps_cycles_not_represented",
        "internal_stratum_not_actual",
        "domain_not_generated_by_qbar_object",
        "cartier_strata_not_native",
        "declared_internal_domain",
    }
    <= set(reasons(declared_internal)),
    ",".join(reasons(declared_internal)),
)


dead_sources = {
    "split_domains": split_domains,
    "external_prime_monoid": external_prime_monoid,
    "codec": codec,
    "register": register,
    "local_euler_stack": local_euler_stack,
    "epstein_shadow": epstein_shadow,
    "control_package": control_package,
    "declared_internal": declared_internal,
}

gate(
    "IED10 only the represented internal effectivity stratum passes",
    accepts_internal_domain(live_source())
    and not any(accepts_internal_domain(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_internal_domain(data) for data in dead_sources.values()),
        accepts_internal_domain(live_source()),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nIED1-IED10 ALL PASS: internal effectivity-domain contract pinned")
print(
    "VERDICT: Qbar_BECD's Euler/effectivity domain must be a represented "
    "internal stratum of the same compactified square that types endpoint "
    "pushforwards, boundary localization, graph/composition, Rosati, "
    "count/degree anchors, and control death. External prime monoids, "
    "valuation registers, degree-pair codecs, local Euler-factor stacks, "
    "declared domain IDs, Epstein norm shadows, and control-formable packages "
    "do not meet this contract."
)
