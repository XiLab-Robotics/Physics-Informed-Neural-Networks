# Project Programming Style Guide

## Reference Sources

- `reference/codes/blind_handover_controller`
- `reference/codes/mediapipe_gesture_recognition`
- `reference/codes/multimodal_fusion`

The main style baseline is `blind_handover_controller`, while the other two repositories reinforce the same naming, comment, structure, and implementation patterns.

## Naming

### Variables

- Prefer explicit, domain-oriented names.
- Representative examples:
  - `trajectory_execution_received`
  - `train_dataloader`
  - `human_radius`
  - `admittance_weight`
  - `joint_states`
  - `process_dataset`

### Constants

- Use full uppercase for module-level constants and flags.
- Examples:
  - `PACKAGE_PATH`
  - `DEVICE`
  - `MODEL_TYPE`
  - `GRIPPER_OPEN`
  - `DYNAMIC_PLANNER`

### Classes

- Use `PascalCase` in most cases.
- Preserve mixed robotics naming when it improves semantic clarity.
- Examples:
  - `TrainingNetwork`
  - `AdmittanceController`
  - `UR_RTDE_Move`
  - `UR_Toolbox`
  - `Handover_Controller`

### Functions And Methods

- Use `snake_case` for general utilities and helper functions.
- For ROS callbacks or node-facing methods, preserve the mixed naming convention already present in the reference repositories.
- Examples:
  - `train_network`
  - `get_model_name`
  - `save_hyperparameters`
  - `jointStatesCallback`
  - `FTSensorCallback`

## Comments

### Comment Style

- Frequent, short, and operational.
- Written in title case.
- Used to structure the flow more than to explain obvious syntax.

### Preferred Patterns

- `# Import ROS Messages`
- `# Initialize Admittance Controller`
- `# Compute Cartesian Velocity`
- `# Save Model`
- `# Move to Home | Error -> Return`

### Practical Rules

- Capitalize the main words.
- Place comments before distinct logical blocks.
- It is acceptable to use `->`, parentheses, or technical acronyms when they improve readability.
- Keep section comments short and scannable.
- Prefer compact labels such as `# Resolve Browser Path`, `# Validate Table Structure`, or `# Flush Pending Paragraph`.
- Avoid sentence-length comments that narrate every small step of an obvious parsing or rendering operation.

## Docstrings

- Use Google-style docstrings as the canonical default for new or materially refactored repository-owned Python scripts.
- This repository uses Sphinx `napoleon`, so public API-facing docstrings should render cleanly through that path without a later retrofit pass.
- Keep trivial helpers concise, but do not fall back to placeholder one-line docstrings for non-trivial workflow functions, public utilities, dataclasses, classes, or module entry points.
- Prefer a short summary line first. Then add `Args`, `Returns`, `Raises`, `Attributes`, or `Notes` sections only when they materially improve API clarity.
- Legacy one-line title-case docstrings may remain in untouched older files, but they are no longer the default target format for new script work.
- For top-level definitions, leave one blank line between the `def` or `class` line and the docstring.
- Apply the same blank-line rule to methods when they use a docstring.
- Apply the same blank-line rule to `@dataclass(...)` declarations followed by `class`.

Representative examples:

- `""" Handover Controller Class """`
- `""" Compute Loss """`
- `""" Cartesian Goal Callback """`

Google-style examples:

```python
def resolve_validation_output_directory(pdf_output_path: Path) -> Path:

    """Resolve the output directory used for PDF validation images.

    Args:
        pdf_output_path: Exported PDF path for the current report.

    Returns:
        Validation-image directory for the current PDF.
    """
```

```python
@dataclass(frozen=True)
class SnapshotRecord:

    """Store one selected report-worthy snapshot candidate.

    Attributes:
        timestamp_seconds: Snapshot timestamp in seconds.
        frame_path: Project-relative path to the frame image.
        selection_reason: Human-readable reason for keeping the snapshot.
    """
```

Spacing examples:

```python
def resolve_project_relative_path(path_value: str | Path) -> Path:

    """ Resolve Project Relative Path """
```

```python
@dataclass(frozen=True)
class TransmissionErrorCurveSample:

    """ Transmission Error Curve Sample """
```

```python
class TransmissionErrorRegressionModule(LightningModule):

    """ Transmission Error Regression Module """

    def compute_loss(self, batch_dictionary: dict[str, torch.Tensor], log_prefix: str) -> torch.Tensor:

        """ Compute Loss """
```

## Code Structure

- Prefer explicit and progressive code.
- Break the reasoning into well-named intermediate blocks.
- Avoid overly compact abstractions when they reduce readability.
- Separate logical groups with comments.
- Keep one blank line between consecutive top-level definitions.
- Reduce superfluous blank lines between adjacent import blocks, constants, and top-level definitions when the file remains easy to scan.

## Manual Refactoring Patterns

The broad manual refactoring applied across the Python scripts in commit `f624b975ab4c1829854a2c1b6dd63c945206ebd7` remains the repository-wide baseline refinement.

