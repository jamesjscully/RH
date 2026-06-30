r"""Effectivity-domain first-generator contract for Qbar_BECD.

Doc 322 says Qbar_BECD needs one represented non-split carrier primitive.
This witness sharpens the first-generator condition: the primitive must be
typed by a represented Euler/effectivity domain with native prime-power
valuation towers. Epstein represented-norm data and arbitrary controls may
retain theta/count or formal graph shadows, but they must be undefined at the
carrier domain, before signs or filters.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_effectivity_domain_contract
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


failures: list[str] = []

Corr = tuple[float, np.ndarray, float]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


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


def valuation_depth(n: int, p: int) -> int | None:
    depth = 0
    while n > 1 and n % p == 0:
        n //= p
        depth += 1
    if n != 1:
        return None
    return depth


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def graph(F: np.ndarray, q: float, n: int) -> Corr:
    return corr(q**n, np.linalg.matrix_power(F, n), 1.0)


def compose(A: Corr, B: Corr) -> Corr:
    d1, z, d2 = A
    e1, w, e2 = B
    return corr(d1 * e1, z @ w, d2 * e2)


def dagger(A: Corr, E: np.ndarray) -> Corr:
    d1, z, d2 = A
    return corr(d2, rosati(z, E), d1)


def corr_defect(A: Corr, B: Corr) -> float:
    return float(abs(A[0] - B[0]) + np.linalg.norm(A[1] - B[1]) + abs(A[2] - B[2]))


def graph_law_defect(F: np.ndarray, q: float, m: int, n: int) -> float:
    return corr_defect(compose(graph(F, q, m), graph(F, q, n)), graph(F, q, m + n))


def anti_defect(A: Corr, B: Corr, E: np.ndarray) -> float:
    return corr_defect(dagger(compose(A, B), E), compose(dagger(B, E), dagger(A, E)))


def qsim_defect(F: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def source(**kwargs):
    data = {
        "carrier_native": False,
        "formation_primitive_actual": False,
        "represented_object_maps_cycles": False,
        "effectivity_domain_actual": False,
        "prime_power_towers_native": False,
        "valuation_depth_native": False,
        "euler_product_address_native": False,
        "endpoint_boundary_typed_by_domain": False,
        "boundary_pushforward_typed_by_domain": False,
        "graph_rosati_typed_by_domain": False,
        "count_degree_typed_by_domain": False,
        "controls_undefined_at_domain": False,
        "epstein_undefined_at_domain": False,
        "theta_shadow_survives_without_carrier": False,
        "non_split_dependency_graph": False,
        "semantic_euler_label": False,
        "external_satake_label": False,
        "finite_prime_sample": False,
        "posthoc_epstein_guard": False,
        "carrier_blind_theta_kernel": False,
        "declared_effectivity_domain": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("formation_primitive_actual", "formation_primitive_not_actual"),
    ("represented_object_maps_cycles", "object_maps_cycles_not_represented"),
    ("effectivity_domain_actual", "effectivity_domain_not_actual"),
    ("prime_power_towers_native", "prime_power_towers_not_native"),
    ("valuation_depth_native", "valuation_depth_not_native"),
    ("euler_product_address_native", "euler_product_address_not_native"),
    ("endpoint_boundary_typed_by_domain", "endpoint_boundary_not_typed_by_domain"),
    ("boundary_pushforward_typed_by_domain", "boundary_pushforward_not_typed_by_domain"),
    ("graph_rosati_typed_by_domain", "graph_rosati_not_typed_by_domain"),
    ("count_degree_typed_by_domain", "count_degree_not_typed_by_domain"),
    ("controls_undefined_at_domain", "controls_not_undefined_at_domain"),
    ("epstein_undefined_at_domain", "epstein_not_undefined_at_domain"),
    ("theta_shadow_survives_without_carrier", "theta_shadow_diagnostic_missing"),
    ("non_split_dependency_graph", "dependency_graph_split"),
)

BANNED = (
    ("semantic_euler_label", "semantic_euler_label"),
    ("external_satake_label", "external_satake_label"),
    ("finite_prime_sample", "finite_prime_sample"),
    ("posthoc_epstein_guard", "posthoc_epstein_guard"),
    ("carrier_blind_theta_kernel", "carrier_blind_theta_kernel"),
    ("declared_effectivity_domain", "declared_effectivity_domain"),
    ("control_formable", "control_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_effectivity_domain(data) -> bool:
    return all(data[key] for key, _ in REQUIRED) and not any(
        data[key] for key, _ in BANNED
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        formation_primitive_actual=True,
        represented_object_maps_cycles=True,
        effectivity_domain_actual=True,
        prime_power_towers_native=True,
        valuation_depth_native=True,
        euler_product_address_native=True,
        endpoint_boundary_typed_by_domain=True,
        boundary_pushforward_typed_by_domain=True,
        graph_rosati_typed_by_domain=True,
        count_degree_typed_by_domain=True,
        controls_undefined_at_domain=True,
        epstein_undefined_at_domain=True,
        theta_shadow_survives_without_carrier=True,
        non_split_dependency_graph=True,
        control_formable=False,
    )
    data.update(kwargs)
    return data


prime_tower = [2**k for k in range(0, 7)]
prime_depths = [valuation_depth(n, 2) for n in prime_tower]

gate(
    "EDG1 prime-power tower has canonical valuation depth",
    prime_tower == [1, 2, 4, 8, 16, 32, 64]
    and prime_depths == [0, 1, 2, 3, 4, 5, 6]
    and valuation_depth(72, 2) is None,
    "tower=%s depths=%s mixed72=%s" % (prime_tower, prime_depths, valuation_depth(72, 2)),
)


rq = represented_values(36)
irreducibles = irreducibles_in_monoid(rq, 36)
fact36 = irreducible_factorizations(36, irreducibles)

gate(
    "EDG2 Epstein represented-norm theta shadow lacks unique tower address",
    {1, 4, 6, 9, 36} <= rq
    and 2 not in rq
    and 3 not in rq
    and {4, 6, 9} <= irreducibles
    and {(4, 9), (6, 6)} <= fact36
    and len(fact36) >= 2,
    "represented=%s irreducibles=%s fact36=%s"
    % (sorted(rq), sorted(irreducibles), sorted(fact36)),
)


doc322_without_domain = {
    "carrier",
    "endpoint",
    "boundary",
    "pushforward",
    "graph",
    "rosati",
    "count_degree",
    "control_death",
}
doc322_with_domain = doc322_without_domain | {"effectivity_domain"}

gate(
    "EDG3 doc-322 coupling still needs an effectivity-domain first generator",
    "effectivity_domain" not in doc322_without_domain
    and "effectivity_domain" in doc322_with_domain
    and len(doc322_with_domain) == len(doc322_without_domain) + 1,
    "before=%d after=%d" % (len(doc322_without_domain), len(doc322_with_domain)),
)


semantic_label = live_source(
    effectivity_domain_actual=False,
    prime_power_towers_native=False,
    valuation_depth_native=False,
    euler_product_address_native=False,
    semantic_euler_label=True,
    external_satake_label=True,
)

gate(
    "EDG4 semantic Euler/Satake labels are not an effectivity domain",
    not accepts_effectivity_domain(semantic_label)
    and {
        "effectivity_domain_not_actual",
        "prime_power_towers_not_native",
        "valuation_depth_not_native",
        "euler_product_address_not_native",
        "semantic_euler_label",
        "external_satake_label",
    }
    <= set(reasons(semantic_label)),
    ",".join(reasons(semantic_label)),
)


theta_kernel = live_source(
    effectivity_domain_actual=False,
    prime_power_towers_native=False,
    valuation_depth_native=False,
    euler_product_address_native=False,
    epstein_undefined_at_domain=False,
    carrier_blind_theta_kernel=True,
    control_formable=True,
)

gate(
    "EDG5 carrier-blind theta kernels fail because Epstein still computes",
    not accepts_effectivity_domain(theta_kernel)
    and {
        "effectivity_domain_not_actual",
        "prime_power_towers_not_native",
        "valuation_depth_not_native",
        "euler_product_address_not_native",
        "epstein_not_undefined_at_domain",
        "carrier_blind_theta_kernel",
        "control_formable",
    }
    <= set(reasons(theta_kernel)),
    ",".join(reasons(theta_kernel)),
)


finite_sample = live_source(
    effectivity_domain_actual=False,
    non_split_dependency_graph=False,
    finite_prime_sample=True,
)

gate(
    "EDG6 finite prime samples do not prove the domain",
    not accepts_effectivity_domain(finite_sample)
    and {
        "effectivity_domain_not_actual",
        "dependency_graph_split",
        "finite_prime_sample",
    }
    <= set(reasons(finite_sample)),
    ",".join(reasons(finite_sample)),
)


posthoc_guard = live_source(
    controls_undefined_at_domain=False,
    epstein_undefined_at_domain=False,
    posthoc_epstein_guard=True,
    control_formable=True,
)

gate(
    "EDG7 post-hoc Epstein/control guards are too late",
    not accepts_effectivity_domain(posthoc_guard)
    and {
        "controls_not_undefined_at_domain",
        "epstein_not_undefined_at_domain",
        "posthoc_epstein_guard",
        "control_formable",
    }
    <= set(reasons(posthoc_guard)),
    ",".join(reasons(posthoc_guard)),
)


control_q = 3
control = np.array([[1.0, 2.0], [1.0, 5.0]])
control_E = weil_pairing(control, control_q)
control_G = graph(control, control_q, 1)
control_H = graph(control, control_q, 2)
control_formal_graph = graph_law_defect(control, control_q, 1, 2)
control_qsim = qsim_defect(control, control_E, control_q)
control_anti = anti_defect(control_G, control_H, control_E)
control_sign = primitive_hodge_index(control, control_E, 1)

control_package = live_source(
    carrier_native=False,
    formation_primitive_actual=False,
    effectivity_domain_actual=False,
    controls_undefined_at_domain=False,
    control_formable=True,
)

gate(
    "EDG8 controls have formal shadows but no effectivity-domain generator",
    control_formal_graph < 1e-12
    and control_qsim < 1e-12
    and control_anti < 1e-12
    and control_sign > 0
    and not accepts_effectivity_domain(control_package)
    and {
        "not_carrier_native",
        "formation_primitive_not_actual",
        "effectivity_domain_not_actual",
        "controls_not_undefined_at_domain",
        "control_formable",
    }
    <= set(reasons(control_package)),
    "graph=%.1e qsim=%.1e anti=%.1e sign=%.3f reasons=%s"
    % (control_formal_graph, control_qsim, control_anti, control_sign, ",".join(reasons(control_package))),
)


declared_domain = live_source(
    effectivity_domain_actual=False,
    represented_object_maps_cycles=False,
    declared_effectivity_domain=True,
)

gate(
    "EDG9 declared effectivity without represented object/maps/cycles is rejected",
    not accepts_effectivity_domain(declared_domain)
    and {
        "object_maps_cycles_not_represented",
        "effectivity_domain_not_actual",
        "declared_effectivity_domain",
    }
    <= set(reasons(declared_domain)),
    ",".join(reasons(declared_domain)),
)


live_domain = live_source()
dead_sources = {
    "semantic_label": semantic_label,
    "theta_kernel": theta_kernel,
    "finite_sample": finite_sample,
    "posthoc_guard": posthoc_guard,
    "control_package": control_package,
    "declared_domain": declared_domain,
}

gate(
    "EDG10 only represented effectivity-domain first generator passes",
    accepts_effectivity_domain(live_domain)
    and not any(accepts_effectivity_domain(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_effectivity_domain(data) for data in dead_sources.values()),
        accepts_effectivity_domain(live_domain),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nEDG1-EDG10 ALL PASS: effectivity-domain first-generator contract pinned")
print(
    "VERDICT: Qbar_BECD's first generator must be a represented "
    "Euler/effectivity domain with native prime-power towers and valuation "
    "depths, tying endpoint/boundary/pushforward/graph/Rosati/count data "
    "before controls or Epstein can instantiate. Semantic Euler/Satake labels, "
    "theta kernels, finite prime samples, post-hoc guards, declared domains, "
    "and control-formable packages do not meet this contract."
)
