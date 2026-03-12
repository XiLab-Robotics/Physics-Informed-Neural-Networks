""" Generate Styled HTML And PDF Report """

from __future__ import annotations

# Import Python Utilities
import argparse, html, tempfile
import re, shutil, subprocess
from pathlib import Path
from typing import Sequence

# Browser And Report Constants
CHROME_EXECUTABLE_CANDIDATE_PATHS = (
    Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
    Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
)

DEFAULT_REPORT_SUBTITLE = "Feedforward Transmission Error Baseline"
DEFAULT_REPORT_CATEGORY = "Analysis Report"
HERO_NOTE_TEXT = (
    "Styled PDF edition generated from the canonical Markdown analysis report "
    "for improved readability, section hierarchy, and table presentation."
)

ALIGN_LEFT = "align-left"
ALIGN_CENTER = "align-center"
ALIGN_RIGHT = "align-right"

CONFIGURATION_TABLE_HEADER_CELLS = (
    "Config",
    "Status",
    "Main Intent",
    "Curve Batch",
    "Point Stride",
    "Max Points/Curve",
    "Workers",
    "Pin Memory",
    "Hidden Layers",
    "Epoch Budget",
    "Patience",
)

CAMPAIGN_SUMMARY_ALIGNMENTS = (ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER)
DATA_PIPELINE_ALIGNMENTS = (ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER)
MODEL_AND_SCHEDULE_ALIGNMENTS = (ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER, ALIGN_CENTER)

BROWSER_PDF_EXPORT_ARGUMENTS = (
    "--headless",
    "--disable-gpu",
    "--disable-breakpad",
    "--disable-crash-reporter",
    "--allow-file-access-from-files",
    "--no-pdf-header-footer",
)

