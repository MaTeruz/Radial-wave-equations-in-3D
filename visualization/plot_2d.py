import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib import cm
from matplotlib.colors import PowerNorm
from skimage.measure import marching_cubes
# from sympy.physics.quantum.constants import hbar
# import pyvista as pv
# import plotly.graph_objects as go

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
        f"Radial-wave-equations-in-3D\graphs/{filename}.png",
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

# 
def plot_radial_function(r, R, filename):
    plt.figure()
    plt.plot(r, R)

    plt.xlabel(r"$r$")
    plt.ylabel(r"$R_{nl}(r)$")

    save_plot(filename)

    plt.close()

def plot_all_radial_functions(r, functions, filename):

    plt.figure(figsize=(10,6))

    for (n, l), R in functions.items():

        plt.plot(
            r,
            R,
            label=rf"$R_{{{n}{l}}}$"
        )

    plt.xlabel(r"$r$")
    plt.ylabel(r"$R_{nl}(r)$")

    plt.legend()
    plt.grid()

    save_plot(filename)
    plt.close()

# 
def plot_radial_probability(r, P, filename):
    plt.figure()
    plt.plot(r, P)

    plt.xlabel(r"$r$")
    plt.ylabel(r"$r^2 |R_{nl}(r)|^2$")

    save_plot(filename)
    plt.close()

def plot_all_probabilities(r, probabilities, filename):

    plt.figure(figsize=(10,6))

    for (n, l), P in probabilities.items():

        plt.plot(
            r,
            P,
            label=rf"$P_{{{n}{l}}}$"
        )

    plt.xlabel(r"$r$")
    plt.ylabel(r"$r^2 |R_{nl}(r)|^2$")

    plt.legend()
    plt.grid()

    save_plot(filename)
    plt.close()
    

def plot_density_subplots(X, Z, densities, n, filename, limits=30):

    orbitals = list(densities.keys())

    num_orbitals = len(orbitals)

    cols = int(np.ceil(np.sqrt(num_orbitals)))
    rows = int(np.ceil(num_orbitals / cols))

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(5 * cols, 5 * rows),
        constrained_layout=True
    )

    axes = np.array(axes).flatten()

    for ax, (l, m) in zip(axes, orbitals):

        density = densities[(l, m)]

        # Normalize density
        density = density / np.max(density)

        # Plot probability density
        im = ax.imshow(
            density,
            origin="lower",
            extent=[X.min(), X.max(), Z.min(), Z.max()],
            cmap=CMAP,
            norm=NORM,
            aspect="equal"
        )

        # Add contour lines
        ax.contour(
            X,
            Z,
            density,
            levels=LEVELS,
            colors=[
                CMAP(NORM(level))
                for level in LEVELS
            ],
            linewidths=1.2
        )

        ax.set_title(f"$n={n}, l={l}, m={m}$")
        ax.set_xlabel("$x$")
        ax.set_ylabel("$z$")

        limits = get_plot_limits(n)

        ax.set_xlim(-limits, limits)
        ax.set_ylim(-limits, limits)

    for ax in axes[num_orbitals:]:
        ax.remove()

    fig.colorbar(
        im,
        ax=fig.axes,
        label=r"$|\psi_{nlm}|^2$",
        shrink=0.8
    )

    fig.suptitle(f"Hydrogen orbital densities: n={n}", fontsize=16)

    save_plot(filename)
    plt.close(fig)

