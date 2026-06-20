"""Close out the Wave 2.2 harmonic temporal hybrid campaign."""

from __future__ import annotations

# Import Python Utilities
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
import yaml

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[4]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path:
    sys.path.insert(0, str(PROJECT_PATH))

CAMPAIGN_NAME = "wave2b_harmonic_temporal_hybrid_campaign_2026_05_25"
CAMPAIGN_OUTPUT_DIRECTORY = PROJECT_PATH / "output" / "training_campaigns" / "2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25"
CAMPAIGN_RESULTS_REPORT_PATH = PROJECT_PATH / "doc" / "reports" / "campaign_results" / "wave2" / "2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report.md"
PLANNING_REPORT_PATH = PROJECT_PATH / "doc" / "reports" / "campaign_plans" / "wave2" / "2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md"
TECHNICAL_DOCUMENT_PATH = PROJECT_PATH / "doc" / "technical" / "2026-05" / "2026-05-25" / "2026-05-25-03-17-26_wave2b_harmonic_temporal_hybrids.md"
WORKFLOW_TECHNICAL_DOCUMENT_PATH = PROJECT_PATH / "doc" / "technical" / "2026-05" / "2026-05-26" / "2026-05-26-14-01-40_campaign_closeout_and_manual_track2_gate.md"
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
DOC_INDEX_PATH = PROJECT_PATH / "doc" / "README.md"

FAMILY_KEY_LIST = [
    "periodic_temporal_convolution",
    "periodic_temporal_convolution_fw",
    "periodic_temporal_convolution_bw",
    "periodic_gru_sequence",
    "periodic_gru_sequence_fw",
    "periodic_gru_sequence_bw",
    "periodic_lstm_sequence",
    "periodic_lstm_sequence_fw",
    "periodic_lstm_sequence_bw",
]


def load_yaml_dictionary(input_path: Path) -> dict[str, Any]:
    """Load one YAML dictionary."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML dictionary | {input_path}"
    return payload


def write_yaml_dictionary(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one YAML dictionary."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(payload, output_file, sort_keys=False, allow_unicode=True)


def write_text_file(output_path: Path, text: str) -> None:
    """Write one UTF-8 text file with a single final newline."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    output_path.write_text(text, encoding="utf-8", newline="\n")


def format_relative_path(path_value: Path | str) -> str:
    """Format a repository-relative path when possible."""

    path_candidate = Path(path_value)
    if not path_candidate.is_absolute():
        return str(path_candidate).replace("\\", "/")
    try:
        return str(path_candidate.relative_to(PROJECT_PATH)).replace("\\", "/")
    except ValueError:
        return str(path_candidate).replace("\\", "/")


def format_metric(value: Any) -> str:
    """Format one metric value for compact report tables."""

    return f"{float(value):.6f}"


def resolve_scope_label(entry: dict[str, Any]) -> str:
    """Resolve the report-facing scope label."""

    variant = str(entry.get("training_variant", "")).strip()
    if variant.lower() == "global":
        return "global"
    return variant


