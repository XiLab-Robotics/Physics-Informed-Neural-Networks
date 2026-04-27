""" Run Report Pipeline """

from __future__ import annotations

# Import Python Utilities
import argparse, shutil, subprocess, sys
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parents[3]

# Report Pipeline Paths
REPORT_PIPELINE_TEMP_ROOT = PROJECT_PATH / ".temp" / "report_pipeline"
REPORT_VALIDATION_ROOT = REPORT_PIPELINE_TEMP_ROOT / "pdf_validation"
REPORT_TOOL_ENV_PATH = PROJECT_PATH / ".tools" / "report_pdf_env"
CURRENT_PYTHON_EXECUTABLE = Path(sys.executable).resolve()

# Script Paths
DIAGRAM_GENERATOR_PATH = PROJECT_PATH / "scripts" / "reports" / "analysis" / "generate_model_report_diagrams.py"
PDF_EXPORTER_PATH = PROJECT_PATH / "scripts" / "reports" / "pdf" / "generate_styled_report_pdf.py"
PDF_VALIDATOR_PATH = PROJECT_PATH / "scripts" / "reports" / "pdf" / "validate_report_pdf.py"

# Report Presets
MODEL_EXPLANATORY_REPORT_PATHS = (
    PROJECT_PATH / "doc" / "guide" / "FeedForward Network" / "FeedForward Network.md",
    PROJECT_PATH / "doc" / "guide" / "Harmonic Regression" / "Harmonic Regression.md",
    PROJECT_PATH / "doc" / "guide" / "Periodic Feature Network" / "Periodic Feature Network.md",
    PROJECT_PATH / "doc" / "guide" / "Residual Harmonic Network" / "Residual Harmonic Network.md",
)

def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    argument_parser = argparse.ArgumentParser(
        description=(
            "Run the repository-owned report pipeline: optional diagram regeneration, "
            "styled PDF export, and real PDF validation."
        )
    )

    # Configure Report Selection
    argument_parser.add_argument(
        "--input-markdown-path",
        action="append",
        default=[],
        help="Path to one Markdown report to export. Repeat the option for multiple reports.",
    )
    argument_parser.add_argument(
        "--use-model-explanatory-reports",
        action="store_true",
        help="Process the four structured-model explanatory reports tracked in the repository.",
    )

    # Configure Pipeline Stages
    argument_parser.add_argument(
        "--regenerate-diagrams",
        action="store_true",
        help="Regenerate repository-owned explanatory SVG diagrams before exporting PDFs.",
    )
    argument_parser.add_argument(
        "--skip-pdf-export",
        action="store_true",
        help="Skip styled PDF export and only run the remaining selected stages.",
    )
    argument_parser.add_argument(
        "--skip-pdf-validation",
        action="store_true",
        help="Skip PDF raster-validation after export.",
    )

    # Configure Validation Environment
    argument_parser.add_argument(
        "--validation-python-path",
        default="",
        help="Optional explicit Python executable for PDF validation.",
    )
    argument_parser.add_argument(
        "--prefer-tool-env",
        action="store_true",
        help="Prefer the repository-local report tool environment for PDF validation when available.",
    )
    argument_parser.add_argument(
        "--bootstrap-tool-env",
        action="store_true",
        help="Create or update the repository-local report tool environment with PyMuPDF before validation.",
    )

    # Configure Temporary Artifacts
    argument_parser.add_argument(
        "--clean-temp",
        action="store_true",
        help="Delete the standardized report-pipeline temporary root before the run starts.",
    )
    argument_parser.add_argument(
        "--cleanup-validation-images",
        action="store_true",
        help="Delete the generated validation PNG images after a successful validation pass.",
    )

    return argument_parser

def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    # Build And Parse CLI
    argument_parser = build_argument_parser()
    parsed_arguments = argument_parser.parse_args()
    return parsed_arguments

def resolve_markdown_path_list(input_markdown_paths: list[str], use_model_explanatory_reports: bool) -> list[Path]:

    """ Resolve Markdown Path List """

    markdown_path_list: list[Path] = []

    # Resolve Explicit Report Paths
    for input_markdown_path in input_markdown_paths:
        resolved_markdown_path = Path(input_markdown_path).expanduser().resolve()
        assert resolved_markdown_path.exists(), f"Markdown report path does not exist | {resolved_markdown_path}"
        assert resolved_markdown_path.is_file(), f"Markdown report path is not a file | {resolved_markdown_path}"
        markdown_path_list.append(resolved_markdown_path)

    # Append Repository Preset Reports
    if use_model_explanatory_reports:
        markdown_path_list.extend(report_path.resolve() for report_path in MODEL_EXPLANATORY_REPORT_PATHS)

    # Deduplicate While Preserving Order
    unique_markdown_path_list = list(dict.fromkeys(markdown_path_list))
    assert unique_markdown_path_list, "At least one report must be selected for the report pipeline."

    return unique_markdown_path_list

