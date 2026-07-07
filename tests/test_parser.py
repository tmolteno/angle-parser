# Copyright (c) Tim Molteno 2026 (tim@elec.ac.nz)

import math

import pytest

from angle_parser import parse_angle


def test_parse_degrees():
    assert parse_angle("90 deg") == math.pi / 2
    assert parse_angle("180 deg") == math.pi
    assert parse_angle("360 deg") == 2 * math.pi
    assert parse_angle("0 deg") == 0.0


def test_parse_arcmin():
    assert parse_angle("60 arcmin") == math.radians(1)
    assert parse_angle("1 arcmin") == math.radians(1 / 60)


def test_parse_arcmin_synonym():
    assert parse_angle("60'") == math.radians(1)
    assert parse_angle("1'") == math.radians(1 / 60)


def test_parse_arcsec():
    assert parse_angle("3600 arcsec") == math.radians(1)
    assert parse_angle("1 arcsec") == math.radians(1 / 3600)


def test_parse_arcsec_synonym():
    assert parse_angle('3600"') == math.radians(1)
    assert parse_angle('1"') == math.radians(1 / 3600)


def test_parse_mas():
    assert parse_angle("1000 mas") == pytest.approx(math.radians(1 / 3600))
    assert parse_angle("1 mas") == pytest.approx(math.radians(1 / 3600000))


def test_parse_uas():
    assert parse_angle("1e6 uas") == pytest.approx(math.radians(1 / 3600))
    assert parse_angle("1 uas") == pytest.approx(math.radians(1 / 3600000000))


def test_parse_radians():
    assert parse_angle("1 rad") == 1.0
    assert parse_angle("3.141592653589793 rad") == math.pi


def test_negative_values():
    assert parse_angle("-90 deg") == -math.pi / 2
    assert parse_angle("-1 rad") == -1.0


def test_scientific_notation():
    assert parse_angle("1e2 deg") == math.radians(100)


def test_whitespace_handling():
    assert parse_angle("  45  deg  ") == math.pi / 4


def test_invalid_string_raises():
    with pytest.raises(ValueError, match="Invalid angle string"):
        parse_angle("not an angle")
    with pytest.raises(ValueError, match="Invalid angle string"):
        parse_angle("90")
    with pytest.raises(ValueError, match="Invalid angle string"):
        parse_angle("90 grad")
    with pytest.raises(ValueError, match="Invalid angle string"):
        parse_angle("")
