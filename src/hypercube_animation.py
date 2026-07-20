from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def generate_hypercube_vertices() -> np.ndarray:
    return np.array(list(product([-1.0, 1.0], repeat=4)))


def generate_hypercube_edges(vertices: np.ndarray) -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []

    for first_index, first_vertex in enumerate(vertices):
        for second_index in range(first_index + 1, len(vertices)):
            second_vertex = vertices[second_index]

            if np.sum(first_vertex != second_vertex) == 1:
                edges.append((first_index, second_index))

    return edges


def rotation_matrix(
    first_axis: int,
    second_axis: int,
    angle_degrees: float,
) -> np.ndarray:
    angle = np.radians(angle_degrees)
    cosine = np.cos(angle)
    sine = np.sin(angle)

    matrix = np.eye(4)
    matrix[first_axis, first_axis] = cosine
    matrix[second_axis, second_axis] = cosine
    matrix[first_axis, second_axis] = -sine
    matrix[second_axis, first_axis] = sine

    return matrix


def project_4d_to_2d(points: np.ndarray) -> np.ndarray:
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

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_xlabel("Projected X")
    ax.set_ylabel("Projected Y")

    edge_lines = [
        ax.plot([], [], linewidth=1.2)[0]
        for _ in edges
    ]

    vertex_scatter = ax.scatter([], [], s=45, zorder=3)

    def update(frame: int):
        xw_rotation = rotation_matrix(0, 3, frame)
        yz_rotation = rotation_matrix(1, 2, frame * 0.7)
        zw_rotation = rotation_matrix(2, 3, frame * 0.4)

        rotated_vertices = vertices @ xw_rotation.T
        rotated_vertices = rotated_vertices @ yz_rotation.T
        rotated_vertices = rotated_vertices @ zw_rotation.T

        projected_vertices = project_4d_to_2d(rotated_vertices)

        vertex_scatter.set_offsets(projected_vertices)

        for line, (start_index, end_index) in zip(edge_lines, edges):
            start = projected_vertices[start_index]
            end = projected_vertices[end_index]

            line.set_data(
                [start[0], end[0]],
                [start[1], end[1]],
            )

        ax.set_title(f"Animated 4D Hypercube v0.5.0 — {frame}°")

        return [vertex_scatter, *edge_lines]

    animation = FuncAnimation(
        fig,
        update,
        frames=np.arange(0, 360, 2),
        interval=40,
        blit=False,
        repeat=True,
    )

    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_dir.mkdir(exist_ok=True)

    # Keep a reference so Matplotlib does not garbage-collect the animation.
    _ = animation

    plt.show()


if __name__ == "__main__":
    main()