"""Close out the completed Wave 5.2R offline-leader promotion campaign."""

from __future__ import annotations

# Import Python Utilities
import csv
from pathlib import Path
import statistics
import sys
from typing import Any

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import YAML Utilities
import yaml


# Define Closeout Paths
CAMPAIGN_NAME = "wave52r_offline_leader_cross_surface_promotion_2026_07_30"
CAMPAIGN_OUTPUT_DIRECTORY = (
    PROJECT_ROOT
    / "output"
    / "training_campaigns"
    / "2026-07-31-10-39-08_wave52r_offline_leader_cross_surface_promotion_2026_07_30"
)
CAMPAIGN_RESULTS_CSV_PATH = CAMPAIGN_OUTPUT_DIRECTORY / "campaign_results.csv"
CAMPAIGN_LEADERBOARD_PATH = CAMPAIGN_OUTPUT_DIRECTORY / "campaign_leaderboard.yaml"
CAMPAIGN_BEST_RUN_PATH = CAMPAIGN_OUTPUT_DIRECTORY / "campaign_best_run.yaml"
CAMPAIGN_STATE_PATH = CAMPAIGN_OUTPUT_DIRECTORY / "campaign_state.yaml"
ACTIVE_CAMPAIGN_STATE_PATH = PROJECT_ROOT / "doc" / "running" / "active_training_campaign.yaml"
REPORT_PATH = (
    PROJECT_ROOT
    / "doc"
    / "reports"
    / "campaign_results"
    / "model_development_waves"
    / "wave_5_2"
    / "2026-07-31-11-18-11_wave52r_offline_leader_cross_surface_promotion_campaign_results_report.md"
)
DOC_INDEX_PATH = PROJECT_ROOT / "doc" / "README.md"
EXPECTED_RESULT_COUNT = 27
EXPECTED_PROMOTION_COUNT = 18
EXPECTED_ANCHOR_COUNT = 9


def read_yaml(input_path: Path) -> dict[str, Any]:
    """Read one YAML mapping."""

    with input_path.open("r", encoding="utf-8") as input_file:
        payload = yaml.safe_load(input_file)
    assert isinstance(payload, dict), f"Expected YAML mapping | {input_path}"
    return payload


def write_yaml(output_path: Path, payload: dict[str, Any]) -> None:
    """Write one stable YAML mapping."""

    with output_path.open("w", encoding="utf-8", newline="\n") as output_file:
        yaml.safe_dump(
            payload,
            output_file,
            sort_keys=False,
            allow_unicode=False,
            width=100,
        )


def read_result_rows() -> tuple[list[str], list[dict[str, str]]]:
    """Read the campaign result table and preserve its column order."""

    with CAMPAIGN_RESULTS_CSV_PATH.open("r", encoding="utf-8", newline="") as input_file:
        reader = csv.DictReader(input_file)
        assert reader.fieldnames is not None
        result_rows = list(reader)
        return list(reader.fieldnames), result_rows


def validate_campaign_artifacts(result_rows: list[dict[str, str]]) -> None:
    """Validate run counts, queue completion, and checkpoint presence."""

    assert len(result_rows) == EXPECTED_RESULT_COUNT
    assert sum(row["model_role"] == "promotion_candidate" for row in result_rows) == EXPECTED_PROMOTION_COUNT
    assert sum(row["model_role"] == "internal_h04_anchor" for row in result_rows) == EXPECTED_ANCHOR_COUNT

    queue_state_paths = sorted((CAMPAIGN_OUTPUT_DIRECTORY / "queue_state").glob("*.yaml"))
    assert len(queue_state_paths) == 9
    for queue_state_path in queue_state_paths:
        assert read_yaml(queue_state_path)["status"] == "completed"

    for result_row in result_rows:
        checkpoint_path = PROJECT_ROOT / result_row["run_directory"] / "best_model.pt"
        assert checkpoint_path.exists(), f"Missing checkpoint | {checkpoint_path}"


