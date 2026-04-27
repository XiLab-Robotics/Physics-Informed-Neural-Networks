"""Shared Track 1 directional reference-archive closeout helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts.reports.closeout.track1.closeout_track1_bidirectional_original_dataset_mega_campaign import (
    AMPLITUDE_HARMONIC_LIST,
    AcceptedTargetArtifact,
    FAMILY_ARCHIVE_FOLDER_MAP,
    FAMILY_ORDER,
    IMPLEMENTATION_TO_PAPER_FAMILY_MAP,
    PAPER_TO_IMPLEMENTATION_FAMILY_MAP,
    PHASE_HARMONIC_LIST,
    TRACK1_REFERENCE_BACKWARD_ROOT,
    TRACK1_REFERENCE_FORWARD_ROOT,
    VALIDATION_ROOT as BIDIRECTIONAL_MEGA_VALIDATION_ROOT,
    build_target_sort_key,
    load_yaml_dictionary,
    parse_target_name,
    refresh_track1_reference_archives,
)
from scripts.training import shared_training_infrastructure


def build_directional_target_name(
    direction_label: str,
    scope_key: str,
    harmonic_order: int,
) -> str:

    """Build one canonical Track 1 target name from direction, scope, and harmonic."""

    direction_prefix = "Fw" if direction_label == "forward" else "Bw"
    target_scope = "ampl" if scope_key == "amplitude" else "phase"
    return f"fft_y_{direction_prefix}_filtered_{target_scope}_{int(harmonic_order)}"


def build_inventory_target_metric_dictionary(
    reference_model_entry: dict[str, Any],
) -> dict[str, Any]:

    """Convert one archived inventory entry into the target-metric payload expected by the archive builder."""

    return {
        "target_name": str(reference_model_entry["target_name"]),
        "mae": float(reference_model_entry["training_metric_mae"]),
        "rmse": float(reference_model_entry["training_metric_rmse"]),
        "mse": float(reference_model_entry["training_metric_mse"]),
        "mape_percent": float(reference_model_entry["training_metric_mape_percent"]),
    }


def load_existing_directional_reference_entry_map(
    direction_label: str,
) -> dict[tuple[str, str], dict[str, Any]]:

    """Load the current archived target entries for one direction."""

    direction_root = (
        TRACK1_REFERENCE_FORWARD_ROOT
        if direction_label == "forward"
        else TRACK1_REFERENCE_BACKWARD_ROOT
    )
    reference_entry_map: dict[tuple[str, str], dict[str, Any]] = {}
    summary_dictionary_cache: dict[Path, dict[str, Any]] = {}
    for paper_family_code in FAMILY_ORDER:
        inventory_path = (
            direction_root
            / FAMILY_ARCHIVE_FOLDER_MAP[paper_family_code]
            / "reference_inventory.yaml"
        )
        if not inventory_path.exists():
            continue
        inventory_dictionary = load_yaml_dictionary(inventory_path)
        reference_model_list = inventory_dictionary.get("reference_models", [])
        assert isinstance(reference_model_list, list), (
            "Expected reference_models list in archive inventory | "
            f"path={inventory_path}"
        )
        for reference_model_entry in reference_model_list:
            target_name = str(reference_model_entry["target_name"])
            summary_path = shared_training_infrastructure.resolve_project_relative_path(
                str(reference_model_entry["source_validation_summary_path"])
            )
            if summary_path not in summary_dictionary_cache:
                summary_dictionary_cache[summary_path] = load_yaml_dictionary(summary_path)
            reference_entry_map[(paper_family_code, target_name)] = {
                "reference_model_entry": dict(reference_model_entry),
                "source_summary_path": summary_path,
                "source_summary_dictionary": summary_dictionary_cache[summary_path],
            }
    return reference_entry_map


def build_directional_accepted_target_artifact_map_from_selection(
    direction_label: str,
    selected_entry_dictionary: dict[tuple[str, str, int], dict[str, Any]],
    fallback_validation_root_list: list[Path] | None = None,
) -> dict[tuple[str, str, str], AcceptedTargetArtifact]:

    """Resolve the accepted target artifacts for one directional closeout selection."""

    if fallback_validation_root_list is None:
        fallback_validation_root_list = [BIDIRECTIONAL_MEGA_VALIDATION_ROOT]
    existing_reference_entry_map = load_existing_directional_reference_entry_map(
        direction_label
    )
    summary_dictionary_cache: dict[Path, dict[str, Any]] = {}
    accepted_target_artifact_map: dict[tuple[str, str, str], AcceptedTargetArtifact] = {}
    full_selection_dictionary: dict[tuple[str, str, int], dict[str, Any]] = {}
    for paper_family_code in FAMILY_ORDER:
        for harmonic_order in AMPLITUDE_HARMONIC_LIST:
            pair_identifier = (paper_family_code, "amplitude", int(harmonic_order))
            full_selection_dictionary[pair_identifier] = dict(
                selected_entry_dictionary.get(
                    pair_identifier,
                    {
                        "entry_origin": "baseline",
                        "paper_family_code": paper_family_code,
                        "scope_key": "amplitude",
                        "harmonic_order": int(harmonic_order),
                    },
                )
            )
        for harmonic_order in PHASE_HARMONIC_LIST:
            pair_identifier = (paper_family_code, "phase", int(harmonic_order))
            full_selection_dictionary[pair_identifier] = dict(
                selected_entry_dictionary.get(
                    pair_identifier,
                    {
                        "entry_origin": "baseline",
                        "paper_family_code": paper_family_code,
                        "scope_key": "phase",
                        "harmonic_order": int(harmonic_order),
                    },
                )
            )

    for pair_identifier, selected_entry in sorted(full_selection_dictionary.items()):
        paper_family_code, scope_key, harmonic_order = pair_identifier
        target_name = build_directional_target_name(
            direction_label,
            str(scope_key),
            int(harmonic_order),
        )
        artifact_key = (direction_label, str(paper_family_code), target_name)
        entry_origin = str(selected_entry["entry_origin"])
        if entry_origin == "campaign":
            summary_path = shared_training_infrastructure.resolve_project_relative_path(
                str(selected_entry["validation_summary_path"])
            )
            if summary_path not in summary_dictionary_cache:
                summary_dictionary_cache[summary_path] = load_yaml_dictionary(summary_path)
            summary_dictionary = summary_dictionary_cache[summary_path]
            winning_family_code = str(summary_dictionary["winner_summary"]["winning_family"])
            assert PAPER_TO_IMPLEMENTATION_FAMILY_MAP[str(paper_family_code)] == winning_family_code, (
                "Winning family mismatch for directional archive refresh | "
                f"paper_family={paper_family_code} | winning_family={winning_family_code}"
            )
            family_ranking_entry = summary_dictionary["family_ranking"][0]
            target_metric_entry = next(
                target_metric_entry
                for target_metric_entry in family_ranking_entry["target_metrics"]
                if str(target_metric_entry["target_name"]) == target_name
            )
            accepted_target_artifact_map[artifact_key] = AcceptedTargetArtifact(
                direction_label=direction_label,
                paper_family_code=str(paper_family_code),
                implementation_family_code=winning_family_code,
                target_name=target_name,
                target_kind=parse_target_name(target_name)[1],
                harmonic_order=int(harmonic_order),
                source_summary_path=summary_path,
                source_summary_dictionary=summary_dictionary,
                source_target_metric=dict(target_metric_entry),
            )
            continue

        existing_entry_key = (str(paper_family_code), target_name)
        if existing_entry_key in existing_reference_entry_map:
            existing_entry_bundle = existing_reference_entry_map[existing_entry_key]
            reference_model_entry = existing_entry_bundle["reference_model_entry"]
            summary_dictionary = existing_entry_bundle["source_summary_dictionary"]
            target_metric_dictionary = build_inventory_target_metric_dictionary(
                reference_model_entry
            )
            accepted_target_artifact_map[artifact_key] = AcceptedTargetArtifact(
                direction_label=direction_label,
                paper_family_code=str(paper_family_code),
                implementation_family_code=PAPER_TO_IMPLEMENTATION_FAMILY_MAP[str(paper_family_code)],
                target_name=target_name,
                target_kind=parse_target_name(target_name)[1],
                harmonic_order=int(harmonic_order),
                source_summary_path=existing_entry_bundle["source_summary_path"],
                source_summary_dictionary=summary_dictionary,
                source_target_metric=target_metric_dictionary,
            )
            continue

        fallback_candidate_artifact = resolve_fallback_target_artifact(
            direction_label=direction_label,
            paper_family_code=str(paper_family_code),
            target_name=target_name,
            fallback_validation_root_list=fallback_validation_root_list,
            summary_dictionary_cache=summary_dictionary_cache,
        )
        accepted_target_artifact_map[artifact_key] = fallback_candidate_artifact

    expected_target_count = len(FAMILY_ORDER) * (
        len(AMPLITUDE_HARMONIC_LIST) + len(PHASE_HARMONIC_LIST)
    )
    assert len(accepted_target_artifact_map) == expected_target_count, (
        "Directional accepted artifact count does not match the full Track 1 target surface | "
        f"resolved={len(accepted_target_artifact_map)} | expected={expected_target_count}"
    )
    return accepted_target_artifact_map


def refresh_directional_reference_archives_from_selection(
    direction_label: str,
    selected_entry_dictionary: dict[tuple[str, str, int], dict[str, Any]],
    archive_note_line: str,
    fallback_validation_root_list: list[Path] | None = None,
) -> list[dict[str, Any]]:

    """Refresh one directional Track 1 archive branch from a closeout selection."""

    accepted_target_artifact_map = (
        build_directional_accepted_target_artifact_map_from_selection(
            direction_label,
            selected_entry_dictionary,
            fallback_validation_root_list=fallback_validation_root_list,
        )
    )
    return refresh_track1_reference_archives(
        accepted_target_artifact_map,
        direction_label_list=[direction_label],
        archive_note_line=archive_note_line,
    )


def resolve_fallback_target_artifact(
    direction_label: str,
    paper_family_code: str,
    target_name: str,
    fallback_validation_root_list: list[Path],
    summary_dictionary_cache: dict[Path, dict[str, Any]],
) -> AcceptedTargetArtifact:

    """Recover one accepted target artifact from raw validation bundles when the archive inventory is incomplete."""

    best_candidate_artifact: AcceptedTargetArtifact | None = None
    for validation_root in fallback_validation_root_list:
        for summary_path in sorted(validation_root.rglob("validation_summary.yaml")):
            if summary_path not in summary_dictionary_cache:
                summary_dictionary_cache[summary_path] = load_yaml_dictionary(summary_path)
            summary_dictionary = summary_dictionary_cache[summary_path]
            winning_family_code = str(summary_dictionary["winner_summary"]["winning_family"])
            if IMPLEMENTATION_TO_PAPER_FAMILY_MAP.get(winning_family_code) != paper_family_code:
                continue
            family_ranking_entry = summary_dictionary["family_ranking"][0]
            matching_target_metric_entry = next(
                (
                    target_metric_entry
                    for target_metric_entry in family_ranking_entry["target_metrics"]
                    if str(target_metric_entry["target_name"]) == target_name
                ),
                None,
            )
            if matching_target_metric_entry is None:
                continue
            candidate_artifact = AcceptedTargetArtifact(
                direction_label=direction_label,
                paper_family_code=paper_family_code,
                implementation_family_code=winning_family_code,
                target_name=target_name,
                target_kind=parse_target_name(target_name)[1],
                harmonic_order=parse_target_name(target_name)[2],
                source_summary_path=summary_path,
                source_summary_dictionary=summary_dictionary,
                source_target_metric=dict(matching_target_metric_entry),
            )
            if best_candidate_artifact is None:
                best_candidate_artifact = candidate_artifact
                continue
            current_sort_key = build_target_sort_key(
                best_candidate_artifact.source_target_metric,
                str(best_candidate_artifact.source_summary_dictionary["experiment"]["run_name"]),
            )
            candidate_sort_key = build_target_sort_key(
                candidate_artifact.source_target_metric,
                str(summary_dictionary["experiment"]["run_name"]),
            )
            if candidate_sort_key < current_sort_key:
                best_candidate_artifact = candidate_artifact

    assert best_candidate_artifact is not None, (
        "Failed to recover fallback target artifact from validation bundles | "
        f"direction={direction_label} | family={paper_family_code} | target={target_name}"
    )
    return best_candidate_artifact
