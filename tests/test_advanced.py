from panel_packing.api import calculate_layout


def test_dense_vs_grid():
    grid = calculate_layout(10, 10, 200, 200, 1, 1, 5, 5, 10, "bbox_grid")
    dense = calculate_layout(10, 10, 200, 200, 1, 1, 5, 5, 10, "dense")

    assert dense.total >= grid.total


def test_dense_validity():
    result = calculate_layout(12, 8, 150, 150, 1, 1, 5, 5, 15, "dense")

    assert result.total >= 0
    assert result.utilization >= 0.0
