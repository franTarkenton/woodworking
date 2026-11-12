# Parametric Woodworking & CAD Design Repository

A code-first woodworking and cabinetry design framework. Instead of wrestling with manual CAD software like SketchUp, this repository uses parametric Python models, clean fractional stack-up math (`1/16"`), and automated generator scripts to produce shop-ready blueprints, interactive 3D exploded assemblies, master cut lists, and print-ready PDFs.

---

## Repository Structure & Project Files

```text
├── .agents/
│   └── skills/
│       └── woodworking-planner/   # Reusable AI skill for designing new furniture
│           ├── SKILL.md            # Workflow guide (interviews, sag checks, joinery math)
│           └── scripts/
│               └── woodworking_math.py # Helper library (fractions, bay splitting, dado checks)
├── AGENTS.md                       # Environment guidelines (pyenv, uv, part ID conventions)
├── pyproject.toml / uv.lock        # Python project configuration managed via uv
│
├── Project: Quarter-Sawn Fir Shelf (44" H x 44 1/2" W x 19" D)
│   ├── generate_shelf_plan.py      # Parametric Python script defining dimensions and cut list
│   ├── shelf_blueprint.svg         # Scaled 2D vector blueprint (Front Elevation & Side Section)
│   ├── shelf_explorer.html         # Interactive 3D model with part explode & drawer pull sliders
│   ├── shelf_cut_list_and_plan.md  # Master Cut List (Parts A–R) & Router Dado Layout Guide
│   ├── generate_print_view.py      # Script to render the plan into print-optimized HTML & PDF
│   ├── shelf_print_view.html       # Print-formatted HTML view (Ctrl+P ready)
│   └── shelf_cut_list_and_plan.pdf # Direct, letter-sized shop printout
└── README.md                       # This documentation file
```

---

## Standard Woodworking Conventions

Every project designed in this repository follows consistent shop standards:

1. **Part Labeling (`A`–`Z`):** Every board is tagged with a single-letter or letter+number ID (`A`, `B`, `C`, `J1`, `R`, etc.) that remains identical across scripts, 2D blueprints, 3D viewers, and the cut list.
2. **Dual Measurements:** Measurements are always shown in tape-measure fractions to the nearest `1/16"` (e.g., `41 3/4"`) alongside decimal equivalents (`41.750"`).
3. **Explicit Joinery Allowances:** All cut lengths explicitly state whether they include dado/rabbet engagement (e.g., `+1/2"` total for two `1/4"` dados).
4. **Router Layout Tables:** Every design includes a setup checklist measuring from a single reference edge (bottom or left) so fence stops and guides can be clamped accurately.

---

## Current Project: Quarter-Sawn Fir Shelf

A multi-bay console shelf with shop-made side-hung inset drawers and an open-back design:

* **Dimensions:** Overall `44 1/2" W × 44" H × 19" D` (Carcass: `42 1/2" W × 42" H × 18" D`).
* **Top:** `2"` thick slab overhanging front and sides by `1"`, flush at back.
* **Base:** `2 1/2"` front and rear floorboard aprons with bottom shelf flush at top.
* **Lower Bay (`12 5/8"` H):** 3-way split (`13 1/4"` Left, `13 1/2"` Center, `13 1/4"` Right) featuring two stacked drawers on shop-made `1/4" × 1/2"` wooden runners.
* **Middle Bay (`10 1/2"` H):** Full-span open bay (`41 1/4"` wide).
* **Upper Bay (`15"` H):** Full-span open bay with heavy-duty `3/4"` shelf for sag prevention and rear anti-racking stretcher.

---

## How to Add a New Woodworking Project

You can design new projects by asking your assistant or running scripts directly:

### 1. Using the Built-In Woodworking Planner Skill
Simply describe your new project in chat (e.g., *"I want to design a bedside nightstand with 3 drawers..."*). The local skill at `.agents/skills/woodworking-planner/` will automatically:
- Verify vertical and horizontal fractional stack-up math before cutting wood.
- Check shelf spans for sag and validate dado depth ratios (`1/3` to `1/2` thickness).
- Ensure racking stability for open-back designs.
- Generate the parametric script, 2D blueprint, 3D interactive viewer, cut list, and PDF.

### 2. Reusing Math Helpers (`woodworking_math.py`)
Import the helper functions into your new parametric script:
```python
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent / ".agents/skills/woodworking-planner/scripts"))

from woodworking_math import fmt_in, split_into_clean_bays, validate_dado

# Example: format 41.75 into a clean fraction string -> '41 3/4"'
print(fmt_in(41.75))

# Example: split a 40" span across 2 dividers into clean tape-measure bays
bays = split_into_clean_bays(clear_span=40.0, num_dividers=2, divider_thickness=0.625)
print(bays)  # [13.25, 13.5, 13.25]
```

### 3. Adding Dependencies & Running Scripts
Always use `uv` and `pyenv` in accordance with repository rules:
```bash
# Add new Python dependencies to the project virtual environment
uv add <package-name>

# Run any parametric script
uv run python generate_shelf_plan.py

# Re-render printable HTML & PDF
uv run python generate_print_view.py
```

---

## Quick Viewing & Printing

* **Interactive 3D Explorer:** Open [shelf_explorer.html](shelf_explorer.html) in Google Chrome or any modern browser to rotate the model, pull the drawers, or explode parts.
* **Shop Cut List (PDF):** Open and print [shelf_cut_list_and_plan.pdf](shelf_cut_list_and_plan.pdf).
* **2D Vector Blueprint:** View [shelf_blueprint.svg](shelf_blueprint.svg) for detailed dimension lines and part callouts.

