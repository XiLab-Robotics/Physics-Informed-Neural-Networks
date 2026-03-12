"""Generate a styled HTML and PDF version of a Markdown report."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import tempfile

from pathlib import Path
from typing import Sequence


CHROME_CANDIDATE_PATHS = (
    Path("C:/Program Files/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"),
    Path("C:/Program Files/Microsoft/Edge/Application/msedge.exe"),
    Path("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"),
)


def build_argument_parser() -> argparse.ArgumentParser:
    """Build argument parser."""

    argument_parser = argparse.ArgumentParser(
        description="Generate a styled HTML and PDF report from a Markdown source.",
    )

    argument_parser.add_argument(
        "--input-markdown-path",
        required=True,
        help="Path to the Markdown source report.",
    )
    argument_parser.add_argument(
        "--output-html-path",
        required=True,
        help="Path to the generated styled HTML file.",
    )
    argument_parser.add_argument(
        "--output-pdf-path",
        required=True,
        help="Path to the generated styled PDF file.",
    )
    argument_parser.add_argument(
        "--report-subtitle",
        default="Feedforward Transmission Error Baseline",
        help="Subtitle displayed below the report title.",
    )
    argument_parser.add_argument(
        "--report-category",
        default="Analysis Report",
        help="Category badge displayed in the cover block.",
    )
    argument_parser.add_argument(
        "--chrome-executable-path",
        default="",
        help="Optional explicit Chrome or Edge executable path.",
    )
    argument_parser.add_argument(
        "--keep-html",
        action="store_true",
        help="Keep the generated HTML file after PDF export.",
    )

    return argument_parser


def detect_browser_executable(explicit_path: str) -> Path:
    """Detect browser executable."""

    if explicit_path:
        explicit_browser_path = Path(explicit_path)

        if not explicit_browser_path.exists():
            raise FileNotFoundError(f"Browser executable not found: {explicit_browser_path}")

        return explicit_browser_path

    for candidate_browser_path in CHROME_CANDIDATE_PATHS:
        if candidate_browser_path.exists():
            return candidate_browser_path

    raise FileNotFoundError(
        "Could not detect a local Chrome/Edge executable for headless PDF export."
    )


def slugify(raw_text: str) -> str:
    """Slugify heading text."""

    normalized_text = re.sub(r"[^a-zA-Z0-9]+", "-", raw_text.strip().lower())

    return normalized_text.strip("-") or "section"


def convert_inline_markup(raw_text: str) -> str:
    """Convert basic inline Markdown markup."""

    code_split_tokens = re.split(r"(`[^`]+`)", raw_text)
    html_tokens: list[str] = []

    for code_split_token in code_split_tokens:
        if not code_split_token:
            continue

        if code_split_token.startswith("`") and code_split_token.endswith("`"):
            html_tokens.append(f"<code>{html.escape(code_split_token[1:-1])}</code>")
            continue

        escaped_token = html.escape(code_split_token)
        escaped_token = re.sub(
            r"\*\*(.+?)\*\*",
            lambda match_object: f"<strong>{match_object.group(1)}</strong>",
            escaped_token,
        )
        html_tokens.append(escaped_token)

    return "".join(html_tokens)


def split_table_row(markdown_row: str) -> list[str]:
    """Split Markdown table row."""

    normalized_row = markdown_row.strip().strip("|")

    return [cell.strip() for cell in normalized_row.split("|")]


def extract_table_alignments(separator_row: str) -> list[str]:
    """Extract table alignments from the Markdown separator row."""

    alignments: list[str] = []

    for separator_cell in split_table_row(separator_row):
        stripped_separator_cell = separator_cell.strip()

        if stripped_separator_cell.startswith(":") and stripped_separator_cell.endswith(":"):
            alignments.append("align-center")
        elif stripped_separator_cell.endswith(":"):
            alignments.append("align-right")
        else:
            alignments.append("align-left")

    return alignments


def is_heading(markdown_line: str) -> bool:
    """Check whether the line is a Markdown heading."""

    return markdown_line.startswith("#")


def is_table_row(markdown_line: str) -> bool:
    """Check whether the line is a Markdown table row."""

    return markdown_line.strip().startswith("|")


def is_list_item(markdown_line: str) -> bool:
    """Check whether the line is a Markdown list item."""

    return bool(re.match(r"^(\s*)([-*]|\d+\.)\s+.+$", markdown_line))


def get_list_item_metadata(markdown_line: str) -> tuple[int, str, str]:
    """Extract indentation, list type, and content from a list item."""

    match_object = re.match(r"^(\s*)([-*]|\d+\.)\s+(.+)$", markdown_line)

    if match_object is None:
        raise ValueError(f"Line is not a list item: {markdown_line}")

    indentation_width = len(match_object.group(1).replace("\t", "    "))
    bullet_token = match_object.group(2)
    item_content = match_object.group(3).strip()
    list_tag = "ol" if bullet_token.endswith(".") else "ul"

    return indentation_width, list_tag, item_content


def render_table(markdown_lines: Sequence[str], start_index: int) -> tuple[str, int]:
    """Render a Markdown table block."""

    table_lines: list[str] = []
    current_index = start_index

    while current_index < len(markdown_lines) and is_table_row(markdown_lines[current_index]):
        table_lines.append(markdown_lines[current_index])
        current_index += 1

    if len(table_lines) < 2:
        raise ValueError("Expected at least header and separator row in Markdown table.")

    header_cells = split_table_row(table_lines[0])
    alignments = extract_table_alignments(table_lines[1])
    body_rows = table_lines[2:]

    table_html_tokens = ['<div class="table-wrap">', '<table class="report-table">', "<thead>", "<tr>"]

    for header_index, header_cell in enumerate(header_cells):
        alignment_class = alignments[header_index] if header_index < len(alignments) else "align-left"
        table_html_tokens.append(
            f'<th class="{alignment_class}">{convert_inline_markup(header_cell)}</th>'
        )

    table_html_tokens.extend(["</tr>", "</thead>", "<tbody>"])

    for body_row in body_rows:
        table_html_tokens.append("<tr>")

        for cell_index, body_cell in enumerate(split_table_row(body_row)):
            alignment_class = alignments[cell_index] if cell_index < len(alignments) else "align-left"
            table_html_tokens.append(
                f'<td class="{alignment_class}">{convert_inline_markup(body_cell)}</td>'
            )

        table_html_tokens.append("</tr>")

    table_html_tokens.extend(["</tbody>", "</table>", "</div>"])

    return "".join(table_html_tokens), current_index


def render_list(markdown_lines: Sequence[str], start_index: int, base_indentation: int) -> tuple[str, int]:
    """Render a Markdown list block, including nested lists."""

    _, current_list_tag, _ = get_list_item_metadata(markdown_lines[start_index])
    current_index = start_index
    list_item_html_tokens: list[str] = []

    while current_index < len(markdown_lines):
        current_line = markdown_lines[current_index]

        if not current_line.strip():
            current_index += 1
            continue

        if not is_list_item(current_line):
            break

        indentation_width, list_tag, item_content = get_list_item_metadata(current_line)

        if indentation_width < base_indentation or list_tag != current_list_tag:
            break

        if indentation_width > base_indentation:
            nested_list_html, current_index = render_list(
                markdown_lines=markdown_lines,
                start_index=current_index,
                base_indentation=indentation_width,
            )

            if list_item_html_tokens:
                list_item_html_tokens[-1] = list_item_html_tokens[-1].replace(
                    "</li>",
                    f'{nested_list_html}</li>',
                    1,
                )

            continue

        current_index += 1
        continuation_lines: list[str] = []
        nested_html_tokens: list[str] = []

        while current_index < len(markdown_lines):
            lookahead_line = markdown_lines[current_index]

            if not lookahead_line.strip():
                current_index += 1
                continue

            if is_heading(lookahead_line) or is_table_row(lookahead_line):
                break

            if is_list_item(lookahead_line):
                next_indentation_width, _, _ = get_list_item_metadata(lookahead_line)

                if next_indentation_width <= base_indentation:
                    break

                nested_list_html, current_index = render_list(
                    markdown_lines=markdown_lines,
                    start_index=current_index,
                    base_indentation=next_indentation_width,
                )
                nested_html_tokens.append(nested_list_html)
                continue

            stripped_lookahead_line = lookahead_line.strip()
            continuation_lines.append(stripped_lookahead_line)
            current_index += 1

        item_body_html = convert_inline_markup(item_content)

        if continuation_lines:
            continuation_text = " ".join(continuation_lines)
            item_body_html += f'<p class="list-continuation">{convert_inline_markup(continuation_text)}</p>'

        list_item_html_tokens.append(
            f'<li><div class="li-body">{item_body_html}</div>{"".join(nested_html_tokens)}</li>'
        )

    return f'<{current_list_tag} class="report-list">{"".join(list_item_html_tokens)}</{current_list_tag}>', current_index


def render_paragraph(paragraph_lines: Sequence[str]) -> str:
    """Render paragraph block."""

    paragraph_text = " ".join(markdown_line.strip() for markdown_line in paragraph_lines).strip()
    normalized_word_count = len(paragraph_text.rstrip(":").split())

    if paragraph_text.endswith(":") and normalized_word_count <= 6:
        label_text = convert_inline_markup(paragraph_text[:-1])

        return f'<p class="block-label">{label_text}</p>'

    return f'<p>{convert_inline_markup(paragraph_text)}</p>'


def render_markdown_body(markdown_text: str) -> tuple[str, str]:
    """Render the Markdown body to styled HTML."""

    markdown_lines = markdown_text.splitlines()

    if not markdown_lines or not markdown_lines[0].startswith("# "):
        raise ValueError("Expected the report Markdown to start with one H1 heading.")

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
        nonlocal paragraph_lines

        if paragraph_lines:
            target_token_list = current_subsection_body_tokens if current_subsection_title else current_section_body_tokens
            target_token_list.append(render_paragraph(paragraph_lines))
            paragraph_lines = []

    def flush_subsection() -> None:
        nonlocal current_subsection_title, current_subsection_body_tokens

        flush_paragraph()

        if not current_subsection_title:
            return

        if current_subsection_body_tokens:
            subsection_title_html = convert_inline_markup(current_subsection_title)
            current_section_body_tokens.append(
                f'<div class="subsection-block"><h3>{subsection_title_html}</h3>{"".join(current_subsection_body_tokens)}</div>'
            )

        current_subsection_title = ""
        current_subsection_body_tokens = []

    def flush_section() -> None:
        nonlocal current_section_title, current_section_slug, current_section_body_tokens

        flush_subsection()

        if current_section_title and current_section_body_tokens:
            section_title_html = convert_inline_markup(current_section_title)
            document_html_tokens.append(
                f'<section class="section-card section-{current_section_slug}"><h2>{section_title_html}</h2>{"".join(current_section_body_tokens)}</section>'
            )

        current_section_title = ""
        current_section_slug = ""
        current_section_body_tokens = []

    while current_index < len(body_lines):
        current_line = body_lines[current_index].rstrip()
        stripped_line = current_line.strip()

        if not stripped_line:
            flush_paragraph()
            current_index += 1
            continue

        if current_line.startswith("## "):
            flush_section()
            current_section_title = current_line[3:].strip()
            current_section_slug = slugify(current_section_title)
            current_index += 1
            continue

        if current_line.startswith("### "):
            flush_subsection()
            current_subsection_title = current_line[4:].strip()
            current_index += 1
            continue

        if is_table_row(current_line):
            flush_paragraph()
            table_html, current_index = render_table(body_lines, current_index)
            target_token_list = current_subsection_body_tokens if current_subsection_title else current_section_body_tokens
            target_token_list.append(table_html)
            continue

        if is_list_item(current_line):
            flush_paragraph()
            indentation_width, _, _ = get_list_item_metadata(current_line)
            list_html, current_index = render_list(body_lines, current_index, indentation_width)
            target_token_list = current_subsection_body_tokens if current_subsection_title else current_section_body_tokens
            target_token_list.append(list_html)
            continue

        paragraph_lines.append(current_line)
        current_index += 1

    flush_section()

    return report_title, "\n".join(document_html_tokens)


def build_html_document(
    report_title: str,
    report_subtitle: str,
    report_category: str,
    body_html: str,
) -> str:
    """Build full styled HTML document."""

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
    @page {{
      size: A4;
      margin: 13mm 10mm 15mm 10mm;
    }}

    * {{
      box-sizing: border-box;
    }}

    html {{
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
      background: #ffffff;
    }}

    body {{
      margin: 0;
      font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
      color: #16193B;
      background: #ffffff;
      line-height: 1.48;
      font-size: 9.35pt;
    }}

    .page-shell {{
      width: 100%;
    }}

    .hero {{
      padding: 16px 18px 15px 18px;
      border-radius: 14px;
      border: 1px solid #7FB2F0;
      background: linear-gradient(180deg, #35478C 0%, #16193B 100%);
      color: #ffffff;
      margin-bottom: 14px;
    }}

    .hero-badge {{
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
    }}

    .hero h1 {{
      margin: 0 0 5px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 19pt;
      line-height: 1.12;
      letter-spacing: -0.01em;
    }}

    .hero-subtitle {{
      margin: 0 0 8px 0;
      font-size: 9.2pt;
      color: rgba(255, 255, 255, 0.86);
    }}

    .hero-note {{
      margin: 0;
      max-width: 88%;
      font-size: 8.2pt;
      color: rgba(255, 255, 255, 0.76);
    }}

    .section-card {{
      break-inside: auto;
      margin: 0 0 10px 0;
      padding: 11px 12px 10px 12px;
      border-radius: 12px;
      border: 1px solid #ADD5F7;
      background: #ffffff;
    }}

    h2 {{
      margin: 0 0 10px 0;
      padding-bottom: 6px;
      border-bottom: 1.5px solid #7FB2F0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 13.1pt;
      line-height: 1.2;
      color: #16193B;
      break-after: avoid-page;
    }}

    h3 {{
      margin: 0 0 6px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 10.3pt;
      color: #35478C;
      break-after: avoid-page;
    }}

    p {{
      margin: 5px 0;
      orphans: 3;
      widows: 3;
    }}

    .block-label {{
      margin: 8px 0 4px 0;
      font-family: "Segoe UI Semibold", "Arial", sans-serif;
      font-size: 8pt;
      letter-spacing: 0;
      text-transform: none;
      color: #4E7AC7;
    }}

    .subsection-block {{
      break-inside: avoid-page;
      margin: 10px 0 0 0;
      padding: 9px 10px 8px 10px;
      border-radius: 10px;
      border: 1px solid rgba(173, 213, 247, 0.9);
      background: #ffffff;
    }}

    .report-list {{
      margin: 4px 0 7px 0;
      padding-left: 18px;
    }}

    .report-list li {{
      margin: 3px 0;
      padding-left: 2px;
    }}

    .report-list ul,
    .report-list ol {{
      margin-top: 4px;
      padding-left: 16px;
    }}

    .li-body {{
      display: inline;
    }}

    .list-continuation {{
      margin-top: 4px;
      margin-bottom: 0;
      color: #35478C;
    }}

    code {{
      padding: 1px 5px 2px 5px;
      border-radius: 5px;
      background: #F4F8FE;
      color: #16193B;
      font-family: "Consolas", "Cascadia Mono", "Courier New", monospace;
      font-size: 8.2pt;
      word-break: break-word;
    }}

    strong {{
      color: #16193B;
    }}

    .table-wrap {{
      margin: 9px 0 10px 0;
      overflow: hidden;
      border-radius: 10px;
      border: 1px solid #ADD5F7;
      background: #ffffff;
    }}

    .report-table {{
      width: 100%;
      table-layout: fixed;
      border-collapse: collapse;
      font-size: 7.2pt;
      line-height: 1.26;
    }}

    .report-table thead {{
      background: #35478C;
      color: #ffffff;
    }}

    .report-table th,
    .report-table td {{
      padding: 5px 5px;
      border-bottom: 1px solid #D8E8FA;
      vertical-align: top;
      overflow-wrap: anywhere;
      word-break: break-word;
      hyphens: auto;
    }}

    .report-table tbody tr:nth-child(even) {{
      background: #F7FBFF;
    }}

    .report-table th:nth-child(1), .report-table td:nth-child(1) {{ width: 8%; }}
    .report-table th:nth-child(2), .report-table td:nth-child(2) {{ width: 9%; }}
    .report-table th:nth-child(3), .report-table td:nth-child(3) {{ width: 18%; }}
    .report-table th:nth-child(4), .report-table td:nth-child(4) {{ width: 7%; }}
    .report-table th:nth-child(5), .report-table td:nth-child(5) {{ width: 7%; }}
    .report-table th:nth-child(6), .report-table td:nth-child(6) {{ width: 10%; }}
    .report-table th:nth-child(7), .report-table td:nth-child(7) {{ width: 6%; }}
    .report-table th:nth-child(8), .report-table td:nth-child(8) {{ width: 8%; }}
    .report-table th:nth-child(9), .report-table td:nth-child(9) {{ width: 15%; }}
    .report-table th:nth-child(10), .report-table td:nth-child(10) {{ width: 7%; }}
    .report-table th:nth-child(11), .report-table td:nth-child(11) {{ width: 5%; }}

    .report-table code {{
      background: rgba(173, 213, 247, 0.18);
      font-size: 7.1pt;
    }}

    .align-right {{
      text-align: right;
    }}

    .align-center {{
      text-align: center;
    }}

    .align-left {{
      text-align: left;
    }}

    .section-final-recommendation {{
      border-color: #7FB2F0;
    }}

    .section-comparing-trial-baseline-and-workstation-variants .table-wrap {{
      margin-bottom: 12px;
    }}
  </style>
</head>
<body>
  <main class="page-shell">
    <header class="hero">
      <div class="hero-badge">{escaped_category}</div>
      <h1>{escaped_title}</h1>
      <p class="hero-subtitle">{escaped_subtitle}</p>
      <p class="hero-note">Styled PDF edition generated from the canonical Markdown analysis report for improved readability, section hierarchy, and table presentation.</p>
    </header>
    {body_html}
  </main>
</body>
</html>
"""