def normalize_completed_status(
    field_names: list[str],
    result_rows: list[dict[str, str]],
) -> None:
    """Repair the missing K01 completion field and future-proof winner YAML."""

    assert "status" in field_names
    for result_row in result_rows:
        if not result_row["status"]:
            assert result_row["candidate_id"] == "K01"
            result_row["status"] = "completed"

    with CAMPAIGN_RESULTS_CSV_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=field_names, lineterminator="\n")
        writer.writeheader()
        writer.writerows(result_rows)

    leaderboard = read_yaml(CAMPAIGN_LEADERBOARD_PATH)
    leaderboard_results = leaderboard["result_list"]
    assert isinstance(leaderboard_results, list)
    for result in leaderboard_results:
        assert isinstance(result, dict)
        result.setdefault("status", "completed")
    write_yaml(CAMPAIGN_LEADERBOARD_PATH, leaderboard)

    best_run_payload = read_yaml(CAMPAIGN_BEST_RUN_PATH)
    best_run = best_run_payload["best_run"]
    assert isinstance(best_run, dict)
    best_run.setdefault("status", "completed")
    write_yaml(CAMPAIGN_BEST_RUN_PATH, best_run_payload)


def aggregate_candidate_rows(
    result_rows: list[dict[str, str]],
    surface: str,
    candidate_id: str,
) -> dict[str, float]:
    """Aggregate scalar campaign metrics for one candidate and surface."""

    matching_rows = [
        row
        for row in result_rows
        if row["surface"] == surface and row["candidate_id"] == candidate_id
    ]
    assert len(matching_rows) == 3
    mae_values = [float(row["mae_deg"]) for row in matching_rows]
    return {
        "mae_mean": statistics.mean(mae_values),
        "mae_std": statistics.pstdev(mae_values),
        "mae_best": min(mae_values),
        "centered_mean": statistics.mean(float(row["centered_mae_deg"]) for row in matching_rows),
        "offset_mean": statistics.mean(float(row["offset_abs_error_deg"]) for row in matching_rows),
    }


def build_results_report(result_rows: list[dict[str, str]]) -> str:
    """Build the canonical normal-closeout report."""

    scalar_summary_lines = []
    decomposition_summary_lines = []
    for surface in ("Fw", "Bw", "global"):
        for candidate_id in ("K01", "H08", "H04"):
            metrics = aggregate_candidate_rows(result_rows, surface, candidate_id)
            scalar_summary_lines.append(
                "| {surface} | {candidate} | {mean:.6f} | {std:.6f} | {best:.6f} |".format(
                    surface=surface,
                    candidate=candidate_id,
                    mean=metrics["mae_mean"],
                    std=metrics["mae_std"],
                    best=metrics["mae_best"],
                )
            )
            decomposition_summary_lines.append(
                "| {surface} | {candidate} | {centered:.6f} | {offset:.6f} |".format(
                    surface=surface,
                    candidate=candidate_id,
                    centered=metrics["centered_mean"],
                    offset=metrics["offset_mean"],
                )
            )

    return f"""# Wave 5.2R Offline Leader Cross-Surface Promotion Campaign Results

## Executive Summary

The approved campaign completed `27 / 27` runs with zero failed queue entries:
`18` K01/H08 promotion runs and `9` matched H04 analytical-anchor runs. Every
declared checkpoint is present.

K01 is the provisional scalar validation winner on `Fw` with seed `271828`
and test MAE `0.001355 deg`. Across the three seeds, K01 also has the lowest
mean test MAE on `Fw`, `Bw`, and direction-aware `global`. This is campaign
evidence only: no global promotion and no incumbent replacement is authorized.

## Campaign Contract

- Dataset: `polished_dataset`.
- Input mode: setpoints.
- Surfaces: `Fw`, `Bw`, and direction-aware `global`.
- Seeds: `314159`, `271828`, and `161803`.
- Promotion candidates: K01 and H08.
- Internal analytical anchor: H04.
- Runtime target-derived inputs: zero.
- Completed runs: `27`.
- Failed runs: `0`.

## Aggregate Raw-Error And Repeatability Results

| Surface | Candidate | Mean MAE [deg] | MAE SD [deg] | Best MAE [deg] |
| --- | --- | ---: | ---: | ---: |
{chr(10).join(scalar_summary_lines)}

## Aggregate Shape And Offset Results

| Surface | Candidate | Centered MAE [deg] | Mean offset [deg] |
| --- | --- | ---: | ---: |
{chr(10).join(decomposition_summary_lines)}

K01 leads mean raw MAE and mean centered MAE on every trained surface. H08 is
highly repeatable across seeds and improves the matched H04 raw MAE on every
surface, but its scalar offset advantage is surface-dependent. These aggregate
training/test metrics do not replace the required per-curve robustness,
harmonic, phase, continuity, and visual evidence.

## Provisional Winner

- Candidate: `K01`.
- Surface: `Fw`.
- Seed: `271828`.
- Run: `2026-07-31-10-45-41__stage9_k01__seed_271828`.
- Test MAE: `0.001354961 deg`.
- Centered MAE: `0.001205198 deg`.
- Offset absolute error: `0.000490818 deg`.
- Per-curve MAE P95: `0.003932765 deg`.
- Chunk-equivalence maximum difference: `3.948808e-07 deg`.
- Reset reproducibility maximum difference: `0 deg`.

The provisional winner is selected by the campaign's validation-only scalar
ordering. It cannot authorize promotion under the repository curve-first
policy.

## Integrity And Bookkeeping

All nine queue-state files report `completed`, all 27 result rows have matching
checkpoints, and the campaign state reports `27` completed and `0` failed. The
closeout repaired a bookkeeping omission where the nine successful K01 rows
lacked the CSV/YAML `status` field even though their queue states, metrics,
predictions, and checkpoints were complete. The campaign runner now writes
that field for future executions.

## Incumbent Preservation

Periodic GRU remains the accepted temporal non-PINN reference. Periodic
harmonic MLP remains the accepted non-temporal non-PINN reference. Neither is
deleted, overwritten, or demoted by this scalar campaign closeout.

## Promotion Decision

The campaign qualifies K01 and H08 for the separate official TE Curve
Verification Pipeline refresh. It does not yet establish that either model is
a global leader. The official review must keep `Fw`, `Bw`, and `global`
separate and compare raw error, centered shape, offset and continuity,
harmonic and phase fidelity, robustness, visual evidence, and deployment
readiness.

## Registry Decision

No accepted family or program leader registry changes in this normal closeout.
K01 remains the temporal offline leader and H08 remains the balanced
non-temporal offline leader pending official curve-first verification and
target-runtime acceptance.

## Future Integrated Specialist TODO

The roadmap retains the separate design study combining the complementary
strengths of K01, H08, F01, S01, H04, Stage 10 R00, and Stage 10 S01. This
closeout does not authorize that model or reopen physics-integrated Wave 6.

## Reproducibility Evidence

- Campaign directory: `{CAMPAIGN_OUTPUT_DIRECTORY.relative_to(PROJECT_ROOT).as_posix()}`.
- Leaderboard: `campaign_leaderboard.yaml`.
- Provisional winner: `campaign_best_run.yaml` and `campaign_best_run.md`.
- Result table: `campaign_results.csv`.
- Immutable run list: `campaign_artifact_path_list.txt`.

## Next Step

Prepare the operator-facing `Fw`/`Bw`/`global` TE Curve Verification Pipeline
launcher, run it separately, and accept or reject each candidate surface using
the official multi-index curve-first policy.
"""


