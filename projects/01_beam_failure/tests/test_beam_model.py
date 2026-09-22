import pytest

from src.beam_model import (
    exceeds_allowable_stress,
    max_bending_moment,
    max_bending_stress,
    second_moment_rectangular,
)


def test_max_bending_moment():
    assert max_bending_moment(1000.0, 2.0) == pytest.approx(500.0)


def test_second_moment_rectangular():
    assert second_moment_rectangular(0.1, 0.2) == pytest.approx(0.0000666666667)


def test_max_bending_stress():
    stress = max_bending_stress(
        load_n=1000.0,
        span_m=2.0,
        width_m=0.1,
        height_m=0.2,
    )
    assert stress == pytest.approx(7_500_000.0)


def test_allowable_stress_check():
    assert exceeds_allowable_stress(80e6, 70e6) is True
    assert exceeds_allowable_stress(60e6, 70e6) is False
