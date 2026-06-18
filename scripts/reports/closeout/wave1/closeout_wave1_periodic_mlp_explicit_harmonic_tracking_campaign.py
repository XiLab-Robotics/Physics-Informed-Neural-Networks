"""Close out the Wave 1 periodic MLP explicit harmonic tracking campaign."""

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
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

CAMPAIGN_NAME = "wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49"
CAMPAIGN_OUTPUT_DIRECTORY = PROJECT_PATH / "output" / "training_campaigns" / "2026-05-20-23-14-17_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42"
CAMPAIGN_RESULTS_REPORT_PATH = PROJECT_PATH / "doc" / "reports" / "campaign_results" / "wave1" / "2026-05-21-09-38-37_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_results_report.md"
PLANNING_REPORT_PATH = PROJECT_PATH / "doc" / "reports" / "campaign_plans" / "wave1" / "2026-05-20-22-42-49_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_plan_report.md"
TECHNICAL_DOCUMENT_PATH = PROJECT_PATH / "doc" / "technical" / "2026-05" / "2026-05-20" / "2026-05-20-22-34-11_periodic_mlp_explicit_harmonic_basis.md"
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_PATH / "doc" / "running" / "active_training_campaign.yaml"
DOC_INDEX_PATH = PROJECT_PATH / "doc" / "README.md"

FAMILY_KEY_LIST = ["periodic_mlp", "periodic_mlp_fw", "periodic_mlp_bw"]

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

def format_float(value: Any) -> str:

    """Format one metric value for compact report tables."""

    return f"{float(value):.6f}"

def resolve_scope_label(entry: dict[str, Any]) -> str:

    """Resolve the report-facing direction scope label."""

    variant = str(entry.get("training_variant", "")).strip()
    if variant.lower() == "global":
        return "global"
    return variant

def resolve_harmonic_bank_label(entry: dict[str, Any]) -> str:

    """Resolve the report-facing harmonic-bank label from the run name."""

    run_name = str(entry["run_name"])
    if "rcim_sparse" in run_name:
        return "RCIM sparse"
    if "dense240" in run_name:
        return "`0..240`"
    if "dense360" in run_name:
        return "`0..360`"
    return "unknown"