def update_campaign_state() -> None:
    """Finalize campaign closeout state and clear protected-file locks."""

    state = read_yaml(CAMPAIGN_STATE_PATH)
    state["closeout_status"] = "completed"
    state["closeout_report_path"] = REPORT_PATH.relative_to(PROJECT_ROOT).as_posix()
    state["protected_file_list"] = []
    state["recommended_next_step"] = (
        "Prepare and operator-run the separate global/Fw/Bw TE Curve Verification Pipeline refresh."
    )
    write_yaml(CAMPAIGN_STATE_PATH, state)
    write_yaml(ACTIVE_CAMPAIGN_STATE_PATH, state)


def register_report() -> None:
    """Register the campaign closeout report from the canonical doc index."""

    index_text = DOC_INDEX_PATH.read_text(encoding="utf-8")
    relative_path = REPORT_PATH.relative_to(DOC_INDEX_PATH.parent).as_posix()
    entry = (
        f"- [Wave 5.2R Offline Leader Cross-Surface Promotion Campaign Results]({relative_path})\n"
        "  Normal closeout for the completed 27-run K01/H08/H04 campaign over `Fw`, `Bw`, and direction-aware `global`.\n"
    )
    if entry.splitlines()[0] in index_text:
        return
    DOC_INDEX_PATH.write_text(index_text.rstrip() + "\n\n" + entry, encoding="utf-8", newline="\n")


def main() -> None:
    """Run integrity validation, bookkeeping repair, and normal closeout."""

    field_names, result_rows = read_result_rows()
    validate_campaign_artifacts(result_rows)
    normalize_completed_status(field_names, result_rows)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_results_report(result_rows), encoding="utf-8", newline="\n")
    update_campaign_state()
    register_report()
    print("[PASS] Campaign integrity | runs=27 | failed=0 | checkpoints=27")
    print(f"[DONE] Normal closeout report | {REPORT_PATH.relative_to(PROJECT_ROOT).as_posix()}")


if __name__ == "__main__":
    main()