REPORT_STYLESHEET = """
    @page {
      size: A4;
      margin: 14mm 15mm 16mm 15mm;
    }

    * {
      box-sizing: border-box;
    }

    html {
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
      background: #ffffff;
    }

    body {
      margin: 0;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      color: #16193B;
      background: #ffffff;
      line-height: 1.48;
      font-size: 9.35pt;
    }

    .page-shell {
      width: 100%;
      max-width: 174mm;
      margin: 0 auto;
    }

    .hero {
      padding: 16px 18px 15px 18px;
      border-radius: 14px;
      border: 1px solid #7FB2F0;
      background: linear-gradient(180deg, #35478C 0%, #16193B 100%);
      color: #ffffff;
      margin-bottom: 14px;
    }

    .hero-badge {
      display: inline-block;
      padding: 4px 9px;
      border-radius: 999px;
      background: rgba(173, 213, 247, 0.16);
      border: 1px solid rgba(173, 213, 247, 0.36);
      font-size: 7.6pt;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }

    .hero h1 {
      margin: 0 0 5px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 19pt;
      line-height: 1.12;
      letter-spacing: -0.01em;
    }

    .hero-subtitle {
      margin: 0 0 8px 0;
      font-size: 9.2pt;
      color: rgba(255, 255, 255, 0.86);
    }

    .hero-note {
      margin: 0;
      max-width: 88%;
      font-size: 8.2pt;
      color: rgba(255, 255, 255, 0.76);
    }

    .section-card {
      break-inside: auto;
      margin: 0 0 10px 0;
      padding: 11px 12px 10px 12px;
      border-radius: 12px;
      border: 1px solid #ADD5F7;
      background: #ffffff;
      max-width: 100%;
    }

    h2 {
      margin: 0 0 10px 0;
      padding-bottom: 6px;
      border-bottom: 1.5px solid #7FB2F0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 13.1pt;
      line-height: 1.2;
      color: #16193B;
      break-after: avoid-page;
    }

    h3 {
      margin: 0 0 6px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 10.3pt;
      color: #35478C;
      break-after: avoid-page;
    }

    p {
      margin: 5px 0;
      orphans: 3;
      widows: 3;
    }

    .block-label {
      margin: 8px 0 4px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 8pt;
      letter-spacing: 0;
      text-transform: none;
      color: #4E7AC7;
    }

    .subsection-block {
      break-inside: avoid-page;
      margin: 10px 0 0 0;
      padding: 9px 10px 8px 10px;
      border-radius: 10px;
      border: 1px solid rgba(173, 213, 247, 0.9);
      background: #ffffff;
      max-width: 100%;
    }

    .report-list {
      margin: 4px 0 7px 0;
      padding-left: 18px;
    }

    .report-list li {
      margin: 3px 0;
      padding-left: 2px;
    }

    .report-list ul,
    .report-list ol {
      margin-top: 4px;
      padding-left: 16px;
    }

    .li-body {
      display: inline;
    }

    .list-continuation {
      margin-top: 4px;
      margin-bottom: 0;
      color: #35478C;
    }

    code {
      padding: 1px 5px 2px 5px;
      border-radius: 5px;
      background: #F4F8FE;
      color: #16193B;
      font-family: "Consolas", "Cascadia Mono", "Courier New", monospace;
      font-size: 8.2pt;
      word-break: break-word;
    }

    strong {
      color: #16193B;
    }

    .table-wrap {
      margin: 9px 0 10px 0;
      overflow: hidden;
      border-radius: 10px;
      border: 1px solid #ADD5F7;
      background: #ffffff;
      max-width: 100%;
    }

    .report-table {
      width: 100%;
      table-layout: fixed;
      border-collapse: collapse;
      font-size: 7.2pt;
      line-height: 1.26;
    }

    .report-table thead {
      background: #35478C;
      color: #ffffff;
    }

    .report-table thead tr {
      height: 30px;
    }

    .report-table th,
    .report-table td {
      padding: 5px 5px;
      border-bottom: 1px solid #D8E8FA;
      vertical-align: top;
      overflow-wrap: anywhere;
      word-break: break-word;
      hyphens: auto;
    }

    .report-table tbody tr:nth-child(even) {
      background: #F7FBFF;
    }

    .report-table th {
      text-align: center;
      vertical-align: middle;
      white-space: nowrap;
      border-right: 1px solid rgba(255, 255, 255, 0.46);
      font-weight: 700;
    }

    .report-table th:last-child {
      border-right: none;
    }

    .report-table th:nth-child(1), .report-table td:nth-child(1) { width: 8%; }
    .report-table th:nth-child(2), .report-table td:nth-child(2) { width: 9%; }
    .report-table th:nth-child(3), .report-table td:nth-child(3) { width: 18%; }
    .report-table th:nth-child(4), .report-table td:nth-child(4) { width: 7%; }
    .report-table th:nth-child(5), .report-table td:nth-child(5) { width: 7%; }
    .report-table th:nth-child(6), .report-table td:nth-child(6) { width: 10%; }
    .report-table th:nth-child(7), .report-table td:nth-child(7) { width: 6%; }
    .report-table th:nth-child(8), .report-table td:nth-child(8) { width: 8%; }
    .report-table th:nth-child(9), .report-table td:nth-child(9) { width: 15%; }
    .report-table th:nth-child(10), .report-table td:nth-child(10) { width: 7%; }
    .report-table th:nth-child(11), .report-table td:nth-child(11) { width: 5%; }

    .report-table code {
      background: rgba(173, 213, 247, 0.18);
      font-size: 7.1pt;
    }

    .split-table-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      width: 100%;
      max-width: 100%;
    }

    .table-wrap-split {
      break-inside: avoid-page;
    }

    .table-caption {
      padding: 8px 10px 7px 10px;
      border-bottom: 1px solid #ADD5F7;
      background: #F7FBFF;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 8.5pt;
      color: #16193B;
    }

    .report-table-summary {
      font-size: 8pt;
    }

    .report-table-summary th:nth-child(1), .report-table-summary td:nth-child(1) { width: 20%; }
    .report-table-summary th:nth-child(2), .report-table-summary td:nth-child(2) { width: 22%; }
    .report-table-summary th:nth-child(3), .report-table-summary td:nth-child(3) { width: 58%; }

    .report-table-technical-data,
    .report-table-technical-schedule {
      font-size: 7.55pt;
    }

    .report-table-technical-data th,
    .report-table-technical-data td,
    .report-table-technical-schedule th,
    .report-table-technical-schedule td {
      padding: 5px 4px;
    }

    .report-table-summary th,
    .report-table-summary td,
    .report-table-technical-data th,
    .report-table-technical-data td,
    .report-table-technical-schedule th,
    .report-table-technical-schedule td {
      text-align: center;
    }

    .report-table-technical-data th:nth-child(1), .report-table-technical-data td:nth-child(1) { width: 16%; }
    .report-table-technical-data th:nth-child(2), .report-table-technical-data td:nth-child(2) { width: 17%; }
    .report-table-technical-data th:nth-child(3), .report-table-technical-data td:nth-child(3) { width: 17%; }
    .report-table-technical-data th:nth-child(4), .report-table-technical-data td:nth-child(4) { width: 18%; }
    .report-table-technical-data th:nth-child(5), .report-table-technical-data td:nth-child(5) { width: 16%; }
    .report-table-technical-data th:nth-child(6), .report-table-technical-data td:nth-child(6) { width: 16%; }

    .report-table-technical-schedule th:nth-child(1), .report-table-technical-schedule td:nth-child(1) { width: 18%; }
    .report-table-technical-schedule th:nth-child(2), .report-table-technical-schedule td:nth-child(2) { width: 34%; }
    .report-table-technical-schedule th:nth-child(3), .report-table-technical-schedule td:nth-child(3) { width: 24%; }
    .report-table-technical-schedule th:nth-child(4), .report-table-technical-schedule td:nth-child(4) { width: 24%; }

    .report-table-technical-data td,
    .report-table-technical-schedule td,
    .report-table-summary td {
      vertical-align: middle;
    }

    .align-right {
      text-align: right;
    }

    .align-center {
      text-align: center;
    }

    .align-left {
      text-align: left;
    }

    .section-final-recommendation {
      border-color: #7FB2F0;
    }

    .section-comparing-trial-baseline-and-workstation-variants .table-wrap {
      margin-bottom: 12px;
    }
"""

