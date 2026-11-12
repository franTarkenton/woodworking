---
name: woodworking-planner
description: >-
  Designs parametric woodworking and cabinetry projects, validates fractional stack-up
  math and structural joinery (dados, rabbets, spans, racking, drawer runners), and generates
  labeled 2D vector blueprints, interactive 3D exploded part viewers, master cut lists, and
  router layout tables. Use this skill whenever the user wants to design, modify, or generate
  plans and cut lists for a woodworking, shelving, cabinet, or furniture project.
---

# Woodworking Planner Skill

Follow this workflow to turn rough woodworking dimensions into verified parametric plans, labeled blueprints, an interactive 3D assembly explorer, and a shop-ready Master Cut List.

> [!IMPORTANT]
> **Save All Artifacts Inside the Project Directory:** Whenever you create any artifact (`.svg` blueprints, `.html` interactive 3D viewers, or `.md` cut lists/plans), **always save a copy directly inside the project root directory** (`/home/kjnether/workspace/sketchup/`) in addition to the conversation's artifact directory.

## Step 1: Interview & Structural Engineering Check

Before generating files, verify the following parameters with the user and check the math:

1. **Overall vs. Carcass Dimensions:** Clarify whether stated Width × Height × Depth measurements represent the **carcass (box)** or the **outermost footprint** including top overhangs and trim.
2. **Vertical & Horizontal Stack-Up Math:**
   - Sum all vertical opening heights + horizontal shelf/divider thicknesses + base/floorboard + top thickness.
   - If the sum does not match the target height, show the exact discrepancy in fractions (`1/16"`) and ask which opening should absorb the difference.
   - Divide horizontal bays so every opening and divider location lands on a clean tape-measure fraction (`1/8"` or `1/4"` increments, avoiding `1/3"` fractions).
3. **Structural & Joinery Checks:**
   - **Shelf Sag:** Flag any unsupported `5/8"` shelf spanning over `36"` and recommend bumping that shelf to `3/4"`, adding an apron/edging, or tying into a back panel.
   - **Dado Depth:** Target `1/3` to `1/2` of stock thickness (e.g., `1/4"` or `3/16"` deep in `5/8"` stock). Verify there are no **back-to-back opposing dados** on the same board face location.
   - **Open-Back Racking:** If the piece has an open back, include a rear base apron/floorboard and an upper rear anti-racking cleat/stretcher.
   - **Shop-Made Drawers:** For side-hung grooved drawers on wooden runners, ensure groove depth (`1/4"`) leaves at least `3/8"` wall thickness in `5/8"` drawer sides, size inset drawer fronts with a uniform `1/8"` reveal (penny gap), and include a rear drawer stop if the back is open.

## Step 2: Parametric Script (`generate_<project>_plan.py`)

Create or update a zero-dependency parametric Python script in the workspace (see [woodworking_math.py](./scripts/woodworking_math.py) for fraction formatting and stack-up helpers):
- Define all primary dimensions as top-level constants in inches.
- Use `assert abs(actual - expected) < 1e-6` to enforce that vertical and horizontal stack-ups match carcass dimensions.
- Assign every unique part a consistent ID (`A`, `B`, `C`, `J1`, `R`, etc.) and export `<project>_cut_list.json`.
- If running Python via CLI, always follow the workspace rule (`uv run python ...`).

## Step 3: Labeled 2D Blueprint & Interactive 3D Explorer

Generate two visual aids in **both** the project workspace directory and the conversation's artifact directory:

1. **2D Vector Blueprint (`<project>_blueprint.svg`):**
   - Draw a scaled **Front Elevation** and **Side Cross-Section**.
   - Tag every board with its Part ID badge (`A`–`Z`) and dimension arrows for overall, carcass, and bay opening measurements.
2. **Interactive 3D Exploded Part Explorer (`<project>_explorer.html`):**
   - Activate the `generative_ui` skill and build a compact inline HTML widget (`<= 440px` tall) with:
     - **Explode Parts** slider (separates boards along assembly axes so dados and rabbets are visible).
     - **Pull Drawers / Open Doors** slider.
     - Drag-to-rotate 3D canvas + quick camera presets (`3D View`, `Front`, `Side`).
     - Clickable **Part ID badges (`A`–`Z`)** that highlight all matching boards on the 3D model and display the part's quantity, exact fractional dimensions (`T × W × L`), and joinery notes.

## Step 4: Master Cut List & Router Layout Guide (`<project>_cut_list_and_plan.md`)

Create a markdown document (in both the project workspace directory and the conversation's artifact directory) containing:
1. Embedded `<project>_blueprint.svg`.
2. **Finished & Carcass Dimensions Summary** + Vertical Height Stack-Up table.
3. **Master Cut List Table** (`Part ID`, `Part Name`, `Qty`, `Thickness`, `Width`, `Cut Length`, `Decimal`, and `Where It Goes & Joinery Notes`), explicitly noting dado allowances (`+1/2"` for two `1/4"` dados).
4. **Router Dado & Groove Layout Checklist** giving exact start-to-end measurements from the bottom or left reference edge of each grooved board so the user can clamp a straightedge directly from the table.
5. **Recommended Shop Assembly Sequence** diagram and step-by-step dry-fit/glue-up order.
