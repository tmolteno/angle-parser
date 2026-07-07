# angle-parser

A simple Python module for parsing angle strings.

## Installation

```bash
pip install angle-parser
```

## Usage

```python
from angle_parser import parse_angle

# Whitespace between value and suffix is optional
parse_angle("90 deg")       # 1.5707963267948966  (π/2 radians)
parse_angle("90deg")        # 1.5707963267948966  (same, no space)
parse_angle("1 arcmin")     # 0.000290888...       (1/60 degree in radians)
parse_angle("1'")           # 0.000290888...       (synonym for arcmin)
parse_angle("1 arcsec")     # 4.8481368...e-06     (1/3600 degree in radians)
parse_angle('1"')           # 4.8481368...e-06     (synonym for arcsec)
parse_angle("1000 mas")     # 4.8481368...e-06     (milli-arcsec)
parse_angle("1e6 uas")      # 4.8481368...e-06     (micro-arcsec)
parse_angle("1 rad")        # 1.0
parse_angle("-45 deg")      # -0.785398...         (negative angles)
parse_angle("1.5e2 deg")    # 2.617993...          (scientific notation)
```

## Supported Suffixes

| Suffix   | Description              | Radians multiplier |
|----------|--------------------------|--------------------|
| `deg`    | Degrees                  | π/180              |
| `arcmin` | Arcminutes (1/60 degree) | π/10800            |
| `'`      | Arcminutes (synonym)     | π/10800            |
| `arcsec` | Arcseconds (1/3600 deg)  | π/648000           |
| `"`      | Arcseconds (synonym)     | π/648000           |
| `mas`    | Milli-arcseconds          | π/648000000        |
| `uas`    | Micro-arcseconds          | π/648000000000     |
| `rad`    | Radians                  | 1.0                |

## API

### `parse_angle(string)`

Parse an angle string and return the value in radians.

- **Parameters:** `string` — A string containing a numeric value followed by a valid suffix (`deg`, `arcmin`/`'`, `arcsec`/`"`, `mas`, `uas`, `rad`). Whitespace between the value and suffix is optional.
- **Returns:** `float` — The angle in radians.
- **Raises:** `ValueError` — if the string does not match the expected format.

## License

Copyright (c) Tim Molteno 2026 (tim@elec.ac.nz)

MIT License
