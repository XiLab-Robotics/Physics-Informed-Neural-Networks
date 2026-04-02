""" Manage Repository Isolated Mode Sessions """

from __future__ import annotations

# Disable Bytecode Cache Writes
import sys
sys.dont_write_bytecode = True

# Import Python Utilities
import argparse, hashlib, json, shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

# Import YAML Utilities
try: import yaml
except ImportError: yaml = None

# Isolated Mode Constants
REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
ISOLATED_ROOT = REPOSITORY_ROOT / "isolated"
ACTIVE_SESSIONS_ROOT = ISOLATED_ROOT / "active"
COMPLETED_SESSIONS_ROOT = ISOLATED_ROOT / "completed"
SNAPSHOT_FILE_NAME = "locked_repository_snapshot.txt"
SESSION_CONTEXT_FILE_NAME = "session_context.md"
WORK_LOG_FILE_NAME = "work_log.md"
MANIFEST_FILE_NAME = "integration_manifest.yaml"
CHECKLIST_FILE_NAME = "integration_checklist.md"
VALIDATION_REPORT_FILE_NAME = "latest_validation_report.yaml"
INTEGRATION_REVIEW_FILE_NAME = "latest_integration_review.yaml"
EXCLUDED_ROOT_NAMES = {".git", "isolated"}
EXCLUDED_DIRECTORY_NAMES = {"__pycache__"}
DEFAULT_SESSION_LABEL = "isolated_session"
ALLOWED_MANIFEST_ACTIONS = {
    "create_new_file",
    "derive_and_merge",
    "replace_generated_artifact",
    "manual_review_required",
}

@dataclass
class SessionValidationResult:

    """ Store Session Validation Result """

    session_path: Path
    modified_locked_paths: list[str]
    deleted_locked_paths: list[str]
    new_external_paths: list[str]

    @property
    def is_clean(self) -> bool:

        """ Return Validation Clean State """

        return not self.modified_locked_paths and not self.deleted_locked_paths and not self.new_external_paths

def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(
        description="Create, validate, and close repository isolated-mode sessions.",
    )
    subparsers = argument_parser.add_subparsers(dest="command", required=True)

    # Configure Start Session Command
    start_parser = subparsers.add_parser(
        "start-session",
        help="Create a new isolated session with locked-file snapshot and staging templates.",
    )
    start_parser.add_argument(
        "--session-label",
        default=DEFAULT_SESSION_LABEL,
        help="Human-readable session label appended to the timestamp-based session id.",
    )
    start_parser.add_argument(
        "--purpose",
        default="",
        help="Short explanation of the isolated work objective.",
    )
    start_parser.add_argument(
        "--user-request",
        default="",
        help="Original user request or activation phrase for the isolated work.",
    )

    # Configure Add Manifest Item Command
    manifest_item_parser = subparsers.add_parser(
        "add-manifest-item",
        help="Register one staged artifact inside the isolated integration manifest.",
    )
    manifest_item_parser.add_argument("--session-path", required=True, help="Path to the isolated session root.")
    manifest_item_parser.add_argument("--staging-path", required=True, help="Repository-relative staging file path inside the session.")
    manifest_item_parser.add_argument("--target-path", required=True, help="Repository-relative canonical destination path.")
    manifest_item_parser.add_argument(
        "--action",
        required=True,
        choices=sorted(ALLOWED_MANIFEST_ACTIONS),
        help="Planned integration action for this staged artifact.",
    )
    manifest_item_parser.add_argument("--source-reason", default="", help="Why this staged artifact exists.")
    manifest_item_parser.add_argument(
        "--dependency-paths",
        nargs="*",
        default=[],
        help="Optional repository-relative paths that must be reviewed before integration.",
    )
    manifest_item_parser.add_argument("--integration-notes", default="", help="Optional integration note for later review.")

    # Configure Validate Session Command
    validate_parser = subparsers.add_parser(
        "validate-session",
        help="Check that the isolated session did not modify locked repository files.",
    )
    validate_parser.add_argument("--session-path", required=True, help="Path to the isolated session root.")
    validate_parser.add_argument(
        "--fail-on-violation",
        action="store_true",
        help="Return a non-zero exit code when violations are detected.",
    )

    # Configure Prepare Integration Command
    integration_parser = subparsers.add_parser(
        "prepare-integration",
        help="Regenerate the integration checklist with double-verification review items.",
    )
    integration_parser.add_argument("--session-path", required=True, help="Path to the isolated session root.")
    integration_parser.add_argument(
        "--fail-on-violation",
        action="store_true",
        help="Return a non-zero exit code when validation fails during preparation.",
    )

    # Configure Close Session Command
    close_parser = subparsers.add_parser(
        "close-session",
        help="Move an isolated session to completed or delete it after integration.",
    )
    close_parser.add_argument("--session-path", required=True, help="Path to the isolated session root.")
    close_parser.add_argument(
        "--destination",
        choices=["completed", "delete"],
        default="completed",
        help="How the session should be retired after successful validation.",
    )
    close_parser.add_argument(
        "--require-clean-validation",
        action="store_true",
        help="Block session closure when the locked-file validation is not clean.",
    )

    return argument_parser

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    # Build Argument Parser
    argument_parser = build_argument_parser()

    # Parse Command-Line Arguments
    parsed_arguments = argument_parser.parse_args()

    return parsed_arguments

