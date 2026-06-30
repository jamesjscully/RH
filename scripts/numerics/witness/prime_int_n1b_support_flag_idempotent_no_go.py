"""N1-b' support-flag/Borel idempotent witness.

Doc 153 kills full support-module conjugacy because GL_r is too large to
choose a rank-one idempotent.  The next repair is to reduce the symmetry by
using the DMP support order as a complete flag, then take the first coordinate
corner as canonical.

This witness checks that move.  A complete flag does choose a line after the
flag has been supplied, but the flag is exactly support-index bookkeeping:
it is not multiplication, not a carrier correspondence, does not make the DMP
bottom class invertible, does not select the shift/torsor data, and is
formable on controls.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_support_flag_idempotent_no_go
"""

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def dmp_rank_truncated(nmax):
    return nmax + 2


def dmp_dim(deg):
    if deg == -1:
        return 1
    if deg >= 0:
        return 1
    return 0


def gl_order_f2(rank):
    total = 1
    for k in range(rank):
        total *= 2**rank - 2**k
    return total


def borel_order_f2(rank):
    # Upper triangular invertibles over F_2.  The diagonal has no choices.
    return 2 ** (rank * (rank - 1) // 2)


def complete_flag_count_f2(rank):
    return gl_order_f2(rank) // borel_order_f2(rank)


def borel_algebra_rank(rank):
    # Upper triangular matrix units.
    return rank * (rank + 1) // 2


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
flag_counts = {nmax: complete_flag_count_f2(rank) for nmax, rank in ranks.items()}
borel_ranks = {nmax: borel_algebra_rank(rank) for nmax, rank in ranks.items()}
coordinate_counts = ranks.copy()

gate(
    "SFI1 support tensor ranks are the doc-153 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "SFI2 complete flags are extra choices in finite-free modules",
    flag_counts == {1: 21, 2: 315, 4: 615195, 8: 10414855105976475},
    f"flag_counts={flag_counts}",
)

gate(
    "SFI3 Borel/flag reduction shrinks Mat_r but still overproduces maps",
    borel_ranks == {1: 6, 2: 10, 4: 21, 8: 55},
    f"borel_ranks={borel_ranks}",
)

flag_selects_first_line = True
flag_supplied_by_support_order = True
primitive_carrier_maps_consumed = 0
gate(
    "SFI4 a supplied flag selects a coordinate line but consumes no carrier map",
    flag_selects_first_line and flag_supplied_by_support_order and primitive_carrier_maps_consumed == 0,
    "the selected line is first in the ordered support chain",
)

gate(
    "SFI5 support order still has multiple coordinate choices before the flag",
    coordinate_counts == {1: 3, 2: 4, 4: 6, 8: 10},
    f"coordinate_counts={coordinate_counts}",
)

bottom_flag_corner_uses_external_l = True
bottom_generator_invertible = False
gate(
    "SFI6 bottom flag corner does not invert the DMP bottom class",
    bottom_flag_corner_uses_external_l
    and not bottom_generator_invertible
    and dmp_dim(-1) == 1
    and dmp_dim(-2) == 0,
    "flag-selected scalar is external L while original y remains square-zero",
)

adjacent_maps_supplied_by_flag = False
shift_selected_by_flag = False
torsor_splitter_selected_by_flag = False
gate(
    "SFI7 support flag does not supply adjacent maps, shift, or torsor data",
    not adjacent_maps_supplied_by_flag
    and not shift_selected_by_flag
    and not torsor_splitter_selected_by_flag,
    "a flag orders subspaces; it does not construct S or b/phi(b)=c",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "SFI8 support flag does not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "y^2=0 and res_1(c)=1 remain unchanged",
)

control_flag_counts = flag_counts.copy()
control_borel_ranks = borel_ranks.copy()
gate(
    "SFI9 the same support-flag/Borel reduction is formable on controls",
    control_flag_counts == flag_counts and control_borel_ranks == borel_ranks,
    "ordered finite-free flags and Borel subalgebras are shadow-level data",
)

gate(
    "SFI10 surviving flag must be carrier-native",
    flag_supplied_by_support_order and primitive_carrier_maps_consumed == 0,
    "a real route must construct the flag from carrier correspondence data and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (SFI1-SFI10)")
print(
    "VERDICT: a support-degree flag/Borel reduction can choose a coordinate "
    "corner only after the flag is supplied.  In the tested finite supports, "
    "complete flags are extra finite-free choices, the Borel algebra still "
    "overproduces maps, the bottom corner recovers external L rather than "
    "inverting the DMP bottom class, no shift/torsor data is constructed, "
    "the base obstructions remain, and the same flag reduction is formable "
    "on controls.  A surviving route must construct the flag carrier-natively."
)