def resolve_pdf_output_path(markdown_path: Path) -> Path:

    """ Resolve PDF Output Path """

    # Convert Markdown Path To PDF Path
    pdf_output_path = markdown_path.with_suffix(".pdf")
    return pdf_output_path

def resolve_pipeline_html_preview_path(pdf_output_path: Path) -> Path:

    """ Resolve Pipeline HTML Preview Path """

    # Build Stable Preview Path
    html_preview_path = pdf_output_path.with_name(f"{pdf_output_path.stem}_preview.html")
    return html_preview_path

def resolve_validation_output_directory(pdf_output_path: Path) -> Path:

    """ Resolve Validation Output Directory """

    # Map PDF Name To Validation Folder
    validation_output_directory = REPORT_VALIDATION_ROOT / pdf_output_path.stem
    return validation_output_directory

def resolve_tool_env_python_path() -> Path:

    """ Resolve Tool Env Python Path """

    # Resolve Windows Tool Env Path
    if sys.platform.startswith("win"):
        return REPORT_TOOL_ENV_PATH / "Scripts" / "python.exe"

    # Resolve Unix Tool Env Path
    return REPORT_TOOL_ENV_PATH / "bin" / "python"

def remove_directory_if_present(directory_path: Path) -> None:

    """ Remove Directory If Present """

    # Remove Existing Directory
    if directory_path.exists():
        shutil.rmtree(directory_path)

def ensure_temp_root_exists() -> None:

    """ Ensure Temp Root Exists """

    # Create Standard Temp Root
    REPORT_PIPELINE_TEMP_ROOT.mkdir(parents=True, exist_ok=True)

def run_subprocess(command: list[str], description: str) -> None:

    """ Run Subprocess """

    # Print Current Step
    print(f"[RUN] {description}", flush=True)

    # Execute Command
    subprocess.run(command, check=True)

def bootstrap_tool_env(tool_env_python_path: Path) -> None:

    """ Bootstrap Tool Env """

    # Ensure Tool Env Parent Exists
    REPORT_TOOL_ENV_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Create Tool Env If Missing
    if not tool_env_python_path.exists():
        run_subprocess(
            [str(CURRENT_PYTHON_EXECUTABLE), "-m", "venv", str(REPORT_TOOL_ENV_PATH)],
            "Create report tool environment",
        )

    # Install Validation Dependency
    run_subprocess(
        [str(tool_env_python_path), "-m", "pip", "install", "pymupdf"],
        "Install PyMuPDF in report tool environment",
    )

