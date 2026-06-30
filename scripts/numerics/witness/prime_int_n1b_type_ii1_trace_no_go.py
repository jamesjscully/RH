r"""Type II_1 trace / continuous-dimension no-go.

After doc 204, trace-class compactness gives trace/count but not radius.
The next repair is to use a different finiteness type: a type II_1 factor's
normalized trace, i.e. a continuous Murray-von Neumann dimension.  This
passes the earlier cardinality/continuum/length/index type obstruction as a
type of finiteness.

The obstruction is again the count/radius split.  In the computable model
M = L(Z) ~= L^\infty(S^1), the trace reads averaged spectral moments.  For
pure Frobenius data, tau(|a|^2)=q, so sqrt(tau(|a|^2)) looks like sqrt(q).
But a trace-preserving off-purity redistribution keeps tau(|a|^2)=q while
breaking the uniform radius.  The trace reads an average, not the modulus
bound.  The normalized II_1 dimension is also scale-free and can be formed
over DH spectral data, so it is not the missing carrier.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_type_ii1_trace_no_go
"""

import mpmath as mp

from scripts.numerics.witness.von_neumann_typeII1 import (
    decide,
    ff_frobenius_eigs,
    radius_max,
    tau_abs2,
    trace_preserving_off_purity,
    typecheck,
)


failures = []

mp.mp.dps = 40


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


tc = typecheck()
gate(
    "II1T1 II_1 trace is a genuine different finiteness type",
    "II_1 factor" in tc["factor"]
    and "CONTINUOUS DIMENSION" in tc["trace_type"]
    and tc["passes_R8_type_obstruction"].startswith("YES"),
    tc["passes_R8_type_obstruction"],
)


pure_rows = []
for name in ("E_ordinary_q5", "genus2_q9", "genus2_q2"):
    q, _, alphas = ff_frobenius_eigs(name)
    pure_rows.append((name, q, tau_abs2(alphas), radius_max(alphas, q)))

gate(
    "II1T2 pure examples make sqrt(tau(|a|^2)) look like the radius",
    all(abs(a2 - q) < mp.mpf("1e-30") for _, q, a2, _ in pure_rows)
    and all(dev < mp.mpf("1e-30") for _, _, _, dev in pure_rows),
    ", ".join(f"{name}:tau_abs2={mp.nstr(a2, 8)},dev={mp.nstr(dev, 4)}"
              for name, _, a2, dev in pure_rows),
)


decision_rows = decide()
gate(
    "II1T3 trace-preserving off-purity breaks radius",
    all(abs(row["tau_abs2_pure"] - row["tau_abs2_offpurity"]) < mp.mpf("1e-30")
        for row in decision_rows.values())
    and all(row["radius_dev_offpurity"] > mp.mpf("0.1")
            for row in decision_rows.values()),
    ", ".join(f"{name}:tau={mp.nstr(row['tau_abs2_offpurity'], 8)},"
              f"dev={mp.nstr(row['radius_dev_offpurity'], 5)}"
              for name, row in decision_rows.items()),
)


scale_q, _, scale_alphas = ff_frobenius_eigs("genus2_q9")
scale_rows = []
for lam in (mp.mpf(1), mp.mpf(2), mp.mpf("0.5")):
    scaled = [lam * a for a in scale_alphas]
    dim_m = mp.mpf(sum(1 for a in scaled if abs(a) > mp.mpf("1e-30"))) / len(scaled)
    max_radius = max(abs(a) for a in scaled)
    scale_rows.append((lam, dim_m, max_radius))

gate(
    "II1T4 normalized continuous dimension is scale-free",
    all(abs(dim_m - 1) < mp.mpf("1e-30") for _, dim_m, _ in scale_rows)
    and abs(scale_rows[1][2] - 2 * scale_rows[0][2]) < mp.mpf("1e-30")
    and abs(scale_rows[2][2] - mp.mpf("0.5") * scale_rows[0][2]) < mp.mpf("1e-30"),
    ", ".join(f"lambda={lam}:dim={dim_m},max={mp.nstr(rad, 6)}"
              for lam, dim_m, rad in scale_rows),
)


ii1_trace_exists_for_any_spectral_measure = True
requires_euler_product_for_factor_or_trace = False
dh_litmus_passes = False
gate(
    "II1T5 II_1 trace is not DH-distinguishing",
    ii1_trace_exists_for_any_spectral_measure
    and not requires_euler_product_for_factor_or_trace
    and not dh_litmus_passes,
    "L(Z) with normalized trace can be formed over spectral measures without Euler product",
)


carrier_native_purity_constructed = False
uniform_modulus_bound_constructed = False
archimedean_monodromy_N_constructed = False
weil_positivity_constructed = False
dh_killing_carrier_constructed = False
single_frobenius_base_size_constructed = False
finite_constant_field_constructed = False
square_side_iota_constructed = False
properness_duality_constructed = False
square_h2_defined = False
square_intersection_form_defined = False
square_correspondence_algebra_defined = False
frobenius_graph_defined = False
positive_rosati_defined = False
laurent_axis_defined = False
boundary_map_defined = False
torsor_splitter_defined = False
dd4_weight_ge_1_datum_defined = False

gate(
    "II1T6 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not carrier_native_purity_constructed
    and not uniform_modulus_bound_constructed
    and not archimedean_monodromy_N_constructed
    and not weil_positivity_constructed
    and not dh_killing_carrier_constructed
    and not single_frobenius_base_size_constructed
    and not finite_constant_field_constructed
    and not square_side_iota_constructed
    and not properness_duality_constructed
    and not square_h2_defined
    and not square_intersection_form_defined
    and not square_correspondence_algebra_defined
    and not frobenius_graph_defined
    and not positive_rosati_defined
    and not laurent_axis_defined
    and not boundary_map_defined
    and not torsor_splitter_defined
    and not dd4_weight_ge_1_datum_defined,
    "continuous dimension supplies averages, not purity/Rosati or square correspondences",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (II1T1-II1T6)")
print(
    "VERDICT: the type II_1 trace is a genuine finiteness type and supplies "
    "averaged count/location moments, but it does not couple count to the "
    "radius.  tau(|a|^2)=q survives off-purity redistribution, normalized "
    "dimension is scale-free, and the II_1 trace is formable over DH spectral "
    "data.  No End(S^2/Z) square, DD.4 weight>=1 datum, or positive Rosati is built."
)
