from panel_packing.api import calculate_layout


def run():
    result_grid = calculate_layout(
        xu=10.0,
        yu=15.0,
        lim_x=200.0,
        lim_y=200.0,
        gap_x=1.0,
        gap_y=1.0,
        margin_x=5.0,
        margin_y=5.0,
        theta_deg=10.0,
        packing_mode="bbox_grid",
    )

    result_dense = calculate_layout(
        xu=10.0,
        yu=15.0,
        lim_x=200.0,
        lim_y=200.0,
        gap_x=1.0,
        gap_y=1.0,
        margin_x=5.0,
        margin_y=5.0,
        theta_deg=10.0,
        packing_mode="dense",
    )

    print("Grid:", result_grid.total, result_grid.utilization)
    print("Dense:", result_dense.total, result_dense.utilization)


if __name__ == "__main__":
    run()
