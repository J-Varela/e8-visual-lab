from itertools import product

import matplotlib.pyplot as plt
import numpy as np


def generate_hypercube_vertices() -> np.ndarray:
    """
    Generate all 16 vertices of a 4D hypercube.

    Each coordinate is either -1 or 1:
    (x, y, z, w)
    """
    return np.array(list(product([-1.0, 1.0], repeat=4)))


def generate_hypercube_edges(vertices: np.ndarray) -> list[tuple[int, int]]:
    """
    Connect vertices that differ in exactly one coordinate.
    """
    edges: list[tuple[int, int]] = []

    for first_index, first_vertex in enumerate(vertices):
        for second_index in range(first_index + 1, len(vertices)):
            second_vertex = vertices[second_index]

            differing_coordinates = np.sum(first_vertex != second_vertex)

            if differing_coordinates == 1:
                edges.append((first_index, second_index))

    return edges


def rotation_matrix_xw(angle_degrees: float) -> np.ndarray:
    """
    Rotate points in the X-W plane of 4D space.
    """
    angle = np.radians(angle_degrees)
    cosine = np.cos(angle)
    sine = np.sin(angle)

    return np.array(
        [
            [cosine, 0.0, 0.0, -sine],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [sine, 0.0, 0.0, cosine],
        ]
    )


def rotation_matrix_yz(angle_degrees: float) -> np.ndarray:
    """
    Rotate points in the Y-Z plane of 4D space.
    """
    angle = np.radians(angle_degrees)
    cosine = np.cos(angle)
    sine = np.sin(angle)

    return np.array(
        [
            [1.0, 0.0, 0.0, 0.0],
            [0.0, cosine, -sine, 0.0],
            [0.0, sine, cosine, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
    )


def project_4d_to_2d(points: np.ndarray) -> np.ndarray:
    """
    Project 4D points directly into 2D.

    The W and Z coordinates influence the visible X and Y positions,
    creating a lower-dimensional shadow of the 4D structure.
    """
    projection_matrix = np.array(
        [
            [1.0, 0.0, 0.35, 0.5],
            [0.0, 1.0, 0.35, -0.5],
        ]
    )

    return points @ projection_matrix.T


def main() -> None:
    vertices = generate_hypercube_vertices()
    edges = generate_hypercube_edges(vertices)

    xw_rotation = rotation_matrix_xw(32)
    yz_rotation = rotation_matrix_yz(20)

    rotated_vertices = vertices @ xw_rotation.T
    rotated_vertices = rotated_vertices @ yz_rotation.T

    projected_vertices = project_4d_to_2d(rotated_vertices)

    fig, ax = plt.subplots(figsize=(8, 8))

    for start_index, end_index in edges:
        start = projected_vertices[start_index]
        end = projected_vertices[end_index]

        ax.plot(
            [start[0], end[0]],
            [start[1], end[1]],
            linewidth=1.2,
        )

    ax.scatter(
        projected_vertices[:, 0],
        projected_vertices[:, 1],
        s=45,
        zorder=3,
    )

    for index, point in enumerate(projected_vertices):
        ax.text(
            point[0] + 0.04,
            point[1] + 0.04,
            str(index),
            fontsize=8,
        )

    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_xlabel("Projected X")
    ax.set_ylabel("Projected Y")
    ax.set_title("4D Hypercube Projection Lab v0.4.0")

    fig.tight_layout()
    fig.savefig(
        "outputs/hypercube_projection_v0.4.0.png",
        dpi=200,
    )

    plt.show()


if __name__ == "__main__":
    main()