"""Close out the Wave 2C residual harmonic temporal hybrid campaign."""

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

CAMPAIGN_NAME = "wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27"
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-05-27-18-55-47_wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27"
)
CAMPAIGN_RESULTS_REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "campaign_results"
    / "wave2"
    / "2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md"
)
PLANNING_REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "campaign_plans"
    / "wave2"
    / "2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = (
    PROJECT_PATH
    / "doc"
    / "technical"
    / "2026-05"
    / "2026-05-27"
    / "2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrids.md"
)
REMOTE_LAUNCHER_TECHNICAL_DOCUMENT_PATH = (
    PROJECT_PATH
    / "doc"
    / "technical"
    / "2026-05"
    / "2026-05-27"
    / "2026-05-27-18-35-06_campaign_launcher_remote_execution_standard.md"
)
CLOSEOUT_TECHNICAL_DOCUMENT_PATH = (
    PROJECT_PATH
    / "doc"
    / "technical"
    / "2026-05"
    / "2026-05-28"
    / "2026-05-28-11-35-34_wave2c_campaign_closeout.md"
)
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
DOC_INDEX_PATH = PROJECT_PATH / "doc" / "README.md"

EXPECTED_RUN_COUNT = 18
FAMILY_KEY_LIST = [
    "residual_harmonic_gru_sequence_sparse_rcim",
    "residual_harmonic_gru_sequence_fw_sparse_rcim",
    "residual_harmonic_gru_sequence_bw_sparse_rcim",
    "residual_harmonic_gru_sequence_dense240",
    "residual_harmonic_gru_sequence_fw_dense240",
    "residual_harmonic_gru_sequence_bw_dense240",
    "residual_harmonic_gru_sequence_dense360",
    "residual_harmonic_gru_sequence_fw_dense360",
    "residual_harmonic_gru_sequence_bw_dense360",
    "residual_harmonic_lstm_sequence_sparse_rcim",
    "residual_harmonic_lstm_sequence_fw_sparse_rcim",
    "residual_harmonic_lstm_sequence_bw_sparse_rcim",
    "residual_harmonic_lstm_sequence_dense240",
    "residual_harmonic_lstm_sequence_fw_dense240",
    "residual_harmonic_lstm_sequence_bw_dense240",
    "residual_harmonic_lstm_sequence_dense360",
    "residual_harmonic_lstm_sequence_fw_dense360",
    "residual_harmonic_lstm_sequence_bw_dense360",
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
    """Load the latest family-best entry for one Wave 2C family surface."""

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


def validate_campaign_artifacts() -> None:
    """Validate required campaign closeout artifacts."""

    assert CAMPAIGN_OUTPUT_DIRECTORY.exists(), f"Missing campaign output directory | {CAMPAIGN_OUTPUT_DIRECTORY}"
    required_file_list = [
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_manifest.yaml",
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml",
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml",
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.md",
        CAMPAIGN_OUTPUT_DIRECTORY / "campaign_execution_report.md",
    ]
    for required_file_path in required_file_list:
        assert required_file_path.exists(), f"Missing closeout artifact | {required_file_path}"

    manifest = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_manifest.yaml")
    run_list = manifest["run_list"]
    assert len(run_list) == EXPECTED_RUN_COUNT, f"Expected {EXPECTED_RUN_COUNT} runs, found {len(run_list)}"
    failed_run_list = [
        run
        for run in run_list
        if str(run.get("queue_status")) != "completed" or int(run.get("process_return_code", -1)) != 0
    ]
    assert not failed_run_list, f"Expected all runs to complete successfully | failed={failed_run_list}"


def build_closeout_report() -> str:
    """Build the final campaign-results report text."""

    validate_campaign_artifacts()
    leaderboard = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml")
    best_run = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml")["best_entry"]
    program_best = load_yaml_dictionary(PROJECT_PATH / "output" / "registries" / "program" / "current_best_solution.yaml")["best_entry"]
    manifest = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_manifest.yaml")
    run_list = manifest["run_list"]
    completed_run_list = [run for run in run_list if str(run["queue_status"]) == "completed"]
    failed_run_list = [run for run in run_list if str(run["queue_status"]) != "completed"]
    started_at = str(completed_run_list[0]["start_time"])
    finished_at = str(completed_run_list[-1]["end_time"])

    leaderboard_entry_list = list(leaderboard["entry_list"])
    leaderboard_table = build_leaderboard_table(leaderboard_entry_list)
    registry_effects_table = build_registry_effects_table(leaderboard_entry_list)
    program_best_changed = str(program_best["run_instance_id"]) == str(best_run["run_instance_id"])
    program_best_text = (
        "Wave 2C became the program-level scalar best."
        if program_best_changed
        else (
            f"The program-level scalar best remains `{program_best['run_name']}` "
            f"with test MAE {format_metric(program_best['test_mae'])}."
        )
    )

    return f"""# Wave 2C Residual Harmonic Temporal Hybrid Campaign Results

## Overview

This report closes the approved `Wave 2C` residual harmonic temporal hybrid
campaign. The campaign tested residual harmonic `GRU` and residual harmonic
`LSTM` sequence regressors across `global`, `Fw`, and `Bw` direction surfaces,
with three harmonic-basis tiers per surface: sparse `RCIM`, dense `0..240`,
and dense `0..360`.

The campaign completed all 18 planned runs with zero launcher failures. The
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
| Remote launcher standard | `{format_relative_path(REMOTE_LAUNCHER_TECHNICAL_DOCUMENT_PATH)}` |
| Closeout technical document | `{format_relative_path(CLOSEOUT_TECHNICAL_DOCUMENT_PATH)}` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `{CAMPAIGN_NAME}` |
| Started at | `{started_at}` |
| Finished at | `{finished_at}` |
| Completed runs | {len(completed_run_list)} |
| Failed runs | {len(failed_run_list)} |
| Tested model types | `residual_harmonic_gru_sequence`, `residual_harmonic_lstm_sequence` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Harmonic basis tiers | `sparse_rcim`, `dense_240`, `dense_360` |
| Sparse harmonic list | `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]` |

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

The strongest Wave 2C scalar training result is the forward-only sparse `RCIM`
residual harmonic `GRU`, with test MAE {format_metric(best_run['test_mae'])}.
The dense harmonic branches did not improve the campaign winner: the second
ranked model is the forward-only dense `0..240` residual harmonic `GRU`, and
the third ranked model is the forward-only sparse `RCIM` residual harmonic
`LSTM`.

This result is execution-valid and useful as a model-family probe, but it does
not exceed the current Wave 2B scalar training winner. {program_best_text}
That means Wave 2C should be retained as a completed comparison branch, while
Wave 2B remains the stronger scalar training baseline until a future campaign
or official `Track 2` review changes that conclusion.

The campaign also shows that adding a recurrent residual branch over an
explicit harmonic base is not automatically superior to feeding the harmonic
prior directly into the recurrent temporal model. That is a useful negative
result: the residual decomposition remains inspectable, but the sparse
periodic recurrent Wave 2B formulation is still the better scalar candidate.

## Registry Effects

{registry_effects_table}

The family registries for the new Wave 2C model surfaces were created or
refreshed by this campaign. The program-level training registry did not move
to Wave 2C because the Wave 2B periodic `GRU` backward-only model still has the
lower scalar test MAE.

## Track 2 Boundary

`Track 2` was not run as part of this closeout. Under the campaign governance
rule, optional `Track 2` verification remains a separate operator-approved
workflow with a repository-owned launcher that can run locally or with
`-Remote`.

Because Wave 2C does not beat the existing Wave 2B scalar best, a full `Track
2` refresh is not mandatory for accepting this closeout. If reviewed later,
the forward-only sparse `RCIM` residual harmonic `GRU` is the only Wave 2C
candidate that should be promoted into the optional verification queue first.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all 18
runs completed, the leaderboard and best-run artifacts exist, and the family
registries were refreshed.

From a modeling standpoint, Wave 2C is a completed comparison branch rather
than a new best branch. The residual harmonic temporal structure remains
available for future analysis, but the current project best should stay on the
Wave 2B periodic recurrent family until official verification says otherwise.

## Recommended Follow-Up

1. Keep the Wave 2C artifacts as a completed negative/neutral comparison
   branch.
2. Do not replace the current Wave 2B scalar best with the Wave 2C winner.
3. Run optional `Track 2` only if visual curve behavior is worth inspecting
   despite the weaker scalar campaign result.
"""


def update_doc_index() -> None:
    """Register the campaign-results report in the documentation index."""

    doc_index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    result_entry = (
        "- [reports/campaign_results/wave_2/2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md]"
        "(./reports/campaign_results/wave_2/2026-05-28-11-35-34_wave2c_residual_harmonic_temporal_hybrid_campaign_results_report.md)\n"
        "  Final results report for the completed `Wave 2C` residual harmonic\n"
        "  temporal hybrid campaign, including the 18-run sparse/dense\n"
        "  harmonic-basis leaderboard, registry effects, and the explicit\n"
        "  boundary that `Track 2` remains a separate optional workflow.\n"
    )

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
            "closeout_technical_document_path": format_relative_path(CLOSEOUT_TECHNICAL_DOCUMENT_PATH),
            "campaign_output_directory": format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY),
            "results_report_path": format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH),
            "best_run_name": str(best_run["run_name"]),
            "best_run_instance_id": str(best_run["run_instance_id"]),
            "best_model_family": str(best_run["model_family"]),
            "best_test_mae": float(best_run["test_mae"]),
            "best_test_rmse": float(best_run["test_rmse"]),
            "track2_status": "not_run_optional_operator_launch_required",
        },
        "protected_file_list": [],
        "queue_config_path_list": [],
        "launch_command_list": [],
    }
    write_yaml_dictionary(ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)


def closeout_campaign() -> None:
    """Run the closeout workflow."""

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
