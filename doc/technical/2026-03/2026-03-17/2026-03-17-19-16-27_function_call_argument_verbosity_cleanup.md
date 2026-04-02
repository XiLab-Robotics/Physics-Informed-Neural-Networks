# Function Call Argument Verbosity Cleanup

## Overview

This document records the requested style cleanup for function and method call sites across the project-authored Python scripts.

The requested rule is:

- avoid redundant keyword argument passing when the local variable name is identical to the parameter name and the positional order remains clear;
- keep explicit keyword arguments when they materially improve readability or when positional passing would become ambiguous;
- preserve explicit keyword style for calls where named boolean or structural options are clearer than compact positional form.

Representative example requested by the user:

Old:

```python
output_directory = shared_training_infrastructure.resolve_output_directory(training_config=training_config, output_suffix=output_suffix)
```

New:

```python
output_directory = shared_training_infrastructure.resolve_output_directory(training_config, output_suffix)
```

Counterexample where explicit keywords should remain:

```python
output_directory.mkdir(parents=True, exist_ok=True)
```

The goal is not to remove all keyword arguments mechanically. The goal is to remove unnecessary repetition while preserving readability.

## Technical Approach

### Style Rule To Apply

The cleanup should apply this decision order at each call site.

#### 1. Prefer Positional Arguments When All Conditions Hold

Convert a call from explicit keyword style to positional style when:

- the variable names repeat the parameter names exactly or near-exactly in a redundant way;
- the function signature order is short and obvious at the call site;
- the call remains easy to scan after conversion;
- no semantic ambiguity is introduced.

Examples of good candidates:

- `function(training_config=training_config)` -> `function(training_config)`
- `helper(output_directory=output_directory, output_suffix=output_suffix)` -> `helper(output_directory, output_suffix)`

#### 2. Keep Keyword Arguments When They Improve Readability

Keep explicit keywords when:

- the arguments are booleans or flags whose meaning would be unclear positionally;
- the function has several same-type arguments where positional order is easy to confuse;
- the call is long enough that named arguments improve scanning;
- the call mixes optional settings where explicit labels reduce mistakes.

Examples:

- `mkdir(parents=True, exist_ok=True)`
- `Trainer(accelerator=\"cpu\", devices=1, logger=False, ...)`
- `assert some_condition, f\"...\"` is unrelated and should not be reformatted by this rule.

#### 3. Respect Signature Order

When converting to positional form, the call must follow the declared parameter order exactly.

The cleanup should never reorder arguments just to drop keywords.

### Scope

The refactor should target project-authored Python scripts under:

- `scripts/`

The primary focus should be the recently touched training utilities and adjacent scripts where the redundant `name=name` style currently appears most often.

The cleanup should not attempt to reformat:

- third-party code;
- generated files;
- Markdown documents;
- YAML configs.

### Safety Rule

This cleanup is style-oriented, but it still changes executable code.

Therefore each modified call site must be checked for:

- signature order correctness;
- unchanged behavior;
- preserved readability.

The cleanup should be conservative. If a call is on the edge, prefer keeping the explicit keyword form.

### Expected Result

After the cleanup:

- the code should contain fewer repetitive `variable=variable` patterns;
- short helper calls should read more directly;
- calls with meaningful named options should remain explicit;
- the repository style should better match the user's requested balance between compactness and clarity.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/README.md`
  Internal documentation index that should also list this note.
- `doc/reference_summaries/06_Programming_Style_Guide.md`
  Persistent style guide that may need a small update after approval so the new call-site rule remains documented.
- `scripts/`
  Primary source-code scope for the cleanup.
- `doc/technical/2026-03/2026-03-17/2026-03-17-19-16-27_function_call_argument_verbosity_cleanup.md`
  This technical note.

## Implementation Steps

1. Create this technical note and register it in the documentation indexes.
2. Wait for explicit user approval before modifying Python source files.
3. Inspect project-authored Python scripts for redundant keyword call sites such as `x=x`.
4. Replace redundant keyword arguments with positional arguments when the signature order is short, obvious, and safe.
5. Keep explicit keyword arguments for boolean flags, readability-critical options, and ambiguous same-type argument groups.
6. Update the persistent programming style guide with a short rule describing this distinction.
7. Run syntax-level verification on the modified Python files.
8. Report completion and wait for explicit user approval before creating any Git commit.