def slugify_session_label(session_label: str) -> str:

    """ Slugify Session Label """

    # Normalize Session Label
    normalized_character_list: list[str] = []
    previous_character_was_separator = False

    for character in session_label.strip().lower():
        if character.isalnum():
            normalized_character_list.append(character)
            previous_character_was_separator = False
            continue
        if previous_character_was_separator:
            continue
        normalized_character_list.append("_")
        previous_character_was_separator = True

    slugified_label = "".join(normalized_character_list).strip("_")
    if not slugified_label:
        slugified_label = DEFAULT_SESSION_LABEL

    return slugified_label

def build_session_id(session_label: str) -> str:

    """ Build Session Id """

    # Resolve Current Timestamp
    current_timestamp = datetime.now().astimezone().strftime("%Y-%m-%d-%H-%M-%S")
    slugified_label = slugify_session_label(session_label)

    # Build Session Identifier
    session_id = f"{current_timestamp}_{slugified_label}"

    return session_id

def normalize_relative_path(path: Path) -> str:

    """ Normalize Relative Path """

    return path.as_posix()

def compute_file_sha256(file_path: Path) -> str:

    """ Compute File SHA256 """

    # Initialize Hash Accumulator
    hash_accumulator = hashlib.sha256()

    # Stream File Contents
    with file_path.open("rb") as file_pointer:
        while True:
            chunk = file_pointer.read(1024 * 1024)
            if not chunk:
                break
            hash_accumulator.update(chunk)

    return hash_accumulator.hexdigest()

def should_skip_path(relative_path: Path) -> bool:

    """ Determine Whether Path Should Be Skipped """

    # Skip Empty Relative Path
    if not relative_path.parts:
        return True

    # Skip Explicitly Excluded Roots
    if relative_path.parts[0] in EXCLUDED_ROOT_NAMES:
        return True

    # Skip Bytecode Cache Folders
    if any(path_part in EXCLUDED_DIRECTORY_NAMES for path_part in relative_path.parts):
        return True

    return False

def collect_repository_file_map() -> dict[str, str]:

    """ Collect Repository File Map """

    # Collect Repository Files
    repository_file_map: dict[str, str] = {}

    for file_path in REPOSITORY_ROOT.rglob("*"):
        if not file_path.is_file():
            continue

        relative_path = file_path.relative_to(REPOSITORY_ROOT)
        if should_skip_path(relative_path):
            continue

        normalized_relative_path = normalize_relative_path(relative_path)
        repository_file_map[normalized_relative_path] = compute_file_sha256(file_path)

    return dict(sorted(repository_file_map.items()))

