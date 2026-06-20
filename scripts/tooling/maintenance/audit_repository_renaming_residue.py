"""Audit the complete working tree for legacy TE names and dataset paths."""

from __future__ import annotations

# Import Python Utilities
import argparse
import concurrent.futures
import gzip
import json
import os
import re
import zipfile
from collections import Counter
from pathlib import Path
from typing import Iterable

# Define Audit Constants
PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT_PATH = PROJECT_PATH / ".temp" / "repository_renaming_audit"
CHUNK_SIZE_BYTES = 8 * 1024 * 1024
CHUNK_OVERLAP_BYTES = 512
MAX_CONTEXT_BYTES = 180
ZIP_MEMBER_SIZE_LIMIT_BYTES = 256 * 1024 * 1024

RAW_PATTERN_DICTIONARY = {
    "dataset_forward": re.compile(rb"data/datasets", re.IGNORECASE),
    "dataset_backward": re.compile(rb"data\\+datasets", re.IGNORECASE),
    "dataset_uri": re.compile(rb"data(?:%2[fF]|%5[cC])datasets", re.IGNORECASE),
    "track_1": re.compile(rb"\bTrack[\x20\t\r\n]+1\b", re.IGNORECASE),
    "track_2": re.compile(
        rb"\bTrack[\x20\t\r\n]+2(?:F-bis|H-L|[A-H])?\b",
        re.IGNORECASE,
    ),
    "wave_2b": re.compile(rb"\bWave[\x20\t\r\n]+2B\b", re.IGNORECASE),
    "wave_2c": re.compile(rb"\bWave[\x20\t\r\n]+2C\b", re.IGNORECASE),
}

PATH_PATTERN_DICTIONARY = {
    name: re.compile(pattern.pattern.decode("ascii"), re.IGNORECASE)
    for name, pattern in RAW_PATTERN_DICTIONARY.items()
}

ZIP_LIKE_SUFFIX_SET = {".docx", ".pptx", ".xlsx", ".zip", ".whl"}
GZIP_SUFFIX_SET = {".gz", ".tgz"}


def _relative_path(path: Path) -> str:
    """Return one stable repository-relative path."""

    return path.relative_to(PROJECT_PATH).as_posix()


def _decode_context(payload: bytes) -> str:
    """Decode a bounded binary context for the audit report."""

    return payload.decode("utf-8", errors="replace").replace("\x00", "")


def _collect_matches(
    payload: bytes,
    source_path: str,
    container_member: str | None,
    scan_method: str,
) -> list[dict[str, object]]:
    """Collect all configured pattern matches from one byte payload."""

    finding_list: list[dict[str, object]] = []
    for pattern_name, pattern in RAW_PATTERN_DICTIONARY.items():
        for match in pattern.finditer(payload):
            context_start = max(0, match.start() - MAX_CONTEXT_BYTES)
            context_end = min(len(payload), match.end() + MAX_CONTEXT_BYTES)
            finding_list.append(
                {
                    "path": source_path,
                    "member": container_member,
                    "pattern": pattern_name,
                    "match": _decode_context(match.group(0)),
                    "context": _decode_context(payload[context_start:context_end]),
                    "scan_method": scan_method,
                }
            )
    return finding_list


def _scan_stream(path: Path, relative_path: str) -> list[dict[str, object]]:
    """Scan one regular file using bounded-memory overlapping chunks."""

    finding_list: list[dict[str, object]] = []
    previous_tail = b""
    with path.open("rb") as input_file:
        while True:
            chunk = input_file.read(CHUNK_SIZE_BYTES)
            if not chunk:
                break
            payload = previous_tail + chunk
            chunk_finding_list = _collect_matches(
                payload,
                relative_path,
                None,
                "raw_bytes",
            )
            if previous_tail:
                chunk_finding_list = [
                    finding
                    for finding in chunk_finding_list
                    if len(finding["context"].encode("utf-8", errors="ignore"))
                    > 0
                ]
            finding_list.extend(chunk_finding_list)
            previous_tail = payload[-CHUNK_OVERLAP_BYTES:]
    return finding_list


def _scan_zip_members(path: Path, relative_path: str) -> tuple[list[dict[str, object]], list[str]]:
    """Scan readable members of a ZIP-compatible container."""

    finding_list: list[dict[str, object]] = []
    warning_list: list[str] = []
    try:
        with zipfile.ZipFile(path) as archive:
            for member in archive.infolist():
                if member.is_dir():
                    continue
                if member.file_size > ZIP_MEMBER_SIZE_LIMIT_BYTES:
                    warning_list.append(
                        f"{relative_path}::{member.filename}: member exceeds "
                        f"{ZIP_MEMBER_SIZE_LIMIT_BYTES} bytes"
                    )
                    continue
                try:
                    payload = archive.read(member)
                except (OSError, RuntimeError, zipfile.BadZipFile) as error:
                    warning_list.append(
                        f"{relative_path}::{member.filename}: {error}"
                    )
                    continue
                finding_list.extend(
                    _collect_matches(
                        payload,
                        relative_path,
                        member.filename,
                        "zip_member",
                    )
                )
    except (OSError, RuntimeError, zipfile.BadZipFile) as error:
        warning_list.append(f"{relative_path}: {error}")
    return finding_list, warning_list


