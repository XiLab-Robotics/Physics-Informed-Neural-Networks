""" Run Markdown Presentation Pipeline """

from __future__ import annotations

# Import Python Utilities
import argparse, shutil, subprocess, sys
from pathlib import Path

# Import PDF Utilities
try: import pymupdf
except ImportError:
    try: import fitz as pymupdf
    except ImportError as import_error: pymupdf, PYMUPDF_IMPORT_ERROR = None, import_error
    else: PYMUPDF_IMPORT_ERROR = None
else: PYMUPDF_IMPORT_ERROR = None

PROJECT_PATH = Path(__file__).resolve().parents[3]
DEFAULT_TEMPLATE_PPTX_PATH = PROJECT_PATH / "reference" / "templates" / "Template_XiLab_Research.pptx"

# Pipeline Paths
PRESENTATION_PIPELINE_TEMP_ROOT = PROJECT_PATH / ".temp" / "presentation_pipeline"
PRESENTATION_VALIDATION_ROOT = PRESENTATION_PIPELINE_TEMP_ROOT / "pdf_validation"
CURRENT_PYTHON_EXECUTABLE = Path(sys.executable).resolve()

# Script Paths
PRESENTATION_GENERATOR_PATH = PROJECT_PATH / "scripts" / "reports" / "presentation" / "generate_markdown_presentation.py"
PDF_VALIDATOR_PATH = PROJECT_PATH / "scripts" / "reports" / "pdf" / "validate_report_pdf.py"

# PowerPoint Constants
POWERPOINT_PDF_FORMAT_CODE = 32

def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    argument_parser = argparse.ArgumentParser(
        description=(
            "Run the repository-owned presentation pipeline: PPTX generation, "
            "PowerPoint PDF export, and slide-PDF validation."
        )
    )

    # Configure Presentation Selection
    argument_parser.add_argument("--input-markdown-path", required=True, help="Path to the Markdown slide-deck source.")
    argument_parser.add_argument("--output-pptx-path", default="", help="Optional explicit PPTX output path.")
    argument_parser.add_argument("--output-pdf-path", default="", help="Optional explicit slide PDF output path.")
    argument_parser.add_argument("--template-pptx-path", default="", help="Optional explicit PPTX template path.")

    # Configure Pipeline Stages
    argument_parser.add_argument("--skip-pptx-generation", action="store_true", help="Skip PPTX generation and only run later stages.")
    argument_parser.add_argument("--skip-pdf-export", action="store_true", help="Skip PowerPoint PDF export.")
    argument_parser.add_argument("--skip-pdf-validation", action="store_true", help="Skip PDF validation after export.")

    # Configure Temporary Artifacts
    argument_parser.add_argument("--clean-temp", action="store_true", help="Delete the standardized presentation-pipeline temp root before the run starts.")
    argument_parser.add_argument("--cleanup-validation-images", action="store_true", help="Delete the generated validation PNG images after a successful validation pass.")

    return argument_parser

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    argument_parser = build_argument_parser()
    parsed_arguments = argument_parser.parse_args()
    return parsed_arguments

def resolve_markdown_path(input_markdown_path: str) -> Path:

    """ Resolve Markdown Path """

    resolved_markdown_path = Path(input_markdown_path).expanduser().resolve()
    assert resolved_markdown_path.exists(), f"Presentation Markdown path does not exist | {resolved_markdown_path}"
    assert resolved_markdown_path.is_file(), f"Presentation Markdown path is not a file | {resolved_markdown_path}"
    return resolved_markdown_path

def resolve_pptx_output_path(markdown_path: Path, output_pptx_path: str) -> Path:

    """ Resolve PPTX Output Path """

    resolved_pptx_output_path = Path(output_pptx_path).expanduser().resolve() if output_pptx_path else markdown_path.with_suffix(".pptx")
    assert resolved_pptx_output_path.suffix.lower() == ".pptx", f"PPTX output path must end with .pptx | {resolved_pptx_output_path}"
    resolved_pptx_output_path.parent.mkdir(parents=True, exist_ok=True)
    return resolved_pptx_output_path