def ensure_isolated_roots_exist() -> None:

    """ Ensure Isolated Roots Exist """

    ACTIVE_SESSIONS_ROOT.mkdir(parents=True, exist_ok=True)
    COMPLETED_SESSIONS_ROOT.mkdir(parents=True, exist_ok=True)

def write_locked_repository_snapshot(snapshot_file_path: Path, locked_file_map: dict[str, str]) -> None:

    """ Write Locked Repository Snapshot """

    # Serialize Locked Repository Snapshot
    snapshot_line_list = [f"{relative_path}\t{file_hash}" for relative_path, file_hash in locked_file_map.items()]
    snapshot_file_path.write_text("\n".join(snapshot_line_list) + "\n", encoding="utf-8")

def read_locked_repository_snapshot(snapshot_file_path: Path) -> dict[str, str]:

    """ Read Locked Repository Snapshot """

    # Validate Snapshot Path
    assert snapshot_file_path.exists(), f"Locked repository snapshot does not exist | {snapshot_file_path}"

    # Parse Snapshot Rows
    locked_file_map: dict[str, str] = {}
    snapshot_line_list = snapshot_file_path.read_text(encoding="utf-8").splitlines()

    for snapshot_line in snapshot_line_list:
        if not snapshot_line.strip():
            continue
        relative_path, file_hash = snapshot_line.split("\t", maxsplit=1)
        locked_file_map[relative_path] = file_hash

    return locked_file_map

def build_session_context_markdown(session_id: str, purpose: str, user_request: str, locked_file_count: int) -> str:

    """ Build Session Context Markdown """

    # Resolve Session Start Timestamp
    session_start_timestamp = datetime.now().astimezone().isoformat(timespec="seconds")

    # Build Session Context Markdown
    session_context_markdown = f"""# Isolated Session Context

## Session Id

- `{session_id}`

## Started At

- `{session_start_timestamp}`

## Purpose

{purpose or "Not provided."}

## User Request

{user_request or "Not provided."}

## Operational Lock

- all repository files present before session start are locked;
- `README.md` and `AGENTS.md` are included in the lock;
- only files created inside this session root may be edited while isolation remains active;
- the locked repository baseline currently contains `{locked_file_count}` files.

## Session Roots

- `staging/`
- `{MANIFEST_FILE_NAME}`
- `{CHECKLIST_FILE_NAME}`
- `{WORK_LOG_FILE_NAME}`
- `{SNAPSHOT_FILE_NAME}`
"""

    return session_context_markdown

def build_initial_work_log_markdown(session_id: str) -> str:

    """ Build Initial Work Log Markdown """

    return f"""# Isolated Work Log

## Session

- `{session_id}`

## Usage

- record analysis performed during isolated mode;
- record every new staged file that was created;
- record deferred edits to locked repository files;
- record integration notes that must be revalidated later.

## Entries

- Session created.
"""

def build_initial_manifest(session_id: str, session_path: Path) -> dict[str, Any]:

    """ Build Initial Manifest """

    session_root_relative_path = normalize_relative_path(session_path.relative_to(REPOSITORY_ROOT))

    return {
        "session_id": session_id,
        "status": "active",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "session_root": session_root_relative_path,
        "items": [],
    }

def write_yaml_file(file_path: Path, payload: Any) -> None:

    """ Write YAML File """

    if yaml is not None:
        serialized_payload = yaml.safe_dump(payload, sort_keys=False, allow_unicode=False)
    else:
        serialized_payload = json.dumps(payload, indent=2)

    file_path.write_text(serialized_payload + "\n", encoding="utf-8")

def read_yaml_file(file_path: Path) -> Any:

    """ Read YAML File """

    assert file_path.exists(), f"YAML file does not exist | {file_path}"
    file_contents = file_path.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(file_contents)
    return json.loads(file_contents)

