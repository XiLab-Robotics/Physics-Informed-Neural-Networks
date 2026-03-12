"""Generate a styled HTML and PDF version of a Markdown report."""

from __future__ import annotations

import argparse
import html
import re
import subprocess

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
        return f'<p class="block-label">{convert_inline_markup(paragraph_text[:-1])}</p>'

    return f'<p>{convert_inline_markup(paragraph_text)}</p>'


def render_markdown_body(markdown_text: str) -> tuple[str, str]:
    """Render the Markdown body to styled HTML."""

    markdown_lines = markdown_text.splitlines()

    if not markdown_lines or not markdown_lines[0].startswith("# "):
        raise ValueError("Expected the report Markdown to start with one H1 heading.")

    report_title = markdown_lines[0][2:].strip()
    body_lines = markdown_lines[1:]
    current_index = 0
    body_html_tokens: list[str] = []
    paragraph_lines: list[str] = []
    current_section_open = False

    def flush_paragraph() -> None:
        nonlocal paragraph_lines

        if paragraph_lines:
            body_html_tokens.append(render_paragraph(paragraph_lines))
            paragraph_lines = []

    while current_index < len(body_lines):
        current_line = body_lines[current_index].rstrip()
        stripped_line = current_line.strip()

        if not stripped_line:
            flush_paragraph()
            current_index += 1
            continue

        if current_line.startswith("## "):
            flush_paragraph()

            if current_section_open:
                body_html_tokens.append("</section>")

            section_title = current_line[3:].strip()
            section_slug = slugify(section_title)
            body_html_tokens.append(
                f'<section class="section-card section-{section_slug}"><h2>{convert_inline_markup(section_title)}</h2>'
            )
            current_section_open = True
            current_index += 1
            continue

        if current_line.startswith("### "):
            flush_paragraph()
            subsection_title = current_line[4:].strip()
            body_html_tokens.append(f"<h3>{convert_inline_markup(subsection_title)}</h3>")
            current_index += 1
            continue

        if is_table_row(current_line):
            flush_paragraph()
            table_html, current_index = render_table(body_lines, current_index)
            body_html_tokens.append(table_html)
            continue

        if is_list_item(current_line):
            flush_paragraph()
            indentation_width, _, _ = get_list_item_metadata(current_line)
            list_html, current_index = render_list(body_lines, current_index, indentation_width)
            body_html_tokens.append(list_html)
            continue

        paragraph_lines.append(current_line)
        current_index += 1

    flush_paragraph()

    if current_section_open:
        body_html_tokens.append("</section>")

    return report_title, "\n".join(body_html_tokens)


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
      margin: 16mm 15mm 18mm 15mm;
    }}

    * {{
      box-sizing: border-box;
    }}

    html {{
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
      background: #eef2f1;
    }}

    body {{
      margin: 0;
      font-family: "Georgia", "Times New Roman", serif;
      color: #1e2a29;
      background:
        radial-gradient(circle at top left, rgba(222, 160, 87, 0.14), transparent 34%),
        linear-gradient(180deg, #f7f5ef 0%, #f2f0e8 100%);
      line-height: 1.56;
      font-size: 11pt;
    }}

    .page-shell {{
      width: 100%;
    }}

    .hero {{
      position: relative;
      overflow: hidden;
      padding: 22px 24px 20px 24px;
      border-radius: 18px;
      background:
        linear-gradient(135deg, rgba(18, 65, 67, 0.96) 0%, rgba(35, 92, 97, 0.92) 48%, rgba(165, 106, 54, 0.88) 100%);
      color: #f5efe2;
      box-shadow: 0 16px 38px rgba(37, 52, 51, 0.18);
      margin-bottom: 18px;
    }}

    .hero::after {{
      content: "";
      position: absolute;
      inset: auto -36px -30px auto;
      width: 180px;
      height: 180px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.08);
      filter: blur(1px);
    }}

    .hero-badge {{
      display: inline-block;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.18);
      font-family: "Segoe UI", "Helvetica Neue", sans-serif;
      font-size: 9pt;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 12px;
    }}

    .hero h1 {{
      margin: 0 0 8px 0;
      font-family: "Segoe UI Semibold", "Trebuchet MS", sans-serif;
      font-size: 24pt;
      line-height: 1.08;
      letter-spacing: -0.02em;
    }}

    .hero-subtitle {{
      margin: 0 0 12px 0;
      font-family: "Segoe UI", "Helvetica Neue", sans-serif;
      font-size: 11pt;
      color: rgba(255, 246, 228, 0.9);
    }}

    .hero-note {{
      margin: 0;
      max-width: 86%;
      font-family: "Segoe UI", "Helvetica Neue", sans-serif;
      font-size: 9.5pt;
      color: rgba(255, 246, 228, 0.84);
    }}

    .section-card {{
      break-inside: avoid;
      margin: 0 0 14px 0;
      padding: 14px 16px 14px 16px;
      border-radius: 16px;
      border: 1px solid rgba(30, 42, 41, 0.08);
      background: rgba(255, 255, 255, 0.76);
      box-shadow: 0 8px 22px rgba(61, 73, 73, 0.08);
    }}

    h2 {{
      margin: 0 0 12px 0;
      padding-bottom: 8px;
      border-bottom: 2px solid rgba(188, 123, 68, 0.22);
      font-family: "Segoe UI Semibold", "Trebuchet MS", sans-serif;
      font-size: 15pt;
      line-height: 1.22;
      color: #183c3d;
    }}

    h3 {{
      margin: 16px 0 8px 0;
      font-family: "Segoe UI Semibold", "Trebuchet MS", sans-serif;
      font-size: 11.6pt;
      color: #234d4d;
    }}

    p {{
      margin: 7px 0;
      orphans: 3;
      widows: 3;
    }}

    .block-label {{
      margin: 14px 0 8px 0;
      font-family: "Segoe UI Semibold", "Trebuchet MS", sans-serif;
      font-size: 9.5pt;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #9a5a25;
    }}

    .report-list {{
      margin: 8px 0 10px 0;
      padding-left: 22px;
    }}

    .report-list li {{
      margin: 5px 0;
      padding-left: 3px;
    }}

    .report-list ul,
    .report-list ol {{
      margin-top: 6px;
      padding-left: 20px;
    }}

    .li-body {{
      display: inline;
    }}

    .list-continuation {{
      margin-top: 6px;
      margin-bottom: 0;
      color: #334746;
    }}

    code {{
      padding: 1px 6px 2px 6px;
      border-radius: 6px;
      background: rgba(24, 60, 61, 0.08);
      color: #123c43;
      font-family: "Consolas", "Cascadia Mono", "Courier New", monospace;
      font-size: 9.2pt;
    }}

    strong {{
      color: #173b3d;
    }}

    .table-wrap {{
      margin: 12px 0 14px 0;
      overflow: hidden;
      border-radius: 14px;
      border: 1px solid rgba(24, 60, 61, 0.09);
      background: #fffdf8;
    }}

    .report-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 9.25pt;
    }}

    .report-table thead {{
      background: linear-gradient(180deg, #1f4c4f 0%, #2f6365 100%);
      color: #fff8ec;
    }}

    .report-table th,
    .report-table td {{
      padding: 8px 9px;
      border-bottom: 1px solid rgba(24, 60, 61, 0.09);
      vertical-align: top;
    }}

    .report-table tbody tr:nth-child(even) {{
      background: rgba(242, 235, 221, 0.42);
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
      border-color: rgba(188, 123, 68, 0.22);
      background:
        linear-gradient(180deg, rgba(255, 251, 244, 0.96) 0%, rgba(248, 243, 232, 0.92) 100%);
    }}

    .section-comparing-trial-baseline-and-workstation-variants .table-wrap {{
      box-shadow: inset 0 0 0 1px rgba(24, 60, 61, 0.04);
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

    subprocess.run(
        [
            str(browser_executable_path),
            "--headless",
            "--disable-gpu",
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
