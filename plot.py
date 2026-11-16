import matplotlib.pyplot as plt
import pyvista as pv
import plotly.graph_objects as go


def save_plot(filename):
    plt.savefig(
        f"Graphs/{filename}.png",
        dpi=300,
        bbox_inches="tight"
    )


def plot_radial_function(r, R, filename):
    plt.figure()
    plt.plot(r, R)

    plt.xlabel(r"$r$")
    plt.ylabel(r"$R_{nl}(r)$")

    save_plot(filename)
    plt.close()


def plot_radial_probability(r, P, filename):
    plt.figure()
    plt.plot(r, P)

    plt.xlabel(r"$r$")
    plt.ylabel(r"$r^2 |R_{nl}(r)|^2$")

    save_plot(filename)
    plt.close()


def plot_density_2d(X, Z, density, filename):
    plt.figure()

    plt.imshow(
        density,
        origin="lower",
        extent=[X.min(), X.max(), Z.min(), Z.max()]
    )

    plt.colorbar(label=r"$|\psi|^2$")

    save_plot(filename)
    plt.close()


def plot_density_3d(X, Y, Z, density):
    pass