def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(description="Generate a styled HTML and PDF report from a Markdown source.")

    # Configure Report Paths
    argument_parser.add_argument("--input-markdown-path", required=True, help="Path to the Markdown source report.")
    argument_parser.add_argument("--output-html-path", required=True, help="Path to the generated styled HTML file.")
    argument_parser.add_argument("--output-pdf-path", required=True, help="Path to the generated styled PDF file.")

    # Configure Report Labels
    argument_parser.add_argument("--report-subtitle", default=DEFAULT_REPORT_SUBTITLE, help="Subtitle displayed below the report title.")
    argument_parser.add_argument("--report-category", default=DEFAULT_REPORT_CATEGORY, help="Category badge displayed in the cover block.")

    # Configure Export Environment
    argument_parser.add_argument("--chrome-executable-path", default="", help="Optional explicit Chrome or Edge executable path.")
    argument_parser.add_argument("--keep-html", action="store_true", help="Keep the generated HTML file after PDF export.")

    return argument_parser

def detect_browser_executable(explicit_path: str) -> Path:

    """ Detect Browser Executable """

    # Resolve Explicit Browser Path
    if explicit_path:

        explicit_browser_path = Path(explicit_path)

        if not explicit_browser_path.exists():
            raise FileNotFoundError(f"Browser executable not found: {explicit_browser_path}")

        return explicit_browser_path

    # Probe Known Browser Installations
    for candidate_browser_path in CHROME_EXECUTABLE_CANDIDATE_PATHS:
        if candidate_browser_path.exists(): return candidate_browser_path

    raise FileNotFoundError("Could not detect a local Chrome/Edge executable for headless PDF export.")

def slugify(raw_text: str) -> str:

    """ Slugify Heading Text """

    # Normalize Heading Slug
    normalized_text = re.sub(r"[^a-zA-Z0-9]+", "-", raw_text.strip().lower())

    return normalized_text.strip("-") or "section"

