""" Generate Model Report Diagrams """

from __future__ import annotations

# Import Python Utilities
import math
from dataclasses import dataclass
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parents[2]
OUTPUT_DIRECTORY = PROJECT_PATH / "doc" / "reports" / "analysis" / "assets" / "2026-03-18_model_explanatory_diagrams"

SVG_WIDTH = 1280
SVG_HEIGHT = 720

CANVAS_COLOR = "#FFFFFF"
HEADER_START_COLOR = "#35478C"
HEADER_END_COLOR = "#16193B"
CARD_BACKGROUND = "#FFFFFF"
CARD_BORDER = "#ADD5F7"
ACCENT_BORDER = "#7FB2F0"
TEXT_COLOR = "#16193B"
SECONDARY_TEXT_COLOR = "#31466E"
NOTE_TEXT_COLOR = "#4E7AC7"
ARROW_COLOR = "#4E7AC7"
SOFT_ARROW_COLOR = "#C8DCF8"
ROW_BACKGROUND = "#F7FBFF"

CARD_RADIUS = 18
CARD_HEADER_HEIGHT = 46
CARD_PADDING_X = 24
CARD_PADDING_Y = 16
CARD_LINE_HEIGHT = 20
NOTE_LINE_HEIGHT = 18
CARD_NOTE_GAP = 12
HEADER_Y = 26
HEADER_HEIGHT = 92
HEADER_BOTTOM = HEADER_Y + HEADER_HEIGHT
CONTENT_REGION_TOP = HEADER_BOTTOM + 28
CONTENT_REGION_BOTTOM = SVG_HEIGHT - 34


@dataclass(frozen=True)
class TextLine:

    """ Text Line """

    text: str
    css_class: str = "card-text"
    font_size: float | None = None
    extra_gap_after: float = 0.0


