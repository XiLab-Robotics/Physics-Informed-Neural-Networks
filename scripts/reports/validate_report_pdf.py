""" Validate Exported PDF Reports """

from __future__ import annotations

# Import Python Utilities
import argparse, shutil
from pathlib import Path

# Import PDF Utilities
try:
    import pymupdf
except ImportError as import_error:
    pymupdf = None
    PYMUPDF_IMPORT_ERROR = import_error
else:
    PYMUPDF_IMPORT_ERROR = None


# Validation Constants
DEFAULT_RENDER_SCALE = 1.8


def build_argument_parser() -> argparse.ArgumentParser:

    """ Build Argument Parser """

    # Initialize Argument Parser
    argument_parser = argparse.ArgumentParser(
        description="Rasterize the real exported PDF into validation PNG pages."
    )

    # Configure Validation Paths
    argument_parser.add_argument(
        "--input-pdf-path",
        required=True,
        help="Path to the exported PDF file that must be validated.",
    )
    argument_parser.add_argument(
        "--output-image-directory",
        required=True,
        help="Directory where the rasterized PDF pages will be written.",
    )

    # Configure Validation Rendering
    argument_parser.add_argument(
        "--render-scale",
        type=float,
        default=DEFAULT_RENDER_SCALE,
        help="Zoom multiplier used during PDF rasterization.",
    )
    argument_parser.add_argument(
        "--clean-output-directory",
        action="store_true",
        help="Delete the output image directory before writing the new validation pages.",
    )

    return argument_parser


def parse_command_line_arguments() -> argparse.Namespace:

    """ Parse Command-Line Arguments """

    # Build Argument Parser
    argument_parser = build_argument_parser()

    # Parse Command-Line Arguments
    parsed_arguments = argument_parser.parse_args()

    return parsed_arguments


def resolve_input_pdf_path(input_pdf_path: str) -> Path:

    """ Resolve Input PDF Path """

    # Resolve Input PDF Path
    resolved_input_pdf_path = Path(input_pdf_path).expanduser().resolve()

    # Validate Input PDF Path
    assert resolved_input_pdf_path.exists(), f"Input PDF Path does not exist | {resolved_input_pdf_path}"
    assert resolved_input_pdf_path.is_file(), f"Input PDF Path is not a file | {resolved_input_pdf_path}"
    assert resolved_input_pdf_path.suffix.lower() == ".pdf", f"Input file is not a PDF | {resolved_input_pdf_path}"

    return resolved_input_pdf_path


def prepare_output_image_directory(output_image_directory: str, clean_output_directory: bool) -> Path:

    """ Prepare Output Image Directory """

    # Resolve Output Image Directory
    resolved_output_image_directory = Path(output_image_directory).expanduser().resolve()

    # Reset Output Image Directory
    if clean_output_directory and resolved_output_image_directory.exists():
        shutil.rmtree(resolved_output_image_directory)

    # Create Output Image Directory
    resolved_output_image_directory.mkdir(parents=True, exist_ok=True)

    return resolved_output_image_directory


def resolve_render_scale(render_scale: float) -> float:

    """ Resolve Render Scale """

    # Validate Render Scale
    assert render_scale > 0.0, f"Render scale must be positive | {render_scale}"

    return render_scale


def ensure_pdf_renderer_is_available() -> None:

    """ Ensure PDF Renderer Is Available """

    # Validate Renderer Dependency
    if PYMUPDF_IMPORT_ERROR is not None:
        raise RuntimeError(
            "PyMuPDF is required to validate exported PDFs. "
            "Install the tracked dependencies with `python -m pip install -r requirements.txt`."
        ) from PYMUPDF_IMPORT_ERROR


def build_page_image_name(input_pdf_path: Path, page_index: int, page_count: int) -> str:

    """ Build Page Image Name """

    # Resolve Page Index Formatting
    page_index_width = max(3, len(str(page_count)))
    page_number = page_index + 1

    # Build Page Image Name
    page_image_name = f"{input_pdf_path.stem}_page_{page_number:0{page_index_width}d}.png"

    return page_image_name


def rasterize_pdf_pages(
    input_pdf_path: Path,
    output_image_directory: Path,
    render_scale: float,
) -> list[Path]:

    """ Rasterize PDF Pages """

    # Open Exported PDF
    pdf_document = pymupdf.open(input_pdf_path)
    assert pdf_document.page_count > 0, f"PDF contains no pages | {input_pdf_path}"

    # Configure Raster Export
    rendered_image_path_list: list[Path] = []
    render_matrix = pymupdf.Matrix(render_scale, render_scale)

    try:

        # Rasterize Each PDF Page
        for page_index in range(pdf_document.page_count):
            page = pdf_document.load_page(page_index)
            page_pixmap = page.get_pixmap(matrix=render_matrix, alpha=False)

            page_image_name = build_page_image_name(
                input_pdf_path=input_pdf_path,
                page_index=page_index,
                page_count=pdf_document.page_count,
            )
            page_image_path = output_image_directory / page_image_name
            page_pixmap.save(page_image_path)

            rendered_image_path_list.append(page_image_path)

    finally:

        # Close PDF Document
        pdf_document.close()

    return rendered_image_path_list


def print_validation_summary(
    input_pdf_path: Path,
    output_image_directory: Path,
    render_scale: float,
    rendered_image_path_list: list[Path],
) -> None:

    """ Print Validation Summary """

    # Print Validation Header
    print("")
    print("================================================================================================")
    print("PDF Validation Summary")
    print("================================================================================================")
    print(f"Input PDF Path                     {input_pdf_path}")
    print(f"Output Image Directory            {output_image_directory}")
    print(f"Render Scale                      {render_scale:.2f}")
    print(f"Rendered Pages                    {len(rendered_image_path_list)}")
    print("")

    # Print Validation Image List
    print("Validation Images")
    print("-----------------")

    for rendered_image_path in rendered_image_path_list:
        print(rendered_image_path)

    # Print Validation Footer
    print("")
    print("[DONE] PDF validation rasterization completed")


def main() -> None:

    """ Run PDF Validation Workflow """

    # Parse Command-Line Arguments
    parsed_arguments = parse_command_line_arguments()

    # Resolve Validation Inputs
    input_pdf_path = resolve_input_pdf_path(parsed_arguments.input_pdf_path)
    output_image_directory = prepare_output_image_directory(
        output_image_directory=parsed_arguments.output_image_directory,
        clean_output_directory=parsed_arguments.clean_output_directory,
    )
    render_scale = resolve_render_scale(parsed_arguments.render_scale)

    # Validate Renderer Dependency
    ensure_pdf_renderer_is_available()

    # Rasterize Exported PDF Pages
    rendered_image_path_list = rasterize_pdf_pages(
        input_pdf_path=input_pdf_path,
        output_image_directory=output_image_directory,
        render_scale=render_scale,
    )

    # Print Validation Summary
    print_validation_summary(
        input_pdf_path=input_pdf_path,
        output_image_directory=output_image_directory,
        render_scale=render_scale,
        rendered_image_path_list=rendered_image_path_list,
    )


if __name__ == "__main__":

    main()
