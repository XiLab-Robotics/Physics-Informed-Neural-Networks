# Class And Dataclass Spacing Normalization

## Overview

The previous repository-wide spacing work normalized top-level function definitions, but it did not extend the same convention to class declarations.

The user clarified that the spacing rule must also apply to:

- regular `class` definitions;
- `@dataclass` declarations followed by `class`.

Concretely, the expected layout is:

```python
@dataclass(frozen=True)
class TransmissionErrorCurveSample:

    """ Transmission Error Curve Sample """
```

and likewise for regular classes:

```python
class TransmissionErrorDataModule(LightningDataModule):

    """ Transmission Error DataModule """
```

## Technical Approach

This change is purely stylistic and must not alter runtime behavior.

The approved repository convention is now:

- one blank line between a top-level `def ...:` line and its docstring;
- one blank line between a top-level `class ...:` line and its docstring;
- the same blank line after a decorated `@dataclass(...)` class header;
- one blank line between consecutive top-level definitions.

`training/train_feedforward_network.py` remains the reference style for the surrounding file layout, while this follow-up extends the same readability rule to class bodies in the remaining project-authored Python files.

The implementation should:

1. inspect project-authored Python files under `models/`, `training/`, and `scripts/`;
2. add a blank line after top-level class headers before the docstring;
3. add the same blank line after top-level dataclass-based class headers before the docstring;
4. preserve the already approved function-spacing convention;
5. keep imports, comments, methods, and runtime logic unchanged.

## Involved Components

- `models/feedforward_network.py`
- `training/transmission_error_datamodule.py`
- `training/transmission_error_regression_module.py`
- `scripts/datasets/transmission_error_dataset.py`
- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index.

## Implementation Steps

1. Scan the project-authored Python files for top-level class and dataclass declarations.
2. Insert one blank line between each top-level class header and its docstring.
3. Insert one blank line between each top-level dataclass declaration and its class docstring.
4. Keep the existing top-level function-spacing normalization unchanged.
5. Run a lightweight syntax validation over the edited files.
6. Create the required Git commit immediately after the approved modification.