def resolve_session_path(session_path_argument: str) -> Path:

    """ Resolve Session Path """

    # Resolve Candidate Session Path
    candidate_session_path = Path(session_path_argument)
    if not candidate_session_path.is_absolute():
        candidate_session_path = (REPOSITORY_ROOT / candidate_session_path).resolve()
    else:
        candidate_session_path = candidate_session_path.resolve()

    # Validate Session Path
    assert candidate_session_path.exists(), f"Session path does not exist | {candidate_session_path}"
    assert candidate_session_path.is_dir(), f"Session path is not a directory | {candidate_session_path}"
    assert (candidate_session_path / SNAPSHOT_FILE_NAME).exists(), f"Session snapshot file is missing | {candidate_session_path / SNAPSHOT_FILE_NAME}"
    assert (candidate_session_path / MANIFEST_FILE_NAME).exists(), f"Session manifest file is missing | {candidate_session_path / MANIFEST_FILE_NAME}"

    return candidate_session_path

def resolve_relative_repository_path(repository_relative_path: str) -> str:

    """ Resolve Relative Repository Path """

    candidate_path = Path(repository_relative_path)
    assert not candidate_path.is_absolute(), f"Path must be repository-relative | {repository_relative_path}"

    normalized_repository_relative_path = normalize_relative_path(candidate_path)
    assert normalized_repository_relative_path, "Repository-relative path must not be empty."
    assert normalized_repository_relative_path not in {".", "./"}, "Repository-relative path must not point to the repository root."

    return normalized_repository_relative_path

def validate_staging_path(session_path: Path, staging_path: str) -> str:

    """ Validate Staging Path """

    # Resolve Staging Path
    normalized_staging_path = resolve_relative_repository_path(staging_path)
    expected_staging_root = session_path / "staging"
    resolved_staging_path = (REPOSITORY_ROOT / normalized_staging_path).resolve()

    # Validate Session Containment
    assert resolved_staging_path.exists(), f"Staging path does not exist | {resolved_staging_path}"
    assert expected_staging_root in resolved_staging_path.parents, (
        "Staging path must live inside the session staging root | "
        f"{resolved_staging_path}"
    )

    return normalized_staging_path

def validate_target_path(target_path: str) -> str:

    """ Validate Target Path """

    normalized_target_path = resolve_relative_repository_path(target_path)
    target_root_name = Path(normalized_target_path).parts[0]
    assert target_root_name != "isolated", f"Target path must point to canonical repository content | {normalized_target_path}"

    return normalized_target_path

def load_manifest(session_path: Path) -> dict[str, Any]:

    """ Load Session Manifest """

    manifest_file_path = session_path / MANIFEST_FILE_NAME
    manifest_payload = read_yaml_file(manifest_file_path)
    assert isinstance(manifest_payload, dict), f"Session manifest must be a YAML mapping | {manifest_file_path}"
    manifest_payload.setdefault("items", [])

    return manifest_payload

def save_manifest(session_path: Path, manifest_payload: dict[str, Any]) -> None:

    """ Save Session Manifest """

    manifest_file_path = session_path / MANIFEST_FILE_NAME
    write_yaml_file(manifest_file_path, manifest_payload)

def build_manifest_item_identifier(item_count: int) -> str:

    """ Build Manifest Item Identifier """

    return f"item_{item_count:03d}"

def build_validation_report_payload(validation_result: SessionValidationResult) -> dict[str, Any]:

    """ Build Validation Report Payload """

    return {
        "session_path": str(validation_result.session_path),
        "validated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "is_clean": validation_result.is_clean,
        "modified_locked_paths": validation_result.modified_locked_paths,
        "deleted_locked_paths": validation_result.deleted_locked_paths,
        "new_external_paths": validation_result.new_external_paths,
    }

def write_validation_report(session_path: Path, validation_result: SessionValidationResult) -> None:

    """ Write Validation Report """

    validation_report_file_path = session_path / VALIDATION_REPORT_FILE_NAME
    validation_report_payload = build_validation_report_payload(validation_result)
    write_yaml_file(validation_report_file_path, validation_report_payload)