def build_leaderboard_table(entry_list: list[dict[str, Any]]) -> str:
    """Build the campaign leaderboard Markdown table."""

    line_list = [
        "| Rank | Run | Family | Scope | Test MAE | Test RMSE | Val MAE | Params |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for index, entry in enumerate(entry_list, start=1):
        line_list.append(
            "| "
            f"{index} | "
            f"`{entry['run_name']}` | "
            f"`{entry['model_family']}` | "
            f"{resolve_scope_label(entry)} | "
            f"{format_metric(entry['test_mae'])} | "
            f"{format_metric(entry['test_rmse'])} | "
            f"{format_metric(entry['val_mae'])} | "
            f"{int(entry['trainable_parameter_count']):,} |"
        )
    return "\n".join(line_list)


def load_latest_family_best_entry(family_key: str) -> dict[str, Any]:
    """Load the latest family-best entry for one Wave 2.2 family surface."""

    latest_family_best_path = PROJECT_PATH / "output" / "registries" / "families" / family_key / "latest_family_best.yaml"
    latest_family_best = load_yaml_dictionary(latest_family_best_path)
    best_entry = latest_family_best["best_entry"]
    assert isinstance(best_entry, dict), f"Expected best entry dictionary | {latest_family_best_path}"
    return best_entry


def build_registry_effects_table(campaign_entry_list: list[dict[str, Any]]) -> str:
    """Build the registry-effects Markdown table."""

    campaign_run_instance_set = {str(entry["run_instance_id"]) for entry in campaign_entry_list}
    line_list = [
        "| Registry Scope | Current Family Best | Test MAE | Interpretation |",
        "| --- | --- | --- | --- |",
    ]
    for family_key in FAMILY_KEY_LIST:
        best_entry = load_latest_family_best_entry(family_key)
        best_run_instance_id = str(best_entry["run_instance_id"])
        interpretation = "Updated by this campaign" if best_run_instance_id in campaign_run_instance_set else "Previous family best remains ahead"
        line_list.append(
            "| "
            f"`{family_key}` | "
            f"`{best_entry['run_name']}` | "
            f"{format_metric(best_entry['test_mae'])} | "
            f"{interpretation} |"
        )
    return "\n".join(line_list)


def build_closeout_report() -> str:
    """Build the final campaign-results report text."""

    leaderboard = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml")
    best_run = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml")["best_entry"]
    manifest = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_manifest.yaml")
    run_list = manifest["run_list"]
    completed_run_list = [run for run in run_list if str(run["queue_status"]) == "completed"]
    failed_run_list = [run for run in run_list if str(run["queue_status"]) != "completed"]
    started_at = str(completed_run_list[0]["start_time"])
    finished_at = str(completed_run_list[-1]["end_time"])

    leaderboard_entry_list = list(leaderboard["entry_list"])
    leaderboard_table = build_leaderboard_table(leaderboard_entry_list)
    registry_effects_table = build_registry_effects_table(leaderboard_entry_list)

    return f"""# Wave 2.2 Harmonic Temporal Hybrid Campaign Results

## Overview

This report closes the approved `Wave 2.2` harmonic-temporal hybrid campaign.
The campaign tested explicit sparse `RCIM` harmonic features inside temporal
convolution, `GRU`, and `LSTM` sequence regressors across the `global`, `Fw`,
and `Bw` surfaces.

The campaign completed all 9 planned runs with zero launcher failures. The
campaign winner by the configured selection policy, minimum `test_mae` with
`test_rmse`, `val_mae`, and trainable parameter count as tie breakers, is
`{best_run['run_name']}`.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY)}` |
| Campaign leaderboard | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_leaderboard.yaml')}` |
| Best-run pointer | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_best_run.yaml')}` |
| Execution report | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_execution_report.md')}` |
| Planning report | `{format_relative_path(PLANNING_REPORT_PATH)}` |
| Model technical document | `{format_relative_path(TECHNICAL_DOCUMENT_PATH)}` |
| Closeout workflow document | `{format_relative_path(WORKFLOW_TECHNICAL_DOCUMENT_PATH)}` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `{CAMPAIGN_NAME}` |
| Started at | `{started_at}` |
| Finished at | `{finished_at}` |
| Completed runs | {len(completed_run_list)} |
| Failed runs | {len(failed_run_list)} |
| Tested model types | `periodic_temporal_convolution`, `periodic_gru_sequence`, `periodic_lstm_sequence` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Harmonic feature list | `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]` |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `{best_run['run_name']}` |
| Run instance | `{best_run['run_instance_id']}` |
| Model family | `{best_run['model_family']}` |
| Model type | `{best_run['model_type']}` |
| Direction scope | {str(best_run['direction_scope_label']).replace('_', ' ')} |
| Trainable parameters | {int(best_run['trainable_parameter_count']):,} |
| Validation MAE | {format_metric(best_run['val_mae'])} |
| Validation RMSE | {format_metric(best_run['val_rmse'])} |
| Test MAE | {format_metric(best_run['test_mae'])} |
| Test RMSE | {format_metric(best_run['test_rmse'])} |

The winning checkpoint is stored at
`{format_relative_path(best_run['best_checkpoint_path'])}`.

## Leaderboard

{leaderboard_table}

## Technical Interpretation

The strongest Wave 2.2 result is the backward-only `periodic_gru_sequence`
surface, with test MAE {format_metric(best_run['test_mae'])}. The two recurrent
hybrid families dominate the periodic temporal-convolution family in this
campaign, and the global `periodic_gru_sequence` and `periodic_lstm_sequence`
results are almost tied on scalar test error.

The campaign is a clear improvement over the first Wave 2.1 temporal-sequence
entry campaign on the same scalar training-registry metric surface. The best
first-wave temporal entry campaign result was `te_gru_sequence_remote_Fw` at
test MAE `0.003333`, while Wave 2.2 reaches `0.002344` on the backward-only
periodic `GRU` surface and `0.002681` on the global periodic `GRU` surface.

This closeout does not promote the Wave 2.2 winner as the official deployed or
accepted `TE Curve Verification Pipeline` baseline. Campaign metrics are training-registry metrics;
the direction-aware offline curve matrix and visual overlays remain a separate
approval step. The interrupted `TE Curve Verification Pipeline` attempt produced no valid result
artifact and was removed from the verification surface.

## Registry Effects

{registry_effects_table}

The program-level training registry now points to
`{best_run['run_name']}` as the scalar best training result. That registry
state is not the same thing as official `TE Curve Verification Pipeline` acceptance.

## TE Curve Verification Pipeline Boundary

`TE Curve Verification Pipeline` was not completed as part of this closeout. Under the updated
campaign governance rule, a future `TE Curve Verification Pipeline` refresh must be prepared as a
separate operator-launched PowerShell workflow with local and `-Remote`
execution modes. Codex should provide the launcher and exact command, then
wait for the operator to run it and report completion.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all 9
runs completed, the leaderboard and best-run artifacts exist, and the family
registries were refreshed.

From a modeling standpoint, the periodic recurrent sequence families are worth
keeping as verified training candidates. The backward-only periodic `GRU` is
the scalar campaign winner, while the global periodic `GRU` and periodic
`LSTM` are the strongest bidirectional candidates to carry into a future
optional `TE Curve Verification Pipeline` review.

## Recommended Follow-Up

1. Review and commit the normal closeout package if the report and PDF are
   accepted.
2. Prepare the separate operator-run `TE Curve Verification Pipeline` launcher only after explicit
   approval.
3. Use the future `TE Curve Verification Pipeline` matrix and visual reports
   to decide whether Wave 2.2 changes any official baseline, rather than using this campaign
   leaderboard alone.
"""


def update_doc_index() -> None:
    """Register the campaign-results report in the documentation index."""

    doc_index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    result_entry = (
        "- [reports/campaign_results/wave_2/2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report.md]"
        "(./reports/campaign_results/wave_2/2026-05-26-14-01-40_wave2b_harmonic_temporal_hybrid_campaign_results_report.md)\n"
        "  Final results report for the completed `Wave 2.2` harmonic-temporal\n"
        "  hybrid campaign, including the 9-run leaderboard, registry effects,\n"
        "  and the explicit boundary that `TE Curve Verification Pipeline` remains a separate\n"
        "  operator-launched workflow.\n"
    )

    latest_anchor = "#### Latest Campaign Results\n\n"
    if result_entry not in doc_index_text and latest_anchor in doc_index_text:
        doc_index_text = doc_index_text.replace(latest_anchor, latest_anchor + result_entry, 1)

    results_anchor = "#### Campaign Results\n\n"
    if result_entry not in doc_index_text and results_anchor in doc_index_text:
        doc_index_text = doc_index_text.replace(results_anchor, results_anchor + result_entry, 1)

    write_text_file(DOC_INDEX_PATH, doc_index_text)


def update_active_campaign_state() -> None:
    """Clear the active campaign state after closeout."""

    manifest = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_manifest.yaml")
    best_run = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml")["best_entry"]
    run_list = manifest["run_list"]
    completed_run_list = [run for run in run_list if str(run["queue_status"]) == "completed"]
    failed_run_list = [run for run in run_list if str(run["queue_status"]) != "completed"]
    now_text = datetime.now().astimezone().isoformat(timespec="seconds")

    active_campaign_state = {
        "status": "none",
        "campaign_name": None,
        "cleared_at": now_text,
        "clear_reason": "completed_campaign_removed_from_running_state_after_closeout_report",
        "last_completed_campaign": {
            "campaign_name": CAMPAIGN_NAME,
            "status": "completed",
            "started_at": str(completed_run_list[0]["start_time"]),
            "finished_at": str(completed_run_list[-1]["end_time"]),
            "completion_recorded_at": str(manifest["generated_at"]),
            "completed_run_count": len(completed_run_list),
            "failed_run_count": len(failed_run_list),
            "planning_report_path": format_relative_path(PLANNING_REPORT_PATH),
            "technical_document_path": format_relative_path(TECHNICAL_DOCUMENT_PATH),
            "closeout_workflow_document_path": format_relative_path(WORKFLOW_TECHNICAL_DOCUMENT_PATH),
            "campaign_output_directory": format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY),
            "results_report_path": format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH),
            "best_run_name": str(best_run["run_name"]),
            "best_run_instance_id": str(best_run["run_instance_id"]),
            "best_model_family": str(best_run["model_family"]),
            "best_test_mae": float(best_run["test_mae"]),
            "best_test_rmse": float(best_run["test_rmse"]),
            "track2_status": "not_run_operator_launch_required",
        },
        "protected_file_list": [],
        "queue_config_path_list": [],
        "launch_command_list": [],
    }
    write_yaml_dictionary(ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)


def closeout_campaign() -> None:
    """Run the closeout workflow."""

    assert CAMPAIGN_OUTPUT_DIRECTORY.exists(), f"Missing campaign output directory | {CAMPAIGN_OUTPUT_DIRECTORY}"
    write_text_file(CAMPAIGN_RESULTS_REPORT_PATH, build_closeout_report())
    update_doc_index()
    update_active_campaign_state()
    print(f"[DONE] Wrote campaign results report | {format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH)}")
    print(f"[DONE] Cleared active campaign state | {format_relative_path(ACTIVE_CAMPAIGN_STATE_PATH)}")


def main() -> int:
    """Run the campaign closeout script."""

    closeout_campaign()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
