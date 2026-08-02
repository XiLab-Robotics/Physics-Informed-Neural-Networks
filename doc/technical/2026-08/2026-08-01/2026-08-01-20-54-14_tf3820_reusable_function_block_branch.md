# TF3820 Reusable Function Block Branch

## Overview

This technical document defines a reusable TwinCAT source-package branch for
`FB_TF3820TransmissionErrorPredictor` in the external
`TwinCAT-TF3820-StandaloneModelTest` submodule.

The current `main` branch is intentionally a complete TwinCAT solution. It
contains the PLC application, Drive Manager project, TwinSAFE project, Scope
configuration, manual test program, CSV replay program, generated project
artifacts, model catalog, and all TF3820 runtime assets. That complete harness
must remain available for development and isolated validation.

The new branch will follow the reuse pattern already established by the
official `CSV_Read-Write` and `FB_Motor` repositories. Those repositories keep
TwinCAT source objects, DUTs, GVLs, utilities, and usage documentation directly
available to a consuming PLC project. `CamLab` mounts them as Git submodules
inside its PLC project and lists their individual objects in the consumer
`.plcproj` file.

The proposed branch name is `standalone-function-block`. It will expose only
the reusable predictor package and its complete dependency closure. It will
not replace the full-solution `main` branch, and the StandardML parent
submodule will continue to track `main` unless a later explicit decision
changes that relationship.

No subagent is planned or authorized. No branch, commit, push, PLC source
change, or submodule-gitlink change may be made until this document is
explicitly approved.

## Technical Approach

### Verified Source Boundary

The reusable public API is:

```text
FB_TF3820TransmissionErrorPredictor
```

Its current source dependency closure contains:

| Component | Count | Role |
| --- | ---: | --- |
| Public predictor FB | 1 | Model selection, lifecycle, history, output normalization |
| Model runner FBs | 39 | TF3820 tensor preparation and asynchronous inference per model family |
| DUT objects | 80 | Model enum, tensor structures, and temporal history |
| Runtime model packages | 39 | ONNX, JSON, and PLCopenXML artifacts per model family |

The predictor exposes a model-agnostic `fTE : REAL` output while preserving
explicit operating inputs for angle, speed, torque, temperature, direction,
sample validity, temporal-history reset, and the analytical anchors required
by H04, H08, and K01.

The current dependency boundary is already encoded by
`scripts/prepare_testrig_predictor_import_pack.py`: all DUTs, all model
runners, and the single public predictor FB. The branch implementation will
reuse that verified boundary rather than selecting files manually.

### Proposed Branch Layout

The `standalone-function-block` branch will use a source-package layout:

```text
README.md
FB_TF3820TransmissionErrorPredictor.TcPOU
DUTs/
Model Runners/
ML_models/
model_catalog.json
scripts/
  validate_model_catalog.py
  validate_standalone_function_block_package.py
```

The predictor is placed at the repository root so that the package resembles
`FB_Motor`. Dependency folders remain explicit and auditable. The model assets
remain in the branch because TF3820 configuration uses the generated JSON
descriptors and the Machine Learning Server loads the paired ONNX models at
runtime. PLCopenXML files remain useful import and provenance companions.

The branch will not contain:

- the TwinCAT solution or system project;
- the complete `PLC_project` wrapper;
- `P_TF3820StandaloneModelTest`;
- `P_TF3820CurveReplay` or `FB_TF3820CsvCurveReader`;
- PLC task configuration;
- Drive Manager content;
- TwinSAFE content;
- Scope projects or recordings;
- trial-license and target-specific configuration files;
- generated `_CompileInfo`, `_Libraries`, TMC, TS project backup, or Python
  bytecode files.

### Branch And Worktree Strategy

The branch will be created from the current synchronized `main` commit
`746708a79452d8808cf00f639afea788078da3e3` in a dedicated temporary Git
worktree. This avoids moving the checkout used by the StandardML parent away
from its recorded `main` gitlink.

The implementation will:

1. fetch and verify `origin/main`;
2. create `standalone-function-block` from the exact verified source commit;
3. construct the package in the dedicated worktree;
4. validate and review the branch without changing the parent gitlink;
5. stop for approval before committing;
6. stop again before any push unless publication is explicitly authorized.

The full-solution `main` branch remains the source of development truth. A
future catalog refresh should be implemented and validated on `main`, then
synchronized into the reusable branch through a deterministic package script
or an explicitly reviewed update commit.

### Consumer Integration Contract

A consuming repository such as `CamLab` will add the branch as a submodule
inside its PLC project, for example:

```powershell
git submodule add -b standalone-function-block `
  https://github.com/XiLab-Robotics/TwinCAT-TF3820-StandaloneModelTest.git `
  "MotorController/CamLabPLC/FB_TF3820TransmissionErrorPredictor"
```

The consumer must then list the package objects in its `.plcproj` in this
order:

1. `DUTs/`;
2. `Model Runners/`;
3. `FB_TF3820TransmissionErrorPredictor.TcPOU`.

The README will provide a complete compile-item block or deterministic helper
output so consumers do not need to discover 120 source files manually.

The required Beckhoff references will be documented explicitly. The source
project currently carries `Tc2_Standard`, `Tc2_System`, `Tc2_Utilities`,
`Tc3_MlServer`, and `Tc3_Module`. The existing import manifest identifies
`Tc3_MlServer`, `Tc2_Standard`, and `Tc2_System` as direct predictor
requirements. Validation must determine and document the exact consumer
reference set rather than silently relying on transitive resolution.

Runtime installation is separate from PLC source import. The README will
explain how to copy each `ML_models/<family>/model.onnx` and `model.json` to
the Machine Learning Server model root expected by the current runner paths,
or how to adapt those paths deliberately in the consuming project.

### Validation Contract

The branch is considered structurally reusable only when all of these checks
pass:

- exactly one public predictor FB is present;
- the model enum, 39 runner FBs, 80 DUTs, 39 catalog entries, and 39 runtime
  model folders remain mutually consistent;
- every catalog entry resolves its runner, enum member, JSON, ONNX, and
  PLCopenXML artifacts;
- ONNX hashes match the catalog;
- no full-solution, Drive, Safety, Scope, replay, test-program, generated
  library, or build artifact enters the branch;
- XML parsing passes for every `.TcPOU` and `.TcDUT` object;
- Python validation scripts compile and pass;
- Markdown QA passes on the branch README;
- a temporary consumer-style PLC project resolves every compile include;
- an isolated TwinCAT build is attempted against the package with the exact
  documented library references.

Static source validation or an isolated build does not prove deployed TF3820
runtime behavior. Model Server configuration, ONNX loading, asynchronous
prediction, latency, reset behavior, invalid-input handling, and live TestRig
execution remain separate commissioning gates.

### Maintenance Contract

The reusable branch must not become an independently edited fork of the
predictor implementation. Its README and validator will record:

- the source `main` commit used to build the package;
- the model count and source-object count;
- the catalog schema and hashes;
- the synchronization command or script;
- the rule that functional changes originate on `main` and are validated there
  before package refresh.

This keeps the branch simple for consumers while avoiding silent divergence
from the complete standalone development harness.

## Involved Components

- `reference/codes/TwinCAT_TF3820_StandaloneModelTest`
  External submodule whose `main` branch remains the complete test solution.
- `FB_TF3820TransmissionErrorPredictor.TcPOU`
  Public model-agnostic predictor function block.
- `PLC_project/DUTs/`
  Current enum, tensor, and temporal-history dependency source.
- `PLC_project/POUs/Model Runners/`
  Current family-specific TF3820 inference adapters.
- `ML_models/`
  Runtime ONNX, JSON, and PLCopenXML packages.
- `model_catalog.json`
  Canonical 39-model coverage and hash registry.
- `scripts/prepare_testrig_predictor_import_pack.py`
  Existing dependency-closure implementation to reuse for branch generation.
- `scripts/validate_model_catalog.py`
  Existing model, runner, tensor, and artifact validator.
- `README.md`
  Source-package integration, library, runtime-installation, and lifecycle
  documentation to rewrite for the reusable branch.
- `doc/README.md`
  Canonical registration point for this technical document.
- `CSV_Read-Write`, `FB_Motor`, and `CamLab`
  Official repository patterns inspected for source-package and consumer
  submodule integration conventions.

## Implementation Steps

1. Register this technical document and wait for explicit approval.
2. Fetch the standalone repository and confirm that local `main`,
   `origin/main`, and the StandardML gitlink still identify the same clean
   source commit.
3. Create a dedicated temporary worktree and the
   `standalone-function-block` branch from that source commit.
4. Extend the existing deterministic import-pack logic so it can materialize
   the branch layout and provenance manifest without manual file selection.
5. Populate the branch with the predictor, all required DUTs and runners, the
   39 runtime model packages, catalog, validators, and a consumer-focused
   README.
6. Remove complete-solution, test, replay, Drive, Safety, Scope, target,
   generated-build, and cache content from the branch.
7. Generate or document the consumer `.plcproj` compile includes and exact
   Beckhoff library references.
8. Run XML, catalog, runner, enum, tensor, artifact, hash, path, Python,
   Markdown, and forbidden-content validation.
9. Build a temporary consumer-style TwinCAT fixture when the local TwinCAT
   automation environment permits it, and distinguish static build evidence
   from runtime commissioning.
10. Review branch diff, file sizes, and source provenance, then stop for user
    approval before creating the branch commit.
11. After explicit commit approval, commit only inside the external submodule
    branch and restore the parent submodule checkout to its recorded `main`
    commit so the StandardML gitlink remains unchanged.
12. Push `standalone-function-block` only after explicit publication approval;
    no consuming repository will be changed automatically.

## Implementation Outcome

The approved implementation was prepared in a separate Git worktree on the
local `standalone-function-block` branch, derived from verified source commit
`746708a79452d8808cf00f639afea788078da3e3`. The complete solution remains
available on `main`, and the StandardML parent repository still records the
same submodule gitlink.

The reusable package contains one public predictor FB, 80 DUTs, 39 model
runner FBs, 39 runtime model folders with 117 runtime artifacts, the model
catalog, a provenance manifest, a generated 120-item consumer compile
fragment, synchronization tooling, validation tooling, and consumer-focused
integration documentation. Complete-solution, Drive, Safety, Scope, replay,
test-program, TwinCAT target, generated-build, license, and cache content were
excluded.

The following checks passed:

- all 120 PLC source objects parse as XML;
- all 39 catalog entries resolve their enum, runner, JSON, ONNX, and
  PLCopenXML dependencies;
- ONNX hashes agree with both the package catalog and the canonical StandardML
  source archives;
- the generated consumer fragment contains exactly 120 valid compile items;
- a temporary consumer-style fixture resolves all 120 package-relative
  compile paths, with no missing source object;
- the branch-to-`main` synchronization check agrees across all 238 managed
  source and runtime files.

Direct MSBuild cannot compile a TwinCAT `.plcproj` in isolation because that
project type does not expose an MSBuild `Build` target. A subsequent TwinCAT
XAE COM automation attempt was rejected during DTE initialization with
`RPC_E_CALL_REJECTED`, before compilation began. Consequently, this work
provides package-integrity and consumer-path evidence, but does not claim a
successful isolated TwinCAT build or runtime qualification. An interactive
XAE build remains an explicit post-publication integration gate.

After explicit publication approval, the reusable package was committed as
`71947f2b81913a7c397401f27dd2a51676ba9840` and pushed to
`origin/standalone-function-block`. The local and remote branch heads were
verified to match. The complete solution remains on `main`, and the StandardML
submodule gitlink remains intentionally unchanged at
`746708a79452d8808cf00f639afea788078da3e3`.