def validate_session_lock(session_path: Path) -> SessionValidationResult:

    """ Validate Session Lock """

    # Resolve Session Snapshot
    snapshot_file_path = session_path / SNAPSHOT_FILE_NAME
    locked_repository_snapshot = read_locked_repository_snapshot(snapshot_file_path)

    # Collect Current Repository State
    current_repository_file_map = collect_repository_file_map()

    # Detect Locked-File Changes
    modified_locked_path_list: list[str] = []
    deleted_locked_path_list: list[str] = []

    for relative_path, locked_file_hash in locked_repository_snapshot.items():
        if relative_path not in current_repository_file_map:
            deleted_locked_path_list.append(relative_path)
            continue
        current_file_hash = current_repository_file_map[relative_path]
        if current_file_hash != locked_file_hash:
            modified_locked_path_list.append(relative_path)

    # Detect New External Files
    new_external_path_list: list[str] = []
    for relative_path in current_repository_file_map:
        if relative_path in locked_repository_snapshot:
            continue
        new_external_path_list.append(relative_path)

    # Build Validation Result
    validation_result = SessionValidationResult(
        session_path=session_path,
        modified_locked_paths=sorted(modified_locked_path_list),
        deleted_locked_paths=sorted(deleted_locked_path_list),
        new_external_paths=sorted(new_external_path_list),
    )

    write_validation_report(session_path, validation_result)

    return validation_result

def print_validation_result(validation_result: SessionValidationResult) -> None:

    """ Print Validation Result """

    print("")
    print("================================================================================================")
    print("Isolated Mode Validation")
    print("================================================================================================")
    print(f"Session Path                       {validation_result.session_path}")
    print(f"Validation Clean                   {validation_result.is_clean}")
    print(f"Modified Locked Paths              {len(validation_result.modified_locked_paths)}")
    print(f"Deleted Locked Paths               {len(validation_result.deleted_locked_paths)}")
    print(f"New External Paths                 {len(validation_result.new_external_paths)}")
    print("")

    if validation_result.modified_locked_paths:
        print("Modified Locked Paths")
        print("---------------------")
        for modified_locked_path in validation_result.modified_locked_paths:
            print(modified_locked_path)
        print("")

    if validation_result.deleted_locked_paths:
        print("Deleted Locked Paths")
        print("--------------------")
        for deleted_locked_path in validation_result.deleted_locked_paths:
            print(deleted_locked_path)
        print("")

    if validation_result.new_external_paths:
        print("New External Paths")
        print("------------------")
        for new_external_path in validation_result.new_external_paths:
            print(new_external_path)
        print("")

    if validation_result.is_clean:
        print("[DONE] Isolated session validation passed with no lock violations")
    else:
        print("[WARNING] Isolated session validation found lock violations")

