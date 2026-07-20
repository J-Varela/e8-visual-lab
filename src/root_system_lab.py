from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def generate_a2_roots() -> np.ndarray:
    """
    Generate the six roots of the A2 root system.

    The vectors are equally spaced around the unit circle.
    """
    angles = np.arange(0, 360, 60)
    radians = np.radians(angles)

    return np.column_stack(
        (
            np.cos(radians),
            np.sin(radians),
        )
    )


def main() -> None:
    roots = generate_a2_roots()

    fig, ax = plt.subplots(figsize=(7, 7))

    for index, root in enumerate(roots):
        ax.quiver(
            0,
            0,
            root[0],
            root[1],
            angles="xy",
            scale_units="xy",
            scale=1,
        )

        ax.text(
            root[0] * 1.12,
            root[1] * 1.12,
            f"α{index + 1}",
            ha="center",
            va="center",
        )

    circle = plt.Circle(
        (0, 0),
        1,
        fill=False,
        linestyle="--",
    )
    ax.add_patch(circle)

    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("A2 Root System Lab v0.6.0")

    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_dir.mkdir(exist_ok=True)

    fig.tight_layout()
    fig.savefig(
        output_dir / "a2_root_system_v0.6.0.png",
        dpi=200,
    )

    plt.show()


if __name__ == "__main__":
    main()