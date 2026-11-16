import matplotlib.pyplot as plt
import os
import numpy as np
# from sympy.physics.quantum.constants import hbar
# import pyvista as pv
# import plotly.graph_objects as go


def save_plot(filename):

    plt.savefig(
        f"Radial-wave-equations-in-3D\graphs/{filename}.png",
        dpi=300,
        bbox_inches="tight"
    )

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
    

def plot_density_subplots(X, Z, densities, n, filename):

    # Antal orbitaler for det givne n
    orbitals = list(densities.keys())

    num_orbitals = len(orbitals)

    # Find antal rækker og kolonner
    cols = int(np.ceil(np.sqrt(num_orbitals)))
    rows = int(np.ceil(num_orbitals / cols))

    fig, axes = plt.subplots(
        rows,
        cols,
        figsize=(5 * cols, 5 * rows),
        constrained_layout=True
    )

    # Sørg for at axes altid er et array
    axes = np.array(axes).flatten()

    for ax, (l, m) in zip(axes, orbitals):

        density = densities[(l, m)]

        # Normalisering
        density = density / np.max(density)

        im = ax.imshow(
            density,
            origin="lower",
            extent=[X.min(), X.max(), Z.min(), Z.max()],
            cmap="cividis",
            aspect="equal"
        )

        ax.set_title(f"$n={n}, l={l}, m={m}$")
        ax.set_xlabel("$x$")
        ax.set_ylabel("$z$")

    # Fjern overskydende subplots
    for ax in axes[num_orbitals:]:
        ax.remove()

    # Colorbar
    fig.colorbar(
        im,
        ax=fig.axes,
        label=r"$|\psi_{nlm}|^2$",
        shrink=0.8
    )

    fig.suptitle(f"Hydrogen orbital densities: n={n}", fontsize=16)

    save_plot(filename)
    plt.close(fig)

def plot_density_3d(X, Y, Z, density):
    pass
