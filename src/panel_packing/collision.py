import math
from typing import Iterable, List, Sequence, Tuple

Point = Tuple[float, float]
Polygon = Sequence[Point]

_EPS = 1e-9


def unit_axes(theta_deg: float) -> Tuple[Point, Point]:
    theta = math.radians(theta_deg)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    return (cos_t, sin_t), (-sin_t, cos_t)


def rotated_rectangle_polygon(
    center_x: float,
    center_y: float,
    width: float,
    height: float,
    theta_deg: float,
) -> List[Point]:
    u_axis, v_axis = unit_axes(theta_deg)
    half_w = width / 2.0
    half_h = height / 2.0
    return [
        (center_x - u_axis[0] * half_w - v_axis[0] * half_h, center_y - u_axis[1] * half_w - v_axis[1] * half_h),
        (center_x + u_axis[0] * half_w - v_axis[0] * half_h, center_y + u_axis[1] * half_w - v_axis[1] * half_h),
        (center_x + u_axis[0] * half_w + v_axis[0] * half_h, center_y + u_axis[1] * half_w + v_axis[1] * half_h),
        (center_x - u_axis[0] * half_w + v_axis[0] * half_h, center_y - u_axis[1] * half_w + v_axis[1] * half_h),
    ]


def polygon_axes(polygon: Polygon) -> List[Point]:
    axes: List[Point] = []
    for index in range(len(polygon)):
        x1, y1 = polygon[index]
        x2, y2 = polygon[(index + 1) % len(polygon)]
        axis_x = -(y2 - y1)
        axis_y = x2 - x1
        length = math.hypot(axis_x, axis_y)
        if length <= _EPS:
            continue
        axes.append((axis_x / length, axis_y / length))
    return axes


def polygon_projection_range(polygon: Polygon, axis: Point) -> Tuple[float, float]:
    dots = [x * axis[0] + y * axis[1] for x, y in polygon]
    return min(dots), max(dots)


def polygons_overlap_sat(polygon_a: Polygon, polygon_b: Polygon) -> bool:
    for axis in polygon_axes(polygon_a) + polygon_axes(polygon_b):
        min_a, max_a = polygon_projection_range(polygon_a, axis)
        min_b, max_b = polygon_projection_range(polygon_b, axis)
        if max_a <= min_b + _EPS or max_b <= min_a + _EPS:
            return False
    return True


def rotated_rectangles_overlap(
    center_a: Point,
    center_b: Point,
    width: float,
    height: float,
    theta_deg: float,
) -> bool:
    polygon_a = rotated_rectangle_polygon(center_a[0], center_a[1], width, height, theta_deg)
    polygon_b = rotated_rectangle_polygon(center_b[0], center_b[1], width, height, theta_deg)
    return polygons_overlap_sat(polygon_a, polygon_b)
