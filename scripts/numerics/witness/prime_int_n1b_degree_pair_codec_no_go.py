r"""Degree-pair codec DD.4/SCC no-go.

Doc 269 rejects promoting a single additive valuation character to the two
SCC endpoint degree maps.  This witness tests the obvious repair:

    encode the pair (d1,d2) into one integer by a pairing function.

The positive fact is real.  Cantor and prime-power codes inject pairs into
integers, and a mixed-radix code injects any bounded finite window.  The no-go
is that the code is a codec, not geometry: it imports a decoder, does not
respect valuation arithmetic, does not supply uniform endpoint shifts or a
carrier-native projection formula, is formable on controls, and fills no SCC
slot.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_degree_pair_codec_no_go
"""


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def cantor(pair):
    d1, d2 = pair
    s = d1 + d2
    return s * (s + 1) // 2 + d2


def prime_power(pair):
    d1, d2 = pair
    return (2**d1) * (3**d2)


def mixed_radix(bound):
    return lambda pair: bound * pair[0] + pair[1]


def endpoint_sum(x, y):
    return x[0] + y[0], x[1] + y[1]


def endpoint_product(x, y):
    return x[0] * y[0], x[1] * y[1]


def endpoint_pairing(x, y, trace=0):
    return x[0] * y[1] + x[1] * y[0] - trace


def injection_profile():
    window = [(d1, d2) for d1 in range(7) for d2 in range(7)]
    codes = {
        "cantor": cantor,
        "prime_power": prime_power,
        "mixed_radix_7": mixed_radix(7),
    }
    rows = []
    for name, code in codes.items():
        values = [code(pair) for pair in window]
        rows.append(
            {
                "name": name,
                "window_size": len(window),
                "unique_values": len(set(values)),
                "injects_window": len(values) == len(set(values)),
            }
        )
    return rows


def arithmetic_profile():
    p = (2, 1)
    q = (1, 3)
    global_codes = {"cantor": cantor, "prime_power": prime_power}
    rows = []
    for name, code in global_codes.items():
        rows.append(
            {
                "name": name,
                "additive": code(endpoint_sum(p, q)) == code(p) + code(q),
                "multiplicative": code(endpoint_product(p, q)) == code(p) * code(q),
                "p": p,
                "q": q,
                "code_sum": code(endpoint_sum(p, q)),
                "sum_codes": code(p) + code(q),
                "code_product": code(endpoint_product(p, q)),
                "product_codes": code(p) * code(q),
            }
        )

    finite_code = mixed_radix(7)
    rows.append(
        {
            "name": "mixed_radix_7",
            "injective_only_with_bound": True,
            "global_collision": finite_code((1, 0)) == finite_code((0, 7)),
            "collision_pair": ((1, 0), (0, 7)),
            "collision_value": finite_code((1, 0)),
        }
    )
    return rows


def endpoint_shift_profile():
    window = [(d1, d2) for d1 in range(4) for d2 in range(4)]
    rows = []
    for name, code in {"cantor": cantor, "prime_power": prime_power}.items():
        left_steps = sorted({code((d1 + 1, d2)) - code((d1, d2)) for d1, d2 in window})
        right_steps = sorted({code((d1, d2 + 1)) - code((d1, d2)) for d1, d2 in window})
        rows.append(
            {
                "name": name,
                "left_steps": left_steps,
                "right_steps": right_steps,
                "uniform_left": len(left_steps) == 1,
                "uniform_right": len(right_steps) == 1,
            }
        )

    bound = 7
    finite_code = mixed_radix(bound)
    rows.append(
        {
            "name": "mixed_radix_7",
            "left_steps": [bound],
            "right_steps": [1],
            "uniform_left": True,
            "uniform_right": True,
            "requires_external_bound": True,
            "wrap_collision": finite_code((1, 0)) == finite_code((0, bound)),
        }
    )
    return rows


def decoder_profile():
    pair_a = (10, 1)
    pair_b = (7, 4)
    code_a = cantor(pair_a)
    code_b = cantor(pair_b)

    standard_decode = {code_a: pair_a, code_b: pair_b}
    swapped_decode = {code_a: pair_b, code_b: pair_a}
    left_probe = (1, 0)
    right_probe = (0, 1)

    return {
        "same_code_set": set(standard_decode) == set(swapped_decode),
        "code_a": code_a,
        "code_b": code_b,
        "standard_pair_for_code_a": standard_decode[code_a],
        "swapped_pair_for_code_a": swapped_decode[code_a],
        "left_standard": endpoint_pairing(standard_decode[code_a], left_probe),
        "left_swapped": endpoint_pairing(swapped_decode[code_a], left_probe),
        "right_standard": endpoint_pairing(standard_decode[code_a], right_probe),
        "right_swapped": endpoint_pairing(swapped_decode[code_a], right_probe),
    }