def convert_inline_markup(raw_text: str) -> str:

    """ Convert Inline Markup """

    # Split Inline Code Segments
    code_split_tokens = re.split(r"(`[^`]+`)", raw_text)
    html_tokens: list[str] = []

    for code_split_token in code_split_tokens:
        if not code_split_token:
            continue

        # Render Inline Code Token
        if code_split_token.startswith("`") and code_split_token.endswith("`"):
            html_tokens.append(f"<code>{html.escape(code_split_token[1:-1])}</code>")
            continue

        # Render Plain Text Token
        escaped_token = html.escape(code_split_token)
        escaped_token = re.sub(
            r"\*\*(.+?)\*\*",
            lambda match_object: f"<strong>{match_object.group(1)}</strong>",
            escaped_token,
        )

        # Append Escaped Text Token
        html_tokens.append(escaped_token)

    return "".join(html_tokens)

def split_table_row(markdown_row: str) -> list[str]:

    """ Split Table Row """

    # Trim Table Row Borders
    normalized_row = markdown_row.strip().strip("|")

    # Split Row Into Cells And Trim Cell Padding
    return [cell.strip() for cell in normalized_row.split("|")]

def extract_table_alignments(separator_row: str) -> list[str]:

    """ Extract Table Alignments """

    alignments: list[str] = []

    for separator_cell in split_table_row(separator_row):

        # Normalize Cell Marker
        stripped_separator_cell = separator_cell.strip()

        # Resolve Cell Alignment
        if stripped_separator_cell.startswith(":") and stripped_separator_cell.endswith(":"): alignments.append(ALIGN_CENTER)
        elif stripped_separator_cell.endswith(":"): alignments.append(ALIGN_RIGHT)
        else: alignments.append(ALIGN_LEFT)

    return alignments

def is_heading(markdown_line: str) -> bool:

    """ Check Heading Line """

    # Match Heading Prefix
    return markdown_line.startswith("#")

def is_table_row(markdown_line: str) -> bool:

    """ Check Table Row """

    # Match Markdown Table Prefix
    return markdown_line.strip().startswith("|")

def is_list_item(markdown_line: str) -> bool:

    """ Check List Item """

    # Match Bullet Or Numbered Item
    return bool(re.match(r"^(\s*)([-*]|\d+\.)\s+.+$", markdown_line))

def get_list_item_metadata(markdown_line: str) -> tuple[int, str, str]:

    """ Get List Item Metadata """

    # Match List Item Structure
    match_object = re.match(r"^(\s*)([-*]|\d+\.)\s+(.+)$", markdown_line)

    # Validate Match Result
    if match_object is None: raise ValueError(f"Line is not a list item: {markdown_line}")

    # Parse List Item Fields
    indentation_width = len(match_object.group(1).replace("\t", "    "))
    bullet_token = match_object.group(2)
    item_content = match_object.group(3).strip()
    list_tag = "ol" if bullet_token.endswith(".") else "ul"

    return indentation_width, list_tag, item_content

def collect_table_lines(markdown_lines: Sequence[str], start_index: int) -> tuple[list[str], int]:

    """ Collect Table Lines """

    table_lines: list[str] = []
    current_index = start_index

    # Collect Consecutive Table Rows
    while current_index < len(markdown_lines) and is_table_row(markdown_lines[current_index]):
        table_lines.append(markdown_lines[current_index])
        current_index += 1

    return table_lines, current_index

def render_table_header_cells(header_cells: Sequence[str], alignments: Sequence[str]) -> str:

    """ Render Table Header Cells """

    header_html_tokens: list[str] = []

    for header_index, header_cell in enumerate(header_cells):

        # Resolve Header Alignment
        alignment_class = alignments[header_index] if header_index < len(alignments) else ALIGN_LEFT
        header_html_tokens.append(f'<th class="{alignment_class}">{convert_inline_markup(header_cell)}</th>')

    return "".join(header_html_tokens)

