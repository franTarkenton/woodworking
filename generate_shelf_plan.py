#!/usr/bin/env python3
"""
Parametric Quarter-Sawn Fir Shelf Calculator (Zero External Dependencies)
Edit any dimension constant below and run:
    python3 generate_shelf_plan.py
to recompute the Master Cut List and Dado/Groove Router Layout coordinates.
"""

import json
import math
from fractions import Fraction


def fmt_in(val: float) -> str:
    """Format decimal inches as a woodworking fraction to the nearest 1/16"."""
    whole = int(math.floor(val + 1e-9))
    rem = val - whole
    frac = Fraction(round(rem * 16), 16)
    if frac.numerator == 16:
        whole += 1
        frac = Fraction(0, 1)
    if frac.numerator == 0:
        return f'{whole}"'
    if whole == 0:
        return f'{frac.numerator}/{frac.denominator}"'
    return f'{whole} {frac.numerator}/{frac.denominator}"'


# ==============================================================================
# 1. PARAMETRIC DIMENSIONS (in inches)
# ==============================================================================
OVERALL_H = 44.0            # 44" total finished height (including 2" top)
TOP_THICK = 2.0             # 2" thick top slab
CARCASS_W = 42.5            # 42 1/2" carcass outer width
CARCASS_H = OVERALL_H - TOP_THICK  # 42" carcass outer height
CARCASS_D = 18.0            # 18" carcass outer depth

TOP_OVERHANG_FRONT = 1.0    # 1" front overhang
TOP_OVERHANG_SIDE = 1.0     # 1" left & right overhangs
TOP_OVERHANG_BACK = 0.0     # Flush at back

STOCK_T = 5 / 8             # 5/8" (0.625") standard board thickness
UPPER_SHELF_T = 3 / 4       # 3/4" (0.750") heavy-duty upper full-span shelf
DRAWER_BOTTOM_T = 3 / 8     # 3/8" (0.375") resawn fir drawer bottom
DADO_DEPTH = 1 / 4          # 1/4" (0.250") dado depth in 5/8" stock

FLOORBOARD_H = 2.5          # 2 1/2" front & rear floorboards
BAY1_H = 12.625             # 12 5/8" lower bay opening (3 bays + 2 center drawers)
BAY2_H = 10.5               # 10 1/2" middle open bay
BAY3_H = CARCASS_H - (FLOORBOARD_H + BAY1_H + STOCK_T + BAY2_H + UPPER_SHELF_T)  # 15" exact!

INSIDE_W = CARCASS_W - 2 * STOCK_T      # 41 1/4" (41.250") clear inside width
FULL_SHELF_LEN = INSIDE_W + 2 * DADO_DEPTH  # 41 3/4" (41.750") shelf cut length

LEFT_BAY_W = 13.25          # 13 1/4" left lower bay
MID_BAY_W = 13.50           # 13 1/2" middle drawer bay
RIGHT_BAY_W = 13.25         # 13 1/4" right lower bay
assert abs((LEFT_BAY_W + STOCK_T + MID_BAY_W + STOCK_T + RIGHT_BAY_W) - INSIDE_W) < 1e-6

