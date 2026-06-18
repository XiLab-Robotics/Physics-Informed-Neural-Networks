"""Migrate campaign artifact roots to canonical snake_case names.

This script intentionally updates path references only. Historical model IDs,
campaign IDs, report filenames, and metric table labels remain unchanged unless
they are part of a moved path.
"""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path


PROJECT_PATH = Path(__file__).resolve().parents[3]
MANIFEST_PATH = (
    PROJECT_PATH
    / "doc"
    / "technical"
    / "2026-06"
    / "2026-06-18"
    / "2026-06-18-14-50-13_campaign_artifact_naming_migration_manifest.yaml"
)

TEXT_FILE_SUFFIX_SET = {
    ".bat",
    ".cfg",
    ".csv",
    ".html",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".rst",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

SCAN_ROOT_LIST = [
    PROJECT_PATH / "config",
    PROJECT_PATH / "doc",
    PROJECT_PATH / "scripts",
    PROJECT_PATH / "site",
    PROJECT_PATH / "output" / "registries",
]

EXCLUDED_TEXT_FILE_PATH_SET = {
    Path(__file__).resolve(),
    MANIFEST_PATH,
}


@dataclass(frozen=True)
class PathMove:
    source: str
    destination: str
    reason: str


DIRECTORY_MOVE_LIST = [
    PathMove(
        "doc/reports/campaign_results/track2",
        "doc/reports/campaign_results/track_2/campaign_closeouts",
        "Merge compact Track 2 closeout root into the canonical Track 2 tree.",
    ),
    PathMove(
        "doc/reports/campaign_results/track 2",
        "doc/reports/campaign_results/track_2/verification_plots",
        "Move literal-space Track 2 plot root under the canonical Track 2 tree.",
    ),
    PathMove(
        "doc/reports/campaign_results/track1",
        "doc/reports/campaign_results/track_1",
        "Use numeric-separated Track 1 result root.",
    ),
    PathMove(
        "doc/reports/campaign_results/wave1",
        "doc/reports/campaign_results/wave_1",
        "Use numeric-separated Wave 1 result root.",
    ),
    PathMove(
        "doc/reports/campaign_results/wave2",
        "doc/reports/campaign_results/wave_2",
        "Use numeric-separated Wave 2 result root.",
    ),
    PathMove(
        "doc/reports/campaign_results/wave3_wave4",
        "doc/reports/campaign_results/wave_3",
        "Move Wave 3 closeout report out of the combined Wave 3/Wave 4 root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/track1",
        "doc/reports/campaign_plans/track_1",
        "Use numeric-separated Track 1 planning root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/track2",
        "doc/reports/campaign_plans/track_2",
        "Use numeric-separated Track 2 planning root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/wave1",
        "doc/reports/campaign_plans/wave_1",
        "Use numeric-separated Wave 1 planning root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/wave2",
        "doc/reports/campaign_plans/wave_2",
        "Use numeric-separated Wave 2 planning root.",
    ),
    PathMove(
        "scripts/campaigns/track1",
        "scripts/campaigns/track_1",
        "Use numeric-separated Track 1 launcher root.",
    ),
    PathMove(
        "scripts/campaigns/track2",
        "scripts/campaigns/track_2",
        "Use numeric-separated Track 2 launcher root.",
    ),
    PathMove(
        "scripts/campaigns/wave1",
        "scripts/campaigns/wave_1",
        "Use numeric-separated Wave 1 launcher root.",
    ),
    PathMove(
        "scripts/campaigns/wave2",
        "scripts/campaigns/wave_2",
        "Use numeric-separated Wave 2 launcher root.",
    ),
    PathMove(
        "scripts/campaigns/wave3",
        "scripts/campaigns/wave_3",
        "Use numeric-separated Wave 3 launcher root.",
    ),
    PathMove(
        "scripts/campaigns/wave4",
        "scripts/campaigns/wave_4",
        "Use numeric-separated Wave 4 launcher root.",
    ),
    PathMove(
        "doc/scripts/campaigns/track2",
        "doc/scripts/campaigns/track_2",
        "Use numeric-separated Track 2 launcher-note root.",
    ),
    PathMove(
        "doc/scripts/campaigns/wave2",
        "doc/scripts/campaigns/wave_2",
        "Use numeric-separated Wave 2 launcher-note root.",
    ),
    PathMove(
        "doc/scripts/campaigns/wave3",
        "doc/scripts/campaigns/wave_3",
        "Use numeric-separated Wave 3 launcher-note root.",
    ),
    PathMove(
        "doc/scripts/campaigns/wave4",
        "doc/scripts/campaigns/wave_4",
        "Use numeric-separated Wave 4 launcher-note root.",
    ),
]

FILE_MOVE_LIST = [
    PathMove(
        "doc/reports/campaign_plans/wave3_wave4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md",
        "doc/reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-15-10-02_wave3_wave4_embryonic_skeleton_plan_report.md",
        "Keep genuinely cross-wave planning evidence under an explicit cross-wave root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/wave3_wave4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md",
        "doc/reports/campaign_plans/cross_wave/wave_3_wave_4/2026-06-11-19-25-32_wave3_wave4_parallel_hardening_plan_report.md",
        "Keep genuinely cross-wave hardening evidence under an explicit cross-wave root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/wave3_wave4/2026-06-12-13-04-05_wave4b_mmt_feature_generator_skeleton_plan_report.md",
        "doc/reports/campaign_plans/wave_4/2026-06-12-13-04-05_wave4b_mmt_feature_generator_skeleton_plan_report.md",
        "Move Wave 4 planning evidence to the Wave 4 root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/wave3_wave4/2026-06-12-14-56-27_wave3_grouped_harmonic_heads_skeleton_plan_report.md",
        "doc/reports/campaign_plans/wave_3/2026-06-12-14-56-27_wave3_grouped_harmonic_heads_skeleton_plan_report.md",
        "Move Wave 3 planning evidence to the Wave 3 root.",
    ),
    PathMove(
        "doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md",
        "doc/reports/campaign_plans/wave_3/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md",
        "Move Wave 3 campaign plan to the Wave 3 root.",
    ),
]


def project_relative(path: Path) -> str:
    return path.relative_to(PROJECT_PATH).as_posix()


def iter_text_file_path_list() -> list[Path]:
    text_file_path_list: list[Path] = []
    for scan_root in SCAN_ROOT_LIST:
        if not scan_root.exists():
            continue
        for file_path in scan_root.rglob("*"):
            if file_path.resolve() in EXCLUDED_TEXT_FILE_PATH_SET:
                continue
            if file_path.is_file() and file_path.suffix.lower() in TEXT_FILE_SUFFIX_SET:
                text_file_path_list.append(file_path)
    return sorted(set(text_file_path_list))


def build_replacement_pair_list() -> list[tuple[str, str]]:
    move_list = FILE_MOVE_LIST + DIRECTORY_MOVE_LIST
    replacement_pair_list: list[tuple[str, str]] = []

    for path_move in move_list:
        source = path_move.source
        destination = path_move.destination
        replacement_pair_list.extend(
            [
                (source, destination),
                (source.replace("/", "\\"), destination.replace("/", "\\")),
                (source.removeprefix("doc/"), destination.removeprefix("doc/")),
                (
                    source.removeprefix("doc/").replace("/", "\\"),
                    destination.removeprefix("doc/").replace("/", "\\"),
                ),
            ]
        )

    replacement_pair_list.append(
        (
            "doc/reports/campaign_plans/wave3_wave4",
            "doc/reports/campaign_plans/cross_wave/wave_3_wave_4",
        )
    )
    replacement_pair_list.append(
        (
            "doc\\reports\\campaign_plans\\wave3_wave4",
            "doc\\reports\\campaign_plans\\cross_wave\\wave_3_wave_4",
        )
    )
    replacement_pair_list.append(
        (
            "reports/campaign_plans/wave3_wave4",
            "reports/campaign_plans/cross_wave/wave_3_wave_4",
        )
    )
    replacement_pair_list.append(
        (
            "reports\\campaign_plans\\wave3_wave4",
            "reports\\campaign_plans\\cross_wave\\wave_3_wave_4",
        )
    )

    unique_pair_dictionary = dict(replacement_pair_list)
    return sorted(unique_pair_dictionary.items(), key=lambda item: len(item[0]), reverse=True)


def move_path(path_move: PathMove, dry_run: bool) -> str:
    source_path = PROJECT_PATH / path_move.source
    destination_path = PROJECT_PATH / path_move.destination

    if dry_run and destination_path.exists():
        return "already_migrated" if not source_path.exists() else "blocked_existing_destination"

    if not source_path.exists():
        if destination_path.exists():
            return "already_migrated"
        return "missing_source"
    if destination_path.exists():
        raise FileExistsError(
            f"Destination already exists: {project_relative(destination_path)}"
        )

    if dry_run:
        return "dry_run"

    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source_path), str(destination_path))
    return "moved"


