"""Round-2 Batch A editorial constants (D-2026-10-12-22)."""
DECISION = "D-2026-10-12-22"
TODAY = "2026-10-12"
ED = {
    "derived_from": [
        "tools/hot_densify/densify_hot_round2_a.py",
        "docs/coverage-map.md",
        f"docs/decisions.md#{DECISION.lower()}",
    ],
    "derived_on": TODAY,
    "notes": (
        f"Hot-pack densify Round-2 Batch A toward denser archive ({DECISION}). "
        "No invented pages/coords/finds/media art. Status stays library-seed-rich "
        "(still below Egypt-level fact-library)."
    ),
}


def patch_densify_lib():
    import densify_lib as dl
    dl.DECISION = DECISION
    dl.TODAY = TODAY
    dl.ED = ED
    return dl