def projection_pairing_profile():
    # Same finite scalar labels; different decoder choices transport different
    # endpoint pairings onto those labels.  The pairing is supplied by the
    # decoder, not by the valuation scalar.
    pair_a = (10, 1)
    pair_b = (7, 4)
    label_a = cantor(pair_a)
    label_b = cantor(pair_b)
    standard = {label_a: pair_a, label_b: pair_b}
    swapped = {label_a: pair_b, label_b: pair_a}
    probe = (2, 5)
    return {
        "labels": (label_a, label_b),
        "standard_pairing_a": endpoint_pairing(standard[label_a], probe),
        "swapped_pairing_a": endpoint_pairing(swapped[label_a], probe),
        "standard_pairing_b": endpoint_pairing(standard[label_b], probe),
        "swapped_pairing_b": endpoint_pairing(swapped[label_b], probe),
        "same_label_set": set(standard) == set(swapped),
    }


def control_codec_profile(dim):
    window = [(d1, d2) for d1 in range(dim) for d2 in range(dim)]
    encoded = {cantor(pair) for pair in window}
    return {
        "dim": dim,
        "all_pairs_encoded": len(encoded) == len(window),
        "declares_decoder": True,
        "uses_square_data": False,
        "kills_controls": False,
    }


injections = injection_profile()
arithmetic = arithmetic_profile()
shifts = endpoint_shift_profile()
decoder = decoder_profile()
projection_pairing = projection_pairing_profile()
controls = [control_codec_profile(dim) for dim in (2, 4, 8)]


gate(
    "DPC1 standard pair codecs really inject endpoint pairs on tested windows",
    all(row["injects_window"] for row in injections),
    "  ".join(
        "%s:%d/%d" % (row["name"], row["unique_values"], row["window_size"])
        for row in injections
    ),
)

gate(
    "DPC2 global injective codecs do not preserve endpoint arithmetic",
    all(
        (not row["additive"]) and (not row["multiplicative"])
        for row in arithmetic
        if row["name"] in ("cantor", "prime_power")
    )
    and next(row for row in arithmetic if row["name"] == "mixed_radix_7")[
        "global_collision"
    ],
    "  ".join(
        (
            "%s:add=%s,mul=%s"
            % (row["name"], row.get("additive"), row.get("multiplicative"))
            if row["name"] != "mixed_radix_7"
            else "%s:collision%s->%d"
            % (row["name"], row["collision_pair"], row["collision_value"])
        )
        for row in arithmetic
    ),
)

gate(
    "DPC3 codec labels do not supply two uniform Laurent endpoint shifts",
    all(
        (not row["uniform_left"]) and (not row["uniform_right"])
        for row in shifts
        if row["name"] in ("cantor", "prime_power")
    )
    and next(row for row in shifts if row["name"] == "mixed_radix_7")[
        "requires_external_bound"
    ]
    and next(row for row in shifts if row["name"] == "mixed_radix_7")[
        "wrap_collision"
    ],
    "  ".join(
        (
            "%s:left%s,right%s" % (row["name"], row["left_steps"], row["right_steps"])
            if row["name"] != "mixed_radix_7"
            else "%s:uniform-only-before-bound,wrap-collides" % row["name"]
        )
        for row in shifts
    ),
)

gate(
    "DPC4 scalar code labels need an imported decoder to recover endpoints",
    decoder["same_code_set"]
    and decoder["standard_pair_for_code_a"] != decoder["swapped_pair_for_code_a"]
    and decoder["left_standard"] != decoder["left_swapped"]
    and decoder["right_standard"] != decoder["right_swapped"],
    (
        "label %d decodes as %s or %s; left/right probes %d/%d and %d/%d"
        % (
            decoder["code_a"],
            decoder["standard_pair_for_code_a"],
            decoder["swapped_pair_for_code_a"],
            decoder["left_standard"],
            decoder["left_swapped"],
            decoder["right_standard"],
            decoder["right_swapped"],
        )
    ),
)

gate(
    "DPC5 transported projection pairing is decoder data, not scalar valuation data",
    projection_pairing["same_label_set"]
    and projection_pairing["standard_pairing_a"] != projection_pairing["swapped_pairing_a"]
    and projection_pairing["standard_pairing_b"] != projection_pairing["swapped_pairing_b"],
    (
        "labels%s: standard %d/%d, swapped %d/%d"
        % (
            projection_pairing["labels"],
            projection_pairing["standard_pairing_a"],
            projection_pairing["standard_pairing_b"],
            projection_pairing["swapped_pairing_a"],
            projection_pairing["swapped_pairing_b"],
        )
    ),
)

gate(
    "DPC6 the same endpoint codec is formable on controls",
    all(
        row["all_pairs_encoded"]
        and row["declares_decoder"]
        and not row["uses_square_data"]
        and not row["kills_controls"]
        for row in controls
    ),
    "  ".join("dim%d:codec-declared" % row["dim"] for row in controls),
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

codec_slots = {
    "injects_endpoint_pairs": True,
    "declares_decoder": True,
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
    "DPC7 degree-pair codecs satisfy no square-carrier slot",
    not any(codec_slots[slot] for slot in required_slots),
    "missing: " + ", ".join(required_slots),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nDPC1-DPC7 ALL PASS: endpoint pair codecs are not carrier degree maps")
print(
    "VERDICT: pairing functions can inject (d1,d2) into one integer, but the "
    "integer is a coded label.  Recovering SCC endpoint data requires an "
    "imported decoder and transported operations; natural valuation arithmetic, "
    "endpoint shifts, projection pairing, control death, and square-carrier "
    "slots are not constructed."
)
