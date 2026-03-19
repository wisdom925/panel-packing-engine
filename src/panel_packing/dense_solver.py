from typing import List, Tuple

from .collision import rotated_rectangles_overlap
from .geometry import rotated_bbox


def dense_row_pitch(
    width: float,
    height: float,
    theta_deg: float,
    gap: float,
    base_pitch: float,
) -> float:
    """Search minimal valid row pitch avoiding overlap."""
    test_pitch = base_pitch

    while test_pitch > gap:
        center_a = (0.0, 0.0)
        center_b = (test_pitch, 0.0)

        if rotated_rectangles_overlap(center_a, center_b, width, height, theta_deg):
            break

        test_pitch -= gap * 0.5

    return max(test_pitch, gap)


def dense_layout(
    xu: float,
    yu: float,
    lim_x: float,
    lim_y: float,
    gap_x: float,
    gap_y: float,
    margin_x: float,
    margin_y: float,
    theta_deg: float,
) -> List[Tuple[float, float]]:
    bw, bh = rotated_bbox(xu, yu, theta_deg)

    pitch_x = dense_row_pitch(xu, yu, theta_deg, gap_x, bw + gap_x)
    pitch_y = dense_row_pitch(xu, yu, theta_deg, gap_y, bh + gap_y)

    usable_x = lim_x - 2 * margin_x
    usable_y = lim_y - 2 * margin_y

    nx = max(int(usable_x // pitch_x), 0)
    ny = max(int(usable_y // pitch_y), 0)

    positions: List[Tuple[float, float]] = []

    for i in range(nx):
        for j in range(ny):
            x = margin_x + i * pitch_x
            y = margin_y + j * pitch_y
            positions.append((x, y))

    return positions
