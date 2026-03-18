""" Generate Model Report Diagrams """

from __future__ import annotations

# Import Python Utilities
import math
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
CARD_NOTE_GAP = 10
HEADER_Y = 26
HEADER_HEIGHT = 92
HEADER_BOTTOM = HEADER_Y + HEADER_HEIGHT


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
    <marker id="arrow_head" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L10,5 L0,10 Z" fill="{ARROW_COLOR}"/>
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


def resolve_text_anchor(align: str, x: int, width: int) -> tuple[str, int]:

    """ Resolve Text Anchor """

    # Resolve Center Alignment
    if align == "center":
        return "middle", x + width // 2

    # Resolve Left Alignment
    return "start", x + CARD_PADDING_X


def validate_card_content(title: str, height: int, line_count: int, note: str) -> None:

    """ Validate Card Content """

    # Resolve Usable Content Area
    content_top = CARD_HEADER_HEIGHT + CARD_PADDING_Y
    content_bottom = height - CARD_PADDING_Y
    content_height = content_bottom - content_top

    # Resolve Required Text Height
    note_height = 16 if note else 0
    note_gap = CARD_NOTE_GAP if note and line_count > 0 else 0
    lines_height = line_count * CARD_LINE_HEIGHT
    required_height = lines_height + note_gap + note_height

    # Validate Card Fit
    assert required_height <= content_height, f"Card content overflows | {title}"


def draw_card(
    x: int,
    y: int,
    width: int,
    height: int,
    title: str,
    lines: list[str],
    note: str = "",
    accent: bool = False,
    align: str = "left",
) -> str:

    """ Draw Card """

    # Validate Content Fit
    validate_card_content(title, height, len(lines), note)

    # Resolve Card Anchors
    border_color = ACCENT_BORDER if accent else CARD_BORDER
    title_anchor, title_x = resolve_text_anchor("center", x, width)
    text_anchor, text_x = resolve_text_anchor(align, x, width)

    # Resolve Card Vertical Layout
    content_top = y + CARD_HEADER_HEIGHT + CARD_PADDING_Y
    content_bottom = y + height - CARD_PADDING_Y
    content_height = content_bottom - content_top
    note_height = 16 if note else 0
    note_gap = CARD_NOTE_GAP if note and lines else 0
    lines_height = len(lines) * CARD_LINE_HEIGHT
    required_height = lines_height + note_gap + note_height
    start_y = content_top + max(0, (content_height - required_height) / 2.0) + 14

    # Draw Card Shell
    content: list[str] = [
        f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{CARD_RADIUS}" fill="{CARD_BACKGROUND}" stroke="{border_color}" stroke-width="3"/>',
        f'  <path d="M{x + CARD_RADIUS}, {y} H{x + width - CARD_RADIUS} Q{x + width}, {y} {x + width}, {y + CARD_RADIUS} V{y + CARD_HEADER_HEIGHT} H{x} V{y + CARD_RADIUS} Q{x}, {y} {x + CARD_RADIUS}, {y} Z" fill="url(#card_header)"/>',
        f'  <line x1="{x}" y1="{y + CARD_HEADER_HEIGHT}" x2="{x + width}" y2="{y + CARD_HEADER_HEIGHT}" stroke="{border_color}" stroke-width="2"/>',
        f'  <text x="{title_x}" y="{y + 31}" text-anchor="{title_anchor}" class="card-title">{escape_xml(title)}</text>',
    ]

    # Draw Card Body Lines
    current_y = start_y
    for line_text in lines:
        content.append(f'  <text x="{text_x}" y="{current_y}" text-anchor="{text_anchor}" class="card-text">{escape_xml(line_text)}</text>')
        current_y += CARD_LINE_HEIGHT

    # Draw Optional Note
    if note:
        current_y += note_gap - 6
        content.append(f'  <text x="{text_x}" y="{current_y}" text-anchor="{text_anchor}" class="card-note">{escape_xml(note)}</text>')

    return "\n".join(content) + "\n"