def escape_xml(raw_text: str) -> str:

    """ Escape XML """

    # Escape Reserved XML Characters
    return (
        raw_text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def build_svg_document(title: str, description: str, body_content: str) -> str:

    """ Build SVG Document """

    # Build Full SVG Document
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{SVG_WIDTH}" height="{SVG_HEIGHT}" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">{escape_xml(title)}</title>
  <desc id="desc">{escape_xml(description)}</desc>
  <defs>
    <linearGradient id="canvas_header" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{HEADER_START_COLOR}"/>
      <stop offset="100%" stop-color="{HEADER_END_COLOR}"/>
    </linearGradient>
    <linearGradient id="card_header" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F6FAFF"/>
      <stop offset="100%" stop-color="#EEF5FF"/>
    </linearGradient>
    <marker id="arrow_head" markerWidth="11" markerHeight="11" refX="9.4" refY="5.5" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L11,5.5 L0,11 Z" fill="{ARROW_COLOR}"/>
    </marker>
    <style>
      .canvas-title {{ font: 700 32px 'Segoe UI', Arial, sans-serif; fill: #ffffff; }}
      .canvas-subtitle {{ font: 500 18px 'Segoe UI', Arial, sans-serif; fill: #dfeaff; }}
      .card-title {{ font: 700 18px 'Segoe UI', Arial, sans-serif; fill: {TEXT_COLOR}; }}
      .card-text {{ font: 500 15px 'Segoe UI', Arial, sans-serif; fill: {SECONDARY_TEXT_COLOR}; }}
      .card-note {{ font: 600 14px 'Segoe UI', Arial, sans-serif; fill: {NOTE_TEXT_COLOR}; }}
      .label {{ font: 700 16px 'Segoe UI', Arial, sans-serif; fill: {TEXT_COLOR}; }}
      .tiny {{ font: 600 14px 'Segoe UI', Arial, sans-serif; fill: {NOTE_TEXT_COLOR}; }}
      .node-label {{ font: 700 12px 'Segoe UI', Arial, sans-serif; fill: {TEXT_COLOR}; }}
      .node-small-label {{ font: 700 11px 'Segoe UI', Arial, sans-serif; fill: {TEXT_COLOR}; }}
      .flow-row-text {{ font: 600 14px 'Segoe UI', Arial, sans-serif; fill: {SECONDARY_TEXT_COLOR}; }}
    </style>
  </defs>
  <rect x="0" y="0" width="{SVG_WIDTH}" height="{SVG_HEIGHT}" rx="28" fill="{CANVAS_COLOR}"/>
{body_content}
</svg>
"""


def draw_header(title: str, subtitle: str) -> str:

    """ Draw Header """

    # Draw Canvas Header
    return (
        f'  <rect x="30" y="{HEADER_Y}" width="{SVG_WIDTH - 60}" height="{HEADER_HEIGHT}" rx="20" fill="url(#canvas_header)"/>\n'
        f'  <text x="64" y="68" class="canvas-title">{escape_xml(title)}</text>\n'
        f'  <text x="64" y="98" class="canvas-subtitle">{escape_xml(subtitle)}</text>\n'
    )


def wrap_centered_body(body_content: str, content_top: float, content_bottom: float) -> str:

    """ Wrap Centered Body """

    # Resolve Available And Current Centers
    available_center = (CONTENT_REGION_TOP + CONTENT_REGION_BOTTOM) / 2.0
    current_center = (content_top + content_bottom) / 2.0
    y_offset = available_center - current_center

    # Wrap Body In A Centered Group
    return f'  <g transform="translate(0,{y_offset:.1f})">\n{body_content}  </g>\n'


def resolve_text_anchor(align: str, x: int, width: int) -> tuple[str, int]:

    """ Resolve Text Anchor """

    # Resolve Center Alignment
    if align == "center":
        return "middle", x + width // 2

    # Resolve Left Alignment
    return "start", x + CARD_PADDING_X


def normalize_text_line_list(raw_line_list: list[str | TextLine] | None, default_css_class: str) -> list[TextLine]:

    """ Normalize Text Line List """

    if not raw_line_list:
        return []

    normalized_line_list: list[TextLine] = []

    # Normalize Mixed String And TextLine Inputs
    for raw_line in raw_line_list:
        if isinstance(raw_line, TextLine):
            normalized_line_list.append(raw_line)
            continue

        # Split Multiline Strings Explicitly
        split_line_list = str(raw_line).split("\n")
        for split_line in split_line_list:
            normalized_line_list.append(TextLine(text=split_line, css_class=default_css_class))

    return normalized_line_list


def compute_text_block_height(text_line_list: list[TextLine], default_line_height: float) -> float:

    """ Compute Text Block Height """

    if not text_line_list:
        return 0.0

    total_height = 0.0

    # Sum Per-Line Heights And Explicit Extra Gaps
    for line_index, text_line in enumerate(text_line_list):
        total_height += default_line_height
        if line_index < len(text_line_list) - 1:
            total_height += text_line.extra_gap_after

    return total_height


def draw_text_line(x: float, y: float, text_anchor: str, text_line: TextLine) -> str:

    """ Draw Text Line """

    # Build Optional Font-Size Override
    style_attribute = f' style="font-size:{text_line.font_size}px;"' if text_line.font_size is not None else ""
    return (
        f'  <text x="{x:.1f}" y="{y:.1f}" text-anchor="{text_anchor}" class="{text_line.css_class}"{style_attribute}>'
        f"{escape_xml(text_line.text)}</text>"
    )


def validate_card_content(title: str, height: int, body_line_list: list[TextLine], note_line_list: list[TextLine]) -> None:

    """ Validate Card Content """

    # Resolve Usable Content Area
    content_top = CARD_HEADER_HEIGHT + CARD_PADDING_Y
    content_bottom = height - CARD_PADDING_Y
    content_height = content_bottom - content_top

    # Resolve Required Text Height
    body_height = compute_text_block_height(body_line_list, CARD_LINE_HEIGHT)
    note_height = compute_text_block_height(note_line_list, NOTE_LINE_HEIGHT)
    note_gap = CARD_NOTE_GAP if body_line_list and note_line_list else 0.0
    required_height = body_height + note_gap + note_height

    # Validate Card Fit
    assert required_height <= content_height, f"Card content overflows | {title}"


def draw_card(
    x: int,
    y: int,
    width: int,
    height: int,
    title: str,
    lines: list[str | TextLine],
    note: str | None = "",
    accent: bool = False,
    align: str = "left",
    note_align: str | None = None,
) -> str:

    """ Draw Card """

    # Normalize Card Text Content
    body_line_list = normalize_text_line_list(lines, "card-text")
    note_line_list = normalize_text_line_list([note] if note else None, "card-note")
    validate_card_content(title, height, body_line_list, note_line_list)

    # Resolve Card Anchors
    border_color = ACCENT_BORDER if accent else CARD_BORDER
    title_anchor, title_x = resolve_text_anchor("center", x, width)
    text_anchor, text_x = resolve_text_anchor(align, x, width)
    note_anchor, note_x = resolve_text_anchor(note_align or align, x, width)

    # Resolve Card Vertical Layout
    content_top = y + CARD_HEADER_HEIGHT + CARD_PADDING_Y
    content_bottom = y + height - CARD_PADDING_Y
    content_height = content_bottom - content_top
    body_height = compute_text_block_height(body_line_list, CARD_LINE_HEIGHT)
    note_height = compute_text_block_height(note_line_list, CARD_LINE_HEIGHT)
    note_gap = CARD_NOTE_GAP if body_line_list and note_line_list else 0.0
    required_height = body_height + note_gap + note_height
    current_y = content_top + max(0.0, (content_height - required_height) / 2.0) + 14

    # Draw Card Shell
    content: list[str] = [
        f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{CARD_RADIUS}" fill="{CARD_BACKGROUND}" stroke="{border_color}" stroke-width="3"/>',
        f'  <path d="M{x + CARD_RADIUS}, {y} H{x + width - CARD_RADIUS} Q{x + width}, {y} {x + width}, {y + CARD_RADIUS} V{y + CARD_HEADER_HEIGHT} H{x} V{y + CARD_RADIUS} Q{x}, {y} {x + CARD_RADIUS}, {y} Z" fill="url(#card_header)"/>',
        f'  <line x1="{x}" y1="{y + CARD_HEADER_HEIGHT}" x2="{x + width}" y2="{y + CARD_HEADER_HEIGHT}" stroke="{border_color}" stroke-width="2"/>',
        f'  <text x="{title_x}" y="{y + 31}" text-anchor="{title_anchor}" class="card-title">{escape_xml(title)}</text>',
    ]

    # Draw Card Body Lines
    for line_index, text_line in enumerate(body_line_list):
        content.append(draw_text_line(text_x, current_y, text_anchor, text_line))
        current_y += CARD_LINE_HEIGHT
        if line_index < len(body_line_list) - 1:
            current_y += text_line.extra_gap_after

    # Draw Optional Note Lines
    if note_line_list:
        current_y += note_gap
        for note_index, note_line in enumerate(note_line_list):
            content.append(draw_text_line(note_x, current_y, note_anchor, note_line))
            current_y += NOTE_LINE_HEIGHT
            if note_index < len(note_line_list) - 1:
                current_y += note_line.extra_gap_after

    return "\n".join(content) + "\n"


def draw_flow_card(
    x: int,
    y: int,
    width: int,
    height: int,
    title: str,
    rows: list[str | TextLine],
    note: str | None = "",
    accent: bool = False,
) -> str:

    """ Draw Flow Card """

    # Normalize Flow Rows
    row_line_list = normalize_text_line_list(rows, "flow-row-text")
    note_line_list = normalize_text_line_list([note] if note else None, "card-note")

    # Resolve Flow Geometry
    row_height = 18
    flow_gap = 12
    content_height = height - CARD_HEADER_HEIGHT - (2 * CARD_PADDING_Y)
    flow_height = (len(row_line_list) * row_height) + (max(0, len(row_line_list) - 1) * flow_gap)
    note_height = compute_text_block_height(note_line_list, NOTE_LINE_HEIGHT)
    note_gap = CARD_NOTE_GAP if note_line_list else 0.0
    required_height = flow_height + note_gap + note_height
    assert required_height <= content_height, f"Flow card content overflows | {title}"

    # Draw Flow Card Shell
    border_color = ACCENT_BORDER if accent else CARD_BORDER
    content: list[str] = [
        f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{CARD_RADIUS}" fill="{CARD_BACKGROUND}" stroke="{border_color}" stroke-width="3"/>',
        f'  <path d="M{x + CARD_RADIUS}, {y} H{x + width - CARD_RADIUS} Q{x + width}, {y} {x + width}, {y + CARD_RADIUS} V{y + CARD_HEADER_HEIGHT} H{x} V{y + CARD_RADIUS} Q{x}, {y} {x + CARD_RADIUS}, {y} Z" fill="url(#card_header)"/>',
        f'  <line x1="{x}" y1="{y + CARD_HEADER_HEIGHT}" x2="{x + width}" y2="{y + CARD_HEADER_HEIGHT}" stroke="{border_color}" stroke-width="2"/>',
        f'  <text x="{x + width / 2:.1f}" y="{y + 31}" text-anchor="middle" class="card-title">{escape_xml(title)}</text>',
    ]

    # Resolve Flow Vertical Placement
    content_top = y + CARD_HEADER_HEIGHT + CARD_PADDING_Y
    current_y = content_top + max(0.0, (content_height - required_height) / 2.0)
    row_width = width - (2 * CARD_PADDING_X)

    # Draw Flow Rows And Connectors
    for row_index, text_line in enumerate(row_line_list):
        row_y = current_y
        row_center_y = row_y + (row_height / 2.0)
        content.append(
            f'  <rect x="{x + CARD_PADDING_X}" y="{row_y:.1f}" width="{row_width}" height="{row_height}" rx="12" fill="{ROW_BACKGROUND}" stroke="{border_color}" stroke-width="1.2"/>'
        )
        content.append(draw_text_line(x + width / 2.0, row_center_y + 5.0, "middle", text_line))

        # Draw Compact Vertical Connector Between Rows
        if row_index < len(row_line_list) - 1:
            arrow_start_y = row_y + row_height + 3
            arrow_end_y = row_y + row_height + flow_gap - 5
            content.append(
                f'  <line x1="{x + width / 2:.1f}" y1="{arrow_start_y:.1f}" x2="{x + width / 2:.1f}" y2="{arrow_end_y:.1f}" '
                f'stroke="{ARROW_COLOR}" stroke-width="2.2" stroke-linecap="round" marker-end="url(#arrow_head)"/>'
            )
        current_y += row_height + flow_gap

    # Draw Optional Note
    if note_line_list:
        current_y += note_gap
        for note_index, note_line in enumerate(note_line_list):
            content.append(draw_text_line(x + width / 2.0, current_y + 12.0, "middle", note_line))
            current_y += NOTE_LINE_HEIGHT
            if note_index < len(note_line_list) - 1:
                current_y += note_line.extra_gap_after

    return "\n".join(content) + "\n"


def draw_arrow(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    color: str = ARROW_COLOR,
    stroke_width: float = 3.0,
    use_arrow_head: bool = True,
) -> str:

    """ Draw Arrow """

    # Resolve Arrow Marker
    marker_suffix = ' marker-end="url(#arrow_head)"' if use_arrow_head else ""

    # Draw Straight Arrow
    return (
        f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{stroke_width}" stroke-linecap="round"{marker_suffix}/>\n'
    )


def draw_polyline_arrow(
    point_list: list[tuple[float, float]],
    *,
    color: str = ARROW_COLOR,
    stroke_width: float = 3.0,
) -> str:

    """ Draw Polyline Arrow """

    # Validate Path Geometry
    assert len(point_list) >= 2, "Polyline arrow requires at least two points"

    # Build SVG Path Commands
    point_command = " ".join(
        f"{'M' if point_index == 0 else 'L'}{point_x:.1f},{point_y:.1f}"
        for point_index, (point_x, point_y) in enumerate(point_list)
    )

    # Draw Polyline Path
    return (
        f'  <path d="{point_command}" fill="none" stroke="{color}" stroke-width="{stroke_width}" '
        f'stroke-linejoin="round" stroke-linecap="round" marker-end="url(#arrow_head)"/>\n'
    )


def compute_circle_border_point(source_x: float, source_y: float, target_x: float, target_y: float, radius: float) -> tuple[float, float]:

    """ Compute Circle Border Point """

    # Resolve Connection Vector
    delta_x = target_x - source_x
    delta_y = target_y - source_y
    distance = math.hypot(delta_x, delta_y)

    # Handle Degenerate Case
    if distance == 0:
        return source_x, source_y

    # Project Point To Circle Border
    scale = radius / distance
    return source_x + delta_x * scale, source_y + delta_y * scale


def compute_distributed_circle_anchor(
    circle_x: float,
    circle_y: float,
    circle_radius: float,
    rank_index: int,
    rank_count: int,
    side: str,
) -> tuple[float, float]:

    """ Compute Distributed Circle Anchor """

    # Resolve Base Side Angle
    if side == "left":
        base_angle = math.pi
    elif side == "right":
        base_angle = 0.0
    elif side == "top":
        base_angle = -math.pi / 2.0
    else:
        base_angle = math.pi / 2.0

    # Resolve Angular Spread
    spread = 0.92
    if rank_count <= 1:
        angle_offset = 0.0
    else:
        angle_offset = -spread / 2.0 + spread * (rank_index / (rank_count - 1))

    # Project Anchor Point On The Circle Border
    angle = base_angle + angle_offset
    return (
        circle_x + math.cos(angle) * circle_radius,
        circle_y + math.sin(angle) * circle_radius,
    )


def compute_point_fan_anchor(point_x: float, point_y: float, rank_index: int, rank_count: int, spread: float = 26.0) -> tuple[float, float]:

    """ Compute Point Fan Anchor """

    if rank_count <= 1:
        return point_x, point_y

    # Spread Anchors Vertically Around The Point
    offset = -spread / 2.0 + spread * (rank_index / (rank_count - 1))
    return point_x, point_y + offset


def draw_circle(
    x: int,
    y: int,
    radius: int,
    *,
    fill_color: str = "#F7FBFF",
    stroke_color: str = CARD_BORDER,
    label: str = "",
) -> str:

    """ Draw Circle """

    # Draw Circle Shell
    content = [
        f'  <circle cx="{x}" cy="{y}" r="{radius}" fill="{fill_color}" stroke="{stroke_color}" stroke-width="2"/>'
    ]

    # Draw Optional Node Label
    if label:
        label_class = "node-small-label" if len(label) >= 3 else "node-label"
        content.append(f'  <text x="{x}" y="{y + 4}" text-anchor="middle" class="{label_class}">{escape_xml(label)}</text>')

    return "\n".join(content) + "\n"


def draw_dense_connections(
    source_coordinates: list[tuple[int, int]],
    target_coordinates: list[tuple[int, int]],
    *,
    source_radius: int,
    target_radius: int,
    color: str = SOFT_ARROW_COLOR,
    stroke_width: float = 1.4,
) -> str:

    """ Draw Dense Connections """

    if not source_coordinates or not target_coordinates:
        return ""

    content: list[str] = []

    # Resolve Per-Target Source Order For Fan-In Distribution
    target_order_dictionary: dict[tuple[int, int], int] = {}
    for target_index, _ in enumerate(target_coordinates):
        ordered_source_indices = sorted(range(len(source_coordinates)), key=lambda source_index: source_coordinates[source_index][1])
        for rank_index, source_index in enumerate(ordered_source_indices):
            target_order_dictionary[(source_index, target_index)] = rank_index

    # Resolve Per-Source Target Order For Fan-Out Distribution
    source_order_dictionary: dict[tuple[int, int], int] = {}
    for source_index, _ in enumerate(source_coordinates):
        ordered_target_indices = sorted(range(len(target_coordinates)), key=lambda target_index: target_coordinates[target_index][1])
        for rank_index, target_index in enumerate(ordered_target_indices):
            source_order_dictionary[(source_index, target_index)] = rank_index

    # Draw Pairwise Connections With Distributed Border Anchors
    for source_index, (source_x, source_y) in enumerate(source_coordinates):
        for target_index, (target_x, target_y) in enumerate(target_coordinates):
            source_side = "right" if target_x >= source_x else "left"
            target_side = "left" if source_x <= target_x else "right"
            source_rank = source_order_dictionary[(source_index, target_index)]
            target_rank = target_order_dictionary[(source_index, target_index)]

            # Resolve Start Anchor
            if source_radius > 0:
                start_x, start_y = compute_distributed_circle_anchor(
                    source_x,
                    source_y,
                    source_radius,
                    source_rank,
                    len(target_coordinates),
                    source_side,
                )
            else:
                start_x, start_y = compute_point_fan_anchor(source_x, source_y, source_rank, len(target_coordinates))

            # Resolve End Anchor
            if target_radius > 0:
                end_x, end_y = compute_distributed_circle_anchor(
                    target_x,
                    target_y,
                    target_radius,
                    target_rank,
                    len(source_coordinates),
                    target_side,
                )
            else:
                end_x, end_y = compute_point_fan_anchor(target_x, target_y, target_rank, len(source_coordinates))

            content.append(
                f'  <line x1="{start_x:.1f}" y1="{start_y:.1f}" x2="{end_x:.1f}" y2="{end_y:.1f}" '
                f'stroke="{color}" stroke-width="{stroke_width}" stroke-linecap="round" marker-end="url(#arrow_head)"/>'
            )

    return "\n".join(content) + ("\n" if content else "")


def draw_layer_block(
    x_positions: list[int],
    layer_nodes: list[list[str]],
    *,
    base_y: int,
    layer_gap: int,
    radius: int,
) -> tuple[str, list[list[tuple[int, int]]]]:

    """ Draw Layer Block """

    # Validate Layer Geometry
    assert len(x_positions) == len(layer_nodes), "x_positions and layer_nodes must have the same length"

    content: list[str] = []
    layer_centers: list[list[tuple[int, int]]] = []

    # Draw Each Layer
    for layer_index, node_label_list in enumerate(layer_nodes):
        x_position = x_positions[layer_index]
        first_y = base_y - ((len(node_label_list) - 1) * layer_gap) // 2
        current_layer_centers: list[tuple[int, int]] = []

        # Draw Layer Nodes
        for node_index, node_label in enumerate(node_label_list):
            current_y = first_y + node_index * layer_gap
            current_layer_centers.append((x_position, current_y))
            content.append(draw_circle(x_position, current_y, radius, label=node_label).rstrip())

        layer_centers.append(current_layer_centers)

    # Draw Inter-Layer Connectivity
    for layer_index in range(len(layer_centers) - 1):
        content.append(
            draw_dense_connections(
                layer_centers[layer_index],
                layer_centers[layer_index + 1],
                source_radius=radius,
                target_radius=radius,
            ).rstrip()
        )

    return "\n".join(content) + "\n", layer_centers


def write_svg(output_name: str, title: str, description: str, body_content: str) -> None:

    """ Write SVG """

    # Ensure Output Directory Exists
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)

    # Write SVG File
    output_path = OUTPUT_DIRECTORY / output_name
    output_path.write_text(build_svg_document(title, description, body_content), encoding="utf-8")


def build_feedforward_conceptual_diagram() -> str:

    """ Build Feedforward Conceptual Diagram """

    # Draw Header
    content = draw_header("Feedforward TE Baseline", "Generic point-wise nonlinear regressor without explicit periodic decomposition")

    # Draw Conceptual Body
    body = ""
    body += draw_card(74, 182, 214, 196, "Input Point", ["Angle sample", "Speed and torque", "Temperature", "Direction"], note="Five operating features")
    body += draw_card(346, 182, 214, 196, "Normalization", ["Input scaling", "Target scaling", "Train-set mean and std"], note="Shared preprocessing")
    body += draw_flow_card(
        618,
        164,
        304,
        232,
        "Feedforward Network",
        ["Linear block", "Optional layer norm", "Activation and dropout", "Scalar output head"],
        note="Learns TE structure implicitly",
        accent=True,
    )
    body += draw_card(980, 182, 226, 196, "Prediction", ["Normalized TE", "Denormalized scalar TE", "MAE and RMSE logging"], note="Single-point inference")

    # Draw Main Flow Arrows
    body += draw_arrow(288, 280, 346, 280)
    body += draw_arrow(560, 280, 618, 280)
    body += draw_arrow(922, 280, 980, 280)

    # Draw Interpretation Card
    body += draw_card(
        112,
        458,
        1056,
        106,
        "Reading Key",
        ["Best used as a neutral nonlinear baseline before adding explicit periodic or physics-aware structure."],
        align="center",
    )

    return content + wrap_centered_body(body, 164, 564)


def build_feedforward_architecture_diagram() -> str:

    """ Build Feedforward Architecture Diagram """

    # Draw Header
    content = draw_header("Feedforward Network Structure", "Dense point-wise network with explicit neuron connectivity")

    # Draw Architecture Body
    body = ""
    body += draw_card(
        56,
        162,
        206,
        394,
        "Inputs",
        [
            TextLine("Angle", extra_gap_after=2.0),
            TextLine("Speed", extra_gap_after=2.0),
            TextLine("Torque", extra_gap_after=2.0),
            TextLine("Temperature", extra_gap_after=2.0),
            TextLine("Direction"),
        ],
        note="Five normalized scalar\nfeatures",
        align="center",
        note_align="center",
    )
    body += draw_card(1036, 286, 160, 128, "Output", ["Transmission\nerror"], align="center")
    body += '  <text x="300" y="164" class="label">Example hidden layout: 5 to 4 to 4 to 3 to 1</text>\n'
    body += '  <text x="300" y="188" class="tiny">The actual hidden width is configured by the training YAML.</text>\n'

    # Draw Dense Layer Stack
    layer_block_svg, layer_centers = draw_layer_block(
        [324, 508, 692, 876],
        [
            ["a", "s", "q", "t", "d"],
            ["h1", "h2", "h3", "h4"],
            ["h1", "h2", "h3", "h4"],
            ["h1", "h2", "h3"],
        ],
        base_y=360,
        layer_gap=74,
        radius=17,
    )
    body += layer_block_svg

    # Draw Input And Output Routing
    body += draw_arrow(262, 360, 300, 360)
    for output_index, (source_x, source_y) in enumerate(layer_centers[-1]):
        target_y = 324 + output_index * 26
        body += draw_arrow(source_x + 17, source_y, 1036, target_y, color="#BFD8FA", stroke_width=1.8)

    return content + wrap_centered_body(body, 162, 556)


def build_harmonic_conceptual_diagram() -> str:

    """ Build Harmonic Conceptual Diagram """

    # Draw Header
    content = draw_header("Harmonic Regression", "Explicit periodic model with a truncated harmonic series")

    # Draw Conceptual Body
    body = ""
    body += draw_card(
        64,
        186,
        220,
        194,
        "Raw Angle",
        ["Angle sample", "Degree-to-radian", "conversion", "Periodic meaning preserved"],
        note="Phase stays explicit",
    )
    body += draw_flow_card(
        334,
        158,
        286,
        248,
        "Harmonic Basis",
        ["Constant term", "Sine channels", "Cosine channels", "Truncated at order K"],
        note="Periodic bias is explicit",
        accent=True,
    )
    body += draw_flow_card(
        680,
        158,
        286,
        248,
        "Coefficient Resolver",
        ["Static coefficients", "Optional linear conditioning", "Operating-state shift"],
        note="Interpretable coefficient space",
    )
    body += draw_card(1024, 186, 194, 194, "Prediction", ["Basis-weight product", "Term summation", "Scalar TE output"], note="Compact periodic estimator")

    # Draw Main Flow Arrows
    body += draw_arrow(284, 282, 334, 282)
    body += draw_arrow(620, 282, 680, 282)
    body += draw_arrow(966, 282, 1024, 282)

    # Draw Interpretation Card
    body += draw_card(
        118,
        462,
        1044,
        106,
        "Interpretation",
        ["Each coefficient directly maps to a harmonic contribution, which keeps the model compact and inspectable."],
        align="center",
    )

    return content + wrap_centered_body(body, 158, 568)


def build_harmonic_architecture_diagram() -> str:

    """ Build Harmonic Architecture Diagram """

    # Draw Header
    content = draw_header("Harmonic Computational Structure", "Basis generation, coefficient resolution, term-wise multiplication, and final summation")

    # Draw Main Computational Blocks
    body = ""
    body += draw_card(54, 258, 180, 124, "Angle Input", ["Theta"], align="center")
    body += draw_card(
        274,
        140,
        234,
        328,
        "Basis Features",
        ["Constant term", "sin(theta)", "cos(theta)", "sin(2 theta)", "cos(2 theta)", "... up to order K"],
        note="Structured periodic basis",
        accent=True,
        align="center",
        note_align="center",
    )
    body += draw_card(
        552,
        140,
        234,
        328,
        "Coefficient Vector",
        ["c0", "a1 and b1", "a2 and b2", "Higher-order pairs", "Optional conditioned shift"],
        note="Static or operating-state\nconditioned",
        align="center",
        note_align="center",
    )
    body += draw_card(836, 258, 168, 124, "Multiply", ["Term-wise\nproduct"], align="center")
    body += draw_card(1052, 258, 156, 124, "Sum", ["Transmission\nerror"], align="center")

    # Draw Main Computational Flow
    body += draw_arrow(234, 320, 274, 320)
    body += draw_arrow(508, 320, 552, 320)
    body += draw_arrow(786, 320, 836, 320)
    body += draw_arrow(1004, 320, 1052, 320)

    # Draw Conditioning Branch
    body += draw_flow_card(
        548,
        500,
        300,
        144,
        "Conditioning Path",
        ["Speed, torque, temp, dir", "Linear shift in coefficient space"],
    )
    body += draw_arrow(698, 500, 698, 468, stroke_width=2.8)

    return content + wrap_centered_body(body, 140, 644)


def build_periodic_conceptual_diagram() -> str:

    """ Build Periodic Conceptual Diagram """

    # Draw Header
    content = draw_header("Periodic Feature Network", "Handcrafted periodic encoding followed by nonlinear dense regression")

    # Draw Conceptual Body
    body = ""
    body += draw_card(58, 188, 204, 190, "Raw Angle", ["Angle sample", "Used to build", "periodic channels"], note="Angle drives expansion")
    body += draw_flow_card(
        316,
        156,
        292,
        252,
        "Periodic Feature Builder",
        ["sin(theta) and cos(theta)", "Higher-order channels", "Optional raw normalized angle"],
        note="Periodic prior enters as features",
        accent=True,
    )
    body += draw_card(670, 188, 224, 190, "Concatenation", ["Periodic channels", "Operating-state features", "One expanded vector"], note="Structured plus generic inputs")
    body += draw_flow_card(
        952,
        156,
        264,
        252,
        "Feedforward Backbone",
        ["Dense nonlinear mixing", "Interaction learning", "Scalar TE head"],
        note="Flexible regressor on structured inputs",
    )

    # Draw Main Flow Arrows
    body += draw_arrow(262, 282, 316, 282)
    body += draw_arrow(608, 282, 670, 282)
    body += draw_arrow(894, 282, 952, 282)

    # Draw Interpretation Card
    body += draw_card(
        114,
        464,
        1048,
        106,
        "Interpretation",
        ["This model is the middle ground between pure harmonic structure and a completely generic feedforward MLP."],
        align="center",
    )

    return content + wrap_centered_body(body, 156, 570)


def build_periodic_architecture_diagram() -> str:

    """ Build Periodic Architecture Diagram """

    # Draw Header
    content = draw_header("Periodic Feature Network Structure", "Feature-expansion front end plus dense neural backbone")

    # Draw Static Architecture Blocks
    body = ""
    body += draw_card(52, 272, 164, 116, "Angle", ["Theta"], align="center")
    body += draw_card(
        254,
        142,
        252,
        332,
        "Feature Expansion",
        ["sin(theta)", "cos(theta)", "sin(2 theta)", "cos(2 theta)", "Higher-order channels", "Optional raw angle"],
        note="2K or 2K + 1 periodic\nchannels",
        accent=True,
        align="center",
        note_align="center",
    )
    body += draw_card(
        548,
        326,
        198,
        198,
        "Conditions",
        ["Speed", "Torque", "Temperature", "Direction"],
        note="Normalized inputs",
        align="center",
        note_align="center",
    )
    body += draw_card(790, 266, 176, 128, "Concat", ["Expanded feature\nvector"], align="center")

    # Draw Neural Backbone
    layer_block_svg, _ = draw_layer_block(
        [1020, 1130, 1230],
        [["h1", "h2", "h3", "h4"], ["h1", "h2", "h3"], ["TE"]],
        base_y=332,
        layer_gap=66,
        radius=15,
    )
    body += layer_block_svg

    # Draw Routed Input Flow
    body += draw_arrow(216, 330, 254, 330)
    body += draw_polyline_arrow([(506, 266), (676, 266), (676, 214), (790, 214), (790, 304)], stroke_width=2.8)
    body += draw_arrow(746, 424, 790, 356, stroke_width=2.8)
    body += draw_arrow(966, 332, 1005, 332)
    body += '  <text x="286" y="556" class="tiny">Periodic structure is handcrafted in front. Nonlinear interaction learning happens in the MLP.</text>\n'

    return content + wrap_centered_body(body, 142, 556)


def build_residual_conceptual_diagram() -> str:

    """ Build Residual Conceptual Diagram """

    # Draw Header
    content = draw_header("Residual Harmonic Network", "Structured harmonic branch plus neural residual correction")

    # Draw Branch Blocks
    body = ""
    body += draw_card(60, 242, 220, 170, "Shared Input", ["Angle sample", "Normalized operating state", "Common input to both branches"], note="One point feeds both paths")
    body += draw_flow_card(
        352,
        162,
        264,
        196,
        "Structured Branch",
        ["Harmonic basis", "Coefficient resolution", "Structured TE prediction"],
        note="Can be frozen or joint-trained",
        accent=True,
    )
    body += draw_flow_card(
        352,
        404,
        264,
        168,
        "Residual Branch",
        ["Dense residual MLP", "Learns remaining error"],
        note="Only models the remaining error",
    )
    body += draw_card(716, 266, 150, 104, "Add", ["H plus R"], align="center")
    body += draw_card(
        952,
        190,
        222,
        252,
        "Outputs",
        ["Structured prediction", "Residual prediction", "Total prediction", "Structured diagnostics"],
        note="Useful for branch-level analysis",
    )

    # Draw Branch Routing
    body += draw_polyline_arrow([(280, 296), (316, 296), (316, 260), (352, 260)], stroke_width=2.8)
    body += draw_polyline_arrow([(280, 350), (316, 350), (316, 488), (352, 488)], stroke_width=2.8)
    body += draw_arrow(616, 260, 716, 298)
    body += draw_arrow(616, 488, 716, 338)
    body += draw_arrow(866, 318, 952, 318)

    # Draw Interpretation Card
    body += draw_card(
        112,
        588,
        1012,
        106,
        "Interpretation",
        ["The network keeps the interpretable periodic backbone and learns only the unexplained residual component."],
        align="center",
    )

    return content + wrap_centered_body(body, 162, 694)


def build_residual_architecture_diagram() -> str:

    """ Build Residual Architecture Diagram """

    # Draw Header
    content = draw_header("Residual Harmonic Network Structure", "Structured harmonic path, residual MLP path, and explicit additive merge")

    # Draw Static Branch Blocks
    body = ""
    body += draw_card(46, 286, 190, 118, "Shared Input", ["Angle and conditions"], align="center")
    body += draw_flow_card(
        302,
        174,
        226,
        188,
        "Structured Path",
        ["Harmonic basis", "Coefficient resolver", "Structured output H"],
        accent=True,
    )
    body += draw_flow_card(
        302,
        414,
        226,
        188,
        "Residual Path",
        ["Normalized input", "Dense residual MLP", "Residual output R"],
    )

    # Draw Input Routing
    body += draw_polyline_arrow([(236, 322), (268, 322), (268, 268), (302, 268)], stroke_width=2.8)
    body += draw_polyline_arrow([(236, 352), (268, 352), (268, 508), (302, 508)], stroke_width=2.8)

    # Draw Residual Neural Stack
    layer_block_svg, layer_centers = draw_layer_block(
        [620, 734, 848],
        [["z1", "z2", "z3", "z4"], ["r1", "r2", "r3"], ["R"]],
        base_y=510,
        layer_gap=58,
        radius=15,
    )
    body += layer_block_svg

    # Draw Merge Blocks
    body += draw_card(620, 192, 192, 104, "Structured Output", ["H"], align="center")
    body += draw_card(946, 286, 166, 112, "Add", ["H plus R"], align="center")
    body += draw_card(1130, 286, 110, 112, "TE", ["Output"], align="center")

    # Draw Merge Routing
    body += draw_arrow(528, 268, 620, 244)
    body += draw_polyline_arrow([(812, 244), (900, 244), (900, 322), (946, 322)], stroke_width=2.8)
    residual_output_x, residual_output_y = layer_centers[-1][0]
    body += draw_polyline_arrow([(residual_output_x + 15, residual_output_y), (900, residual_output_y), (900, 360), (946, 360)], stroke_width=2.8)
    body += draw_arrow(1112, 342, 1130, 342)
    body += '  <text x="612" y="624" class="tiny">Training can log H, R, and H + R separately for diagnostics.</text>\n'

    return content + wrap_centered_body(body, 174, 624)


def generate_all_diagrams() -> None:

    """ Generate All Diagrams """

    # Generate Feedforward Diagrams
    write_svg(
        "feedforward_model_diagram.svg",
        "Feedforward TE Model Diagram",
        "Conceptual flow diagram of the feedforward transmission-error model.",
        build_feedforward_conceptual_diagram(),
    )
    write_svg(
        "feedforward_model_architecture_diagram.svg",
        "Feedforward TE Architecture Diagram",
        "Architecture-style diagram of a feedforward multilayer perceptron for transmission-error prediction.",
        build_feedforward_architecture_diagram(),
    )

    # Generate Harmonic Diagrams
    write_svg(
        "harmonic_regression_model_diagram.svg",
        "Harmonic Regression TE Model Diagram",
        "Conceptual flow diagram of the harmonic regression transmission-error model.",
        build_harmonic_conceptual_diagram(),
    )
    write_svg(
        "harmonic_regression_model_architecture_diagram.svg",
        "Harmonic Regression TE Architecture Diagram",
        "Architecture-style computational graph of the harmonic regression transmission-error model.",
        build_harmonic_architecture_diagram(),
    )

    # Generate Periodic-Feature Diagrams
    write_svg(
        "periodic_feature_network_model_diagram.svg",
        "Periodic Feature Network TE Model Diagram",
        "Conceptual flow diagram of the periodic feature network transmission-error model.",
        build_periodic_conceptual_diagram(),
    )
    write_svg(
        "periodic_feature_network_model_architecture_diagram.svg",
        "Periodic Feature Network TE Architecture Diagram",
        "Architecture-style diagram of periodic feature expansion followed by a dense neural network.",
        build_periodic_architecture_diagram(),
    )

    # Generate Residual-Harmonic Diagrams
    write_svg(
        "residual_harmonic_network_model_diagram.svg",
        "Residual Harmonic Network TE Model Diagram",
        "Conceptual flow diagram of the residual harmonic network transmission-error model.",
        build_residual_conceptual_diagram(),
    )
    write_svg(
        "residual_harmonic_network_model_architecture_diagram.svg",
        "Residual Harmonic Network TE Architecture Diagram",
        "Architecture-style diagram of the residual harmonic network with structured and residual branches.",
        build_residual_architecture_diagram(),
    )


def main() -> None:

    """ Main Function """

    # Generate All Diagram Assets
    generate_all_diagrams()

    # Print Completion Marker
    print(f"[DONE] Model report diagrams generated | {OUTPUT_DIRECTORY}")


if __name__ == "__main__":

    main()