def render_table_body_rows(body_rows: Sequence[str], alignments: Sequence[str]) -> str:

    """ Render Table Body Rows """

    body_html_tokens: list[str] = []

    for body_row in body_rows:

        body_html_tokens.append("<tr>")

        for cell_index, body_cell in enumerate(split_table_row(body_row)):

            # Resolve Cell Alignment
            alignment_class = alignments[cell_index] if cell_index < len(alignments) else ALIGN_LEFT
            body_html_tokens.append(f'<td class="{alignment_class}">{convert_inline_markup(body_cell)}</td>')

        body_html_tokens.append("</tr>")

    return "".join(body_html_tokens)

def render_split_table_body_rows(body_rows: Sequence[str], alignments: Sequence[str], selected_indexes: Sequence[int]) -> str:

    """ Render Split Table Body Rows """

    body_html_tokens: list[str] = []

    for body_row in body_rows:

        # Split Row Cells
        row_cells = split_table_row(body_row)
        body_html_tokens.append("<tr>")

        for output_index, source_index in enumerate(selected_indexes):

            # Resolve Cell Alignment
            body_cell = row_cells[source_index]
            alignment_class = alignments[output_index] if output_index < len(alignments) else ALIGN_LEFT
            body_html_tokens.append(f'<td class="{alignment_class}">{convert_inline_markup(body_cell)}</td>')

        body_html_tokens.append("</tr>")

    return "".join(body_html_tokens)

def render_standard_table(header_cells: Sequence[str], alignments: Sequence[str], body_rows: Sequence[str]) -> str:

    """ Render Standard Table """

    # Render Table Sections
    header_html = render_table_header_cells(header_cells, alignments)
    body_html = render_table_body_rows(body_rows, alignments)

    return (
        '<div class="table-wrap">'
        '<table class="report-table">'
        "<thead><tr>"
        f"{header_html}"
        "</tr></thead>"
        "<tbody>"
        f"{body_html}"
        "</tbody></table></div>"
    )

def render_split_configuration_table(
    table_title: str,
    header_cells: Sequence[str],
    alignments: Sequence[str],
    body_rows: Sequence[str],
    selected_indexes: Sequence[int],
    table_class_name: str,
) -> str:

    """ Render Split Configuration Table """

    # Render Selected Table Sections
    header_html = render_table_header_cells(header_cells, alignments)
    body_html = render_split_table_body_rows(body_rows, alignments, selected_indexes)

    return (
        '<div class="table-wrap table-wrap-split">'
        f'<div class="table-caption">{html.escape(table_title)}</div>'
        f'<table class="{table_class_name}">'
        "<thead><tr>"
        f"{header_html}"
        "</tr></thead>"
        "<tbody>"
        f"{body_html}"
        "</tbody></table></div>"
    )

def render_configuration_split_tables(body_rows: Sequence[str]) -> str:

    """ Render Configuration Split Tables """

    # Render Campaign Summary
    campaign_summary_html = render_split_configuration_table(
        table_title="Campaign Summary",
        header_cells=CONFIGURATION_TABLE_HEADER_CELLS[:3],
        alignments=CAMPAIGN_SUMMARY_ALIGNMENTS,
        body_rows=body_rows,
        selected_indexes=(0, 1, 2),
        table_class_name="report-table report-table-summary",
    )

    # Render Data Pipeline Settings
    data_pipeline_html = render_split_configuration_table(
        table_title="Data Pipeline Settings",
        header_cells=(CONFIGURATION_TABLE_HEADER_CELLS[0], *CONFIGURATION_TABLE_HEADER_CELLS[3:8]),
        alignments=DATA_PIPELINE_ALIGNMENTS,
        body_rows=body_rows,
        selected_indexes=(0, 3, 4, 5, 6, 7),
        table_class_name="report-table report-table-technical-data",
    )

    # Render Model And Schedule Settings
    model_and_schedule_html = render_split_configuration_table(
        table_title="Model And Schedule Settings",
        header_cells=(CONFIGURATION_TABLE_HEADER_CELLS[0], *CONFIGURATION_TABLE_HEADER_CELLS[8:11]),
        alignments=MODEL_AND_SCHEDULE_ALIGNMENTS,
        body_rows=body_rows,
        selected_indexes=(0, 8, 9, 10),
        table_class_name="report-table report-table-technical-schedule",
    )

    return (
        '<div class="split-table-grid">'
        f"{campaign_summary_html}"
        f"{data_pipeline_html}"
        f"{model_and_schedule_html}"
        "</div>"
    )

