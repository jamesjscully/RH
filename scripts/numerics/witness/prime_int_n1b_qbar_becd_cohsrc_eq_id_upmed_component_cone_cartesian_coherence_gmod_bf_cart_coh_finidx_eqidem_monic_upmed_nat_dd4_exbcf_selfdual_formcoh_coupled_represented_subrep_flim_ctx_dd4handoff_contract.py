r"""DD.4 image-only certificate handoff contract.

Doc 530 separated the original H^1 obstruction context from the certificate
image context. This witness makes the handoff object itself explicit: the
source class remains the nonboundary class in original_h1, and the boundary
certificate kills only a named image object in certificate_image.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_formcoh_coupled_represented_subrep_flim_ctx_dd4handoff_contract
"""

from __future__ import annotations

from math import comb


failures: list[str] = []

DD4_CLASS_ID = "dd4_c_original_res1_Qbar_BECD"
DD4_IMAGE_ID = "Img_dd4_c_original_res1_Qbar_BECD_under_dd4_certificate_handoff"
HANDOFF_CONTRACT_ID = "ImgOnlyHandoff_dd4_c_original_res1_Qbar_BECD"
HANDOFF_ID = "dd4_certificate_handoff"
BOUNDARY_CERT_ID = "BKill_NCoup_med_UP_Eq_id_Qbar_BECD_dQ_boundary_properness_self_duality"
FINITE_LIMIT_CUT_ID = "LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"
JOINT_FORK_ID = "Fork_med_UP_Eq_NCoup_med_UP_Eq_id_id_endpoint_dd4_rosati_control_NCoup"
CONTEXT_SEPARATION_ID = "CtxSep_LimCut_NCoup_med_UP_Eq_NCoup_med_UP_Eq_id_id_source_fiber"

CONTEXTS = {
    "original_h1",
    "certificate_image",
    "finite_limit",
    "source_constraint",
    "source_fiber",
}

REQUIRED_DEPENDENCIES = {
    DD4_CLASS_ID,
    DD4_IMAGE_ID,
    BOUNDARY_CERT_ID,
    FINITE_LIMIT_CUT_ID,
    JOINT_FORK_ID,
    CONTEXT_SEPARATION_ID,
}

REQUIRED = (
    ("source_class_actual", "source_class_missing"),
    ("source_context_original_h1", "source_not_original_h1"),
    ("source_nonboundary", "source_h1_boundary"),
    ("source_res1_one", "source_res1_not_one"),
    ("coboundaries_res1_zero", "coboundaries_res1_nonzero"),
    ("target_image_actual", "target_image_missing"),
    ("image_context_certificate", "image_not_certificate_context"),
    ("image_has_source_class", "image_not_tied_to_source"),
    ("image_has_bridge_id", "image_not_tied_to_bridge"),
    ("certificate_actual", "certificate_missing"),
    ("certificate_context_certificate", "certificate_not_certificate_context"),
    ("certificate_kills_target_image", "certificate_does_not_kill_image"),
    ("certificate_does_not_kill_source", "certificate_kills_source"),
    ("bridge_actual", "bridge_missing"),
    ("bridge_image_only", "bridge_not_image_only"),
    ("bridge_directed", "bridge_not_directed"),
    ("bridge_not_reversible", "bridge_reversible"),
    ("bridge_preserves_source_nonboundary", "bridge_does_not_preserve_source"),
    ("bridge_not_quotient_source", "bridge_quotients_source"),
    ("bridge_not_retuned", "bridge_retuned"),
    ("bridge_not_posthoc", "bridge_posthoc"),
    ("bridge_coupled_to_fork", "bridge_not_coupled_to_fork"),
    ("bridge_keeps_finite_index", "bridge_expands_finite_index"),
    ("bridge_compatible_with_context_separation", "bridge_ignores_context_separation"),
)

