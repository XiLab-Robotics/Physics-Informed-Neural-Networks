"""Close out the Wave 3.1 offset-aware probe campaign."""

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

CAMPAIGN_NAME = "track2f_offset_aware_probe_campaign_2026_06_03"
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_PATH
    / "output"
    / "training_campaigns"
    / "2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03"
)
CAMPAIGN_RESULTS_REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "campaign_results"
    / "track2"
    / "2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report.md"
)
PLANNING_REPORT_PATH = (
    PROJECT_PATH
    / "doc"
    / "reports"
    / "campaign_plans"
    / "track2"
    / "2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md"
)
TECHNICAL_DOCUMENT_PATH = (
    PROJECT_PATH
    / "doc"
    / "technical"
    / "2026-06"
    / "2026-06-03"
    / "2026-06-03-17-25-37_track2f_offset_aware_probe_campaign.md"
)
MODEL_TECHNICAL_DOCUMENT_PATH = (
    PROJECT_PATH
    / "doc"
    / "technical"
    / "2026-06"
    / "2026-06-03"
    / "2026-06-03-18-18-20_track2f_sequential_residual_offset_probe.md"
)
CLOSEOUT_TECHNICAL_DOCUMENT_PATH = (
    PROJECT_PATH
    / "doc"
    / "technical"
    / "2026-06"
    / "2026-06-04"
    / "2026-06-04-12-28-46_track2f_campaign_closeout.md"
)
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
DOC_INDEX_PATH = PROJECT_PATH / "doc" / "README.md"

EXPECTED_RUN_COUNT = 3
BRANCH_ORDER = ("global", "Fw", "Bw")
BRANCH_LABEL_BY_VARIANT = {
    "global": "bidirectional",
    "Fw": "forward only",
    "Bw": "backward only",
}


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
    """Format a path relative to the repository root."""

    path = Path(path_value)
    if not path.is_absolute():
        return path.as_posix()
    return path.relative_to(PROJECT_PATH).as_posix()


def format_metric(value: Any) -> str:
    """Format one scalar metric for report tables."""

    return f"{float(value):.6f}"


def format_integer(value: Any) -> str:
    """Format one integer with thousands separators."""

    return f"{int(value):,}"


def format_duration(seconds_value: Any) -> str:
    """Format a duration from seconds."""

    seconds = int(round(float(seconds_value)))
    minutes, second_remainder = divmod(seconds, 60)
    return f"{minutes}m {second_remainder:02d}s"


def load_campaign_payloads() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Load and validate the campaign payloads."""

    manifest = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_manifest.yaml")
    leaderboard = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml")
    best_run = load_yaml_dictionary(CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml")

    run_list = list(manifest["run_list"])
    assert len(run_list) == EXPECTED_RUN_COUNT, f"Expected {EXPECTED_RUN_COUNT} runs | found={len(run_list)}"
    failed_run_list = [
        run
        for run in run_list
        if str(run.get("queue_status")) != "completed" or int(run.get("process_return_code", -1)) != 0
    ]
    assert not failed_run_list, f"Expected all runs to complete successfully | failed={failed_run_list}"
    assert int(leaderboard["entry_count"]) == EXPECTED_RUN_COUNT, "Leaderboard entry count mismatch."
    return manifest, leaderboard, best_run


def build_branch_best_entry_list(leaderboard_entry_list: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Build the branch-best list in global, forward, backward order."""

    branch_best_entry_list: list[dict[str, Any]] = []
    for branch_name in BRANCH_ORDER:
        matching_entry_list = [
            entry
            for entry in leaderboard_entry_list
            if str(entry.get("training_variant")) == branch_name
        ]
        assert len(matching_entry_list) == 1, f"Expected one entry for branch {branch_name}"
        branch_best_entry_list.append(matching_entry_list[0])
    return branch_best_entry_list