def render_table(markdown_lines: Sequence[str], start_index: int) -> tuple[str, int]:

    """ Render Table """

    # Collect Table Lines
    table_lines, current_index = collect_table_lines(markdown_lines, start_index)

    # Validate Table Structure
    if len(table_lines) < 2: raise ValueError("Expected at least header and separator row in Markdown table.")

    # Parse Table Sections
    header_cells = split_table_row(table_lines[0])
    alignments = extract_table_alignments(table_lines[1])
    body_rows = table_lines[2:]

    # Render Configuration Comparison Matrix
    if tuple(header_cells) == CONFIGURATION_TABLE_HEADER_CELLS:
        return render_configuration_split_tables(body_rows), current_index

    # Render Generic Markdown Table
    return render_standard_table(header_cells, alignments, body_rows), current_index

def render_list(markdown_lines: Sequence[str], start_index: int, base_indentation: int) -> tuple[str, int]:

    """ Render List """

    # Resolve List Type
    _, current_list_tag, _ = get_list_item_metadata(markdown_lines[start_index])
    current_index = start_index
    list_item_html_tokens: list[str] = []

    while current_index < len(markdown_lines):

        # Read Current Line
        current_line = markdown_lines[current_index]

        # Skip Empty Lines
        if not current_line.strip():
            current_index += 1
            continue

        # Validate List Item
        if not is_list_item(current_line): break

        # Parse List Item Metadata
        indentation_width, list_tag, item_content = get_list_item_metadata(current_line)

        # Validate Nesting Level
        if indentation_width < base_indentation or list_tag != current_list_tag: break

        # Render Nested List Branch
        if indentation_width > base_indentation:
            nested_list_html, current_index = render_list(
                markdown_lines=markdown_lines,
                start_index=current_index,
                base_indentation=indentation_width,
            )

            if list_item_html_tokens:
                list_item_html_tokens[-1] = list_item_html_tokens[-1].replace(
                    "</li>",
                    f"{nested_list_html}</li>",
                    1,
                )

            continue

        current_index += 1
        continuation_lines: list[str] = []
        nested_html_tokens: list[str] = []

        # Collect Continuation Paragraphs And Nested Blocks
        while current_index < len(markdown_lines):

            # Read Lookahead Line
            lookahead_line = markdown_lines[current_index]

            # Skip Empty Spacing
            if not lookahead_line.strip():
                current_index += 1
                continue

            # Stop On Heading Or Table
            if is_heading(lookahead_line) or is_table_row(lookahead_line): break

            # Render Nested List Branch
            if is_list_item(lookahead_line):

                # Read Nested Indentation
                next_indentation_width, _, _ = get_list_item_metadata(lookahead_line)
                if next_indentation_width <= base_indentation: break

                # Render Nested List Branch
                nested_list_html, current_index = render_list(
                    markdown_lines=markdown_lines,
                    start_index=current_index,
                    base_indentation=next_indentation_width,
                )
                nested_html_tokens.append(nested_list_html)
                continue

            continuation_lines.append(lookahead_line.strip())
            current_index += 1

        # Render One List Item
        item_body_html = convert_inline_markup(item_content)

        if continuation_lines:

            # Render Continuation Text
            continuation_text = " ".join(continuation_lines)
            item_body_html += (f'<p class="list-continuation">{convert_inline_markup(continuation_text)}</p>')

        # Append List Item HTML
        list_item_html_tokens.append(f'<li><div class="li-body">{item_body_html}</div>{"".join(nested_html_tokens)}</li>')

    # Return List HTML
    return (f'<{current_list_tag} class="report-list">{"".join(list_item_html_tokens)}</{current_list_tag}>', current_index)

