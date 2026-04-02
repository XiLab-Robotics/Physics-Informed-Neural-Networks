# Training Workflow Report Requirements Rule

## Overview

The user requested a new permanent workflow rule for every future training activity in this repository.

The requested rule has two mandatory reporting stages:

1. **Before any training execution**
   create not only the technical document already required by the repository, but also a preliminary planning report similar in structure and depth to:
   - `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`

   This preliminary report must describe:
   - all relevant training parameters;
   - what each parameter means and does;
   - the planned configuration choices;
   - a comparison table of the candidate configurations that are worth testing.

2. **After the training execution**
   create a detailed results report that includes:
   - the final metrics;
   - comparison tables across runs;
   - written interpretation of what happened;
   - which configuration performed best and why;
   - proposed future improvements or follow-up experiments.

This change is a workflow/documentation rule update. It is not a model implementation change by itself.

## Technical Approach

The repository already requires:

- a technical document before each approved repository change;
- user approval before execution;
- a final commit after modifications.

The new rule should extend that existing workflow specifically for training requests.

The intended future sequence for any training campaign should become:

1. create the technical document in the appropriate day folder under `doc/technical/YYYY-MM-DD/`;
2. create a **preliminary training report** in `doc/reports/campaign_plans/` describing the parameters, planned comparisons, and rationale;
3. wait for the user's explicit approval;
4. execute the approved training runs;
5. create a **post-training results report** in `doc/reports/campaign_results/` summarizing metrics, interpretation, best configuration, and future suggestions;
6. update any relevant user-facing guide if the runnable workflow or recommended default configuration changes;
7. create the required Git commit.

This new rule should be reflected in the repository documentation where workflow rules are already expressed, most likely:

- `AGENTS.md`
- `README.md`
- possibly `doc/guide/project_usage_guide.md` if the new rule is considered part of the practical training workflow expectations.

The rule should be written clearly enough that future training work cannot skip either reporting stage.

## Involved Components

- `AGENTS.md`
  Main repository instruction file where the rule should likely be made explicit after approval.
- `README.md`
  Main project document that must reference this technical document and may need to reflect the strengthened workflow rule.
- `doc/README.md`
  Internal documentation index that must include this technical document.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`
  Reference example for the required preliminary planning-report style.
- `doc/technical/2026-03/2026-03-12/2026-03-12-15-33-38_training_workflow_report_requirements_rule.md`
  This technical planning document.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, update the permanent repository workflow instructions so that every future training request requires:
   - the technical document;
   - the preliminary planning report;
   - the final post-training results report.
3. Keep the wording specific to training work so general non-training repository changes do not inherit unnecessary extra steps.
4. Update any additional documentation indexes or workflow guides that should reflect the new rule.
5. Create the required Git commit immediately after the approved documentation update is completed.