def draw_flow_card(
    x: int,
    y: int,
    width: int,
    height: int,
    title: str,
    rows: list[str],
    note: str = "",
    accent: bool = False,
) -> str:

    """ Draw Flow Card """

    # Resolve Flow Geometry
    row_height = 28
    flow_gap = 10
    note_height = 16 if note else 0
    note_gap = 12 if note else 0
    content_height = height - CARD_HEADER_HEIGHT - (2 * CARD_PADDING_Y)
    flow_height = (len(rows) * row_height) + (max(0, len(rows) - 1) * flow_gap)
    required_height = flow_height + note_height + note_gap
    assert required_height <= content_height, f"Flow card content overflows | {title}"

    # Draw Flow Card Shell
    border_color = ACCENT_BORDER if accent else CARD_BORDER
    content: list[str] = [
        f'  <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{CARD_RADIUS}" fill="{CARD_BACKGROUND}" stroke="{border_color}" stroke-width="3"/>',
        f'  <path d="M{x + CARD_RADIUS}, {y} H{x + width - CARD_RADIUS} Q{x + width}, {y} {x + width}, {y + CARD_RADIUS} V{y + CARD_HEADER_HEIGHT} H{x} V{y + CARD_RADIUS} Q{x}, {y} {x + CARD_RADIUS}, {y} Z" fill="url(#card_header)"/>',
        f'  <line x1="{x}" y1="{y + CARD_HEADER_HEIGHT}" x2="{x + width}" y2="{y + CARD_HEADER_HEIGHT}" stroke="{border_color}" stroke-width="2"/>',
        f'  <text x="{x + width / 2}" y="{y + 31}" text-anchor="middle" class="card-title">{escape_xml(title)}</text>',
    ]

    # Resolve Flow Layout
    content_top = y + CARD_HEADER_HEIGHT + CARD_PADDING_Y
    start_y = content_top + max(0, (content_height - required_height) / 2.0)
    row_width = width - (2 * CARD_PADDING_X)

    # Draw Flow Rows
    for row_index, row_text in enumerate(rows):
        row_y = start_y + row_index * (row_height + flow_gap)
        row_center_y = row_y + (row_height / 2.0)
        content.append(
            f'  <rect x="{x + CARD_PADDING_X}" y="{row_y}" width="{row_width}" height="{row_height}" rx="12" fill="{ROW_BACKGROUND}" stroke="{border_color}" stroke-width="1.2"/>'
        )
        content.append(
            f'  <text x="{x + width / 2}" y="{row_center_y + 5}" text-anchor="middle" class="flow-row-text">{escape_xml(row_text)}</text>'
        )

        # Draw Row Connector
        if row_index < len(rows) - 1:
            arrow_start_y = row_y + row_height
            arrow_end_y = row_y + row_height + flow_gap - 2
            content.append(
                f'  <line x1="{x + width / 2}" y1="{arrow_start_y + 2}" x2="{x + width / 2}" y2="{arrow_end_y}" '
                f'stroke="{ARROW_COLOR}" stroke-width="2.6" marker-end="url(#arrow_head)"/>'
            )

    # Draw Optional Note
    if note:
        note_y = start_y + flow_height + note_gap + 11
        content.append(f'  <text x="{x + width / 2}" y="{note_y}" text-anchor="middle" class="card-note">{escape_xml(note)}</text>')

    return "\n".join(content) + "\n"


def draw_arrow(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    color: str = ARROW_COLOR,
    stroke_width: float = 3.5,
    use_arrow_head: bool = True,
) -> str:

    """ Draw Arrow """

    # Resolve Arrow Marker
    marker_suffix = ' marker-end="url(#arrow_head)"' if use_arrow_head else ""

    # Draw Straight Arrow
    return (
        f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="{color}" stroke-width="{stroke_width}"{marker_suffix}/>\n'
    )


