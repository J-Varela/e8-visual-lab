import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def rotation_matrix(theta):
    theta = np.radians(theta)

    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)],
    ])


original = np.array([3, 1])

fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect("equal")
ax.grid(True)

vector = ax.quiver(
    0,
    0,
    original[0],
    original[1],
    angles="xy",
    scale_units="xy",
    scale=1,
    color="red",
)


def update(frame):

    rotated = rotation_matrix(frame) @ original

    vector.set_UVC(rotated[0], rotated[1])

    ax.set_title(f"Rotation: {frame}°")

    return vector,


animation = FuncAnimation(
    fig,
    update,
    frames=np.arange(0, 361, 2),
    interval=30,
    blit=True,
)

plt.show()