def build_checklist_markdown(
    session_path: Path,
    manifest_payload: dict[str, Any],
    validation_result: SessionValidationResult | None = None,
    integration_review_payload: dict[str, Any] | None = None,
) -> str:

    """ Build Checklist Markdown """

    # Resolve Checklist Summary
    session_identifier = manifest_payload.get("session_id", session_path.name)
    item_payload_list = manifest_payload.get("items", [])
    validation_summary_line = "- Validation not run yet."
    if validation_result is not None:
        validation_summary_line = (
            f"- Validation clean: `{validation_result.is_clean}` | "
            f"modified locked paths: `{len(validation_result.modified_locked_paths)}` | "
            f"deleted locked paths: `{len(validation_result.deleted_locked_paths)}` | "
            f"new external paths: `{len(validation_result.new_external_paths)}`"
        )

    # Build Checklist Header
    checklist_line_list = [
        "# Integration Checklist",
        "",
        "## Session",
        "",
        f"- `{session_identifier}`",
        f"- Session Path: `{normalize_relative_path(session_path.relative_to(REPOSITORY_ROOT))}`",
        validation_summary_line,
        "",
        "## Double Verification Rule",
        "",
        "- Pass A: revalidate the current canonical repository state before integrating each item.",
        "- Pass B: compare the staged artifact against the target and confirm that the intended content was actually absorbed.",
        "",
        "## Items",
        "",
    ]

    # Build Item Review Blocks
    if not item_payload_list:
        checklist_line_list.append("- No manifest items registered yet.")
    else:
        review_item_map = {}
        if integration_review_payload is not None:
            review_item_map = {item_review["id"]: item_review for item_review in integration_review_payload.get("items", [])}

        for item_payload in item_payload_list:
            item_identifier = item_payload["id"]
            item_review_payload = review_item_map.get(item_identifier, {})

            checklist_line_list.extend(
                [
                    f"### {item_identifier}",
                    "",
                    f"- Staging Path: `{item_payload['staging_path']}`",
                    f"- Target Path: `{item_payload['target_path']}`",
                    f"- Action: `{item_payload['action']}`",
                    f"- Manifest Status: `{item_payload.get('status', 'prepared')}`",
                    f"- Pass A / Target Exists Now: `{item_review_payload.get('target_exists_now', 'not_checked')}`",
                    f"- Pass A / Target Changed Since Session Start: `{item_review_payload.get('target_changed_since_session_start', 'not_checked')}`",
                    f"- Pass A / Staging Exists Now: `{item_review_payload.get('staging_exists_now', 'not_checked')}`",
                    "- Pass B / Repository Revalidation Completed: [ ]",
                    "- Pass B / Staged Review Completed: [ ]",
                    "- Pass B / Integrated Result Rechecked: [ ]",
                ]
            )

            dependency_path_list = item_payload.get("dependency_paths", [])
            if dependency_path_list:
                checklist_line_list.append(f"- Dependency Paths: `{', '.join(dependency_path_list)}`")

            integration_notes = item_payload.get("integration_notes", "")
            if integration_notes:
                checklist_line_list.append(f"- Integration Notes: {integration_notes}")

            checklist_line_list.append("")

    return "\n".join(checklist_line_list).rstrip() + "\n"

def build_integration_review_payload(session_path: Path, manifest_payload: dict[str, Any], locked_repository_snapshot: dict[str, str]) -> dict[str, Any]:

    """ Build Integration Review Payload """

    # Initialize Review Payload
    integration_review_payload: dict[str, Any] = {
        "session_id": manifest_payload.get("session_id", session_path.name),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "items": [],
    }

    for item_payload in manifest_payload.get("items", []):

        # Resolve Staging And Target Paths
        staging_path = (REPOSITORY_ROOT / item_payload["staging_path"]).resolve()
        target_path = (REPOSITORY_ROOT / item_payload["target_path"]).resolve()
        normalized_target_path = item_payload["target_path"]

        # Review Current State
        target_exists_now = target_path.exists()
        staging_exists_now = staging_path.exists()
        target_changed_since_session_start: str | bool = "not_locked_at_session_start"

        if normalized_target_path in locked_repository_snapshot:
            if not target_exists_now:
                target_changed_since_session_start = True
            else:
                target_changed_since_session_start = (
                    compute_file_sha256(target_path) != locked_repository_snapshot[normalized_target_path]
                )

        integration_review_payload["items"].append(
            {
                "id": item_payload["id"],
                "staging_path": item_payload["staging_path"],
                "target_path": normalized_target_path,
                "target_exists_now": target_exists_now,
                "staging_exists_now": staging_exists_now,
                "target_changed_since_session_start": target_changed_since_session_start,
                "action": item_payload["action"],
                "status": item_payload.get("status", "prepared"),
            }
        )

    return integration_review_payload

