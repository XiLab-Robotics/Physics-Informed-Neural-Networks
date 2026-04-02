# Transmission Error Foundations Bundle

## Overview

This bundle collects imported onboarding-oriented presentation and video assets
derived from the project-status analysis package in
[project_status/[2026-03-27]](../../reports/analysis/project_status/%5B2026-03-27%5D/).

The intent is different from the implementation-heavy model guides in the rest
of `doc/guide/`: this bundle is designed to help a new student understand the
problem from the foundations upward.

The promoted assets focus on:

* what transmission error is;
* why TE has a periodic or harmonic structure;
* how TE can be measured on the TestRig;
* why measuring and estimating TE matters for robot and machine accuracy;
* how the modeling roadmap progresses from analytical methods to neural
  baselines, structured hybrid models, and finally PINNs.

## Bundle Structure

* [English](./English/)
  English-language slides and overview video.
* [Italiano](./Italiano/)
  Italian-language slides and overview video.
* Root companion asset:
  [Transmission Error Analysis with PINNs.pptx](./Transmission%20Error%20Analysis%20with%20PINNs.pptx)

## Canonical Asset Map

### English

* [Transmission Error Foundations - Introduction to Transmission Error.pptx](./English/Transmission%20Error%20Foundations%20-%20Introduction%20to%20Transmission%20Error.pptx)
* [Transmission Error Foundations - Introduction to Transmission Error.pdf](./English/Transmission%20Error%20Foundations%20-%20Introduction%20to%20Transmission%20Error.pdf)
* [Transmission Error Foundations - Taming The Wave.pptx](./English/Transmission%20Error%20Foundations%20-%20Taming%20The%20Wave.pptx)
* [Transmission Error Foundations - Taming The Wave.pdf](./English/Transmission%20Error%20Foundations%20-%20Taming%20The%20Wave.pdf)
* [Transmission Error Foundations - Overview.mp4](./English/Transmission%20Error%20Foundations%20-%20Overview.mp4)

### Italiano

* [Transmission Error Foundations - Introduzione All'Errore Di Trasmissione.pptx](./Italiano/Transmission%20Error%20Foundations%20-%20Introduzione%20All'Errore%20Di%20Trasmissione.pptx)
* [Transmission Error Foundations - Introduzione All'Errore Di Trasmissione.pdf](./Italiano/Transmission%20Error%20Foundations%20-%20Introduzione%20All'Errore%20Di%20Trasmissione.pdf)
* [Transmission Error Foundations - Overview.mp4](./Italiano/Transmission%20Error%20Foundations%20-%20Overview.mp4)

### Companion Asset

* [Transmission Error Analysis with PINNs.pptx](./Transmission%20Error%20Analysis%20with%20PINNs.pptx)

## Provenance

The imported assets were staged in `.temp/Project_Status/` and then promoted
into this canonical tracked bundle.

The original staged filenames were:

* `Transmission_Error_ML_Blueprint.pptx`
* `Transmission_Error_ML_Blueprint.pdf`
* `Taming_the_Wave.pptx`
* `Taming_the_Wave.pdf`
* `StandardML_Codex_Motion_Blueprint.pptx`
* `StandardML_Codex_Motion_Blueprint.pdf`
* `L_oscillazione_nascosta.mp4`
* `Modeling_Robot_Accuracy.mp4`
* `PINNs Presentation.pptx`

The canonical source report bundle that motivated this onboarding package
remains:

* [Project Status Report.md](../../reports/analysis/project_status/%5B2026-03-27%5D/Project%20Status%20Report.md)
* [Project Status Presentation.md](../../reports/analysis/project_status/%5B2026-03-27%5D/Project%20Status%20Presentation.md)
* [StandardML - Codex Project Status - NotebookLM Presentation.pptx](../../reports/analysis/project_status/%5B2026-03-27%5D/StandardML%20-%20Codex%20Project%20Status%20-%20NotebookLM%20Presentation.pptx)
* [StandardML - Codex Project Status - NotebookLM Video Overview.mp4](../../reports/analysis/project_status/%5B2026-03-27%5D/StandardML%20-%20Codex%20Project%20Status%20-%20NotebookLM%20Video%20Overview.mp4)

## Integration Notes

These assets are treated as repository-tracked onboarding material, not as the
canonical source-of-truth for project facts. The fact boundary still belongs to
the repository-owned Markdown analysis and guide corpus.

The imported PINNs deck is kept at the root of this bundle as a companion
advanced-topic artifact. When a dedicated PINNs guide is created, that deck can
later be replaced or absorbed into a PINNs-specific guide bundle.
