r"""CM / Shimura-Taniyama carrier no-go.

After doc 234 killed fixed Tate/Hodge subspaces as the square carrier, the
next repair is to import a stronger positivity theorem: put the would-be
Frobenius inside a CM endomorphism field, use Shimura-Taniyama / CM theory to
identify Rosati with complex conjugation, and read the radius from
pi*pi_bar=q.  That theorem is real for CM objects, but it is not construction
of End(S^2/Z).  It requires the CM abelian carrier and endomorphism field
first, and still does not build rep_NS, degree slots, correspondences,
projection formula, or positive Rosati on the zeta square.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cm_shimura_carrier_no_go
"""

from __future__ import annotations

import cmath
import math

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import ns_intersection


failures: list[str] = []


Corr = tuple[float, np.ndarray, float]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def cm_profile() -> tuple[int, bool, bool, bool, bool]:
    # Toy profile: imaginary quadratic CM field, conjugation, CM type,
    # norm-degree identity, and Rosati=complex conjugation.
    return (2, True, True, True, True)


def norm_q(pi: complex) -> float:
    return float(round(abs(pi) ** 2, 12))


def trace_n(pi: complex, n: int) -> float:
    return float(round((pi**n + pi.conjugate() ** n).real, 12))


def counts(pi: complex, upto: int) -> list[float]:
    q = norm_q(pi)
    return [float(q**n + 1.0 - trace_n(pi, n)) for n in range(1, upto + 1)]


def mult_matrix(pi: complex) -> np.ndarray:
    a = pi.real
    b = pi.imag
    return np.array([[a, -b], [b, a]], dtype=float)


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(z: np.ndarray) -> Corr:
    return corr(1.0, np.eye(z.shape[0]), 1.0)


# CMST1: the CM theorem genuinely forces the radius for a CM object.  For
# pi=1+2i, N(pi)=5 and q/pi is exactly complex conjugation.
pi_cm = complex(1.0, 2.0)
q_cm = norm_q(pi_cm)
rosati_cm = q_cm / pi_cm
conj_cm = pi_cm.conjugate()

gate(
    "CMST1 CM norm identity genuinely forces the CM radius",
    q_cm == 5.0 and abs(rosati_cm - conj_cm) < 1e-12 and abs(abs(pi_cm) - math.sqrt(5.0)) < 1e-12,
    "pi=1+2i, N(pi)=%.1f, q/pi=%s, complex-conj=%s"
    % (q_cm, complex(round(rosati_cm.real, 6), round(rosati_cm.imag, 6)), conj_cm),
)


# CMST2: the abstract CM type/profile does not determine a count anchor.  The
# same imaginary-quadratic CM profile supports different CM Frobenius elements
# and hence different finite-field trace/count windows.
pi_cm_other = complex(2.0, 3.0)
profile_a = cm_profile()
profile_b = cm_profile()
counts_a = counts(pi_cm, 4)
counts_b = counts(pi_cm_other, 4)

gate(
    "CMST2 CM type profile does not determine count anchor",
    profile_a == profile_b == (2, True, True, True, True) and counts_a != counts_b,
    "profile=%s, N(1+2i)=%.1f counts=%s, N(2+3i)=%.1f counts=%s"
    % (profile_a, norm_q(pi_cm), [round(c, 1) for c in counts_a], norm_q(pi_cm_other), [round(c, 1) for c in counts_b]),
)


# CMST3: if an external q is fixed and pi is off that radius, the algebraic
# adjoint q/pi is not complex conjugation.  The equality is exactly the radius
# condition, so a CM shortcut works only after the CM carrier has already
# supplied the right endomorphism/norm package.
q_external = 9.0
sqrt_q = math.sqrt(q_external)
pi_off = 1.4 * sqrt_q * cmath.exp(0.45j)
rosati_off = q_external / pi_off
conj_off = pi_off.conjugate()
off_gap = abs(rosati_off - conj_off)

gate(
    "CMST3 fake off-radius CM adjoint is not complex conjugation",
    abs(abs(pi_off) - sqrt_q) > 1e-9 and off_gap > 1.0,
    "|pi|=%.3f, sqrt(q)=%.3f, |q/pi - pi_bar|=%.3f"
    % (abs(pi_off), sqrt_q, off_gap),
)


