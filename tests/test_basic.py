from panel_packing.solvers import calculate_layout


def test_layout_runs():
    result = calculate_layout(
        xu=10.0,
        yu=20.0,
        lim_x=200.0,
        lim_y=200.0,
        gap_x=1.0,
        gap_y=1.0,
        margin_x=5.0,
        margin_y=5.0,
        theta_deg=10.0,
    )

    assert result.total >= 0
    assert result.utilization >= 0.0


def test_layout_scaling():
    small = calculate_layout(10, 10, 100, 100, 1, 1, 5, 5, 0)
    large = calculate_layout(10, 10, 200, 200, 1, 1, 5, 5, 0)

    assert large.total >= small.total