def render_paragraph(paragraph_lines: Sequence[str]) -> str:

    """ Render Paragraph """

    # Normalize Paragraph Text
    paragraph_text = " ".join(markdown_line.strip() for markdown_line in paragraph_lines).strip()
    normalized_word_count = len(paragraph_text.rstrip(":").split())

    # Render Short Label Paragraph
    if paragraph_text.endswith(":") and normalized_word_count <= 6:
        label_text = convert_inline_markup(paragraph_text[:-1])
        return f'<p class="block-label">{label_text}</p>'

    # Render Standard Paragraph
    return f"<p>{convert_inline_markup(paragraph_text)}</p>"

def render_markdown_body(markdown_text: str) -> tuple[str, str]:

    """ Render Markdown Body """

    markdown_lines = markdown_text.splitlines()

    # Validate Report Heading
    if not markdown_lines or not markdown_lines[0].startswith("# "):
        raise ValueError("Expected the report Markdown to start with one H1 heading.")

    # Initialize Markdown Parsing State
    report_title = markdown_lines[0][2:].strip()
    body_lines = markdown_lines[1:]
    current_index = 0
    paragraph_lines: list[str] = []
    document_html_tokens: list[str] = []
    current_section_title = ""
    current_section_slug = ""
    current_section_body_tokens: list[str] = []
    current_subsection_title = ""
    current_subsection_body_tokens: list[str] = []

    def flush_paragraph() -> None:

        """ Flush Paragraph """

        nonlocal paragraph_lines

        if paragraph_lines:

            # Append Paragraph HTML
            if current_subsection_title: current_subsection_body_tokens.append(render_paragraph(paragraph_lines))
            else: current_section_body_tokens.append(render_paragraph(paragraph_lines))

            paragraph_lines = []

    def flush_subsection() -> None:

        """ Flush Subsection """

        nonlocal current_subsection_title, current_subsection_body_tokens

        # Flush Paragraph Content
        flush_paragraph()

        if not current_subsection_title: return

        if current_subsection_body_tokens:

            # Append Subsection Block
            subsection_title_html = convert_inline_markup(current_subsection_title)
            current_section_body_tokens.append(f'<div class="subsection-block"><h3>{subsection_title_html}</h3>{"".join(current_subsection_body_tokens)}</div>')

        current_subsection_title = ""
        current_subsection_body_tokens = []

    def flush_section() -> None:

        """ Flush Section """

        nonlocal current_section_title, current_section_slug, current_section_body_tokens

        # Flush Nested Subsection
        flush_subsection()

        if current_section_title and current_section_body_tokens:

            # Append Section Block
            section_title_html = convert_inline_markup(current_section_title)
            document_html_tokens.append(f'<section class="section-card section-{current_section_slug}"><h2>{section_title_html}</h2>{"".join(current_section_body_tokens)}</section>')

        current_section_title = ""
        current_section_slug = ""
        current_section_body_tokens = []

    while current_index < len(body_lines):

        # Read Current Line
        current_line = body_lines[current_index].rstrip()
        stripped_line = current_line.strip()

        # Flush On Empty Line
        if not stripped_line:
            flush_paragraph()
            current_index += 1
            continue

        # Start New Section
        if current_line.startswith("## "):
            flush_section()
            current_section_title = current_line[3:].strip()
            current_section_slug = slugify(current_section_title)
            current_index += 1
            continue

        # Start New Subsection
        if current_line.startswith("### "):
            flush_subsection()
            current_subsection_title = current_line[4:].strip()
            current_index += 1
            continue

        # Render Table Block
        if is_table_row(current_line):

            # Flush Pending Paragraph
            flush_paragraph()
            table_html, current_index = render_table(body_lines, current_index)

            # Append Table HTML
            if current_subsection_title: current_subsection_body_tokens.append(table_html)
            else: current_section_body_tokens.append(table_html)

            continue

        # Render List Block
        if is_list_item(current_line):

            # Flush Pending Paragraph
            flush_paragraph()
            indentation_width, _, _ = get_list_item_metadata(current_line)
            list_html, current_index = render_list(body_lines, current_index, indentation_width)

            # Append List HTML
            if current_subsection_title: current_subsection_body_tokens.append(list_html)
            else: current_section_body_tokens.append(list_html)

            continue

        # Accumulate Paragraph Lines
        paragraph_lines.append(current_line)
        current_index += 1

    flush_section()

    return report_title, "\n".join(document_html_tokens)

