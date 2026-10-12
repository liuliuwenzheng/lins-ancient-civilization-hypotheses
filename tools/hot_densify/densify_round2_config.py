"""Round-2 hot densify editorial constants (Batch A: D-22; Batch B: D-23)."""
TODAY = "2026-10-12"


def make_ed(decision: str, script: str) -> dict:
    return {
        "derived_from": [
            f"tools/hot_densify/{script}",
            "docs/coverage-map.md",
            f"docs/decisions.md#{decision.lower()}",
        ],
        "derived_on": TODAY,
        "notes": (
            f"Hot-pack densify Round-2 toward denser archive ({decision}). "
            "No invented pages/coords/finds/media art. Status stays library-seed-rich "
            "(still below Egypt-level fact-library)."
        ),
    }


# Defaults = Batch A Round-2 (kept for import compatibility)
DECISION = "D-2026-10-12-22"
ED = make_ed(DECISION, "densify_hot_round2_a.py")


def patch_densify_lib(decision: str | None = None, script: str | None = None):
    import densify_lib as dl
    d = decision or DECISION
    s = script or "densify_hot_round2_a.py"
    ed = make_ed(d, s)
    dl.DECISION = d
    dl.TODAY = TODAY
    dl.ED = ed
    return dl