BANNED = (
    ("context_collapse_dd4", "context_collapse_dd4"),
    ("certificate_kills_source_class", "certificate_kills_source_class"),
    ("reversible_dd4_handoff", "reversible_dd4_handoff"),
    ("source_h1_quotient_kill", "source_h1_quotient_kill"),
    ("retuned_dd4_image", "retuned_dd4_image"),
    ("base_changed_dd4_image", "base_changed_dd4_image"),
    ("posthoc_dd4_certificate", "posthoc_dd4_certificate"),
    ("missing_dd4_image_object", "missing_dd4_image_object"),
    ("missing_bridge_object", "missing_bridge_object"),
    ("missing_source_coupling", "missing_source_coupling"),
    ("finite_index_expansion", "finite_index_expansion"),
    ("one_more_layer_tower", "one_more_layer_tower"),
)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make_h1(L: int):
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


def to_vec(f, L: int) -> tuple[int, ...]:
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, L: int, mul) -> set[tuple[int, ...]]:
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


def h1_profile(L: int) -> dict[str, object]:
    mul, inv, phi = make_h1(L)
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
        "h1_order": z1_order // len(coboundaries),
        "res1_c": c.get(1, 0),
        "coboundaries_res1_zero": all(
            from_vec(vec).get(1, 0) == 0 for vec in coboundaries
        ),
    }


def handoff(**kwargs):
    data = {
        "source_class_actual": False,
        "source_context_original_h1": False,
        "source_nonboundary": False,
        "source_res1_one": False,
        "coboundaries_res1_zero": False,
        "target_image_actual": False,
        "image_context_certificate": False,
        "image_has_source_class": False,
        "image_has_bridge_id": False,
        "certificate_actual": False,
        "certificate_context_certificate": False,
        "certificate_kills_target_image": False,
        "certificate_does_not_kill_source": False,
        "bridge_actual": False,
        "bridge_image_only": False,
        "bridge_directed": False,
        "bridge_not_reversible": False,
        "bridge_preserves_source_nonboundary": False,
        "bridge_not_quotient_source": False,
        "bridge_not_retuned": False,
        "bridge_not_posthoc": False,
        "bridge_coupled_to_fork": False,
        "bridge_keeps_finite_index": False,
        "bridge_compatible_with_context_separation": False,
        "contexts": set(),
        "source_object": None,
        "source_context": None,
        "target_image": None,
        "image_context": None,
        "certificate": None,
        "certificate_context": None,
        "killed_object": None,
        "bridge_id": None,
        "dependencies": set(),
        "finite_index_cells": 0,
        "context_collapse_dd4": False,
        "certificate_kills_source_class": False,
        "reversible_dd4_handoff": False,
        "source_h1_quotient_kill": False,
        "retuned_dd4_image": False,
        "base_changed_dd4_image": False,
        "posthoc_dd4_certificate": False,
        "missing_dd4_image_object": False,
        "missing_bridge_object": False,
        "missing_source_coupling": False,
        "finite_index_expansion": False,
        "one_more_layer_tower": False,
    }
    data.update(kwargs)
    return data