def python_has_pdf_renderer(python_executable_path: Path) -> bool:

    """ Python Has PDF Renderer """

    # Skip Missing Interpreter
    if not python_executable_path.exists():
        return False

    try:

        # Probe Validation Dependency Availability
        subprocess.run(
            [
                str(python_executable_path),
                "-c",
                (
                    "import importlib.util; "
                    "import sys; "
                    "sys.exit(0 if (importlib.util.find_spec('pymupdf') or importlib.util.find_spec('fitz')) else 1)"
                ),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError:

        # Report Missing Renderer
        return False

    # Report Available Renderer
    return True

def resolve_validation_python_path(
    explicit_validation_python_path: str,
    prefer_tool_env: bool,
    bootstrap_requested: bool,
) -> Path:

    """ Resolve Validation Python Path """

    # Use Explicit Interpreter
    if explicit_validation_python_path:
        resolved_validation_python_path = Path(explicit_validation_python_path).expanduser().resolve()
        assert resolved_validation_python_path.exists(), f"Validation Python path does not exist | {resolved_validation_python_path}"
        return resolved_validation_python_path

    # Resolve Repository Tool Env Path
    tool_env_python_path = resolve_tool_env_python_path()

    # Bootstrap Tool Env On Demand
    if bootstrap_requested:
        bootstrap_tool_env(tool_env_python_path)
        return tool_env_python_path

    # Prefer Existing Tool Env
    if prefer_tool_env and tool_env_python_path.exists():
        return tool_env_python_path

    # Reuse Active Python When Possible
    if python_has_pdf_renderer(CURRENT_PYTHON_EXECUTABLE):
        return CURRENT_PYTHON_EXECUTABLE

    # Fall Back To Existing Tool Env
    if tool_env_python_path.exists():
        return tool_env_python_path

    # Fail When No Renderer Is Available
    raise RuntimeError(
        "No usable Python executable for PDF validation was found. "
        "Either install `pymupdf` in the active environment, "
        f"bootstrap the tool environment at `{REPORT_TOOL_ENV_PATH}`, "
        "or pass `--validation-python-path` explicitly."
    )

def regenerate_diagrams_if_requested(regenerate_diagrams: bool) -> None:

    """ Regenerate Diagrams If Requested """

    # Skip Diagram Regeneration
    if not regenerate_diagrams:
        return

    # Run Diagram Generator
    run_subprocess(
        [str(CURRENT_PYTHON_EXECUTABLE), str(DIAGRAM_GENERATOR_PATH)],
        "Regenerate explanatory diagrams",
    )

def export_pdf_if_requested(markdown_path: Path, pdf_output_path: Path, skip_pdf_export: bool) -> Path | None:

    """ Export PDF If Requested """

    # Skip PDF Export
    if skip_pdf_export:
        return None

    # Resolve Stable HTML Preview Path
    html_preview_path = resolve_pipeline_html_preview_path(pdf_output_path)

    # Run PDF Export
    run_subprocess(
        [
            str(CURRENT_PYTHON_EXECUTABLE),
            str(PDF_EXPORTER_PATH),
            "--input-markdown-path",
            str(markdown_path),
            "--output-html-path",
            str(html_preview_path),
            "--output-pdf-path",
            str(pdf_output_path),
        ],
        f"Export styled PDF | {pdf_output_path.name}",
    )

    return html_preview_path

def validate_pdf_if_requested(
    pdf_output_path: Path,
    validation_output_directory: Path,
    validation_python_path: Path,
    skip_pdf_validation: bool,
    cleanup_validation_images: bool,
) -> None:

    """ Validate PDF If Requested """

    # Skip PDF Validation
    if skip_pdf_validation:
        return

    # Run PDF Validation
    run_subprocess(
        [
            str(validation_python_path),
            str(PDF_VALIDATOR_PATH),
            "--input-pdf-path",
            str(pdf_output_path),
            "--output-image-directory",
            str(validation_output_directory),
            "--clean-output-directory",
        ],
        f"Validate exported PDF | {pdf_output_path.name}",
    )

    # Remove Validation Images On Request
    if cleanup_validation_images:
        remove_directory_if_present(validation_output_directory)

def print_pipeline_summary(markdown_path_list: list[Path], validation_python_path: Path, skip_pdf_validation: bool) -> None:

    """ Print Pipeline Summary """

    # Print Summary Header
    print("")
    print("================================================================================================")
    print("Report Pipeline Summary")
    print("================================================================================================")
    print(f"Selected Reports                    {len(markdown_path_list)}")
    print(f"Temp Root                           {REPORT_PIPELINE_TEMP_ROOT}")
    print(f"Tool Env                            {REPORT_TOOL_ENV_PATH}")
    print(f"Validation Python                   {validation_python_path if not skip_pdf_validation else 'Validation skipped'}")
    print("")

    # Print Per-Report Summary
    for markdown_path in markdown_path_list:
        pdf_output_path = resolve_pdf_output_path(markdown_path)
        validation_output_directory = resolve_validation_output_directory(pdf_output_path)
        print(f"- Markdown                          {markdown_path}")
        print(f"  PDF                               {pdf_output_path}")
        if not skip_pdf_validation:
            print(f"  Validation Images                 {validation_output_directory}")
        print("")

def main() -> None:

    """ Main Function """

    # Parse Pipeline Arguments
    parsed_arguments = parse_command_line_arguments()

    # Resolve Selected Reports
    markdown_path_list = resolve_markdown_path_list(
        parsed_arguments.input_markdown_path,
        parsed_arguments.use_model_explanatory_reports,
    )

    # Reset Temp Root On Request
    if parsed_arguments.clean_temp:
        remove_directory_if_present(REPORT_PIPELINE_TEMP_ROOT)

    # Ensure Standard Temp Layout
    ensure_temp_root_exists()

    # Resolve Validation Interpreter
    validation_python_path = CURRENT_PYTHON_EXECUTABLE
    if not parsed_arguments.skip_pdf_validation:
        validation_python_path = resolve_validation_python_path(
            parsed_arguments.validation_python_path,
            parsed_arguments.prefer_tool_env,
            parsed_arguments.bootstrap_tool_env,
        )

    # Print Planned Execution Summary
    print_pipeline_summary(
        markdown_path_list,
        validation_python_path,
        parsed_arguments.skip_pdf_validation,
    )

    # Regenerate Shared Diagrams
    regenerate_diagrams_if_requested(parsed_arguments.regenerate_diagrams)

    # Process Each Selected Report
    for markdown_path in markdown_path_list:

        # Resolve Per-Report Paths
        pdf_output_path = resolve_pdf_output_path(markdown_path)
        validation_output_directory = resolve_validation_output_directory(pdf_output_path)
        html_preview_path = None

        try:

            # Export Styled PDF
            html_preview_path = export_pdf_if_requested(
                markdown_path,
                pdf_output_path,
                parsed_arguments.skip_pdf_export,
            )

            # Validate Exported PDF
            validate_pdf_if_requested(
                pdf_output_path,
                validation_output_directory,
                validation_python_path,
                parsed_arguments.skip_pdf_validation,
                parsed_arguments.cleanup_validation_images,
            )

        finally:

            # Remove Stable HTML Preview After Pipeline Use
            if html_preview_path is not None and html_preview_path.exists():
                html_preview_path.unlink()

    # Print Final Completion Marker
    print("[DONE] Report pipeline completed")


if __name__ == "__main__":

    main()