def _scan_gzip_payload(path: Path, relative_path: str) -> tuple[list[dict[str, object]], list[str]]:
    """Scan one gzip-compressed payload."""

    try:
        with gzip.open(path, "rb") as input_file:
            payload = input_file.read(ZIP_MEMBER_SIZE_LIMIT_BYTES + 1)
        if len(payload) > ZIP_MEMBER_SIZE_LIMIT_BYTES:
            return [], [f"{relative_path}: decompressed payload exceeds limit"]
        return (
            _collect_matches(payload, relative_path, None, "gzip_payload"),
            [],
        )
    except (OSError, EOFError) as error:
        return [], [f"{relative_path}: {error}"]


def _scan_path(path: Path) -> dict[str, object]:
    """Scan one filesystem path and return its complete audit record."""

    relative_path = _relative_path(path)
    path_finding_list: list[dict[str, object]] = []
    for pattern_name, pattern in PATH_PATTERN_DICTIONARY.items():
        if pattern.search(relative_path):
            path_finding_list.append(
                {
                    "path": relative_path,
                    "member": None,
                    "pattern": pattern_name,
                    "match": relative_path,
                    "context": relative_path,
                    "scan_method": "path_name",
                }
            )

    warning_list: list[str] = []
    try:
        raw_finding_list = _scan_stream(path, relative_path)
    except (OSError, PermissionError) as error:
        raw_finding_list = []
        warning_list.append(f"{relative_path}: {error}")

    container_finding_list: list[dict[str, object]] = []
    suffix = path.suffix.lower()
    if suffix in ZIP_LIKE_SUFFIX_SET:
        container_finding_list, container_warning_list = _scan_zip_members(
            path,
            relative_path,
        )
        warning_list.extend(container_warning_list)
    elif suffix in GZIP_SUFFIX_SET:
        container_finding_list, container_warning_list = _scan_gzip_payload(
            path,
            relative_path,
        )
        warning_list.extend(container_warning_list)

    return {
        "path": relative_path,
        "size_bytes": path.stat().st_size,
        "suffix": suffix,
        "findings": path_finding_list + raw_finding_list + container_finding_list,
        "warnings": warning_list,
    }


def _iter_repository_files(output_path: Path) -> Iterable[Path]:
    """Yield every current working-tree file except Git internals and audit output."""

    git_path = PROJECT_PATH / ".git"
    resolved_output_path = output_path.resolve()
    audit_output_parent_path = DEFAULT_OUTPUT_PATH.parent.resolve()
    for directory_path, directory_name_list, file_name_list in os.walk(PROJECT_PATH):
        directory = Path(directory_path)
        directory_name_list[:] = [
            name
            for name in directory_name_list
            if (directory / name).resolve() != git_path.resolve()
            and not (directory / name).resolve().is_relative_to(resolved_output_path)
            and not (
                (directory / name).resolve().parent == audit_output_parent_path
                and (directory / name).name.startswith("repository_renaming_audit")
            )
        ]
        for file_name in file_name_list:
            path = directory / file_name
            if path.resolve().is_relative_to(resolved_output_path):
                continue
            yield path


def _write_json_lines(path: Path, row_list: list[dict[str, object]]) -> None:
    """Write deterministic JSON Lines output."""

    with path.open("w", encoding="utf-8", newline="\n") as output_file:
        for row in row_list:
            output_file.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            output_file.write("\n")


def run_audit(output_path: Path, worker_count: int) -> None:
    """Run the complete working-tree audit."""

    output_path.mkdir(parents=True, exist_ok=True)
    file_list = list(_iter_repository_files(output_path))

    result_list: list[dict[str, object]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker_count) as executor:
        for index, result in enumerate(executor.map(_scan_path, file_list), start=1):
            result_list.append(result)
            if index % 1000 == 0 or index == len(file_list):
                print(f"[INFO] Audited {index}/{len(file_list)} files")

    finding_list = [
        finding
        for result in result_list
        for finding in result["findings"]
    ]
    warning_list = [
        warning
        for result in result_list
        for warning in result["warnings"]
    ]

    pattern_counter = Counter(
        finding["pattern"]
        for finding in finding_list
    )
    method_counter = Counter(
        finding["scan_method"]
        for finding in finding_list
    )
    suffix_counter = Counter(result["suffix"] for result in result_list)

    summary = {
        "project_path": str(PROJECT_PATH),
        "file_count": len(result_list),
        "total_size_bytes": sum(result["size_bytes"] for result in result_list),
        "finding_count": len(finding_list),
        "finding_file_count": len({finding["path"] for finding in finding_list}),
        "warning_count": len(warning_list),
        "pattern_counts": dict(sorted(pattern_counter.items())),
        "scan_method_counts": dict(sorted(method_counter.items())),
        "suffix_counts": dict(sorted(suffix_counter.items())),
    }

    _write_json_lines(output_path / "manifest.jsonl", result_list)
    _write_json_lines(output_path / "findings.jsonl", finding_list)
    (output_path / "warnings.txt").write_text(
        "\n".join(warning_list) + ("\n" if warning_list else ""),
        encoding="utf-8",
    )
    (output_path / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


def _parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-path",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Directory for manifest, findings, warnings, and summary outputs.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=max(2, min(8, os.cpu_count() or 2)),
        help="Number of concurrent file scanners.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the command-line audit."""

    arguments = _parse_arguments()
    output_path = arguments.output_path
    if not output_path.is_absolute():
        output_path = PROJECT_PATH / output_path
    run_audit(output_path.resolve(), arguments.workers)


if __name__ == "__main__":
    main()
