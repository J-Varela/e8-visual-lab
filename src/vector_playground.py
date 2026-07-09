import numpy as np
import matplotlib.pyplot as plt


def draw_vector(ax, vector, label):
    origin = np.array([0, 0])
    ax.quiver(
        origin[0],
        origin[1],
        vector[0],
        vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
    )
    ax.text(vector[0] + 0.1, vector[1] + 0.1, label)


def main():
    v1 = np.array([3, 2])
    v2 = np.array([-1, 4])
    v3 = v1 + v2

    fig, ax = plt.subplots()

    draw_vector(ax, v1, "v1")
    draw_vector(ax, v2, "v2")
    draw_vector(ax, v3, "v1 + v2")

    ax.set_xlim(-5, 6)
    ax.set_ylim(-1, 7)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_title("Vector Playground v0.1.0")

    plt.savefig("outputs/vector_playground_v0.1.0.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()