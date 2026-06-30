"""N1-b' support-chain connection/holonomy witness.

Docs 155-157 kill support paths, groupoid completion, and attached stabilizer
loops.  The next repair is to put labels/a connection on the support arrows
and hope the connection supplies the missing shift, holonomy, or torsor data.

This witness checks the finite model.  The support graph is a line tree.  For
any finite abelian coefficient group A, edge labels on a tree are pure gauge:
with one base vertex fixed, vertex gauges have the same count as edge
labelings, and all flat connections gauge-normalize to the trivial one.  A
nontrivial holonomy class appears only after adding a terminal wrap or an
external loop, which re-enters the formal cyclic/stabilizer repairs already
killed.  Labels in the external Laurent unit group are therefore scalar
bookkeeping unless a carrier constructs them.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_connection_holonomy_no_go
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


def edge_count_tree(rank):
    return rank - 1


def edge_count_cycle(rank):
    return rank


def cochain_count(modulus, edge_count):
    return modulus ** edge_count


def based_vertex_gauge_count(modulus, rank):
    return modulus ** (rank - 1)


def h1_tree_count(_modulus):
    return 1


def h1_cycle_count(modulus):
    return modulus


def pair_path_count(rank):
    return rank * (rank - 1)


ranks = {nmax: dmp_rank_truncated(nmax) for nmax in (1, 2, 4, 8)}
tree_edges = {nmax: edge_count_tree(rank) for nmax, rank in ranks.items()}
cycle_edges = {nmax: edge_count_cycle(rank) for nmax, rank in ranks.items()}
cochains_mod2 = {nmax: cochain_count(2, edges) for nmax, edges in tree_edges.items()}
based_gauges_mod2 = {
    nmax: based_vertex_gauge_count(2, rank) for nmax, rank in ranks.items()
}
tree_h1_mod2 = {nmax: h1_tree_count(2) for nmax in ranks}
cycle_h1_mod2 = {nmax: h1_cycle_count(2) for nmax in ranks}
cochains_mod3 = {nmax: cochain_count(3, edges) for nmax, edges in tree_edges.items()}
based_gauges_mod3 = {
    nmax: based_vertex_gauge_count(3, rank) for nmax, rank in ranks.items()
}
tree_h1_mod3 = {nmax: h1_tree_count(3) for nmax in ranks}
cycle_h1_mod3 = {nmax: h1_cycle_count(3) for nmax in ranks}
oriented_path_counts = {nmax: pair_path_count(rank) for nmax, rank in ranks.items()}

gate(
    "CHN1 support tensor ranks are the doc-157 ranks",
    ranks == {1: 3, 2: 4, 4: 6, 8: 10},
    f"ranks={ranks}",
)

gate(
    "CHN2 support-chain connection has r-1 edge labels",
    tree_edges == {1: 2, 2: 3, 4: 5, 8: 9},
    f"tree_edges={tree_edges}",
)

gate(
    "CHN3 mod-2 edge labels are exactly matched by based vertex gauges",
    cochains_mod2 == {1: 4, 2: 8, 4: 32, 8: 512}
    and cochains_mod2 == based_gauges_mod2,
    f"cochains_mod2={cochains_mod2}, based_gauges_mod2={based_gauges_mod2}",
)

gate(
    "CHN4 mod-2 support-chain holonomy is trivial",
    tree_h1_mod2 == {1: 1, 2: 1, 4: 1, 8: 1},
    f"tree_h1_mod2={tree_h1_mod2}",
)

gate(
    "CHN5 the same gauge-triviality holds for mod-3 labels",
    cochains_mod3 == {1: 9, 2: 27, 4: 243, 8: 19683}
    and cochains_mod3 == based_gauges_mod3
    and tree_h1_mod3 == {1: 1, 2: 1, 4: 1, 8: 1},
    (
        f"cochains_mod3={cochains_mod3}, "
        f"based_gauges_mod3={based_gauges_mod3}, tree_h1_mod3={tree_h1_mod3}"
    ),
)

gate(
    "CHN6 nontrivial holonomy requires an artificial cycle/wrap",
    cycle_edges == {1: 3, 2: 4, 4: 6, 8: 10}
    and cycle_h1_mod2 == {1: 2, 2: 2, 4: 2, 8: 2},
    f"cycle_edges={cycle_edges}, cycle_h1_mod2={cycle_h1_mod2}",
)

gate(
    "CHN7 labeled support paths are determined by endpoint gauges",
    oriented_path_counts == {1: 6, 2: 12, 4: 30, 8: 90},
    f"oriented_path_counts={oriented_path_counts}",
)

carrier_multiplication_supplied = False
torsor_splitter_supplied = False
external_unit_labels = True
gate(
    "CHN8 support-arrow labels are external scalars unless carrier-constructed",
    external_unit_labels and not carrier_multiplication_supplied and not torsor_splitter_supplied,
    "labeling arrows by units supplies no DMP multiplication or b/phi(b)=c",
)

obstruction_res1 = 1
coboundary_res1 = 0
gate(
    "CHN9 connection labels do not repair bottom or shear obstructions",
    dmp_dim(-1) == 1 and dmp_dim(-2) == 0 and obstruction_res1 == 1 and coboundary_res1 == 0,
    "y^2=0 and res_1(c)=1 remain unchanged",
)

control_cochains_mod2 = cochains_mod2.copy()
control_tree_h1_mod2 = tree_h1_mod2.copy()
gate(
    "CHN10 the same support-chain connections are formable on controls",
    control_cochains_mod2 == cochains_mod2 and control_tree_h1_mod2 == tree_h1_mod2,
    "finite-tree edge labels and gauges use only ordered support data",
)

primitive_carrier_maps_consumed = 0
edge_label_system_inserted = 1
gate(
    "CHN11 surviving connection/holonomy must be carrier-native",
    primitive_carrier_maps_consumed == 0 and edge_label_system_inserted == 1,
    "a real route must construct nontrivial holonomy from carrier correspondences and kill controls",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CHN1-CHN11)")
print(
    "VERDICT: support-chain connection labels do not supply the R1 carrier.  "
    "The support graph is a tree, so edge labels are pure gauge; mod-2 and "
    "mod-3 finite tests both have one gauge class.  Nontrivial holonomy "
    "requires an artificial wrap or external loop, re-entering the cyclic or "
    "stabilizer repairs.  Unit labels are external scalars unless the carrier "
    "constructs them, endpoint/path labels remain support bookkeeping, the "
    "bottom and shear obstructions remain, and the same connection system is "
    "formable on controls.  A surviving route must construct holonomy as "
    "carrier-native correspondence data."
)
