import numpy as np

from scipy.special import sph_harm_y
from math import factorial
from scipy.special import assoc_laguerre

a0 = 1.0

def R10(r):
    x = r/a0
    return 2*a0**(-3/2)*np.exp(-x)

def R20(r):
    x = r/a0
    return (1/np.sqrt(2))*a0**(-3/2)*(1 - 1/2*x)*np.exp(-x/2)

def R21(r):
    x = r/a0
    return (1/(2*np.sqrt(6))*a0**(-3/2)*x*np.exp(-x/2))

def R30(r):
    x = r/a0
    return (2/(3*np.sqrt(3))*a0**(-3/2)*(1- 2/3*x+2/27*x**2)*np.exp(-x/3))


def R31(r):
    x = r/a0
    return (8/(27*np.sqrt(6))*a0**(-3/2)*x*(1 - x/6)*np.exp(-x/3))

def R32(r):
    x = r/a0
    return (4/(81*np.sqrt(30))*a0**(-3/2)*x**2*np.exp(-x/3))

def R40(r):
    x = r/a0
    return (1/4*a0**(-3/2)*(1 - 3*x/4 + x**2/8 - x**3/192)*np.exp(-x/4))


def R41(r):
    x = r/a0
    return (5/(16*np.sqrt(15))*a0**(-3/2)*x*(1 - x/4 + x**2/80)*np.exp(-x/4))


def R42(r):
    x = r/a0
    return (1/(64*np.sqrt(5))*a0**(-3/2)*x**2*(1 - x/12)*np.exp(-x/4))


def R43(r):
    x = r/a0
    return (1/(768*np.sqrt(35))*a0**(-3/2)* x**3 * np.exp(-x/4))



# radial wave funktion
def radial_wavefunction (n, l, r) :
    rho = 2*r/(n*a0)

    N = np.sqrt(
        (2/(n*a0))**3
        * factorial(n-l-1)
        / (2*n*factorial(n+l))
    )

    return (
        N
        * np.exp(-rho/2)
        * rho**l
        * assoc_laguerre(
            rho,
            n-l-1,
            2*l+1
        )
    )

def psi(n, l, m, r, theta, phi):

    R = radial_wavefunction(n, l, r)

    Y = sph_harm_y(l, m, theta, phi)

    return R * Y


def compute_density(n, l, m, r, theta, phi):

    Psi = psi(
        n,
        l,
        m,
        r,
        theta,
        phi
    )

    density = np.abs(Psi)**2

    # print(f"n={n}, l={l}, m={m}")
    # print("max =", np.max(density))
    # print("min =", np.min(density))

    return density

# # 3D density:
# def compute_density_3d(n, l, m, grid_size=100, extent=20):

#     x = np.linspace(-extent, extent, grid_size)
#     y = np.linspace(-extent, extent, grid_size)
#     z = np.linspace(-extent, extent, grid_size)

#     X, Y, Z = np.meshgrid(
#         x, y, z,
#         indexing="ij"
#     )

#     # Cartesian -> spherical coordinates
#     r = np.sqrt(X**2 + Y**2 + Z**2)

#     theta = np.arccos(
#         np.clip(
#             Z / np.where(r == 0, 1, r),
#             -1, 1
#         )
#     )