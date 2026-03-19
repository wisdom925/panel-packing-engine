# Panel Packing Engine

A lightweight Python library for solving 2D panel packing problems with rotated rectangular units.

This project provides reusable geometric solvers for placing rectangular units inside a bounded panel under multiple packing strategies, including standard grid placement, compact local-axis packing, dense cross-axis layouts, and grouped layouts.

## Features

- Rotated rectangle bounding box computation
- Convex polygon collision checks using the Separating Axis Theorem (SAT)
- Dense pitch search for compact arrangements
- Multiple packing solvers under a unified API
- Clustered layout strategies with configurable grouping rules
- Clean and testable package structure

## Installation

```bash
pip install -e .
```

## Quick Start

```python
from panel_packing.solvers import calculate_layout

result = calculate_layout(
    xu=UNIT_WIDTH,
    yu=UNIT_HEIGHT,
    lim_x=PANEL_WIDTH,
    lim_y=PANEL_HEIGHT,
    gap_x=GAP_X,
    gap_y=GAP_Y,
    margin_x=MARGIN_X,
    margin_y=MARGIN_Y,
    theta_deg=ROTATION_DEG,
    packing_mode="bbox_grid",
)

print(result.total)
print(result.util)
```

## Packing Modes

### Bounding Box Grid
Places rotated units on a regular grid using axis-aligned bounding boxes.

### Local-Axis Compact
Compresses spacing along the primary placement axis while preserving geometric feasibility.

### Cross-Axis Dense
Searches for tighter row or column pitches using collision-aware geometry checks.

### Clustered Layout
Supports grouped placement with configurable group size and tail-handling strategies.

## Project Structure

```text
src/panel_packing/
examples/
tests/
docs/
```

## Why This Project

Many engineering layout tools are tightly coupled with internal interfaces or process-specific rules.
This repository focuses on the reusable core: geometry, collision checks, and packing solvers.

It is intended as a foundation for:

- layout simulation
- computational geometry experiments
- engineering tooling
- packing strategy benchmarking

## Testing

```bash
pytest
```

## Roadmap

- Add benchmark datasets
- Add visualization examples
- Add CLI support
- Add solver comparison reports
- Publish to PyPI

## License

MIT
