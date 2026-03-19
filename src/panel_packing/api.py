from .dense_solver import dense_layout
from .geometry import rotated_bbox
from .solvers import LayoutResult


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
    """Public API for panel packing.

    Supported modes:
    - bbox_grid
    - dense
    """
    bw, bh = rotated_bbox(xu, yu, theta_deg)
    unit_area = xu * yu
    panel_area = lim_x * lim_y if lim_x > 0 and lim_y > 0 else 0.0

    if packing_mode == "dense":
        positions = dense_layout(
            xu=xu,
            yu=yu,
            lim_x=lim_x,
            lim_y=lim_y,
            gap_x=gap_x,
            gap_y=gap_y,
            margin_x=margin_x,
            margin_y=margin_y,
            theta_deg=theta_deg,
        )
        total = len(positions)
        utilization = (total * unit_area) / panel_area if panel_area > 0 else 0.0
        return LayoutResult(total=total, positions=positions, utilization=utilization)

    usable_x = lim_x - 2 * margin_x
    usable_y = lim_y - 2 * margin_y
    step_x = bw + gap_x
    step_y = bh + gap_y

    nx = max(int(usable_x // step_x), 0)
    ny = max(int(usable_y // step_y), 0)

    positions = []
    for i in range(nx):
        for j in range(ny):
            positions.append((margin_x + i * step_x, margin_y + j * step_y))

    total = len(positions)
    utilization = (total * unit_area) / panel_area if panel_area > 0 else 0.0
    return LayoutResult(total=total, positions=positions, utilization=utilization)
