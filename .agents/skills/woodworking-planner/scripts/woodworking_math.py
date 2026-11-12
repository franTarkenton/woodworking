#!/usr/bin/env python3
"""
Reusable woodworking math helpers for the woodworking-planner skill.
Provides 1/16" fraction formatting, bay width splitting onto clean 1/8" tape marks,
and dado depth validation.
"""

import math
from fractions import Fraction


def fmt_in(val: float, denom: int = 16) -> str:
    """Format decimal inches as a woodworking fraction to the nearest 1/denom inch."""
    whole = int(math.floor(val + 1e-9))
    rem = val - whole
    frac = Fraction(round(rem * denom), denom)
    if frac.numerator == denom:
        whole += 1
        frac = Fraction(0, 1)
    if frac.numerator == 0:
        return f'{whole}"'
    if whole == 0:
        return f'{frac.numerator}/{frac.denominator}"'
    return f'{whole} {frac.numerator}/{frac.denominator}"'


def split_into_clean_bays(clear_span: float, num_dividers: int, divider_thickness: float, step: float = 0.25) -> list[float]:
    """
    Split a clear inside span into (num_dividers + 1) bays whose widths all land on
    clean tape-measure increments (default 1/4" steps), with the center bay absorbing
    any remainder so outer bays are symmetric.
    """
    n_bays = num_dividers + 1
    net_open = clear_span - num_dividers * divider_thickness
    outer_w = round((net_open / n_bays) / step) * step
    if n_bays == 3:
        center_w = net_open - 2 * outer_w
        return [outer_w, center_w, outer_w]
    bays = [outer_w] * (n_bays - 1)
    bays.append(net_open - sum(bays))
    return bays


def validate_dado(stock_thickness: float, dado_depth: float, opposing: bool = False) -> dict:
    """Check whether a dado depth leaves sufficient wall thickness."""
    remaining = stock_thickness - (2 * dado_depth if opposing else dado_depth)
    ratio = dado_depth / stock_thickness
    ok = (0.25 <= ratio <= 0.50) and (remaining >= 0.25)
    return {
        "ok": ok,
        "stock_thickness": fmt_in(stock_thickness),
        "dado_depth": fmt_in(dado_depth),
        "remaining_wall": fmt_in(remaining),
        "depth_ratio_pct": round(ratio * 100, 1),
    }