def draw_elbow_arrow(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    elbow_x: float,
    *,
    color: str = ARROW_COLOR,
    stroke_width: float = 3.0,
) -> str:

    """ Draw Elbow Arrow """

    # Draw Elbow Connector
    return (
        f'  <path d="M{x1:.1f},{y1:.1f} L{elbow_x:.1f},{y1:.1f} L{elbow_x:.1f},{y2:.1f} L{x2:.1f},{y2:.1f}" '
        f'fill="none" stroke="{color}" stroke-width="{stroke_width}" stroke-linejoin="round" stroke-linecap="round" '
        f'marker-end="url(#arrow_head)"/>\n'
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
    stroke_width: float = 1.5,
) -> str:

    """ Draw Dense Connections """

    content: list[str] = []

    # Draw All Pairwise Connections
    for source_x, source_y in source_coordinates:
        for target_x, target_y in target_coordinates:
            start_x, start_y = compute_circle_border_point(source_x, source_y, target_x, target_y, source_radius)
            end_x, end_y = compute_circle_border_point(target_x, target_y, source_x, source_y, target_radius)
            content.append(
                f'  <line x1="{start_x:.1f}" y1="{start_y:.1f}" x2="{end_x:.1f}" y2="{end_y:.1f}" '
                f'stroke="{color}" stroke-width="{stroke_width}" marker-end="url(#arrow_head)"/>'
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

    # Draw Header And Main Cards
    content = draw_header("Feedforward TE Baseline", "Generic point-wise nonlinear regressor without explicit periodic decomposition")
    content += draw_card(76, 184, 214, 190, "Input Point", ["Angle sample", "Speed and torque", "Temperature", "Direction"], note="Five raw operating features")
    content += draw_card(350, 184, 208, 190, "Normalization", ["Input scaling", "Target scaling", "Train-set mean and std"], note="Shared preprocessing stage")
    content += draw_flow_card(
        622,
        154,
        314,
        248,
        "FeedForward Network",
        ["Linear block", "Optional layer normalization", "Activation and dropout", "Scalar output head"],
        note="Learns TE structure implicitly",
        accent=True,
    )
    content += draw_card(996, 184, 208, 190, "Prediction", ["Normalized TE", "Denormalized scalar TE", "MAE and RMSE logging"], note="Single-point inference output")

    # Draw Main Flow Arrows
    content += draw_arrow(290, 279, 350, 279)
    content += draw_arrow(558, 279, 622, 279)
    content += draw_arrow(936, 279, 996, 279)

    # Draw Interpretation Card
    content += draw_card(
        118,
        462,
        1044,
        106,
        "Reading Key",
        ["Best used as a neutral nonlinear baseline before adding explicit periodic or physics-aware structure."],
        align="center",
    )
    return content


def build_feedforward_architecture_diagram() -> str:

    """ Build Feedforward Architecture Diagram """

    # Draw Static Layout Blocks
    content = draw_header("Feedforward Network Structure", "Dense point-wise network with explicit neuron connectivity")
    content += draw_card(58, 168, 194, 360, "Inputs", ["Angle", "Speed", "Torque", "Temperature", "Direction"], note="Five normalized scalar features", align="center")
    content += draw_card(1044, 272, 146, 132, "Output", ["Transmission error"], align="center")
    content += '  <text x="292" y="152" class="label">Example hidden layout: 5 to 4 to 4 to 3 to 1</text>\n'
    content += '  <text x="292" y="176" class="tiny">The actual hidden width is configured by the training YAML.</text>\n'

    # Draw Dense Layer Stack
    layer_block_svg, layer_centers = draw_layer_block(
        [322, 510, 698, 886],
        [
            ["a", "s", "q", "t", "d"],
            ["h1", "h2", "h3", "h4"],
            ["h1", "h2", "h3", "h4"],
            ["h1", "h2", "h3"],
        ],
        base_y=346,
        layer_gap=62,
        radius=17,
    )
    content += layer_block_svg

    # Draw Output Connectivity
    output_anchor = (1044, 338)
    last_layer = layer_centers[-1]
    content += draw_dense_connections(last_layer, [output_anchor], source_radius=17, target_radius=0, color="#BFD8FA", stroke_width=1.8)
    content += draw_arrow(252, 346, 290, 346)
    content += draw_arrow(1030, 338, 1044, 338)
    return content


def build_harmonic_conceptual_diagram() -> str:

    """ Build Harmonic Conceptual Diagram """

    # Draw Header And Main Cards
    content = draw_header("Harmonic Regression", "Explicit periodic model with a truncated harmonic series")
    content += draw_card(64, 188, 208, 188, "Raw Angle", ["Angle sample", "Degree-to-radian conversion", "Periodic interpretation preserved"], note="Phase information stays explicit")
    content += draw_flow_card(
        332,
        158,
        284,
        248,
        "Harmonic Basis",
        ["Constant term", "Sine channels", "Cosine channels", "Truncated at order K"],
        note="Periodic bias is explicit",
        accent=True,
    )
    content += draw_flow_card(
        676,
        158,
        282,
        248,
        "Coefficient Resolver",
        ["Static coefficients", "Optional linear conditioning", "Shift by operating state"],
        note="Interpretable coefficient space",
    )
    content += draw_card(1018, 188, 198, 188, "Prediction", ["Basis-weight product", "Term summation", "Scalar TE output"], note="Compact periodic estimator")

    # Draw Main Flow Arrows
    content += draw_arrow(272, 282, 332, 282)
    content += draw_arrow(616, 282, 676, 282)
    content += draw_arrow(958, 282, 1018, 282)

    # Draw Interpretation Card
    content += draw_card(
        122,
        462,
        1036,
        106,
        "Interpretation",
        ["Each coefficient directly maps to a harmonic contribution, which keeps the model compact and inspectable."],
        align="center",
    )
    return content


def build_harmonic_architecture_diagram() -> str:

    """ Build Harmonic Architecture Diagram """

    # Draw Main Computational Blocks
    content = draw_header("Harmonic Computational Structure", "Basis generation, coefficient resolution, term-wise multiplication, and final summation")
    content += draw_card(54, 246, 176, 120, "Angle Input", ["Theta"], align="center")
    content += draw_card(274, 132, 228, 320, "Basis Features", ["Constant term", "sin(theta)", "cos(theta)", "sin(2 theta)", "cos(2 theta)", "... up to order K"], note="Structured periodic basis", accent=True, align="center")
    content += draw_card(548, 132, 232, 320, "Coefficient Vector", ["c0", "a1 and b1", "a2 and b2", "Higher-order pairs", "Optional conditioned shift"], note="Static or operating-state conditioned", align="center")
    content += draw_card(830, 246, 170, 120, "Multiply", ["Term-wise product"], align="center")
    content += draw_card(1050, 246, 154, 120, "Sum", ["Transmission error"], align="center")

    # Draw Main Computational Flow
    content += draw_arrow(230, 306, 274, 306)
    content += draw_arrow(502, 306, 548, 306)
    content += draw_arrow(780, 306, 830, 306)
    content += draw_arrow(1000, 306, 1050, 306)

    # Draw Conditioning Branch
    content += draw_flow_card(
        548,
        498,
        290,
        146,
        "Conditioning Path",
        ["Speed, torque, temperature, direction", "Linear shift in coefficient space"],
    )
    content += draw_arrow(692, 498, 692, 452)
    return content


def build_periodic_conceptual_diagram() -> str:

    """ Build Periodic Conceptual Diagram """

    # Draw Header And Main Cards
    content = draw_header("Periodic Feature Network", "Handcrafted periodic encoding followed by nonlinear dense regression")
    content += draw_card(58, 188, 198, 188, "Raw Angle", ["Angle sample", "Used to build periodic channels"], note="Angle itself drives feature expansion")
    content += draw_flow_card(
        316,
        158,
        286,
        248,
        "Periodic Feature Builder",
        ["sin(theta) and cos(theta)", "Higher-order periodic channels", "Optional raw normalized angle"],
        note="Periodic prior enters as features",
        accent=True,
    )
    content += draw_card(662, 188, 220, 188, "Concatenation", ["Periodic channels", "Operating-state features", "One expanded vector"], note="Structured plus generic inputs")
    content += draw_flow_card(
        942,
        158,
        276,
        248,
        "FeedForward Backbone",
        ["Dense nonlinear mixing", "Interaction learning", "Scalar TE head"],
        note="Flexible regressor on structured inputs",
    )

    # Draw Main Flow Arrows
    content += draw_arrow(256, 282, 316, 282)
    content += draw_arrow(602, 282, 662, 282)
    content += draw_arrow(882, 282, 942, 282)

    # Draw Interpretation Card
    content += draw_card(
        114,
        462,
        1048,
        106,
        "Interpretation",
        ["This model is the middle ground between pure harmonic structure and a completely generic feedforward MLP."],
        align="center",
    )
    return content


def build_periodic_architecture_diagram() -> str:

    """ Build Periodic Architecture Diagram """

    # Draw Static Architecture Blocks
    content = draw_header("Periodic Feature Network Structure", "Feature-expansion front end plus dense neural backbone")
    content += draw_card(52, 258, 164, 116, "Angle", ["Theta"], align="center")
    content += draw_card(258, 138, 246, 328, "Feature Expansion", ["sin(theta)", "cos(theta)", "sin(2 theta)", "cos(2 theta)", "Higher-order channels", "Optional raw angle"], note="2K or 2K + 1 periodic channels", accent=True, align="center")
    content += draw_card(544, 214, 196, 204, "Conditions", ["Speed", "Torque", "Temperature", "Direction"], note="Normalized operating inputs", align="center")
    content += draw_card(780, 258, 170, 116, "Concat", ["Expanded feature vector"], align="center")

    # Draw Neural Backbone
    layer_block_svg, _ = draw_layer_block(
        [1012, 1122, 1222],
        [["h1", "h2", "h3", "h4"], ["h1", "h2", "h3"], ["TE"]],
        base_y=318,
        layer_gap=62,
        radius=15,
    )
    content += layer_block_svg

    # Draw Input Routing
    content += draw_arrow(216, 316, 258, 316)
    content += draw_arrow(504, 316, 780, 286)
    content += draw_arrow(740, 316, 780, 346)
    content += draw_arrow(950, 316, 986, 316)
    content += '  <text x="286" y="538" class="tiny">Periodic structure is handcrafted in front. Nonlinear interaction learning happens in the MLP.</text>\n'
    return content


def build_residual_conceptual_diagram() -> str:

    """ Build Residual Conceptual Diagram """

    # Draw Header And Branch Blocks
    content = draw_header("Residual Harmonic Network", "Structured harmonic branch plus neural residual correction")
    content += draw_card(60, 236, 218, 176, "Shared Input", ["Angle sample", "Normalized operating state", "Common input to both branches"], note="One point feeds both paths")
    content += draw_flow_card(
        350,
        148,
        258,
        212,
        "Structured Branch",
        ["Harmonic basis", "Coefficient resolution", "Structured TE prediction"],
        note="Can be frozen or joint-trained",
        accent=True,
    )
    content += draw_flow_card(
        350,
        388,
        258,
        180,
        "Residual Branch",
        ["Dense residual MLP", "Learns remaining error"],
        note="Only models what the harmonic branch misses",
    )
    content += draw_card(702, 254, 152, 104, "Add", ["H plus R"], align="center")
    content += draw_card(946, 186, 224, 240, "Outputs", ["Structured prediction", "Residual prediction", "Total prediction", "Structured diagnostics"], note="Useful for branch-level analysis", align="center")

    # Draw Branch Routing
    content += draw_arrow(278, 292, 350, 252)
    content += draw_arrow(278, 350, 350, 478)
    content += draw_arrow(608, 254, 702, 286)
    content += draw_arrow(608, 478, 702, 326)
    content += draw_arrow(854, 306, 946, 306)

    # Draw Interpretation Card
    content += draw_card(
        110,
        576,
        1012,
        112,
        "Interpretation",
        ["The network keeps the interpretable periodic backbone and learns only the unexplained residual component."],
        align="center",
    )
    return content


def build_residual_architecture_diagram() -> str:

    """ Build Residual Architecture Diagram """

    # Draw Static Branch Blocks
    content = draw_header("Residual Harmonic Network Structure", "Structured harmonic path, residual MLP path, and explicit additive merge")
    content += draw_card(46, 266, 190, 118, "Shared Input", ["Angle and conditions"], align="center")
    content += draw_flow_card(
        292,
        148,
        226,
        204,
        "Structured Path",
        ["Harmonic basis", "Coefficient resolver", "Structured output H"],
        accent=True,
    )
    content += draw_flow_card(
        292,
        398,
        226,
        204,
        "Residual Path",
        ["Normalized input", "Dense residual MLP", "Residual output R"],
    )

    # Draw Input Routing
    content += draw_arrow(236, 312, 292, 250)
    content += draw_arrow(236, 338, 292, 500)

    # Draw Residual Neural Stack
    layer_block_svg, layer_centers = draw_layer_block(
        [612, 726, 840],
        [["z1", "z2", "z3", "z4"], ["r1", "r2", "r3"], ["R"]],
        base_y=498,
        layer_gap=58,
        radius=15,
    )
    content += layer_block_svg

    # Draw Merge Blocks
    content += draw_card(610, 172, 192, 104, "Structured Output", ["H"], align="center")
    content += draw_card(936, 276, 164, 112, "Add", ["H plus R"], align="center")
    content += draw_card(1120, 276, 116, 112, "TE", ["Output"], align="center")

    # Draw Merge Routing
    content += draw_arrow(518, 250, 610, 224)
    content += draw_arrow(802, 212, 936, 312)
    residual_output_x, residual_output_y = layer_centers[-1][0]
    content += draw_arrow(residual_output_x + 15, residual_output_y, 936, 344)
    content += draw_arrow(1100, 332, 1120, 332)
    content += '  <text x="610" y="620" class="tiny">Training can log H, R, and H + R separately for diagnostics.</text>\n'
    return content


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
