import matplotlib.pyplot as plt
# import os
import numpy as np
# from matplotlib.colors import PowerNorm
from skimage.measure import marching_cubes

def save_plot(filename):

    plt.savefig(
        f"Radial-wave-equations-in-3D\isosurfaces/{filename}.png",
        dpi=300,
        bbox_inches="tight"
    )

def plot_isosurface_3d(x, y, z, densities, n, threshold=0.15, filename="isosurface"):

    # Number of orbitals
    orbitals = list(densities.keys())

    num_orbitals = len(orbitals)

    # Find rows and columns
    cols = int(np.ceil(np.sqrt(num_orbitals)))
    rows = int(np.ceil(num_orbitals / cols))

    fig = plt.figure(
        figsize=(5 * cols, 5 * rows),
        constrained_layout=True
    )

    # Grid spacing
    spacing = (
        x[1] - x[0],
        y[1] - y[0],
        z[1] - z[0]
    )

    for i, (l, m) in enumerate(orbitals):

        density = densities[(l, m)]

        # Define probability threshold
        level = threshold * np.max(density)

        # Marching cubes
        vertices, faces, normals, values = marching_cubes(
            density,
            level=level,
            spacing=spacing
        )

        # Shift vertices to correct coordinates
        vertices += np.array([x[0], y[0], z[0]])

        # Create 3D subplot
        ax = fig.add_subplot(
            rows,
            cols,
            i + 1,
            projection="3d"
        )

        # Plot isosurface
        ax.plot_trisurf(
            vertices[:, 0],
            vertices[:, 1],
            vertices[:, 2],
            triangles=faces,
            color="green",
            alpha=0.85,
            linewidth=0,
            antialiased=True
        )

        ax.set_title(f"$n={n}, l={l}, m={m}$")

        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        ax.set_zlabel("$z$")

        ax.set_xlim(-30, 30)
        ax.set_ylim(-30, 30)
        ax.set_zlim(-30, 30)

        ax.set_box_aspect((1, 1, 1))

    fig.suptitle(
        f"Hydrogen orbital isosurfaces: n={n}",
        fontsize=16
    )

    # plt.tight_layout()

    save_plot(filename)
    plt.close(fig)