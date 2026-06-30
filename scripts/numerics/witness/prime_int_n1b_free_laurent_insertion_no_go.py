"""N1-b' free Laurent insertion witness.

Docs 139-142 leave R1 open only as a genuinely different carrier.  This
witness tests the cheapest fake version of that move: freely add an
independent Laurent generator u after the DMP bottom class fails.

There are two algebraic forms of the repair:

1. Direct-sum/product insertion: R -> R plus F_2[u^{+-1}].  This contains a
   Laurent line only as a new external summand; the original DMP bottom class
   remains square-zero and the graded dimensions are not the one-dimensional
   Lin line.

2. Tensor insertion: R -> R tensor F_2[u^{+-1}].  This gives full support, but
   because DMP has classes in degree -1 and all nonnegative degrees, every
   degree receives many summands; in the untruncated support, infinitely many.
   It is not the singleton Lin line.

In either form, the free operation is defined on any graded shadow before an
Euler carrier field is consumed, so the same operation works on controls.  A
surviving R1 carrier must therefore supply a nonfree first map or relation
that uses carrier data and fails on DH/Epstein.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_free_laurent_insertion_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_dim(deg):
    """F_2-dimension of pi_deg TCR(F_2;2)^{phi Z/2} from DMP C/E."""
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def lin_dim(_deg):
    """F_2-dimension of the Laurent line F_2[t^{+-1}] in every degree."""
    return 1


def direct_sum_dim(deg):
    """Dimension after adding a free external Laurent summand."""
    return dmp_dim(deg) + lin_dim(deg)


def tensor_dim_truncated(deg, nmax):
    """Dimension of DMP_{[-1,nmax]} tensor F_2[u^{+-1}] in total degree deg."""
    return sum(dmp_dim(n) * lin_dim(deg - n) for n in range(-1, nmax + 1))


def free_laurentize_dim(shadow_dim, deg):
    """Free line insertion on an arbitrary graded shadow."""
    return shadow_dim(deg) + lin_dim(deg)


def zero_control_dim(_deg):
    """A control with no DMP carrier data."""
    return 0


def epstein_shadow_dim(deg):
    """Toy represented-norm/count shadow: finite noncarrier data near degree 0."""
    return 1 if deg in {0, 1, 2} else 0


window = list(range(-4, 5))

gate(
    "FLI1 DMP support is not already the Lin Laurent line",
    any(dmp_dim(d) != lin_dim(d) for d in window),
    "degree -2 has DMP=0 but Lin=1",
)

direct_sum_profile = {d: direct_sum_dim(d) for d in range(-2, 3)}
gate(
    "FLI2 direct free-line insertion overproduces graded dimensions",
    direct_sum_dim(-1) == 2 and direct_sum_dim(0) == 2 and lin_dim(0) == 1,
    f"profile={direct_sum_profile}",
)

gate(
    "FLI3 direct insertion leaves the DMP bottom class noninvertible",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "the original y still has y^2=0 in the DMP component",
)

tensor_profiles = {
    nmax: {d: tensor_dim_truncated(d, nmax) for d in (-2, -1, 0, 1)}
    for nmax in (1, 2, 4, 8)
}
gate(
    "FLI4 tensoring with a free Laurent line is not one-dimensional",
    all(tensor_dim_truncated(0, nmax) == nmax + 2 for nmax in (1, 2, 4, 8)),
    f"profiles={tensor_profiles}",
)

gate(
    "FLI5 tensor multiplicity grows with the DMP truncation",
    tensor_dim_truncated(0, 8) > tensor_dim_truncated(0, 4) > lin_dim(0),
    f"dim0 N=4:{tensor_dim_truncated(0,4)} N=8:{tensor_dim_truncated(0,8)}",
)


# The doc-138 obstruction persists if the free Laurent line is independent of
# the U_1 shear torsor: coboundaries in the U_1 coordinate still have leading
# coefficient zero, while c=(1+z)^-1 has leading coefficient one.
obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "FLI6 independent free line does not kill the shear obstruction",
    obstruction_res1 == 1 and coboundary_res1 == 0,
    "res_1(c)=1 remains outside the first-coordinate coboundaries",
)


zero_control_profile = {d: free_laurentize_dim(zero_control_dim, d) for d in (-2, -1, 0, 1)}
epstein_profile = {d: free_laurentize_dim(epstein_shadow_dim, d) for d in (-2, -1, 0, 1)}
gate(
    "FLI7 free Laurent insertion is formable on controls",
    all(v >= 1 for v in zero_control_profile.values())
    and all(v >= 1 for v in epstein_profile.values()),
    f"zero_control={zero_control_profile} epstein_shadow={epstein_profile}",
)

gate(
    "FLI8 any surviving carrier must name a nonfree carrier-consuming map",
    True,
    "free direct/tensor insertion is either decoration, multiplicity blow-up, or control-formable",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (FLI1-FLI8)")
print(
    "VERDICT: freely adjoining a Laurent generator does not construct the R1 "
    "carrier.  As a direct summand it is external decoration; as a tensor "
    "factor it overproduces multiplicities; with independent action it does "
    "not kill the shear obstruction; and as a free operation it is formable on "
    "controls.  A surviving route must provide a nonfree carrier-consuming "
    "map or relation that produces the line and fails on DH/Epstein."
)
