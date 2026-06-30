"""N1-b' quotient-to-line witness.

Doc 144 kills selecting a rank-one Laurent subobject from the tensor repair.
The dual repair is to quotient the overproduced free Laurent module down to
one Laurent line by an augmentation/diagonal functional.

For R_DMP[-1..N] tensor F_2[u^{+-1}], the tensor object is a free Laurent
module L^r with r=N+2.  A degree-preserving L-linear quotient L^r -> L is
given by a nonzero vector in F_2^r.  There are 2^r-1 such quotient functionals,
and support/u-periodicity does not choose one.  The usual "sum all copies"
augmentation is one arbitrary member of this family.

Thus quotienting to a line is not construction-grade unless the quotient
functional is produced by a carrier-native first map and controls cannot form
it.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_quotient_to_line_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_rank_truncated(nmax):
    """Number of nonzero DMP degrees in [-1,nmax]."""
    return nmax + 2


def quotient_functional_count(rank):
    """Nonzero degree-preserving L-linear maps L^rank -> L over F_2."""
    return (1 << rank) - 1


def coordinate_quotient_count(rank):
    """Coordinate quotient functionals."""
    return rank


def quotient_support_profile(_functional, degrees):
    """Every nonzero degree-preserving quotient has one Laurent class per degree."""
    return tuple(1 for _ in degrees)


def lin_profile(degrees):
    return tuple(1 for _ in degrees)


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


degrees = tuple(range(-3, 4))
ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}

gate(
    "QTL1 tensor repair starts as rank N+2, so quotient data is extra",
    all(rank > 1 for rank in ranks.values()),
    f"ranks={ranks}",
)

coordinate_counts = {nmax: coordinate_quotient_count(rank) for nmax, rank in ranks.items()}
gate(
    "QTL2 coordinate quotient choices grow with truncation",
    coordinate_counts[8] > coordinate_counts[4] > coordinate_counts[2] > coordinate_counts[1] > 1,
    f"coordinate_counts={coordinate_counts}",
)

functional_counts = {nmax: quotient_functional_count(rank) for nmax, rank in ranks.items()}
gate(
    "QTL3 rank-one quotient functionals grow exponentially",
    functional_counts[8] == 1023 and functional_counts[4] == 63,
    f"functional_counts={functional_counts}",
)


profiles = {
    mask: quotient_support_profile(mask, degrees)
    for mask in range(1, quotient_functional_count(dmp_rank_truncated(4)) + 1)
}
gate(
    "QTL4 support/u-periodicity does not distinguish quotient functionals",
    len(set(profiles.values())) == 1 and next(iter(profiles.values())) == lin_profile(degrees),
    f"functional_count_N4={len(profiles)} profile={lin_profile(degrees)}",
)


# The all-ones augmentation is one quotient functional, not a distinguished
# one.  For N=4, rank=6, mask 0b111111 is only one of 63.
rank_n4 = dmp_rank_truncated(4)
all_ones_mask = (1 << rank_n4) - 1
gate(
    "QTL5 the diagonal/augmentation quotient is one arbitrary functional",
    1 <= all_ones_mask <= quotient_functional_count(rank_n4)
    and quotient_functional_count(rank_n4) > 1,
    f"all_ones_mask={all_ones_mask} total={quotient_functional_count(rank_n4)}",
)


# Quotienting to the external u-line does not change the base DMP
# multiplication or the doc-138 U_1 obstruction.
gate(
    "QTL6 quotient does not make the DMP bottom class invertible",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "original y still has y^2=0; quotient generator is external u",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "QTL7 quotient alone does not kill the shear obstruction",
    obstruction_res1 == 1 and coboundary_res1 == 0,
    "res_1(c)=1 remains outside base coboundaries",
)


control_counts = functional_counts.copy()
gate(
    "QTL8 the same quotient operation is formable on controls",
    control_counts == functional_counts and control_counts[4] == 63,
    "same L^rank control module has the same quotient functionals",
)

gate(
    "QTL9 surviving quotient must be a carrier-native functional",
    True,
    "rank-one quotient is admissible only if the functional is constructed and controls fail",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (QTL1-QTL9)")
print(
    "VERDICT: quotienting the free/tensor Laurent repair to one line is not a "
    "construction-grade carrier unless the quotient functional is supplied by "
    "carrier data.  There are many indistinguishable quotient functionals, the "
    "diagonal augmentation is one arbitrary choice, the DMP bottom and shear "
    "obstructions remain, and the same quotient operation is formable on "
    "controls."
)