def resolve_pdf_output_path(markdown_path: Path, output_pdf_path: str) -> Path:

    """ Resolve PDF Output Path """

    resolved_pdf_output_path = Path(output_pdf_path).expanduser().resolve() if output_pdf_path else markdown_path.with_suffix(".pdf")
    assert resolved_pdf_output_path.suffix.lower() == ".pdf", f"PDF output path must end with .pdf | {resolved_pdf_output_path}"
    resolved_pdf_output_path.parent.mkdir(parents=True, exist_ok=True)
    return resolved_pdf_output_path

def resolve_template_pptx_path(template_pptx_path: str) -> Path:

    """ Resolve Template PPTX Path """

    resolved_template_pptx_path = Path(template_pptx_path).expanduser().resolve() if template_pptx_path else DEFAULT_TEMPLATE_PPTX_PATH.resolve()
    assert resolved_template_pptx_path.exists(), f"Template PPTX path does not exist | {resolved_template_pptx_path}"
    assert resolved_template_pptx_path.is_file(), f"Template PPTX path is not a file | {resolved_template_pptx_path}"
    assert resolved_template_pptx_path.suffix.lower() == ".pptx", f"Template PPTX path is not a PPTX file | {resolved_template_pptx_path}"
    return resolved_template_pptx_path

def resolve_validation_output_directory(pdf_output_path: Path) -> Path:

    """ Resolve Validation Output Directory """

    return PRESENTATION_VALIDATION_ROOT / pdf_output_path.stem

def remove_directory_if_present(directory_path: Path) -> None:

    """ Remove Directory If Present """

    if directory_path.exists():
        shutil.rmtree(directory_path)

def ensure_temp_root_exists() -> None:

    """ Ensure Temp Root Exists """

    PRESENTATION_PIPELINE_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

def run_subprocess(command: list[str], description: str) -> None:

    """ Run Subprocess """

    print(f"[RUN] {description}", flush=True)
    subprocess.run(command, check=True)

def count_markdown_slide_segments(markdown_path: Path) -> int:

    """ Count Markdown Slide Segments """

    markdown_text = markdown_path.read_text(encoding="utf-8")
    slide_segment_count = len([segment for segment in markdown_text.split("\n---") if segment.strip()])
    assert slide_segment_count > 0, f"Presentation Markdown contains no slide segments | {markdown_path}"
    return slide_segment_count

def generate_pptx(markdown_path: Path, output_pptx_path: Path, template_pptx_path: Path) -> None:

    """ Generate PPTX """

    run_subprocess(
        [
            str(CURRENT_PYTHON_EXECUTABLE),
            str(PRESENTATION_GENERATOR_PATH),
            "--input-markdown-path",
            str(markdown_path),
            "--output-pptx-path",
            str(output_pptx_path),
            "--template-pptx-path",
            str(template_pptx_path),
        ],
        "Generate PPTX from Markdown presentation source",
    )

def export_pptx_to_pdf(output_pptx_path: Path, output_pdf_path: Path) -> None:

    """ Export PPTX To PDF """

    escaped_input_path = str(output_pptx_path).replace("'", "''")
    escaped_output_path = str(output_pdf_path).replace("'", "''")

    powershell_script = (
        "$ErrorActionPreference = 'Stop'; "
        f"$inputPath = [System.IO.Path]::GetFullPath('{escaped_input_path}'); "
        f"$outputPath = [System.IO.Path]::GetFullPath('{escaped_output_path}'); "
        "$powerpoint = $null; "
        "$presentation = $null; "
        "try { "
        "$powerpoint = New-Object -ComObject PowerPoint.Application; "
        "$presentation = $powerpoint.Presentations.Open($inputPath, $true, $false, $false); "
        f"$presentation.SaveAs($outputPath, {POWERPOINT_PDF_FORMAT_CODE}); "
        "} finally { "
        "if ($presentation -ne $null) { $presentation.Close() }; "
        "if ($powerpoint -ne $null) { $powerpoint.Quit() } "
        "}"
    )

    run_subprocess(
        [
            "powershell",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            powershell_script,
        ],
        "Export PPTX to slide PDF with PowerPoint COM",
    )

def validate_pdf_renderer_is_available() -> None:

    """ Validate PDF Renderer Is Available """

    if PYMUPDF_IMPORT_ERROR is not None:
        raise RuntimeError(
            "PyMuPDF is required for slide-PDF validation. "
            "Install the tracked dependencies with `python -m pip install -r requirements.txt`."
        ) from PYMUPDF_IMPORT_ERROR

