import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def rotation_matrix(theta_degrees: float) -> np.ndarray:
    theta = np.radians(theta_degrees)

    return np.array(
        [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)],
        ]
    )


def main() -> None:
    original = np.array([3.0, 1.0])

    fig, ax = plt.subplots(figsize=(7, 7))
    plt.subplots_adjust(bottom=0.2)

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    original_vector = ax.quiver(
        0,
        0,
        original[0],
        original[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        label="Original",
    )

    rotated_vector = ax.quiver(
        0,
        0,
        original[0],
        original[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        label="Rotated",
    )

    angle_text = ax.text(
        0.03,
        0.95,
        "Angle: 0°",
        transform=ax.transAxes,
        verticalalignment="top",
    )

    ax.legend(handles=[original_vector, rotated_vector])
    ax.set_title("Interactive Rotation Lab v0.3.0")

    slider_axis = fig.add_axes([0.2, 0.08, 0.6, 0.04])

    angle_slider = Slider(
        ax=slider_axis,
        label="Rotation angle",
        valmin=0,
        valmax=360,
        valinit=0,
        valstep=1,
    )

    def update(angle: float) -> None:
        rotated = rotation_matrix(angle) @ original

        rotated_vector.set_UVC(rotated[0], rotated[1])
        angle_text.set_text(f"Angle: {angle:.0f}°")

        fig.canvas.draw_idle()

    angle_slider.on_changed(update)

    plt.show()


if __name__ == "__main__":
    main()