def build_leaderboard_table(entry_list: list[dict[str, Any]]) -> str:

    """Build the campaign leaderboard Markdown table."""

    line_list = [
        "| Rank | Run | Scope | Harmonics | Test MAE | Test RMSE | Params |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for index, entry in enumerate(entry_list, start=1):
        line_list.append(
            "| "
            f"{index} | "
            f"`{entry['run_name']}` | "
            f"{resolve_scope_label(entry)} | "
            f"{resolve_harmonic_bank_label(entry)} | "
            f"{format_float(entry['test_mae'])} | "
            f"{format_float(entry['test_rmse'])} | "
            f"{int(entry['trainable_parameter_count']):,} |"
        )
    return "\n".join(line_list)

def load_latest_family_best_entry(family_key: str) -> dict[str, Any]:

    """Load the latest family-best entry for one periodic MLP surface."""

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
        interpretation = "Updated by this campaign" if best_run_instance_id in campaign_run_instance_set else "Previous Optuna best remains ahead"
        line_list.append(
            "| "
            f"`{family_key}` | "
            f"`{best_entry['run_name']}` | "
            f"{format_float(best_entry['test_mae'])} | "
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

    leaderboard_table = build_leaderboard_table(list(leaderboard["entry_list"]))
    registry_effects_table = build_registry_effects_table(list(leaderboard["entry_list"]))

    report_text = f"""# Wave 1 Periodic MLP Explicit Harmonic Tracking Campaign Results

## Overview

This report closes the approved `Wave 1` periodic MLP explicit harmonic
tracking campaign. The campaign tested whether fixed sparse and dense harmonic
feature dictionaries improve the existing `periodic_mlp` family without
changing the pure `feedforward` baseline or redefining the future
`Fourier-Feature MLP` family.

The campaign completed all 9 planned runs with zero launcher failures. The
campaign winner by the configured selection policy, minimum `test_mae` with
`test_rmse`, `val_mae`, and parameter count as tie breakers, is
`{best_run['run_name']}`.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY)}` |
| Campaign leaderboard | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_leaderboard.yaml')}` |
| Best-run pointer | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_best_run.yaml')}` |
| Execution report | `{format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY / 'campaign_execution_report.md')}` |
| Planning report | `{format_relative_path(PLANNING_REPORT_PATH)}` |
| Technical document | `{format_relative_path(TECHNICAL_DOCUMENT_PATH)}` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `{CAMPAIGN_NAME}` |
| Started at | `{started_at}` |
| Finished at | `{finished_at}` |
| Completed runs | {len(completed_run_list)} |
| Failed runs | {len(failed_run_list)} |
| Tested model type | `periodic_mlp` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Tested harmonic banks | `RCIM sparse`, `0..240`, `0..360` |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `{best_run['run_name']}` |
| Run instance | `{best_run['run_instance_id']}` |
| Model family | `{best_run['model_family']}` |
| Model type | `{best_run['model_type']}` |
| Direction scope | {str(best_run['direction_scope_label']).replace('_', ' ')} |
| Harmonic bank | {resolve_harmonic_bank_label(best_run)} |
| Trainable parameters | {int(best_run['trainable_parameter_count']):,} |
| Validation MAE | {format_float(best_run['val_mae'])} |
| Validation RMSE | {format_float(best_run['val_rmse'])} |
| Test MAE | {format_float(best_run['test_mae'])} |
| Test RMSE | {format_float(best_run['test_rmse'])} |

The winning checkpoint is stored at
`{format_relative_path(best_run['best_checkpoint_path'])}`.

## Leaderboard

{leaderboard_table}

## Technical Interpretation

The strongest new result is forward-only `periodic_mlp` with the dense `0..240`
fixed periodic-feature bank. It reaches test MAE {format_float(best_run['test_mae'])},
ahead of the forward RCIM sparse candidate at 0.003131 and the forward dense
`0..360` candidate at 0.003155.

The result does not create a universal improvement for every direction scope.
The global campaign candidates remain behind the previous global Optuna
`periodic_mlp` winner, and the backward campaign candidates remain behind the
previous backward Optuna winner. This suggests that simply increasing the
fixed harmonic dictionary is useful in the forward-only surface but is not a
drop-in replacement for the earlier tuned compact periodic MLP surfaces.

The dense `0..240` forward model is also much larger than the compact Optuna
periodic MLP baseline. It should therefore be treated as a stronger
curve-fidelity candidate, not as an automatic deployment promotion. The Track
2 curve-overlay workflow is still required to decide whether the extra
harmonic inputs recover visible TE oscillations or only improve scalar error
locally.

## Registry Effects

{registry_effects_table}

The current program-level winner remains the previously registered `tree_fw`
run with test MAE 0.002743. This closeout therefore does not promote a new
program-level best model for deployment.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all 9
runs completed, the leaderboard and best-run artifacts exist, and the relevant
family registries were refreshed.

From a modeling standpoint, the explicit harmonic periodic-feature extension
is worth keeping. The forward dense `0..240` result is the main candidate to
carry into visual validation. The global and backward high-order periodic MLP
candidates should not replace the existing compact Optuna-selected family
bests unless later curve-level evidence justifies the larger feature bank.

## Recommended Follow-Up

1. Generate Track 2 curve overlays for the forward dense `0..240`, forward
   RCIM sparse, and forward dense `0..360` periodic MLP candidates.
2. Compare the same curves against the existing `tree_fw` program winner and
   earlier compact `periodic_mlp_fw` Optuna baseline.
3. Promote no periodic MLP checkpoint until the overlay review confirms real
   oscillation tracking rather than scalar-only improvement.
4. Keep the future `Fourier-Feature MLP` family separate from this fixed
   engineered-feature `periodic_mlp` extension.
"""
    return report_text

def update_doc_index() -> None:

    """Register the campaign-results report in the documentation index."""

    doc_index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    result_entry = (
        "- [reports/campaign_results/wave_1/2026-05-21-09-38-37_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_results_report.md]"
        "(./reports/campaign_results/wave_1/2026-05-21-09-38-37_wave1_periodic_mlp_explicit_harmonic_tracking_campaign_results_report.md)\n"
        "  Final results report for the completed `Wave 1` `periodic_mlp` explicit\n"
        "  harmonic tracking campaign, including the 9-run leaderboard and\n"
        "  registry-impact summary.\n"
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
            "campaign_output_directory": format_relative_path(CAMPAIGN_OUTPUT_DIRECTORY),
            "results_report_path": format_relative_path(CAMPAIGN_RESULTS_REPORT_PATH),
            "best_run_name": str(best_run["run_name"]),
            "best_run_instance_id": str(best_run["run_instance_id"]),
            "best_model_family": str(best_run["model_family"]),
            "best_test_mae": float(best_run["test_mae"]),
            "best_test_rmse": float(best_run["test_rmse"]),
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
