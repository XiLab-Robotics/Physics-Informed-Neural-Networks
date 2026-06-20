"""Replace legacy TE labels inside imported guide PDFs in place."""

from __future__ import annotations

# Import Python Utilities
import argparse
from pathlib import Path

# Import Third-Party Utilities
import fitz

# Define Project Constants
PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_PDF_PATH_LIST = (
    PROJECT_PATH
    / "doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/English"
    / "Harmonic-Wise Paper Reimplementation Pipeline - Concept Guide.pdf",
    PROJECT_PATH
    / "doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/English"
    / "Harmonic-Wise Paper Reimplementation Pipeline - Project Guide.pdf",
    PROJECT_PATH
    / "doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Italiano"
    / "Harmonic-Wise Paper Reimplementation Pipeline - Concept Guide.pdf",
    PROJECT_PATH
    / "doc/guide/Harmonic-Wise Paper Reimplementation Pipeline/Italiano"
    / "Harmonic-Wise Paper Reimplementation Pipeline - Project Guide.pdf",
)
LABEL_REPLACEMENT_LIST = (
    ("RCIM Model-Bank Reproduction", "RCIM-MBR"),
    ("TE Curve Verification Pipeline", "TE-CVP"),
    ("Track 2H-L", "Wave 4.4"),
    ("Track 2F-bis", "Wave 3.2"),
    ("Track 2B", "CVP 1.1"),
    ("Track 2C", "CVP 1.2"),
    ("Track 2D", "CVP 1.4"),
    ("Track 2E", "CVP 1.5"),
    ("Track 2F", "Wave 3.1"),
    ("Track 2G", "Wave 3.3"),
    ("Track 2H", "Wave 4 series"),
    ("Wave 2B", "Wave 2.2"),
    ("Wave 2C", "Wave 2.3"),
    ("Track 1", "RCIM-MBR"),
    ("Track 2", "TE-CVP"),
)


def _insert_fitted_text(
    page: fitz.Page,
    rectangle: fitz.Rect,
    replacement_text: str,
) -> None:
    """Insert replacement text at the largest size that fits its old rectangle."""

    expanded_rectangle = fitz.Rect(
        rectangle.x0,
        rectangle.y0 - 3.0,
        min(page.rect.x1 - 4.0, max(rectangle.x1 + 2.0, rectangle.x0 + 42.0)),
        rectangle.y1 + 3.0,
    )
    for font_size in (9.0, 8.5, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5, 5.0):
        result = page.insert_textbox(
            expanded_rectangle,
            replacement_text,
            fontname="helv",
            fontsize=font_size,
            color=(0.0, 0.0, 0.0),
            align=fitz.TEXT_ALIGN_LEFT,
            overlay=True,
        )
        if result >= 0:
            return
    raise RuntimeError(
        f"Could not fit replacement {replacement_text!r} in {expanded_rectangle}"
    )


def normalize_pdf(pdf_path: Path) -> int:
    """Normalize all legacy labels in one PDF and return the replacement count."""

    document = fitz.open(pdf_path)
    page_replacement_dictionary: dict[int, list[tuple[fitz.Rect, str]]] = {}

    for page_index, page in enumerate(document):
        replacement_list: list[tuple[fitz.Rect, str]] = []
        occupied_rectangle_list: list[fitz.Rect] = []
        for legacy_text, canonical_text in LABEL_REPLACEMENT_LIST:
            for rectangle in page.search_for(legacy_text):
                if any(rectangle.intersects(existing) for existing in occupied_rectangle_list):
                    continue
                occupied_rectangle_list.append(rectangle)
                replacement_list.append((rectangle, canonical_text))
                page.add_redact_annot(rectangle, fill=(1.0, 1.0, 1.0))
        if replacement_list:
            page_replacement_dictionary[page_index] = replacement_list

    for page_index, replacement_list in page_replacement_dictionary.items():
        page = document[page_index]
        page.apply_redactions()
        for rectangle, canonical_text in replacement_list:
            _insert_fitted_text(page, rectangle, canonical_text)

    replacement_count = sum(
        len(replacement_list)
        for replacement_list in page_replacement_dictionary.values()
    )
    temporary_path = pdf_path.with_suffix(".normalized.tmp.pdf")
    document.save(temporary_path, garbage=4, deflate=True)
    document.close()
    temporary_path.replace(pdf_path)
    return replacement_count


def _parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pdf_paths",
        nargs="*",
        type=Path,
        help="Optional explicit PDF paths. Defaults to the four imported guides.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the PDF normalization command."""

    arguments = _parse_arguments()
    pdf_path_list = arguments.pdf_paths or list(DEFAULT_PDF_PATH_LIST)
    total_replacement_count = 0
    for pdf_path in pdf_path_list:
        resolved_path = pdf_path if pdf_path.is_absolute() else PROJECT_PATH / pdf_path
        replacement_count = normalize_pdf(resolved_path)
        total_replacement_count += replacement_count
        print(f"[DONE] {resolved_path}: {replacement_count} replacements")
    print(f"[DONE] Total replacements: {total_replacement_count}")


if __name__ == "__main__":
    main()