def write_integration_artifacts(session_path: Path, manifest_payload: dict[str, Any], validation_result: SessionValidationResult | None = None) -> None:

    """ Write Integration Artifacts """

    # Resolve Session Snapshot
    locked_repository_snapshot = read_locked_repository_snapshot(session_path / SNAPSHOT_FILE_NAME)

    # Build Integration Review Payload
    integration_review_payload = build_integration_review_payload(
        session_path,
        manifest_payload,
        locked_repository_snapshot,
    )

    # Write Integration Review File
    integration_review_file_path = session_path / INTEGRATION_REVIEW_FILE_NAME
    write_yaml_file(integration_review_file_path, integration_review_payload)

    # Write Integration Checklist
    checklist_markdown = build_checklist_markdown(
        session_path,
        manifest_payload,
        validation_result=validation_result,
        integration_review_payload=integration_review_payload,
    )
    checklist_file_path = session_path / CHECKLIST_FILE_NAME
    checklist_file_path.write_text(checklist_markdown, encoding="utf-8")

def start_session(parsed_arguments: argparse.Namespace) -> None:

    """ Start Isolated Session """

    # Ensure Session Roots Exist
    ensure_isolated_roots_exist()

    # Resolve Session Identity
    session_id = build_session_id(parsed_arguments.session_label)
    session_path = ACTIVE_SESSIONS_ROOT / session_id
    staging_root = session_path / "staging"
    assert not session_path.exists(), f"Session path already exists | {session_path}"

    # Collect Locked Repository Snapshot Before Session Creation
    locked_file_map = collect_repository_file_map()

    # Create Session Root
    staging_root.mkdir(parents=True, exist_ok=False)

    # Write Session Files
    write_locked_repository_snapshot(session_path / SNAPSHOT_FILE_NAME, locked_file_map)
    (session_path / SESSION_CONTEXT_FILE_NAME).write_text(
        build_session_context_markdown(
            session_id,
            parsed_arguments.purpose,
            parsed_arguments.user_request,
            len(locked_file_map),
        ),
        encoding="utf-8",
    )
    (session_path / WORK_LOG_FILE_NAME).write_text(
        build_initial_work_log_markdown(session_id),
        encoding="utf-8",
    )

    manifest_payload = build_initial_manifest(session_id, session_path)
    save_manifest(session_path, manifest_payload)
    write_integration_artifacts(session_path, manifest_payload, validation_result=None)

    # Print Session Summary
    print("")
    print("================================================================================================")
    print("Isolated Session Started")
    print("================================================================================================")
    print(f"Session Id                         {session_id}")
    print(f"Session Path                       {session_path}")
    print(f"Locked Repository Files            {len(locked_file_map)}")
    print("")
    print("Session Files")
    print("-------------")
    print(session_path / SESSION_CONTEXT_FILE_NAME)
    print(session_path / WORK_LOG_FILE_NAME)
    print(session_path / SNAPSHOT_FILE_NAME)
    print(session_path / MANIFEST_FILE_NAME)
    print(session_path / CHECKLIST_FILE_NAME)
    print(session_path / "staging")
    print("")
    print("[DONE] Isolated session created")

def add_manifest_item(parsed_arguments: argparse.Namespace) -> None:

    """ Add Manifest Item """

    # Resolve Session State
    session_path = resolve_session_path(parsed_arguments.session_path)
    staging_path = validate_staging_path(session_path, parsed_arguments.staging_path)
    target_path = validate_target_path(parsed_arguments.target_path)
    manifest_payload = load_manifest(session_path)
    manifest_item_list = manifest_payload.get("items", [])

    # Validate Dependencies
    dependency_path_list = [resolve_relative_repository_path(dependency_path) for dependency_path in parsed_arguments.dependency_paths]

    # Register Manifest Item
    manifest_item_payload = {
        "id": build_manifest_item_identifier(len(manifest_item_list) + 1),
        "staging_path": staging_path,
        "target_path": target_path,
        "action": parsed_arguments.action,
        "source_reason": parsed_arguments.source_reason,
        "dependency_paths": dependency_path_list,
        "integration_notes": parsed_arguments.integration_notes,
        "status": "prepared",
    }
    manifest_item_list.append(manifest_item_payload)
    manifest_payload["items"] = manifest_item_list
    save_manifest(session_path, manifest_payload)
    write_integration_artifacts(session_path, manifest_payload, validation_result=None)

    # Print Manifest Update Summary
    print("")
    print("================================================================================================")
    print("Manifest Item Added")
    print("================================================================================================")
    print(f"Session Path                       {session_path}")
    print(f"Item Id                            {manifest_item_payload['id']}")
    print(f"Staging Path                       {manifest_item_payload['staging_path']}")
    print(f"Target Path                        {manifest_item_payload['target_path']}")
    print(f"Action                             {manifest_item_payload['action']}")
    print("")
    print("[DONE] Manifest item registered")

