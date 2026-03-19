import math
from typing import Tuple


def rotated_bbox(width: float, height: float, theta_deg: float) -> Tuple[float, float]:
    """Compute axis-aligned bounding box of a rotated rectangle."""
    theta = math.radians(theta_deg)
    cos_t = abs(math.cos(theta))
    sin_t = abs(math.sin(theta))
    bw = width * cos_t + height * sin_t
    bh = width * sin_t + height * cos_t
    return bw, bh


def rect_overlap(a, b) -> bool:
    """Axis-aligned rectangle overlap check.
    a, b: (x, y, w, h)
    """
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return not (ax + aw <= bx or bx + bw <= ax or ay + ah <= by or by + bh <= ay)