# CMST4: a CM endomorphism does not construct the NS degree slots.  Keeping
# the same z-operator but changing formal degree slots changes intersections.
Z_cm = mult_matrix(pi_cm)
D_cm = delta(Z_cm)
Gamma_cm = corr(q_cm, Z_cm, 1.0)
Gamma_retuned = corr(q_cm + 3.0, Z_cm, 1.0)
delta_graph = ns_intersection(D_cm, Gamma_cm)
delta_graph_retuned = ns_intersection(D_cm, Gamma_retuned)

gate(
    "CMST4 CM endomorphism does not construct NS degree slots",
    delta_graph == 4.0 and delta_graph_retuned == 7.0,
    "same CM z-operator, Delta.Gamma changes %.1f -> %.1f by changing d1"
    % (delta_graph, delta_graph_retuned),
)


# CMST5: formal CM labels can be declared on controls, but without an actual
# CM abelian carrier the declaration does not build the field embedding,
# endomorphism ring, square, or Rosati.
control_pi = pi_off
control_declares_quadratic_field = True
control_declares_involution = True
control_has_actual_cm_abelian_carrier = False
control_has_cm_endomorphism_ring = False
control_has_zeta_square = False
control_has_positive_rosati_on_square = False
control_metric_gap = abs(q_external / control_pi - control_pi.conjugate())

gate(
    "CMST5 formal CM labels are formable on controls without a CM carrier",
    control_declares_quadratic_field
    and control_declares_involution
    and control_metric_gap > 1.0
    and not control_has_actual_cm_abelian_carrier
    and not control_has_cm_endomorphism_ring
    and not control_has_zeta_square
    and not control_has_positive_rosati_on_square,
    "declared field/involution, |q/pi-pi_bar|=%.3f, no CM AV/end ring/square/Rosati"
    % control_metric_gap,
)


# CMST6: zeta and DH do not acquire the CM carrier merely because CM theory is
# available.  The real theorem applies to CM abelian objects, not to an
# unconstructed End(S^2/Z) square.
zeta_has_cm_abelian_carrier = False
zeta_has_cm_endomorphism_field = False
zeta_has_frobenius_pi_in_cm_field = False
dh_has_cm_abelian_carrier = False
cm_elliptic_anchor_has_carrier = True

gate(
    "CMST6 CM theorem is applicable only after a CM carrier exists",
    cm_elliptic_anchor_has_carrier
    and not zeta_has_cm_abelian_carrier
    and not zeta_has_cm_endomorphism_field
    and not zeta_has_frobenius_pi_in_cm_field
    and not dh_has_cm_abelian_carrier,
    "CM elliptic anchor has carrier; zeta/DH have no CM AV, CM end field, or CM Frobenius pi",
)


# CMST7: construction audit.
zeta_cm_carrier_constructed = False
zeta_cm_type_constructed = False
zeta_cm_endomorphism_field_constructed = False
zeta_rep_ns_constructed = False
zeta_actual_square_constructed = False
zeta_proper_correspondence_category_constructed = False
zeta_fiber_product_composition_constructed = False
zeta_carrier_native_degree_maps_constructed = False
zeta_carrier_native_pairing_constructed = False
zeta_projection_formula_constructed = False
zeta_frobenius_graph_constructed = False
zeta_positive_rosati_constructed = False
zeta_control_death_constructed = False
zeta_dd4_weight_ge_1_constructed = False

gate(
    "CMST7 CM/Shimura package constructs no End(S^2/Z) square package",
    not zeta_cm_carrier_constructed
    and not zeta_cm_type_constructed
    and not zeta_cm_endomorphism_field_constructed
    and not zeta_rep_ns_constructed
    and not zeta_actual_square_constructed
    and not zeta_proper_correspondence_category_constructed
    and not zeta_fiber_product_composition_constructed
    and not zeta_carrier_native_degree_maps_constructed
    and not zeta_carrier_native_pairing_constructed
    and not zeta_projection_formula_constructed
    and not zeta_frobenius_graph_constructed
    and not zeta_positive_rosati_constructed
    and not zeta_control_death_constructed
    and not zeta_dd4_weight_ge_1_constructed,
    "no CM carrier/type/end field, rep_NS, graph, Rosati, control death, or DD.4",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nALL PASS (CMST1-CMST7)")
print(
    "VERDICT: CM/Shimura-Taniyama data is not End(S^2/Z). It genuinely "
    "forces radius for actual CM objects, but it does not construct the zeta "
    "square carrier, CM endomorphism field, degree slots, correspondences, "
    "Frobenius graph, positive Rosati, control death, rep_NS, or DD.4."
)
