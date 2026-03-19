from dataclasses import dataclass
from typing import List, Tuple
from .geometry import rotated_bbox


@dataclass
class LayoutResult:
    total: int
    positions: List[Tuple[float, float]]
    utilization: float


def calculate_layout(
    xu: float,
    yu: float,
    lim_x: float,
    lim_y: float,
    gap_x: float,
    gap_y: float,
    margin_x: float,
    margin_y: float,
    theta_deg: float,
    packing_mode: str = "bbox_grid",
) -> LayoutResult:
    """Basic bounding-box grid layout solver."""

    bw, bh = rotated_bbox(xu, yu, theta_deg)

    usable_x = lim_x - 2 * margin_x
    usable_y = lim_y - 2 * margin_y

    step_x = bw + gap_x
    step_y = bh + gap_y

    nx = max(int(usable_x // step_x), 0)
    ny = max(int(usable_y // step_y), 0)

    positions = []
    for i in range(nx):
        for j in range(ny):
            x = margin_x + i * step_x
            y = margin_y + j * step_y
            positions.append((x, y))

    total = len(positions)
    panel_area = lim_x * lim_y
    unit_area = xu * yu

    utilization = (total * unit_area) / panel_area if panel_area > 0 else 0.0

    return LayoutResult(total=total, positions=positions, utilization=utilization)