def prepare_integration(parsed_arguments: argparse.Namespace) -> int:

    """ Prepare Integration """

    # Resolve Session State
    session_path = resolve_session_path(parsed_arguments.session_path)
    manifest_payload = load_manifest(session_path)
    validation_result = validate_session_lock(session_path)

    # Rebuild Integration Artifacts
    write_integration_artifacts(session_path, manifest_payload, validation_result=validation_result)
    print_validation_result(validation_result)
    print("")
    print(f"Integration Review File            {session_path / INTEGRATION_REVIEW_FILE_NAME}")
    print(f"Integration Checklist              {session_path / CHECKLIST_FILE_NAME}")
    print("")
    print("[DONE] Integration preparation artifacts regenerated")

    if parsed_arguments.fail_on_violation and not validation_result.is_clean:
        return 1

    return 0

def close_session(parsed_arguments: argparse.Namespace) -> int:

    """ Close Session """

    # Resolve Session State
    session_path = resolve_session_path(parsed_arguments.session_path)
    validation_result = validate_session_lock(session_path)

    if parsed_arguments.require_clean_validation and not validation_result.is_clean:
        print_validation_result(validation_result)
        print("")
        print("[ERROR] Session closure blocked because validation is not clean")
        return 1

    # Move Or Delete Session
    if parsed_arguments.destination == "completed":
        destination_path = COMPLETED_SESSIONS_ROOT / session_path.name
        ensure_isolated_roots_exist()
        assert not destination_path.exists(), f"Completed session path already exists | {destination_path}"
        shutil.move(str(session_path), str(destination_path))
        print("")
        print("================================================================================================")
        print("Session Closed")
        print("================================================================================================")
        print(f"Source Session Path                {session_path}")
        print(f"Completed Session Path             {destination_path}")
        print("")
        print("[DONE] Session moved to completed")
        return 0

    shutil.rmtree(session_path)
    print("")
    print("================================================================================================")
    print("Session Closed")
    print("================================================================================================")
    print(f"Deleted Session Path               {session_path}")
    print("")
    print("[DONE] Session deleted")
    return 0

def main() -> int:

    """ Run Isolated Mode Workflow """

    # Parse Command-Line Arguments
    parsed_arguments = parse_command_line_arguments()

    # Dispatch Commands
    if parsed_arguments.command == "start-session":
        start_session(parsed_arguments)
        return 0

    if parsed_arguments.command == "add-manifest-item":
        add_manifest_item(parsed_arguments)
        return 0

    if parsed_arguments.command == "validate-session":
        session_path = resolve_session_path(parsed_arguments.session_path)
        validation_result = validate_session_lock(session_path)
        print_validation_result(validation_result)
        if parsed_arguments.fail_on_violation and not validation_result.is_clean:
            return 1
        return 0

    if parsed_arguments.command == "prepare-integration":
        return prepare_integration(parsed_arguments)

    if parsed_arguments.command == "close-session":
        return close_session(parsed_arguments)

    raise RuntimeError(f"Unsupported isolated mode command | {parsed_arguments.command}")

if __name__ == "__main__":

    raise SystemExit(main())