def remove_empty_legacy_directory(relative_path: str, dry_run: bool) -> str:
    directory_path = PROJECT_PATH / relative_path
    if not directory_path.exists():
        return "missing"
    if any(directory_path.iterdir()):
        return "not_empty"
    if dry_run:
        return "dry_run"
    directory_path.rmdir()
    return "removed"


def update_text_references(dry_run: bool) -> list[dict[str, str | int]]:
    replacement_pair_list = build_replacement_pair_list()
    changed_file_entry_list: list[dict[str, str | int]] = []

    for file_path in iter_text_file_path_list():
        original_text = file_path.read_text(encoding="utf-8")
        updated_text = original_text
        replacement_count = 0
        for source, destination in replacement_pair_list:
            count = updated_text.count(source)
            if count:
                updated_text = updated_text.replace(source, destination)
                replacement_count += count
        if updated_text == original_text:
            continue
        changed_file_entry_list.append(
            {
                "path": project_relative(file_path),
                "replacement_count": replacement_count,
            }
        )
        if not dry_run:
            file_path.write_text(updated_text, encoding="utf-8", newline="")

    return changed_file_entry_list


def write_manifest(
    directory_move_result_list: list[dict[str, str]],
    file_move_result_list: list[dict[str, str]],
    legacy_directory_result_list: list[dict[str, str]],
    changed_file_entry_list: list[dict[str, str | int]],
    dry_run: bool,
) -> None:
    if dry_run:
        return

    line_list = [
        "# Generated by scripts/tooling/maintenance/migrate_campaign_artifact_naming.py",
        "migration_id: campaign_artifact_naming_reorganization_2026_06_18",
        "scope: campaign artifact path naming",
        "path_policy:",
        "  filesystem_slugs: lowercase_snake_case",
        "  display_names: spaced_title_case",
        "  historical_model_ids: preserved",
        "directory_moves:",
    ]
    for result in directory_move_result_list:
        line_list.extend(
            [
                f"  - source: {result['source']}",
                f"    destination: {result['destination']}",
                f"    status: {result['status']}",
                f"    reason: {result['reason']}",
            ]
        )
    line_list.append("file_moves:")
    for result in file_move_result_list:
        line_list.extend(
            [
                f"  - source: {result['source']}",
                f"    destination: {result['destination']}",
                f"    status: {result['status']}",
                f"    reason: {result['reason']}",
            ]
        )
    line_list.append("legacy_directory_cleanup:")
    for result in legacy_directory_result_list:
        line_list.extend(
            [
                f"  - path: {result['path']}",
                f"    status: {result['status']}",
            ]
        )
    line_list.append("updated_text_files:")
    for changed_file_entry in changed_file_entry_list:
        line_list.extend(
            [
                f"  - path: {changed_file_entry['path']}",
                f"    replacement_count: {changed_file_entry['replacement_count']}",
            ]
        )
    MANIFEST_PATH.write_text("\n".join(line_list) + "\n", encoding="utf-8")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Migrate campaign artifact roots to canonical names."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report planned moves and replacements without modifying files.",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()

    directory_move_result_list: list[dict[str, str]] = []
    file_move_result_list: list[dict[str, str]] = []

    for path_move in DIRECTORY_MOVE_LIST:
        status = move_path(path_move, arguments.dry_run)
        directory_move_result_list.append(
            {
                "source": path_move.source,
                "destination": path_move.destination,
                "status": status,
                "reason": path_move.reason,
            }
        )

    for path_move in FILE_MOVE_LIST:
        status = move_path(path_move, arguments.dry_run)
        file_move_result_list.append(
            {
                "source": path_move.source,
                "destination": path_move.destination,
                "status": status,
                "reason": path_move.reason,
            }
        )

    legacy_directory_result_list = [
        {
            "path": "doc/reports/campaign_plans/cross_wave/wave_3_wave_4",
            "status": remove_empty_legacy_directory(
                "doc/reports/campaign_plans/cross_wave/wave_3_wave_4",
                arguments.dry_run,
            ),
        }
    ]
    changed_file_entry_list = update_text_references(arguments.dry_run)

    write_manifest(
        directory_move_result_list,
        file_move_result_list,
        legacy_directory_result_list,
        changed_file_entry_list,
        arguments.dry_run,
    )

    print("[DONE] Campaign artifact naming migration inventory")
    print(f"dry_run: {arguments.dry_run}")
    print(f"directory_moves: {len(directory_move_result_list)}")
    print(f"file_moves: {len(file_move_result_list)}")
    print(f"text_files_updated: {len(changed_file_entry_list)}")
    if not arguments.dry_run:
        print(f"manifest: {project_relative(MANIFEST_PATH)}")


if __name__ == "__main__":
    main()
