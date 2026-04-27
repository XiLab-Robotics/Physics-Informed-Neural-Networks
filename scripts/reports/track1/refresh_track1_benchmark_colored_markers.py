"""Refresh colored status markers in the Track 1 benchmark full-matrix tables."""

from __future__ import annotations

# Import Python Utilities
import re
from pathlib import Path
from typing import Sequence

PROJECT_PATH = Path(__file__).resolve().parents[3]
BENCHMARK_REPORT_PATH = (
    PROJECT_PATH / "doc" / "reports" / "analysis" / "RCIM Paper Reference Benchmark.md"
)

GREEN_MARKER = "\U0001F7E2"
YELLOW_MARKER = "\U0001F7E1"
RED_MARKER = "\U0001F534"

FULL_MATRIX_SECTION_SPECS = (
    ("#### Table 2 - Amplitude MAE Full-Matrix Replication", 10),
    ("#### Table 3 - Amplitude RMSE Full-Matrix Replication", 10),
    ("#### Table 4 - Phase MAE Full-Matrix Replication", 10),
    ("#### Table 5 - Phase RMSE Full-Matrix Replication", 10),
)


def parse_table_row(table_line: str) -> list[str]:

    """Parse one Markdown table row into stripped cells."""

    normalized_line = table_line.strip().strip("|")
    return [cell.strip() for cell in normalized_line.split("|")]


def sanitize_repository_metric_cell(cell_text: str) -> str:

    """Remove any existing marker prefix from one repository matrix cell."""

    normalized_cell_text = cell_text.strip().strip("`")
    normalized_cell_text = re.sub(
        r"^(?:\?\?|G|Y|R|🟢|🟡|🔴|ðŸŸ¢|ðŸŸ¡|ðŸ”´)\s+",
        "",
        normalized_cell_text,
    )
    return normalized_cell_text


def resolve_marker(repository_value: float, paper_value: float) -> str:

    """Resolve the colored marker for one repository-vs-paper comparison."""

    if repository_value <= paper_value:
        return GREEN_MARKER
    if repository_value <= (paper_value * 1.25):
        return YELLOW_MARKER
    return RED_MARKER


def collect_table_rows(
    line_list: Sequence[str],
    start_index: int,
    expected_row_count: int,
) -> list[tuple[int, list[str]]]:

    """Collect the expected model rows from one Markdown table block."""

    collected_row_list: list[tuple[int, list[str]]] = []

    # Scan Forward Until The Expected Model Rows Are Found
    for line_index in range(start_index, len(line_list)):
        current_line = line_list[line_index]
        if current_line.startswith("| `"):
            collected_row_list.append((line_index, parse_table_row(current_line)))
            if len(collected_row_list) == expected_row_count:
                return collected_row_list

    raise RuntimeError(
        "Failed to collect the expected full-matrix row count | "
        f"start_index={start_index} | expected_row_count={expected_row_count}"
    )


def refresh_full_matrix_section_markers(line_list: list[str]) -> list[str]:

    """Refresh the colored legend and repository matrix markers in-place."""

    refreshed_line_list = list(line_list)

    # Refresh Legend Block
    legend_index = next(
        index
        for index, line in enumerate(refreshed_line_list)
        if line.strip() == "Status legend used in the repository matrices:"
    )
    refreshed_line_list[legend_index + 2] = (
        f"- `{GREEN_MARKER}` repository value reached or beat the paper cell"
    )
    refreshed_line_list[legend_index + 3] = (
        f"- `{YELLOW_MARKER}` repository value is still above the paper cell, but the positive gap is"
    )
    refreshed_line_list[legend_index + 5] = (
        f"- `{RED_MARKER}` repository value is still materially above the paper cell"
    )

    # Refresh Each Full-Matrix Repository Table
    for section_heading, expected_row_count in FULL_MATRIX_SECTION_SPECS:
        heading_index = next(
            index
            for index, line in enumerate(refreshed_line_list)
            if line.strip() == section_heading
        )
        paper_anchor_index = next(
            index
            for index in range(heading_index, len(refreshed_line_list))
            if refreshed_line_list[index].strip() == "Paper-side repository-owned reconstruction:"
        )
        repository_anchor_index = next(
            index
            for index in range(heading_index, len(refreshed_line_list))
            if refreshed_line_list[index].strip() == "Repository-side analogous matrix:"
        )

        paper_row_list = collect_table_rows(
            refreshed_line_list,
            paper_anchor_index,
            expected_row_count,
        )
        repository_row_list = collect_table_rows(
            refreshed_line_list,
            repository_anchor_index,
            expected_row_count,
        )

        # Refresh Repository Cells Model-By-Model
        for (_, paper_row), (repository_line_index, repository_row) in zip(
            paper_row_list,
            repository_row_list,
        ):
            refreshed_repository_row = [repository_row[0]]

            for paper_cell, repository_cell in zip(paper_row[1:], repository_row[1:]):
                paper_value = float(paper_cell)
                repository_value_text = sanitize_repository_metric_cell(repository_cell)
                repository_value = float(repository_value_text)
                marker = resolve_marker(repository_value, paper_value)
                refreshed_repository_row.append(f"`{marker} {repository_value_text}`")

            refreshed_line_list[repository_line_index] = (
                "| " + " | ".join(refreshed_repository_row) + " |"
            )

    return refreshed_line_list


def refresh_track1_benchmark_colored_markers() -> Path:

    """Refresh and persist the Track 1 benchmark colored full-matrix markers."""

    benchmark_text = BENCHMARK_REPORT_PATH.read_text(encoding="utf-8")
    benchmark_line_list = benchmark_text.splitlines()
    refreshed_line_list = refresh_full_matrix_section_markers(benchmark_line_list)
    refreshed_text = "\n".join(refreshed_line_list) + "\n"
    BENCHMARK_REPORT_PATH.write_text(refreshed_text, encoding="utf-8")
    return BENCHMARK_REPORT_PATH


def main() -> None:

    """Run the benchmark colored-marker refresh CLI."""

    refreshed_report_path = refresh_track1_benchmark_colored_markers()
    print(f"[DONE] Refreshed Track 1 benchmark colored markers | {refreshed_report_path}")


if __name__ == "__main__":
    main()
