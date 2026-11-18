
import matplotlib.pyplot as plt
import numpy as np

from skimage.measure import marching_cubes
from matplotlib import cm
from matplotlib.colors import PowerNorm
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Shared visualization settings
CMAP = cm.viridis

LEVELS = [0.05, 0.15, 0.30, 0.50, 0.75]

NORM = PowerNorm(
    gamma=0.4,
    vmin=0,
    vmax=1
)

def save_plot(filename):

    plt.savefig(
        f"Radial-wave-equations-in-3D/isosurfaces/{filename}.png",
        dpi=300,
        bbox_inches="tight"
    )


def get_plot_limits(n):

    limits = {
        1: 8,
        2: 15,
        3: 22,
        4: 30
    }

    return limits[n]



def plot_isosurface_3d(
    x, y, z, densities, n,
    filename="isosurface"
):

    orbitals = list(densities.keys())

    num_orbitals = len(orbitals)

    cols = int(np.ceil(np.sqrt(num_orbitals)))
    rows = int(np.ceil(num_orbitals / cols))

    fig = plt.figure(
        figsize=(5 * cols, 5 * rows),
        constrained_layout=True
    )

    spacing = (
        x[1] - x[0],
        y[1] - y[0],
        z[1] - z[0]
    )

    limits = get_plot_limits(n)

    for i, (l, m) in enumerate(orbitals):

        density = densities[(l, m)]

        # Normalize density
        density = density / np.max(density)

        ax = fig.add_subplot(
            rows,
            cols,
            i + 1,
            projection="3d"
        )

        # Plot each isosurface
        for level in LEVELS:

            vertices, faces, normals, values = marching_cubes(
                density,
                level=level,
                spacing=spacing
            )

            # Shift vertices to physical coordinates
            vertices += np.array([x[0], y[0], z[0]])

            # Construct triangular mesh
            mesh = vertices[faces]

            # Get corresponding colormap color
            color = CMAP(NORM(level))

            # Create isosurface
            surface = Poly3DCollection(
                mesh,
                facecolors=color,
                edgecolors="none",
                alpha=0.18
            )

            ax.add_collection3d(surface)

        ax.set_title(f"$n={n}, l={l}, m={m}$")

        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        ax.set_zlabel("$z$")

        ax.set_xlim(-limits, limits)
        ax.set_ylim(-limits, limits)
        ax.set_zlim(-limits, limits)

        ax.set_box_aspect((1, 1, 1))

    # Shared colorbar
    scalar_map = cm.ScalarMappable(
        norm=NORM,
        cmap=CMAP
    )

    scalar_map.set_array([])

    fig.colorbar(
        scalar_map,
        ax=fig.axes,
        shrink=0.7,
        label=r"Relative probability density $|\psi|^2/\max(|\psi|^2)$"
    )

    fig.suptitle(
        f"Hydrogen orbital isosurfaces: n={n}",
        fontsize=16
    )

    save_plot(filename)
    plt.close(fig)