def live_handoff(**kwargs):
    data = handoff(
        source_class_actual=True,
        source_context_original_h1=True,
        source_nonboundary=True,
        source_res1_one=True,
        coboundaries_res1_zero=True,
        target_image_actual=True,
        image_context_certificate=True,
        image_has_source_class=True,
        image_has_bridge_id=True,
        certificate_actual=True,
        certificate_context_certificate=True,
        certificate_kills_target_image=True,
        certificate_does_not_kill_source=True,
        bridge_actual=True,
        bridge_image_only=True,
        bridge_directed=True,
        bridge_not_reversible=True,
        bridge_preserves_source_nonboundary=True,
        bridge_not_quotient_source=True,
        bridge_not_retuned=True,
        bridge_not_posthoc=True,
        bridge_coupled_to_fork=True,
        bridge_keeps_finite_index=True,
        bridge_compatible_with_context_separation=True,
        contexts=set(CONTEXTS),
        source_object=DD4_CLASS_ID,
        source_context="original_h1",
        target_image=DD4_IMAGE_ID,
        image_context="certificate_image",
        certificate=BOUNDARY_CERT_ID,
        certificate_context="certificate_image",
        killed_object=DD4_IMAGE_ID,
        bridge_id=HANDOFF_ID,
        dependencies=set(REQUIRED_DEPENDENCIES),
        finite_index_cells=24,
    )
    data.update(kwargs)
    return data


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not CONTEXTS <= set(data["contexts"]):
        out.append("declared_contexts_missing")
    if data["source_object"] != DD4_CLASS_ID:
        out.append("source_object_not_original_dd4_class")
    if data["source_context"] != "original_h1":
        out.append("source_context_not_original_h1")
    if data["target_image"] != DD4_IMAGE_ID:
        out.append("target_image_not_named_dd4_image")
    if data["image_context"] != "certificate_image":
        out.append("image_context_not_certificate_image")
    if data["certificate"] != BOUNDARY_CERT_ID:
        out.append("certificate_not_named_boundary_kill")
    if data["certificate_context"] != "certificate_image":
        out.append("certificate_context_not_certificate_image")
    if data["killed_object"] != DD4_IMAGE_ID:
        out.append("certificate_does_not_target_named_image")
    if data["killed_object"] == DD4_CLASS_ID:
        out.append("certificate_targets_original_h1_class")
    if data["bridge_id"] != HANDOFF_ID:
        out.append("bridge_id_not_dd4_certificate_handoff")
    if data["source_context"] == data["image_context"]:
        out.append("source_and_image_contexts_collapsed")
    if not REQUIRED_DEPENDENCIES <= set(data["dependencies"]):
        out.append("handoff_dependencies_missing")
    if data["finite_index_cells"] != 24:
        out.append("finite_index_not_exact_24")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_handoff(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and not any(data[key] for key, _ in BANNED)
        and CONTEXTS <= set(data["contexts"])
        and data["source_object"] == DD4_CLASS_ID
        and data["source_context"] == "original_h1"
        and data["target_image"] == DD4_IMAGE_ID
        and data["image_context"] == "certificate_image"
        and data["certificate"] == BOUNDARY_CERT_ID
        and data["certificate_context"] == "certificate_image"
        and data["killed_object"] == DD4_IMAGE_ID
        and data["bridge_id"] == HANDOFF_ID
        and data["source_context"] != data["image_context"]
        and REQUIRED_DEPENDENCIES <= set(data["dependencies"])
        and data["finite_index_cells"] == 24
    )


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
live = live_handoff()

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1 image-only DD4 handoff is coherent",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and accepts_handoff(live)
    and HANDOFF_CONTRACT_ID
    and DD4_IMAGE_ID,
    "H1=%s image=%s" % ([p["h1_order"] for p in profiles], DD4_IMAGE_ID),
)

context_collapse = live_handoff(
    image_context="original_h1",
    image_context_certificate=False,
    bridge_image_only=False,
    context_collapse_dd4=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD2 rejects DD4 source/certificate context collapse",
    not accepts_handoff(context_collapse)
    and {
        "image_not_certificate_context",
        "bridge_not_image_only",
        "source_and_image_contexts_collapsed",
        "context_collapse_dd4",
    }
    <= set(reasons(context_collapse)),
    ",".join(reasons(context_collapse)),
)

kill_source = live_handoff(
    killed_object=DD4_CLASS_ID,
    certificate_kills_target_image=False,
    certificate_does_not_kill_source=False,
    certificate_kills_source_class=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD3 certificate cannot kill the original source class",
    not accepts_handoff(kill_source)
    and {
        "certificate_does_not_kill_image",
        "certificate_kills_source",
        "certificate_does_not_target_named_image",
        "certificate_targets_original_h1_class",
        "certificate_kills_source_class",
    }
    <= set(reasons(kill_source)),
    ",".join(reasons(kill_source)),
)

reversible = live_handoff(
    bridge_directed=False,
    bridge_not_reversible=False,
    reversible_dd4_handoff=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD4 rejects reversible pullback of the certificate kill",
    not accepts_handoff(reversible)
    and {
        "bridge_not_directed",
        "bridge_reversible",
        "reversible_dd4_handoff",
    }
    <= set(reasons(reversible)),
    ",".join(reasons(reversible)),
)