def build_html_document(report_title: str, report_subtitle: str, report_category: str, body_html: str) -> str:

    """ Build HTML Document """

    # Escape Header Text
    escaped_title = html.escape(report_title)
    escaped_subtitle = html.escape(report_subtitle)
    escaped_category = html.escape(report_category)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{escaped_title}</title>
  <style>
{REPORT_STYLESHEET}
  </style>
</head>
<body>
  <main class="page-shell">
    <header class="hero">
      <div class="hero-badge">{escaped_category}</div>
      <h1>{escaped_title}</h1>
      <p class="hero-subtitle">{escaped_subtitle}</p>
      <p class="hero-note">{html.escape(HERO_NOTE_TEXT)}</p>
    </header>
    {body_html}
  </main>
</body>
</html>
"""

def write_text_file(file_path: Path, file_content: str) -> None:

    """ Write Text File """

    # Create Parent Directory
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Save Text Content
    file_path.write_text(file_content, encoding="utf-8")

def convert_html_to_pdf(browser_executable_path: Path, html_path: Path, pdf_path: Path) -> None:

    """ Convert HTML To PDF """

    # Resolve Export Paths
    html_uri = html_path.resolve().as_uri()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_profile_root = pdf_path.parent / ".tmp_chrome_profiles"
    temporary_profile_root.mkdir(parents=True, exist_ok=True)
    temporary_profile_path = Path(
        tempfile.mkdtemp(
            prefix="codex_report_chrome_",
            dir=temporary_profile_root,
        )
    )

    try:

        # Export PDF Through Headless Browser
        subprocess.run(
            [
                str(browser_executable_path),
                *BROWSER_PDF_EXPORT_ARGUMENTS,
                f"--user-data-dir={temporary_profile_path}",
                f"--print-to-pdf={pdf_path.resolve()}",
                html_uri,
            ],
            check=True,
            capture_output=True,
            text=True,
        )

    finally:

        # Remove Temporary Browser Profile
        shutil.rmtree(temporary_profile_path, ignore_errors=True)
        shutil.rmtree(temporary_profile_root, ignore_errors=True)

def main() -> None:

    """ Run Export Pipeline """

    # Parse Command-Line Arguments
    argument_parser = build_argument_parser()
    parsed_arguments = argument_parser.parse_args()

    # Resolve Report Paths
    input_markdown_path = Path(parsed_arguments.input_markdown_path)
    output_html_path = Path(parsed_arguments.output_html_path)
    output_pdf_path = Path(parsed_arguments.output_pdf_path)

    # Render Styled HTML Document
    markdown_text = input_markdown_path.read_text(encoding="utf-8")
    report_title, body_html = render_markdown_body(markdown_text)
    html_document = build_html_document(
        report_title=report_title,
        report_subtitle=parsed_arguments.report_subtitle,
        report_category=parsed_arguments.report_category,
        body_html=body_html,
    )
    write_text_file(output_html_path, html_document)

    # Export Final PDF Report
    browser_executable_path = detect_browser_executable(parsed_arguments.chrome_executable_path)
    convert_html_to_pdf(
        browser_executable_path=browser_executable_path,
        html_path=output_html_path,
        pdf_path=output_pdf_path,
    )

    # Optionally Remove HTML Preview
    if not parsed_arguments.keep_html and output_html_path.exists():
        output_html_path.unlink()

    print(f"Styled PDF generated at: {output_pdf_path}")

if __name__ == "__main__":

    main()
