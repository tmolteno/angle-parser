# Copyright (c) Tim Molteno 2026 (tim@elec.ac.nz)
# Licensed under the MIT License.

import math
import re

_SUFFIX_TO_RADIANS = {
    "deg": math.pi / 180,
    "arcmin": math.pi / 10800,
    "arcsec": math.pi / 648000,
    "rad": 1.0,
}

_PATTERN = re.compile(
    r"^\s*"
    r"(?P<value>[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)"
    r"\s*"
    r"(?P<suffix>deg|arcmin|arcsec|rad)"
    r"\s*$"
)


def parse_angle(string: str) -> float:
    """Parse an angle string and return the value in radians.

    Supported suffixes: deg, arcmin, arcsec, rad.

    >>> parse_angle("90 deg")
    1.5707963267948966
    >>> parse_angle("1 rad")
    1.0
    """
    match = _PATTERN.match(string)
    if not match:
        raise ValueError(f"Invalid angle string: {string!r}")

    value = float(match.group("value"))
    suffix = match.group("suffix")
    return value * _SUFFIX_TO_RADIANS[suffix]