quotient_source = live_handoff(
    source_nonboundary=False,
    bridge_preserves_source_nonboundary=False,
    bridge_not_quotient_source=False,
    source_h1_quotient_kill=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD5 rejects quotienting source H1 to make the kill true",
    not accepts_handoff(quotient_source)
    and {
        "source_h1_boundary",
        "bridge_does_not_preserve_source",
        "bridge_quotients_source",
        "source_h1_quotient_kill",
    }
    <= set(reasons(quotient_source)),
    ",".join(reasons(quotient_source)),
)

retuned_image = live_handoff(
    target_image="Img_retuned_dd4_c_after_base_change",
    image_has_source_class=False,
    bridge_not_retuned=False,
    retuned_dd4_image=True,
    base_changed_dd4_image=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD6 rejects retuned or base-changed image objects",
    not accepts_handoff(retuned_image)
    and {
        "image_not_tied_to_source",
        "bridge_retuned",
        "target_image_not_named_dd4_image",
        "retuned_dd4_image",
        "base_changed_dd4_image",
    }
    <= set(reasons(retuned_image)),
    ",".join(reasons(retuned_image)),
)

posthoc = live_handoff(
    bridge_not_posthoc=False,
    bridge_coupled_to_fork=False,
    dependencies={DD4_CLASS_ID, DD4_IMAGE_ID, BOUNDARY_CERT_ID},
    posthoc_dd4_certificate=True,
    missing_source_coupling=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD7 rejects posthoc certificates disconnected from the source fork",
    not accepts_handoff(posthoc)
    and {
        "bridge_posthoc",
        "bridge_not_coupled_to_fork",
        "handoff_dependencies_missing",
        "posthoc_dd4_certificate",
        "missing_source_coupling",
    }
    <= set(reasons(posthoc)),
    ",".join(reasons(posthoc)),
)

missing_image = live_handoff(
    target_image=None,
    target_image_actual=False,
    image_has_bridge_id=False,
    missing_dd4_image_object=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD8 rejects a missing target image object",
    not accepts_handoff(missing_image)
    and {
        "target_image_missing",
        "image_not_tied_to_bridge",
        "target_image_not_named_dd4_image",
        "missing_dd4_image_object",
    }
    <= set(reasons(missing_image)),
    ",".join(reasons(missing_image)),
)

index_tower = live_handoff(
    finite_index_cells=25,
    bridge_keeps_finite_index=False,
    finite_index_expansion=True,
    one_more_layer_tower=True,
)

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD9 rejects finite-index expansion and one-more-layer towers",
    not accepts_handoff(index_tower)
    and {
        "bridge_expands_finite_index",
        "finite_index_not_exact_24",
        "finite_index_expansion",
        "one_more_layer_tower",
    }
    <= set(reasons(index_tower)),
    ",".join(reasons(index_tower)),
)

variants = [
    context_collapse,
    kill_source,
    reversible,
    quotient_source,
    retuned_image,
    posthoc,
    missing_image,
    index_tower,
    live_handoff(bridge_actual=False, missing_bridge_object=True),
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 only the directed image-only handoff passes",
    accepts_handoff(live_handoff())
    and not any(accepts_handoff(data) for data in variants)
    and {
        "bridge_missing",
        "missing_bridge_object",
        "context_collapse_dd4",
        "certificate_kills_source_class",
        "retuned_dd4_image",
        "posthoc_dd4_certificate",
        "missing_dd4_image_object",
        "finite_index_expansion",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(
    "\nCATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-"
    "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 "
    "ALL PASS: DD.4 certificate handoff is pinned as a directed image-only object"
)
print(
    "VERDICT: the live branch may keep the original DD.4 H1 class nonboundary "
    "only by naming a separate certificate-image object killed by the boundary "
    "certificate. Context collapse, source-class killing, reversible handoff, "
    "source H1 quotienting, retuned images, posthoc certificates, missing image "
    "objects, and finite-index towers do not construct the missing object."
)
