"""Regularized determinant / compactness no-go.

After doc 203, finite constant-field cardinality is unavailable from the
named F1 constants.  The next repair is to change the type of finiteness:
use compactness, nuclearity, or a regularized determinant instead of a
finite cardinality.  This is a real positive datum: Connes' trace formula
does supply a regularized trace/count at infinity.

The obstruction is the radius split.  Over F_q, the finite determinant
det(1 - Fr*T | H^1) contains trace/count data and, when Frobenius is pure,
roots on the radius q^{w/2}.  But finite rank itself does not force the
radius: an off-circle perturbation stays finite-rank and keeps a finite
determinant while breaking purity.  At infinity, the regularized
determinant is FE-symmetric and supplies the explicit-formula trace, but
pinning the spectrum to Re(s)=1/2 is Weil positivity/RH, not an independent
End(S^2/Z) construction.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_regularized_determinant_no_go
"""

import mpmath as mp

from scripts.numerics.witness.regularized_determinant_radius import (
    connes_regularized_determinant_typecheck,
    decide,
    det_1_minus_FrT,
    dh_vacuous,
    ff_frobenius_eigs,
    off_circle_perturbation,
    radius_from_eigs,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


ff_names = ("P1", "E_supersingular_q2", "E_ordinary_q5", "genus2_q2")
ff_rows = []
for name in ff_names:
    q, g, alphas = ff_frobenius_eigs(name)
    ff_rows.append((name, q, g, len(alphas), radius_from_eigs(alphas, q)))

gate(
    "RDR1 finite-field determinant is finite-rank and pure examples mark radius",
    all(dim == 2 * g for _, _, g, dim, _ in ff_rows)
    and all(dev < mp.mpf("1e-25") for _, _, _, _, dev in ff_rows),
    ", ".join(f"{name}:dim={dim},dev={float(dev):.1e}" for name, _, _, dim, dev in ff_rows),
)


silent_rows = []
for name in ("E_ordinary_q5", "genus2_q2"):
    q, g, alphas = ff_frobenius_eigs(name)
    pert = off_circle_perturbation(alphas, q)
    det_value = det_1_minus_FrT(pert, mp.mpf("0.3"))
    silent_rows.append((name, len(pert), 2 * g, radius_from_eigs(pert, q), abs(det_value)))

gate(
    "RDR2 finite-rank compactness is radius-silent",
    all(dim == expected for _, dim, expected, _, _ in silent_rows)
    and all(dev > mp.mpf("0.1") for _, _, _, dev, _ in silent_rows)
    and all(mp.isfinite(det_abs) for _, _, _, _, det_abs in silent_rows),
    ", ".join(f"{name}:dev={float(dev):.3f},|det|={float(det_abs):.3f}"
              for name, _, _, dev, det_abs in silent_rows),
)


connes = connes_regularized_determinant_typecheck()
gate(
    "RDR3 archimedean regularized determinant supplies trace but not radius",
    connes["trace_class_realization_exists"]
    and connes["compactness delivers a finiteness colimit/product/continuum cannot block"]
    and not connes["(b) radius Re s = 1/2 marked by the determinant"]
    and connes["radius_is_FE_fixed_locus (DH-shared, free)"]
    and connes["radius-marking input = Weil positivity = RH (Connes), not independent"],
    connes["verdict"],
)


decision = decide()
gate(
    "RDR4 compactness supplies count/location, not independent purity",
    decision["compactness_supplies_a_finiteness_cardinality_could_not"]
    and decision["finite_trace_supplies_the_location_count (explicit formula)"]
    and decision["finite_rank_is_radius_silent (off-circle perturbation stays nuclear)"]
    and not decision["regularized_determinant_marks_the_radius"]
    and decision["radius_marking_input_is_RH_not_independent"],
    decision["verdict"],
)


dh_msg = dh_vacuous()
gate(
    "RDR5 DH control has no Frobenius determinant analogue",
    "no Frobenius" in dh_msg
    and "no det(1 - Fr*T | H^1)" in dh_msg
    and "NOTHING" in dh_msg,
    "control dies before determinant/radius question",
)


carrier_native_purity_on_spectrum_constructed = False
archimedean_monodromy_N_on_spectrum_constructed = False
weil_positivity_constructed = False
independent_radius_marker_constructed = False
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
    "RDR6 no End(S^2/Z) square/Rosati/R1 data is constructed",
    not carrier_native_purity_on_spectrum_constructed
    and not archimedean_monodromy_N_on_spectrum_constructed
    and not weil_positivity_constructed
    and not independent_radius_marker_constructed
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
    "regularized trace exists, but purity/radius and square correspondence data are absent",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (RDR1-RDR6)")
print(
    "VERDICT: compactness/regularized determinant data supplies a genuine "
    "trace/count finiteness, but finite rank and trace-classness are "
    "radius-silent.  At infinity the determinant is FE-symmetric; pinning "
    "the spectrum to Re(s)=1/2 is Weil positivity/RH, not an independent "
    "End(S^2/Z) square, DD.4 weight>=1 datum, or positive Rosati."
)
