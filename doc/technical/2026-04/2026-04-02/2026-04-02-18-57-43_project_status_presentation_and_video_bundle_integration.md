# Overview

This scope promotes the externally prepared project-status presentation and
video assets from `.temp/Project_Status/` into a canonical repository-owned
location and integrates them into the guide and reference surface of the
repository.

The incoming bundle currently contains:

* three presentation families:
  * `Transmission_Error_ML_Blueprint`
  * `Taming_the_Wave`
  * `StandardML_Codex_Motion_Blueprint`
* paired overview videos in Italian and English;
* a manually prepared `PINNs Presentation.pptx`.

The originating narrative is based on
`doc/reports/analysis/project_status/[2026-03-27]/` and is intended as a
foundational onboarding package for a new student: what transmission error is,
why it matters, how it is measured, why TE estimation improves machine/robot
accuracy, and how the planned TE model families progress from classical methods
to neural networks and PINNs.

## Technical Approach

The integration should preserve the incoming assets while making their role,
language, provenance, and topic boundaries explicit.

The recommended structure is:

* a canonical guide-local or report-local bundle under `doc/guide/` for the
  onboarding-facing deck and overview assets;
* a reference note that explains what each imported presentation/video is, in
  which language it exists, and how it relates to the `project_status` report
  bundle;
* stable naming that avoids ad hoc temp names and makes Italian versus English
  variants explicit;
* README/index updates so a new user can actually discover the bundle from the
  main documentation entry points.

The `PINNs Presentation.pptx` should be assessed separately from the broader
project-status bundle because it is topic-specific and may belong either inside
the project-status onboarding package as a companion advanced-topic artifact or
inside a future PINN-specific guide/report package.

## Involved Components

* `.temp/Project_Status/`
* `doc/reports/analysis/project_status/[2026-03-27]/`
* `doc/guide/`
* `doc/README.md`
* `README.md` if the main documentation entry flow changes materially
* `doc/guide/project_usage_guide.md` if the promoted bundle becomes part of the
  expected repository usage/discovery flow

## Implementation Steps

1. Inspect the imported bundle and classify each deck/video by language, topic,
   and intended role.
2. Choose a canonical repository location and naming convention for the
   promoted assets.
3. Promote the approved assets out of `.temp/Project_Status/` into the chosen
   tracked location.
4. Create a repository-owned README or companion note for the promoted bundle
   documenting provenance, language variants, and intended usage.
5. Integrate the promoted bundle into the relevant guide/reference entry points
   under `doc/`.
6. Run Markdown warning checks on the touched Markdown files before closing the
   task.
