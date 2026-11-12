# Workspace Guidelines & Environment Rules

## Artifact & Output File Locations
- **Keep Everything Strictly in the Project:** All project files, generated documents, blueprints, scripts, HTML viewers, and PDFs MUST live exclusively in the project workspace (`/home/kjnether/workspace/sketchup/`). Never copy or write project files into `~/.gemini/` or any other external directory.

## Python Environment (`pyenv` & `uv`)
- **Python Manager:** `pyenv` is installed and used for Python version management.
- **Package Management:** Always use `uv add <pkg>` to add dependencies to the project venv. Never use bare `pip`, `uv pip`, or `--with` flags.
- **Script Runner:** Always use `uv run python <script.py>` to run scripts.
- **Zero-Dependency Preference:** When generating parametric woodworking scripts or SVG/JSON generators, prefer standard-library Python where practical so scripts run instantaneously without external binary dependencies.

## Woodworking & CAD Project Conventions
- **Part Labeling (`A`–`Z`):** Every distinct part in a project must have a consistent single-letter (or letter+number) ID (`A`, `B`, `C`, `J1`, `R`, etc.) shared across the parametric script, 2D blueprints, 3D viewer, and Master Cut List.
- **Woodworking Fractions:** Always display measurements in standard woodworking fractions to the nearest `1/16"` (e.g., `41 3/4"`) alongside decimal inches (`41.750"`) in cut lists.
- **Joinery Allowances:** Explicitly state whether cut lengths include dado/rabbet engagement depths (e.g., `+1/2"` total for two `1/4"` dados) and provide a router layout checklist measuring from a single reference edge (bottom or left end).