def build_branch_results_table(branch_best_entry_list: list[dict[str, Any]]) -> str:
    """Build the directional branch results table."""

    row_list = [
        "| Surface | Role | Run | Family | Test MAE | Test RMSE | Val MAE | Params |",
        "| --- | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for entry in branch_best_entry_list:
        variant = str(entry["training_variant"])
        row_list.append(
            "| "
            f"{variant} | "
            f"{BRANCH_LABEL_BY_VARIANT[variant]} | "
            f"`{entry['run_name']}` | "
            f"`{entry['model_family']}` | "
            f"{format_metric(entry['test_mae'])} | "
            f"{format_metric(entry['test_rmse'])} | "
            f"{format_metric(entry['val_mae'])} | "
            f"{format_integer(entry['trainable_parameter_count'])} |"
        )
    return "\n".join(row_list)


def build_scalar_leaderboard_table(leaderboard_entry_list: list[dict[str, Any]]) -> str:
    """Build the scalar leaderboard table."""

    row_list = [
        "| Rank | Surface | Run | Family | Test MAE | Test RMSE | Val MAE | Params |",
        "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for rank_index, entry in enumerate(leaderboard_entry_list, start=1):
        row_list.append(
            "| "
            f"{rank_index} | "
            f"{entry['training_variant']} | "
            f"`{entry['run_name']}` | "
            f"`{entry['model_family']}` | "
            f"{format_metric(entry['test_mae'])} | "
            f"{format_metric(entry['test_rmse'])} | "
            f"{format_metric(entry['val_mae'])} | "
            f"{format_integer(entry['trainable_parameter_count'])} |"
        )
    return "\n".join(row_list)


def build_execution_table(manifest: dict[str, Any]) -> str:
    """Build the run execution table."""

    row_list = [
        "| Surface | Run | Status | Duration | Return Code |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    for run in manifest["run_list"]:
        source_config_name = Path(str(run["source_config_path"])).stem
        if "global" in source_config_name:
            surface = "global"
        elif "fw" in source_config_name:
            surface = "Fw"
        else:
            surface = "Bw"
        row_list.append(
            "| "
            f"{surface} | "
            f"`{run['run_name']}` | "
            f"`{run['queue_status']}` | "
            f"{format_duration(run['duration_seconds'])} | "
            f"{int(run['process_return_code'])} |"
        )
    return "\n".join(row_list)


def build_artifact_table() -> str:
    """Build the campaign artifact table."""

    row_list = [
        "| Artifact | Path |",
        "| --- | --- |",
        f"| Campaign output | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY)}` |",
        f"| Campaign leaderboard | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_leaderboard.yaml')}` |",
        f"| Branch scalar pointer | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_best_run.yaml')}` |",
        f"| Execution report | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_execution_report.md')}` |",
        f"| Planning report | `{format_relative_path(PLANNING_REPORT_PATH)}` |",
        f"| Campaign technical document | `{format_relative_path(TECHNICAL_DOCUMENT_PATH)}` |",
        f"| Model technical document | `{format_relative_path(MODEL_TECHNICAL_DOCUMENT_PATH)}` |",
        f"| Closeout technical document | `{format_relative_path(CLOSEOUT_TECHNICAL_DOCUMENT_PATH)}` |",
    ]
    return "\n".join(row_list)


def build_closeout_report() -> str:
    """Build the Wave 3.1 closeout report markdown."""

    manifest, leaderboard, best_run_payload = load_campaign_payloads()
    leaderboard_entry_list = list(leaderboard["entry_list"])
    branch_best_entry_list = build_branch_best_entry_list(leaderboard_entry_list)
    completed_run_list = [run for run in manifest["run_list"] if str(run["queue_status"]) == "completed"]
    failed_run_list = [run for run in manifest["run_list"] if str(run["queue_status"]) != "completed"]
    best_entry = best_run_payload["best_entry"]

    return f"""# Wave 3.1 Offset-Aware Probe Campaign Results

## Overview

This report closes the approved `Wave 3.1` offset-aware probe campaign. The
executed package trained the first learned `sequential_residual_offset_probe`
candidate across the three required direction surfaces: `global`, `Fw`, and
`Bw`.

The campaign completed all {len(completed_run_list)} planned runs with zero
training failures. A terminal-level `conda run` message appeared after the
runner printed the completed-campaign summary, but the generated campaign
artifacts show `0` failed runs, per-run process return code `0`, and no
traceback in the run logs.

The scalar leaderboard ranks `Fw` first by `test_mae`, but that ranking is only
a diagnostic ordering. `Wave 3.1` keeps three parallel best branches for future
verification and deployment analysis: one `global`, one `Fw`, and one `Bw`
candidate.

## Campaign Artifacts

{build_artifact_table()}

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `{CAMPAIGN_NAME}` |
| Started at | `{completed_run_list[0]["start_time"]}` |
| Finished at | `{completed_run_list[-1]["end_time"]}` |
| Completed runs | {len(completed_run_list)} |
| Failed runs | {len(failed_run_list)} |
| Tested model type | `sequential_residual_offset_probe` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `{best_entry["run_name"]}` |

## Directional Branch Results

{build_branch_results_table(branch_best_entry_list)}

These three rows are the closeout result. The `Fw` row is the scalar first
entry in this small campaign, but it does not replace the required `global` or
`Bw` branch candidates.

## Execution Details

{build_execution_table(manifest)}

## Scalar Leaderboard

{build_scalar_leaderboard_table(leaderboard_entry_list)}

## Technical Interpretation

The sequential residual-offset probe is execution-valid and provides the first
learned branch that directly targets the mean-offset failure mode found by the
`TE Curve Verification Pipeline` mean-centered diagnostic, `CVP 1.4`, and `CVP 1.5`.

The scalar test metrics do not beat the current program-level scalar training
winner, `te_periodic_gru_sequence_remote_Bw`, which remains at test `MAE`
`0.002344`. This is expected for a narrow offset-aware probe: the campaign was
designed to test whether the offset branch is feasible, not to promote a new
global scalar winner from pointwise training alone.

The important closeout result is therefore structural. The repository now has
three trained sequential residual-offset candidates that can be evaluated in
the official curve-first `TE Curve Verification Pipeline` surface:

- `global`: bidirectional/general candidate.
- `Fw`: forward-only candidate.
- `Bw`: backward-only candidate.

## Registry Effects

| Registry Scope | Current Family Best | Test MAE | Interpretation |
| --- | --- | ---: | --- |
| `sequential_residual_offset_probe` | `te_sequential_residual_offset_probe_remote_global` | 0.003537 | New `global` Wave 3.1 branch candidate |
| `sequential_residual_offset_probe_fw` | `te_sequential_residual_offset_probe_remote_fw` | 0.003385 | New forward-only Wave 3.1 branch candidate |
| `sequential_residual_offset_probe_bw` | `te_sequential_residual_offset_probe_remote_bw` | 0.003638 | New backward-only Wave 3.1 branch candidate |

The campaign runner refreshed the family registries for all three branch
families and updated the program registry. The program-level scalar best did
not move because the existing Wave 2.2 periodic `GRU` backward-only model is
still stronger on scalar `test_mae`.

## TE Curve Verification Pipeline Boundary

`TE Curve Verification Pipeline` was not run as part of this closeout. Under campaign governance, the
official curve-first verification remains a separate operator-approved workflow
after the final campaign-results report and PDF are complete.

The next verification package should evaluate all three Wave 3.1 branches in
parallel, not only the scalar-first `Fw` row. The goal is to measure whether
the offset-aware structure improves curve following and mean-offset behavior on
the matching `global`, `Fw`, and `Bw` surfaces.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all three
runs completed, the leaderboard and best-run artifacts exist, and the three
family registries were refreshed.

From a modeling standpoint, Wave 3.1 is a completed feasibility branch. It is
not promoted over the current scalar program winner until a separate official
TE Curve Verification Pipeline curve-first refresh confirms a real curve-level gain.

## Recommended Follow-Up

1. Keep all three Wave 3.1 branch candidates: `global`, `Fw`, and `Bw`.
2. Do not collapse Wave 3.1 to the scalar-first `Fw` candidate.
3. Prepare the optional TE curve-first verification refresh as the next
   operator-launched step.
"""


def update_doc_index() -> None:
    """Register the campaign results report from the documentation index."""

    index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    report_entry = (
        "- [reports/campaign_results/track_2/campaign_closeouts/2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report.md]"
        "(./reports/campaign_results/track_2/campaign_closeouts/2026-06-04-12-28-46_track2f_offset_aware_probe_campaign_results_report.md)\n"
        "  Final results report for the completed `Wave 3.1` offset-aware\n"
        "  probe campaign, including separate `global`, `Fw`, and `Bw`\n"
        "  branch results, runner-wrapper diagnostics, registry effects, and\n"
        "  the boundary that official `TE Curve Verification Pipeline` verification remains a\n"
        "  separate operator-launched workflow.\n\n"
    )
    if report_entry in index_text:
        return
    anchor = "#### Campaign Results\n\n"
    assert anchor in index_text, "Campaign Results section not found in doc index."
    index_text = index_text.replace(anchor, anchor + report_entry, 1)
    write_text_file(DOC_INDEX_PATH, index_text)


def build_active_campaign_state(
    manifest: dict[str, Any],
    leaderboard_entry_list: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build the cleared active campaign state."""

    completed_run_list = [run for run in manifest["run_list"] if str(run["queue_status"]) == "completed"]
    failed_run_list = [run for run in manifest["run_list"] if str(run["queue_status"]) != "completed"]
    now_text = datetime.now().astimezone().isoformat(timespec="seconds")
    branch_best_entry_list = build_branch_best_entry_list(leaderboard_entry_list)

    return {
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
            "closeout_report_path": format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH),
            "campaign_output_directory": format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY),
            "track2_status": "not_run_optional_operator_launch_required",
            "branch_best_list": [
                {
                    "surface": str(entry["training_variant"]),
                    "run_name": str(entry["run_name"]),
                    "run_instance_id": str(entry["run_instance_id"]),
                    "model_family": str(entry["model_family"]),
                    "model_type": str(entry["model_type"]),
                    "test_mae": float(entry["test_mae"]),
                    "test_rmse": float(entry["test_rmse"]),
                    "val_mae": float(entry["val_mae"]),
                    "best_checkpoint_path": str(entry["best_checkpoint_path"]),
                }
                for entry in branch_best_entry_list
            ],
        },
        "protected_file_list": [],
        "queue_config_path_list": [],
        "launch_command_list": [],
    }


def update_active_campaign_state() -> None:
    """Clear the active campaign state after closeout."""

    manifest, leaderboard, _best_run_payload = load_campaign_payloads()
    active_campaign_state = build_active_campaign_state(manifest, list(leaderboard["entry_list"]))
    write_yaml_dictionary(ACTIVE_CAMPAIGN_STATE_PATH, active_campaign_state)


def closeout_campaign() -> None:
    """Close out the campaign."""

    write_text_file(CAMPAIGN_RESULTS_REPORT_PATH, build_closeout_report())
    update_doc_index()
    update_active_campaign_state()
    print(f"[DONE] Wrote campaign results report | {format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH)}")
    print(f"[DONE] Cleared active campaign state | {format_relative_path(ACTIVE_CAMPAIGN_STATE_PATH)}")


def main() -> int:
    """Run the closeout."""

    closeout_campaign()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
