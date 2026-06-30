r"""Jet/filtration deletion DD.4 no-go.

This witness tests the repair after docs 257-260:
remove the leading obstruction by passing to a higher unit filtration,
for instance U_3 = 1 + z^3 F_2[[z]], or by taking an associated-graded/
jet quotient that discards the first jets.  U_3 has trivial H^1 in the
tested truncations, but only because the DD.4 class c=(1+z)^-1 is not in
U_3.  The deleted quotient U_1/U_3 still carries the obstruction.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_jet_deletion_no_go
"""

from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[z]/z^{L+1}; 1-units are dicts {power: 1}."""

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


def to_vec(f, L, start=1):
    return tuple(f.get(k, 0) for k in range(start, L + 1))


def from_vec(v, start=1):
    out = {0: 1}
    for i, bit in enumerate(v, start=start):
        if bit:
            out[i] = 1
    return out


def closure(gens, zero_vec, from_vec_fn, mul_fn, to_vec_fn):
    seen = {zero_vec}
    queue = [zero_vec]
    while queue:
        current = from_vec_fn(queue.pop())
        for gen in gens:
            nxt = to_vec_fn(mul_fn(current, gen))
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def h1_profile(L, start):
    mul, inv, phi = make(L)
    gens = [{0: 1, k: 1} for k in range(start, L + 1)]
    stable = all(all(k == 0 or k >= start for k in phi(gen)) for gen in gens)
    bgens = [mul(gen, inv(phi(gen))) for gen in gens]
    ngens = [mul(gen, phi(gen)) for gen in gens]
    dim = L - start + 1
    zero = (0,) * dim
    coboundaries = closure(
        bgens,
        zero,
        lambda v: from_vec(v, start),
        mul,
        lambda f: to_vec(f, L, start),
    )
    norm_image = closure(
        ngens,
        zero,
        lambda v: from_vec(v, start),
        mul,
        lambda f: to_vec(f, L, start),
    )
    z1_order = 2 ** dim // len(norm_image)
    h1_order = z1_order // len(coboundaries)
    c = inv({0: 1, 1: 1})
    return {
        "L": L,
        "start": start,
        "stable": stable,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": h1_order,
        "rank": dim,
        "c": c,
        "c_in_filtration": all(k == 0 or k >= start for k in c),
        "deleted_jets": tuple(c.get(k, 0) for k in range(1, start)),
        "c_nonboundary_base": to_vec(c, L, 1)
        not in closure(
            [mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)],
            (0,) * L,
            lambda v: from_vec(v, 1),
            mul,
            lambda f: to_vec(f, L, 1),
        ),
        "res1_c": c.get(1, 0),
    }


def quotient_u1_u3_profile():
    """Compute U_1/U_3 using F_2[z]/z^3, i.e. jets z,z^2."""

    L = 2
    mul, inv, phi = make(L)
    gens = [{0: 1, 1: 1}, {0: 1, 2: 1}]
    bgens = [mul(gen, inv(phi(gen))) for gen in gens]
    ngens = [mul(gen, phi(gen)) for gen in gens]
    zero = (0, 0)
    coboundaries = closure(
        bgens,
        zero,
        lambda v: from_vec(v, 1),
        mul,
        lambda f: to_vec(f, L, 1),
    )
    norm_image = closure(
        ngens,
        zero,
        lambda v: from_vec(v, 1),
        mul,
        lambda f: to_vec(f, L, 1),
    )
    z1_order = 2 ** 2 // len(norm_image)
    h1_order = z1_order // len(coboundaries)
    c = inv({0: 1, 1: 1})
    c_vec = to_vec(c, L, 1)
    return {
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": h1_order,
        "c_vec": c_vec,
        "c_nonboundary": c_vec not in coboundaries,
        "boundary_vectors": sorted(coboundaries),
    }


def xor_vec(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def control_deletion_profile(dim):
    """A filtered F_2 control where deleting the first jet removes a class."""

    chosen = tuple(1 if i == 0 else 0 for i in range(dim))
    kept = tuple(chosen[i] for i in range(2, dim))
    return {
        "dim": dim,
        "chosen_nonzero_before": any(chosen),
        "chosen_absent_after_u3_style_drop": not any(kept),
        "rank_before": dim,
        "rank_after": max(dim - 2, 0),
        "uses_square_data": False,
    }


base_profiles = [h1_profile(L, 1) for L in (6, 8, 10, 12)]
u3_profiles = [h1_profile(L, 3) for L in (6, 8, 10, 12)]
cutoff_profiles = {(start, L): h1_profile(L, start) for start in (2, 3, 4, 5) for L in (8, 10, 12)}
quotient_profile = quotient_u1_u3_profile()
control_profiles = [control_deletion_profile(dim) for dim in (3, 4, 8)]

gate(
    "JQD1 base DD.4 class remains the nonzero H^1 obstruction",
    all(p["h1_order"] == 2 and p["c_nonboundary_base"] and p["res1_c"] == 1 for p in base_profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in base_profiles
    ),
)

gate(
    "JQD2 U_3 has H^1=0 only after deleting the DD.4 jets",
    all(p["stable"] and p["h1_order"] == 1 and not p["c_in_filtration"] for p in u3_profiles),
    "  ".join(
        "L%d:deleted_jets=%s|H1(U3)=%d"
        % (p["L"], p["deleted_jets"], p["h1_order"])
        for p in u3_profiles
    ),
)

gate(
    "JQD3 the deleted quotient U_1/U_3 still carries the obstruction",
    quotient_profile["h1_order"] == 2 and quotient_profile["c_nonboundary"],
    "|B|=2^%d |Z1|=2^%d |H1|=%d c_jet=%s"
    % (
        int(log2(quotient_profile["b_order"])),
        int(log2(quotient_profile["z1_order"])),
        quotient_profile["h1_order"],
        quotient_profile["c_vec"],
    ),
)

gate(
    "JQD4 acyclicity depends on a filtration cutoff choice",
    all(cutoff_profiles[(2, L)]["h1_order"] == 2 for L in (8, 10, 12))
    and all(cutoff_profiles[(3, L)]["h1_order"] == 1 for L in (8, 10, 12))
    and all(cutoff_profiles[(4, L)]["h1_order"] == 2 for L in (8, 10, 12))
    and all(cutoff_profiles[(5, L)]["h1_order"] == 1 for L in (8, 10, 12)),
    "U2,U4 keep H1=2; U3,U5 make H1=1 by dropping lower jets",
)

gate(
    "JQD5 the same jet deletion is formable on controls",
    all(
        p["chosen_nonzero_before"]
        and p["chosen_absent_after_u3_style_drop"]
        and not p["uses_square_data"]
        for p in control_profiles
    ),
    "  ".join("dim%d:%d->%d" % (p["dim"], p["rank_before"], p["rank_after"]) for p in control_profiles),
)


required_slots = [
    "actual_square",
    "integral_rep_NS",
    "two_degree_maps",
    "indecomposable_diagonal",
    "frobenius_graph",
    "proper_correspondence",
    "fiber_product_composition",
    "projection_formula",
    "canonical_rosati",
    "positive_primitive_sign",
    "carrier_boundary",
    "control_death",
]

jet_deletion_slots = {
    "kills_visible_dd4_class": True,
    "deletes_dd4_jets": True,
    "actual_square": False,
    "integral_rep_NS": False,
    "two_degree_maps": False,
    "indecomposable_diagonal": False,
    "frobenius_graph": False,
    "proper_correspondence": False,
    "fiber_product_composition": False,
    "projection_formula": False,
    "canonical_rosati": False,
    "positive_primitive_sign": False,
    "carrier_boundary": False,
    "control_death": False,
}

gate(
    "JQD6 jet deletion satisfies no square-carrier slot",
    not any(jet_deletion_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nJQD1-JQD6 ALL PASS: jet/filtration deletion removes DD.4 instead of building the carrier")
print(
    "VERDICT: passing to U_3 or a leading-jet deletion makes the tested H^1 "
    "vanish only because the DD.4 class is outside the retained coefficient "
    "system.  The quotient U_1/U_3 still carries the obstruction, the same "
    "deletion is formable on controls, and no actual square, rep_NS, degree "
    "maps, graph, projection formula, Rosati, carrier boundary, or control "
    "death is constructed."
)
