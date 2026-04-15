"""Build the artifact sync list for one completed remote training campaign."""

from __future__ import annotations

# Import Python Utilities
import argparse, json, sys
from pathlib import Path

# Define Project Path
PROJECT_PATH = Path(__file__).resolve().parents[2]

# Ensure Repository Root Is Available For Direct Script Execution
if str(PROJECT_PATH) not in sys.path: sys.path.insert(0, str(PROJECT_PATH))

# Import YAML Utilities
import yaml

# Import Project Utilities
from scripts.training import shared_training_infrastructure


def parse_command_line_arguments() -> argparse.Namespace:

    """Parse command-line arguments for the sync-manifest helper.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """

    argument_parser = argparse.ArgumentParser(description="Build the relative-path sync list for a completed remote training campaign.")
    argument_parser.add_argument("--campaign-manifest-path", type=Path, required=True, help="Path to the local copy of the campaign manifest YAML file.")
    argument_parser.add_argument("--output-path", type=Path, default=None, help="Optional JSON output path. If omitted, the JSON is written to stdout.")
    return argument_parser.parse_args()


def normalize_relative_path(relative_path_text: str | None) -> str | None:

    """Normalize one repository-relative path for sync planning.

    Args:
        relative_path_text: Raw relative path text from the campaign manifest.

    Returns:
        str | None: Normalized repository-relative POSIX path, or `None` when
        the input is empty.
    """

    if relative_path_text in [None, ""]:
        return None

    normalized_path = Path(str(relative_path_text).replace("\\", "/")).as_posix()
    return normalized_path.strip("/")


def format_project_relative_path(path: Path) -> str:

    """Format one absolute repository path as a relative POSIX path.

    Args:
        path: Absolute repository path.

    Returns:
        str: Repository-relative POSIX path.
    """

    return path.resolve().relative_to(PROJECT_PATH).as_posix()


def resolve_run_output_directory_relative_path(run_dictionary: dict) -> str | None:

    """Resolve the real output directory for one campaign run.

    Args:
        run_dictionary: One run entry from the campaign manifest.

    Returns:
        str | None: Repository-relative output-directory path that exists on
        disk, or `None` when the run did not materialize a canonical
        output-directory artifact.

    Raises:
        AssertionError: If the helper cannot recover a real output directory.
    """

    # Prefer the Manifest Path When it Already Matches a Real Directory
    raw_output_directory = run_dictionary.get("output_directory")
    manifest_output_directory_relative_path = normalize_relative_path(raw_output_directory)

    if raw_output_directory not in [None, ""]:
        raw_output_directory_path = Path(str(raw_output_directory).replace("\\", "/"))
        output_directory_parts = raw_output_directory_path.parts

        # Accept Absolute Manifest Paths That Already Point Inside This Project
        if raw_output_directory_path.is_absolute():
            absolute_output_directory_path = raw_output_directory_path.resolve()
            if absolute_output_directory_path.exists() and absolute_output_directory_path.is_relative_to(PROJECT_PATH):
                return format_project_relative_path(absolute_output_directory_path)

            if (
                len(output_directory_parts) >= 3
                and output_directory_parts[-4:-2] == ("output", "validation_checks")
            ):
                return None

        # Accept Repository-Relative Manifest Paths That Already Exist
        if manifest_output_directory_relative_path is not None:
            manifest_output_directory_path = (PROJECT_PATH / manifest_output_directory_relative_path).resolve()
            if manifest_output_directory_path.exists():
                return manifest_output_directory_relative_path

            manifest_output_directory_parts = Path(manifest_output_directory_relative_path).parts
            if len(manifest_output_directory_parts) >= 3 and manifest_output_directory_parts[:2] == ("output", "validation_checks"):
                return None

    # Recover the Real Directory from Canonical Run Metadata
    normalized_run_name = str(run_dictionary.get("run_name", "")).strip()
    normalized_run_instance_id = str(run_dictionary.get("run_instance_id", "")).strip()
    model_family = ""

    if manifest_output_directory_relative_path is not None:
        output_directory_parts = Path(manifest_output_directory_relative_path).parts
        if len(output_directory_parts) >= 3 and output_directory_parts[:2] == ("output", "training_runs"):
            model_family = str(output_directory_parts[2]).strip()

    assert model_family, (
        "Could not resolve model family for one campaign run while building the remote sync manifest | "
        f"run_name={normalized_run_name} | output_directory={run_dictionary.get('output_directory')}"
    )

    recovered_output_directory = shared_training_infrastructure.find_run_output_directory(
        model_family=model_family,
        run_name=normalized_run_name,
        run_instance_id=normalized_run_instance_id,
    )
    assert recovered_output_directory is not None, (
        "Could not recover the canonical output directory for one remote campaign run | "
        f"run_name={normalized_run_name} | run_instance_id={normalized_run_instance_id}"
    )

    return format_project_relative_path(recovered_output_directory)