def count_pdf_pages(input_pdf_path: Path) -> int:

    """ Count PDF Pages """

    validate_pdf_renderer_is_available()

    if hasattr(pymupdf, "open"): pdf_document = pymupdf.open(input_pdf_path)
    elif hasattr(pymupdf, "Document"): pdf_document = pymupdf.Document(input_pdf_path)
    else: raise RuntimeError("PyMuPDF binding does not expose `open` or `Document`.")

    try:
        page_count = pdf_document.page_count
    finally:
        pdf_document.close()

    assert page_count > 0, f"Exported slide PDF contains no pages | {input_pdf_path}"
    return page_count

def validate_slide_count(markdown_slide_count: int, pdf_page_count: int) -> None:

    """ Validate Slide Count """

    assert markdown_slide_count == pdf_page_count, (
        "Slide-count mismatch between Markdown deck and exported PDF | "
        f"markdown_slides={markdown_slide_count} pdf_pages={pdf_page_count}"
    )

def validate_slide_pdf(output_pdf_path: Path, cleanup_validation_images: bool) -> None:

    """ Validate Slide PDF """

    validation_output_directory = resolve_validation_output_directory(output_pdf_path)

    run_subprocess(
        [
            str(CURRENT_PYTHON_EXECUTABLE),
            str(PDF_VALIDATOR_PATH),
            "--input-pdf-path",
            str(output_pdf_path),
            "--output-image-directory",
            str(validation_output_directory),
            "--clean-output-directory",
        ],
        "Raster-validate exported slide PDF",
    )

    if cleanup_validation_images:
        remove_directory_if_present(validation_output_directory)

def print_pipeline_summary(
    markdown_path: Path,
    output_pptx_path: Path,
    output_pdf_path: Path,
    template_pptx_path: Path,
    markdown_slide_count: int,
    pdf_page_count: int,
) -> None:

    """ Print Pipeline Summary """

    print("")
    print("================================================================================================")
    print("Presentation Pipeline Summary")
    print("================================================================================================")
    print(f"Input Markdown Path                {markdown_path}")
    print(f"Template PPTX Path                 {template_pptx_path}")
    print(f"Output PPTX Path                   {output_pptx_path}")
    print(f"Output PDF Path                    {output_pdf_path}")
    print(f"Markdown Slide Count               {markdown_slide_count}")
    print(f"Exported PDF Page Count            {pdf_page_count}")
    print("")
    print("[DONE] Presentation pipeline completed")

def main() -> None:

    """ Run Presentation Pipeline """

    parsed_arguments = parse_command_line_arguments()

    # Resolve Pipeline Paths
    markdown_path = resolve_markdown_path(parsed_arguments.input_markdown_path)
    output_pptx_path = resolve_pptx_output_path(markdown_path, parsed_arguments.output_pptx_path)
    output_pdf_path = resolve_pdf_output_path(markdown_path, parsed_arguments.output_pdf_path)
    template_pptx_path = resolve_template_pptx_path(parsed_arguments.template_pptx_path)

    # Prepare Temp Root
    if parsed_arguments.clean_temp:
        remove_directory_if_present(PRESENTATION_PIPELINE_TEMP_ROOT)
    ensure_temp_root_exists()

    # Run PPTX Generation
    if not parsed_arguments.skip_pptx_generation:
        generate_pptx(markdown_path, output_pptx_path, template_pptx_path)

    # Run PDF Export
    if not parsed_arguments.skip_pdf_export:
        export_pptx_to_pdf(output_pptx_path, output_pdf_path)

    # Resolve Counts
    markdown_slide_count = count_markdown_slide_segments(markdown_path)
    pdf_page_count = count_pdf_pages(output_pdf_path)
    validate_slide_count(markdown_slide_count, pdf_page_count)

    # Run PDF Validation
    if not parsed_arguments.skip_pdf_validation:
        validate_slide_pdf(output_pdf_path, parsed_arguments.cleanup_validation_images)

    # Print Summary
    print_pipeline_summary(
        markdown_path,
        output_pptx_path,
        output_pdf_path,
        template_pptx_path,
        markdown_slide_count,
        pdf_page_count,
    )

if __name__ == "__main__":

    main()
