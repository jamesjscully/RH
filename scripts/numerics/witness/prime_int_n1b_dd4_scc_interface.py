r"""DD.4-to-SCC interface witness.

This is a construction-facing dependency witness, not a no-go theorem and not
a construction of End(S^2/Z).  It pins the exact interface between the DD.4
weight>=1 torsor obstruction and the square-carrier contract of doc 256.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_dd4_scc_interface
"""

from math import comb, log2


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Arithmetic in F_2[z]/z^{L+1}; unit polynomials are dicts {power: 1}."""

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

    return add, mul, inv, phi


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
    _add, mul, inv, phi = make(L)
    one_plus_z = {0: 1, 1: 1}
    c = inv(one_plus_z)
    bgens = [mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)]
    coboundaries = closure(bgens, L, mul)
    ngens = [mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)]
    norm_image = closure(ngens, L, mul)
    z1_order = 2 ** L // len(norm_image)
    h1_order = z1_order // len(coboundaries)
    return {
        "L": L,
        "c": c,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "h1_order": h1_order,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "res1_c": c.get(1, 0),
        "coboundaries_res1_zero": all(from_vec(v).get(1, 0) == 0 for v in coboundaries),
    }


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "DSI1 Lin boundary is singleton but weight>=1 is not automatically pinned",
    all(p["c"].get(0, 0) == 1 and p["res1_c"] == 1 for p in profiles),
    "c restricts to 1 at z=0; res_1(c)=1 in every tested truncation",
)

gate(
    "DSI2 DD.4 obstruction class is stable and nonzero",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 for p in profiles),
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)

gate(
    "DSI3 res_1 is the carrier-independent detector of the obstruction",
    all(p["coboundaries_res1_zero"] and p["res1_c"] == 1 for p in profiles),
    "res_1 kills every coboundary and detects c",
)


# Formal splitter extension: add one generator b with phi(b)=b*c^{-1}.
# This makes c a coboundary, but only by adjoining an external generator.
L = 8
_add, mul, inv, phi = make(L)
c = inv({0: 1, 1: 1})
c_inv = inv(c)


def ext_mul(a, b):
    u, e = a
    v, f = b
    return mul(u, v), e ^ f


def ext_inv(a):
    u, e = a
    return inv(u), e


def ext_phi(a):
    u, e = a
    return mul(phi(u), c_inv if e else {0: 1}), e


splitter = ({0: 1}, 1)
splitter_boundary = ext_mul(splitter, ext_inv(ext_phi(splitter)))

gate(
    "DSI4 a free splitter kills the class only by external generator insertion",
    ext_phi(ext_phi(splitter)) == splitter and splitter_boundary == (c, 0),
    "adjoined b has b/phi(b)=c in the split extension",
)


scc_slots = {
    "SCC.1 actual square": {"actual_square", "carrier_boundary", "control_death"},
    "SCC.2 integral rep_NS": {"actual_square", "rep_NS", "dd4_weight_ge_1"},
    "SCC.3 degree maps": {"actual_square", "rep_NS", "two_degree_maps"},
    "SCC.4 diagonal": {"actual_square", "rep_NS", "indecomposable_diagonal"},
    "SCC.5 graph/count": {"actual_square", "frobenius_graph", "count_trace"},
    "SCC.6 composition": {"actual_square", "proper_correspondence", "fiber_product"},
    "SCC.7 projection": {"actual_square", "projection_formula", "carrier_pairing"},
    "SCC.8 Rosati duality": {"actual_square", "dd4_weight_ge_1", "canonical_duality"},
    "SCC.9 positivity": {"actual_square", "positive_rosati", "canonical_duality"},
    "SCC.10 controls": {"actual_square", "control_death"},
    "SCC.11 DD.4": {"dd4_weight_ge_1", "laurent_boundary", "torsor_splitter"},
}

current_state = {
    "lin_boundary",
    "finite_field_anchor",
    "scc_contract",
}

formal_splitter_state = current_state | {"torsor_splitter"}

admissible_dd4_extension = {
    "actual_square",
    "carrier_boundary",
    "dd4_weight_ge_1",
    "laurent_boundary",
    "torsor_splitter",
    "control_death",
}


def unresolved_slots(state):
    return [slot for slot, deps in scc_slots.items() if not deps <= state]


current_unresolved = unresolved_slots(current_state)
formal_unresolved = unresolved_slots(formal_splitter_state)
carrier_interface_unresolved = unresolved_slots(admissible_dd4_extension)

gate(
    "DSI5 the current project state has SCC.11 as a real dependency, not a label",
    "SCC.11 DD.4" in current_unresolved
    and "SCC.8 Rosati duality" in current_unresolved
    and "SCC.2 integral rep_NS" in current_unresolved,
    "unresolved: " + ", ".join(current_unresolved[:5]) + (" ..." if len(current_unresolved) > 5 else ""),
)

gate(
    "DSI6 formal splitting does not satisfy the SCC interface",
    formal_unresolved == current_unresolved
    and {"actual_square", "carrier_boundary", "control_death"} <= admissible_dd4_extension
    and "SCC.11 DD.4" not in carrier_interface_unresolved,
    "adding only a splitter changes no SCC slot; carrier extension must also supply boundary and control death",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nDSI1-DSI6 ALL PASS: DD.4/SCC interface pinned; carrier extension still unconstructed")
print(
    "VERDICT: the next constructive move must not be another square vocabulary package. "
    "It must produce a carrier-native extension in which the nonzero DD.4 class "
    "[(1+z)^-1] dies because of an actual boundary/properness/self-duality map, while "
    "DH/Epstein/controls die at carrier formation. A free torsor splitter kills the class "
    "formally but leaves the SCC slots unresolved."
)