def build_sync_path_list(campaign_manifest: dict) -> list[str]:

    """Build the unique ordered list of repository-relative paths to sync.

    Args:
        campaign_manifest: Parsed campaign manifest dictionary.

    Returns:
        list[str]: Unique repository-relative paths required to reconstruct the
        executed campaign state locally.
    """

    # Collect Campaign-Wide Artifacts
    sync_path_list: list[str] = []
    seen_path_set: set[str] = set()

    def append_sync_path(relative_path_text: str | None) -> None:

        """Append one path once while preserving insertion order.

        Args:
            relative_path_text: Candidate repository-relative path.
        """

        normalized_relative_path = normalize_relative_path(relative_path_text)
        if normalized_relative_path in [None, ""]:
            return

        if normalized_relative_path in seen_path_set:
            return

        seen_path_set.add(normalized_relative_path)
        sync_path_list.append(normalized_relative_path)

    append_sync_path(campaign_manifest.get("campaign_output_directory"))

    # Collect Per-Run Artifacts And Queue End State
    model_family_set: set[str] = set()

    for run_dictionary in campaign_manifest.get("run_list", []):

        resolved_run_output_directory_relative_path = resolve_run_output_directory_relative_path(run_dictionary)
        append_sync_path(resolved_run_output_directory_relative_path)
        append_sync_path(run_dictionary.get("final_queue_config_path"))

        output_directory_relative_path = normalize_relative_path(resolved_run_output_directory_relative_path)
        if output_directory_relative_path is None:
            continue

        output_directory_parts = Path(output_directory_relative_path).parts
        if len(output_directory_parts) >= 3 and output_directory_parts[:2] == ("output", "training_runs"):
            model_family_set.add(output_directory_parts[2])

    # Collect Registry Files For The Families Touched By The Campaign
    for model_family in sorted(model_family_set):

        append_sync_path(f"output/registries/families/{model_family}/leaderboard.yaml")
        append_sync_path(f"output/registries/families/{model_family}/latest_family_best.yaml")

    append_sync_path("output/registries/program/current_best_solution.yaml")
    return sync_path_list


def main() -> int:

    """Run the sync-manifest helper from the command line.

    Returns:
        int: Process exit code.
    """

    # Parse Command-Line Arguments
    command_line_arguments = parse_command_line_arguments()
    campaign_manifest_path = command_line_arguments.campaign_manifest_path.resolve()
    assert campaign_manifest_path.exists(), f"Campaign Manifest Path does not exist | {campaign_manifest_path}"

    # Load Manifest YAML
    with campaign_manifest_path.open("r", encoding="utf-8") as manifest_file:
        campaign_manifest = yaml.safe_load(manifest_file)

    assert isinstance(campaign_manifest, dict), "Campaign manifest must be a dictionary"

    # Build JSON Payload
    sync_payload = {
        "campaign_manifest_path": campaign_manifest_path.as_posix(),
        "sync_path_list": build_sync_path_list(campaign_manifest),
    }

    output_text = json.dumps(sync_payload, indent=2) + "\n"

    # Write Output Payload
    if command_line_arguments.output_path is None:
        print(output_text, end="")
        return 0

    output_path = command_line_arguments.output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