# ==============================================================================
# 2. MASTER CUT LIST
# ==============================================================================
CUT_LIST = [
    {
        "id": "A",
        "name": "Top Slab (Overhanging)",
        "qty": 1,
        "t": TOP_THICK,
        "w": CARCASS_D + TOP_OVERHANG_FRONT,
        "l": CARCASS_W + 2 * TOP_OVERHANG_SIDE,
        "where": 'Sits on top of carcass; overhangs front & sides by 1", flush at back.'
    },
    {
        "id": "B",
        "name": "Outer Side Panels (Left & Right)",
        "qty": 2,
        "t": STOCK_T,
        "w": CARCASS_D,
        "l": CARCASS_H,
        "where": 'Left & right vertical sides. Route 1/4" deep cross-dados on inside face.'
    },
    {
        "id": "C",
        "name": "Bottom Shelf (Flush w/ Floorboard)",
        "qty": 1,
        "t": STOCK_T,
        "w": CARCASS_D - 2 * STOCK_T,
        "l": FULL_SHELF_LEN,
        "where": 'Fits between front & rear floorboards F; top face flush at 2 1/2" from floor.'
    },
    {
        "id": "D",
        "name": "Lower Full Shelf (Above 3 Bays)",
        "qty": 1,
        "t": STOCK_T,
        "w": CARCASS_D,
        "l": FULL_SHELF_LEN,
        "where": 'Separates 12 5/8" lower bay from 10 1/2" middle bay (bottom at 15 1/8").'
    },
    {
        "id": "E",
        "name": 'Upper Full Shelf (3/4" Thick)',
        "qty": 1,
        "t": UPPER_SHELF_T,
        "w": CARCASS_D,
        "l": FULL_SHELF_LEN,
        "where": 'Separates 10 1/2" middle bay from 15" top bay (bottom at 26 1/4").'
    },
    {
        "id": "F",
        "name": "Front & Rear Floorboards (Base Aprons)",
        "qty": 2,
        "t": STOCK_T,
        "w": FLOORBOARD_H,
        "l": FULL_SHELF_LEN,
        "where": '1 at bottom front, 1 matching at bottom back to prevent racking.'
    },
    {
        "id": "G",
        "name": "Lower Vertical Bay Dividers",
        "qty": 2,
        "t": STOCK_T,
        "w": CARCASS_D,
        "l": BAY1_H + 2 * DADO_DEPTH,
        "where": 'Divides lower 12 5/8" section into 13 1/4" (L), 13 1/2" (Drawers), 13 1/4" (R).'
    },
    {
        "id": "H1",
        "name": "Top Rear Anti-Racking Cleat",
        "qty": 1,
        "t": STOCK_T,
        "w": 2.0,
        "l": FULL_SHELF_LEN,
        "where": 'Tucked under back edge of 2" top A inside upper bay to lock frame square.'
    },
    {
        "id": "H2",
        "name": "Rear Drawer Stop Stretcher",
        "qty": 1,
        "t": STOCK_T,
        "w": 2.0,
        "l": MID_BAY_W,
        "where": 'At rear of 13 1/2" middle drawer bay so inset drawers stop flush at front.'
    },
    {
        "id": "J1",
        "name": "Inset Drawer Fronts (2 Drawers)",
        "qty": 2,
        "t": STOCK_T,
        "w": 6.125,
        "l": 13.375,
        "where": 'Front faces of upper & lower drawers (1/8" reveal top/middle/bottom).'
    },
    {
        "id": "J2",
        "name": "Drawer Backs (2 Drawers)",
        "qty": 2,
        "t": STOCK_T,
        "w": 5.375,
        "l": 12.625,
        "where": 'Rear faces of upper & lower drawer boxes (set into dados in sides K).'
    },
    {
        "id": "K",
        "name": "Grooved Drawer Sides (2 Drawers)",
        "qty": 4,
        "t": STOCK_T,
        "w": 5.875,
        "l": 17.0,
        "where": 'Left & right drawer sides; 1/4" deep x 17/32" wide groove on outside face.'
    },
    {
        "id": "L",
        "name": "Drawer Bottom Panels (2 Drawers)",
        "qty": 2,
        "t": DRAWER_BOTTOM_T,
        "w": 12.625,
        "l": 16.25,
        "where": 'Captured in 1/4" deep grooves on inside bottom of J1 and K.'
    },
    {
        "id": "R",
        "name": "Shop-Made Drawer Runners",
        "qty": 4,
        "t": 0.25,
        "w": 0.50,
        "l": 17.0,
        "where": 'Glued & screwed inside vertical dividers G for drawer grooves K to ride on.'
    },
]

if __name__ == "__main__":
    with open("shelf_cut_list.json", "w") as f:
        json.dump(CUT_LIST, f, indent=2)
    print(f"Generated shelf_cut_list.json with {len(CUT_LIST)} part groups.")
    for p in CUT_LIST:
        print(f"[{p['id']:2s}] Qty {p['qty']} | {fmt_in(p['t']):>6s} T x {fmt_in(p['w']):>8s} W x {fmt_in(p['l']):>8s} L | {p['name']}")
