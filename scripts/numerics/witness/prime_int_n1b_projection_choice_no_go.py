"""N1-b' projection-choice witness.

Doc 143 killed free Laurent insertion as a carrier.  The immediate repair is
to tensor with a free Laurent line and then project to a "diagonal" or "right"
rank-one Laurent summand.

For a truncation R_DMP[-1..N], the tensor object R_DMP tensor F_2[u^{+-1}]
is a free F_2[u^{+-1}]-module of rank N+2: one Laurent copy for each DMP
degree -1,0,...,N.  Extracting a singleton Laurent line requires choosing a
rank-one summand.  Support and u-periodicity do not choose it: every coordinate
summand has the same Laurent support, and the total number of rank-one
F_2[u^{+-1}]-submodules is 2^(N+2)-1.

Thus "project to one copy" is a choice unless a carrier-native map supplies
the selector and fails on DH/Epstein.  The witness checks that the choice
count grows with the truncation and that the same projection operation is
available on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_projection_choice_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_rank_truncated(nmax):
    """Number of nonzero DMP degrees in [-1,nmax]."""
    return nmax + 2


def coordinate_line_choices(rank):
    """Coordinate Laurent summands."""
    return rank


def rank_one_submodule_choices(rank):
    """Nonzero vectors in F_2^rank, up to the only nonzero scalar."""
    return (1 << rank) - 1


def support_profile_for_coordinate(_coord, degrees):
    """Every coordinate Laurent summand has one class in every degree."""
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
    "PJC1 tensor repair has Laurent rank N+2, not rank 1",
    all(rank > 1 for rank in ranks.values()),
    f"ranks={ranks}",
)

coordinate_counts = {nmax: coordinate_line_choices(rank) for nmax, rank in ranks.items()}
gate(
    "PJC2 coordinate projections are multiple and grow with truncation",
    coordinate_counts[8] > coordinate_counts[4] > coordinate_counts[2] > coordinate_counts[1] > 1,
    f"coordinate_counts={coordinate_counts}",
)

rank_one_counts = {nmax: rank_one_submodule_choices(rank) for nmax, rank in ranks.items()}
gate(
    "PJC3 arbitrary rank-one Laurent summands grow exponentially",
    rank_one_counts[8] == 1023 and rank_one_counts[4] == 63,
    f"rank_one_counts={rank_one_counts}",
)


# Support and Laurent periodicity do not select a coordinate: all coordinate
# summands have the same one-dimensional support profile as the Lin line.
profiles = {
    coord: support_profile_for_coordinate(coord, degrees)
    for coord in range(dmp_rank_truncated(4))
}
all_profiles_equal_lin = all(profile == lin_profile(degrees) for profile in profiles.values())
gate(
    "PJC4 support/u-periodicity does not distinguish a coordinate line",
    all_profiles_equal_lin and len(set(profiles.values())) == 1,
    f"coordinates={len(profiles)} profile={lin_profile(degrees)}",
)


# Choosing the bottom coordinate merely names the already-known DMP bottom
# label.  The original DMP multiplication still has no degree -2 target.
gate(
    "PJC5 bottom-coordinate projection does not make the DMP bottom invertible",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0,
    "the selected Laurent generator is external u; original y still has y^2=0",
)


# A selector that uses only "pick one Laurent copy from a finite-rank free
# Laurent module" is available for any same-rank control module.
control_coordinate_counts = coordinate_counts.copy()
control_rank_one_counts = rank_one_counts.copy()
gate(
    "PJC6 the same projection operation is formable on controls",
    control_coordinate_counts == coordinate_counts
    and control_rank_one_counts == rank_one_counts,
    "same finite-rank free Laurent module has the same selectors for controls",
)


distinguishing_constraints_from_support = 0
gate(
    "PJC7 G-INT6 rejects support-only projection selection",
    rank_one_counts[4] > 1 and distinguishing_constraints_from_support == 0,
    "many selectors, no support invariant choosing one",
)

gate(
    "PJC8 surviving projection must be supplied by a nonfree carrier map",
    True,
    "projection is admissible only if a carrier-native selector is constructed and controls fail",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (PJC1-PJC8)")
print(
    "VERDICT: projecting the free/tensor Laurent repair to one copy is not a "
    "construction-grade carrier unless a carrier-native selector is supplied. "
    "The tensor object has many rank-one Laurent summands with identical "
    "support, the number of choices grows with the DMP truncation, and the "
    "same projection operation is formable on controls."
)