The later exporter-focused manual refactoring in commit `0c8b5003ddcce34d672b2822c2afe8e357a1fb26` further clarified how that style should be applied in compact utility scripts.

The later manual refactoring of `scripts/reports/validate_report_pdf.py` further sharpened the preferred style for very small utility scripts that still need explicit staged logic.

Apply these patterns conservatively:

- use compact grouped imports when the grouping remains readable;
- reduce unnecessary blank lines between adjacent top-level blocks when readability is preserved;
- keep helper signatures on one line when they are short enough to stay readable;
- keep short method signatures on one line when wrapping is unnecessary;
- keep short `try/except/else` import guards on one line when the whole block remains immediately readable;
- keep short parser `add_argument(...)` calls on one line when each declaration still scans cleanly;
- use inline `if` statements only when the branch is obvious in context and the resulting line stays readable;
- compact asserts, list comprehensions, and call expressions when the result remains easy to scan;
- collapse single obvious follow-up statements when they remain easy to scan;
- keep section comments short, operational, and easy to scan;
- prefer comment labels that mark intent without turning into sentence-length prose;
- for compact utility scripts, allow a tighter vertical rhythm between small staged helpers when the file remains easy to scan top-to-bottom;
- preserve engineering readability over compactness when the two conflict.
- when a helper or utility call passes a local variable with the same parameter name and the argument order is short and obvious, prefer positional arguments over redundant `name=name` repetition;
- keep explicit keyword arguments for readability-critical calls, especially booleans, flags, constructor-style calls, and filesystem operations such as `mkdir(parents=True, exist_ok=True)`.

Representative examples:

```python
import sys, shutil, logging, warnings
```

```python
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))
```

```python
# Resolve Browser Path
```

```python
if logger.log_dir: print_key_value("TensorBoard Log Directory", logger.log_dir, value_color=Fore.YELLOW)
```

```python
import re, random
```

```python
try: import pymupdf
except ImportError as import_error: pymupdf, PYMUPDF_IMPORT_ERROR = None, import_error
else: PYMUPDF_IMPORT_ERROR = None
```

```python
argument_parser.add_argument("--render-scale", type=float, default=DEFAULT_RENDER_SCALE, help="Zoom multiplier used during PDF rasterization.")
```

```python
def resolve_csv_file_path(dataset_root: Path, csv_path: Path | None, file_index: int) -> Path:

    """ Resolve CSV File Path """
```

```python
assert csv_columns == expected_columns, (f"Unexpected CSV columns detected | Expected: {sorted(expected_columns)} | Given: {sorted(csv_columns)}")
```

## Imports

- Organize imports in grouped blocks.
- Add short heading comments above important import groups.
- When several imports belong to the same compact utility group and the result stays readable, it is acceptable to combine them on one line.
- When a compact import line hurts readability, split it back into the clearer multi-line form.

Typical pattern:

```python
from termcolor import colored

# Import PyTorch Lightning Functions
from pytorch_lightning.callbacks import EarlyStopping

# Import Processed Dataset and DataLoader
from process_dataset import ProcessDataset
```

## Checks And Validation

- Use explicit assertions with detailed messages.
- Make assumptions about data type and shape visible.

Correct tone example:

```python
assert len(joint_positions) == 6, f"Joint Positions Length must be 6 | {len(joint_positions)} given"
```

## Type Hints

- Use type hints when they clarify tensors, arrays, ROS messages, return tuples, and dataloaders.
- They do not need to be forced everywhere, but they are part of the technical tone of the reference code.

## Logging And Debug

- Use direct, concrete messages, often through `print` or ROS loggers.
- If useful, use colorized output for training, debugging, or controller state.
- Avoid generic or overly narrative logging text.

## Rules To Apply In This Repository

- Every new file should use explicit and readable naming.
- Every new or materially refactored repository-owned Python script should use Google-style docstrings for public modules, classes, dataclasses, and non-trivial public functions.
- Every non-trivial function should be split into blocks with title-case comments.
- Keep those block comments compact unless extra detail is genuinely needed for domain logic or safety.
- Configurations and constants should remain semantically transparent.
- ML code should remain understandable from an engineering perspective and compatible with future export or deployment.
- Apply the approved blank-line spacing rules to top-level functions, classes, dataclasses, and documented methods.
- Treat Sphinx plus `napoleon` compatibility as part of the default definition of a complete script implementation, not as a later documentation-only cleanup step.
- Use the latest relevant manually refactored Python-script style as the repository reference when choosing between equally valid compact layouts.
- For compact utility and exporter scripts, treat commit `0c8b5003ddcce34d672b2822c2afe8e357a1fb26` as the sharper reference for comment length, grouped imports, and concise helper layout.
- For very small validation and reporting utilities, also treat the manual `scripts/reports/validate_report_pdf.py` refactor as a reference for compact import guards, one-line parser declarations, and tighter helper spacing when readability remains high.
- When in doubt, follow the pattern used in `blind_handover_controller`.
