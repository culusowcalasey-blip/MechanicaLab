"""Basic mechanics model for a simply supported beam with a center load."""


def max_bending_moment(load_n: float, span_m: float) -> float:
    """Return maximum bending moment in N*m."""
    return load_n * span_m / 4.0


def second_moment_rectangular(width_m: float, height_m: float) -> float:
    """Return second moment of area for a rectangle in m^4."""
    return width_m * height_m**3 / 12.0


def max_bending_stress(
    load_n: float,
    span_m: float,
    width_m: float,
    height_m: float,
) -> float:
    """Return maximum bending stress in Pa."""
    moment = max_bending_moment(load_n, span_m)
    inertia = second_moment_rectangular(width_m, height_m)
    c = height_m / 2.0
    return moment * c / inertia


def exceeds_allowable_stress(stress_pa: float, allowable_pa: float) -> bool:
    """Return True when stress exceeds the allowable stress."""
    return stress_pa > allowable_pa
