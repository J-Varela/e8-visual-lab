import numpy as np
import matplotlib.pyplot as plt


def rotation_matrix(theta_degrees: float) -> np.ndarray:
    theta = np.radians(theta_degrees)

    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)],
    ])


def draw_vector(ax, vector, label):
    ax.quiver(
        0,
        0,
        vector[0],
        vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
    )
    ax.text(vector[0] + 0.1, vector[1] + 0.1, label)


def main():
    original = np.array([3, 1])
    rotated_45 = rotation_matrix(45) @ original
    rotated_90 = rotation_matrix(90) @ original

    fig, ax = plt.subplots()

    draw_vector(ax, original, "original")
    draw_vector(ax, rotated_45, "45°")
    draw_vector(ax, rotated_90, "90°")

    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 4)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Rotation Lab v0.2.0")

    plt.savefig("outputs/rotation_lab_v0.2.0.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()