def write_text_file(file_path: Path, file_content: str) -> None:
    """Write text file."""

    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(file_content, encoding="utf-8")


def convert_html_to_pdf(browser_executable_path: Path, html_path: Path, pdf_path: Path) -> None:
    """Convert styled HTML to PDF using headless Chrome/Edge."""

    html_uri = html_path.resolve().as_uri()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="codex_report_chrome_") as temporary_profile_path:
        subprocess.run(
            [
                str(browser_executable_path),
                "--headless",
                "--disable-gpu",
                "--disable-breakpad",
                "--disable-crash-reporter",
                f"--user-data-dir={temporary_profile_path}",
                "--allow-file-access-from-files",
                f"--print-to-pdf={pdf_path.resolve()}",
                "--no-pdf-header-footer",
                html_uri,
            ],
            check=True,
            capture_output=True,
            text=True,
        )


def main() -> None:
    """Run export pipeline."""

    argument_parser = build_argument_parser()
    parsed_arguments = argument_parser.parse_args()

    input_markdown_path = Path(parsed_arguments.input_markdown_path)
    output_html_path = Path(parsed_arguments.output_html_path)
    output_pdf_path = Path(parsed_arguments.output_pdf_path)

    markdown_text = input_markdown_path.read_text(encoding="utf-8")
    report_title, body_html = render_markdown_body(markdown_text)
    html_document = build_html_document(
        report_title=report_title,
        report_subtitle=parsed_arguments.report_subtitle,
        report_category=parsed_arguments.report_category,
        body_html=body_html,
    )

    write_text_file(output_html_path, html_document)

    browser_executable_path = detect_browser_executable(parsed_arguments.chrome_executable_path)
    convert_html_to_pdf(
        browser_executable_path=browser_executable_path,
        html_path=output_html_path,
        pdf_path=output_pdf_path,
    )

    if not parsed_arguments.keep_html and output_html_path.exists():
        output_html_path.unlink()

    print(f"Styled PDF generated at: {output_pdf_path}")


if __name__ == "__main__":
    main()
