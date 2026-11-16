import numpy as np

from hydrogen import (
    R10,
    R20,
    R21,
    R30,
    R31,
    R32, 
    R40, 
    R41, 
    R42, 
    R43,
)
from hydrogen import (
    psi
)

from plot import (
    plot_all_radial_functions,
    plot_all_probabilities,
    plot_density_subplots

)

r = np.linspace(0,20,1000)

radial_functions = {

    (1,0): R10(r),
    (2,0): R20(r),
    (2,1): R21(r),
    (3,0): R30(r),
    (3,1): R31(r),
    (3,2): R32(r),
    (4,0): R40(r),
    (4,1): R41(r),
    (4,2): R42(r),
    (4,3): R43(r)
}

probabilities = {

    key: r**2*np.abs(R)**2
    for key, R in radial_functions.items()
}

plot_all_radial_functions(
    r,
    radial_functions,
    "all_R"
)

plot_all_probabilities(
    r,
    probabilities,
    "all_P"
)

x = np.linspace(-20,20,500)
z = np.linspace(-20,20,500)

X, Z = np.meshgrid(x,z)

r_grid = np.sqrt(X**2 + Z**2)

theta = np.arccos(
    np.where(r_grid == 0, 1, Z/r_grid)
)

phi = np.where(X >= 0, 0, np.pi)

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

    print(f"n={n}, l={l}, m={m}")
    print("max =", np.max(density))
    print("min =", np.min(density))

    return density


for n in range(1, 5):

    densities = {}

    for l in range(n):

        for m in range(-l, l+1):

            density = compute_density(
                n,
                l,
                m,
                r_grid,
                theta,
                phi
            )

            print("max:", np.max(density))
            print("min:", np.min(density))

            densities[(l, m)] = density

    plot_density_subplots(
        X,
        Z,
        densities,
        n,
        f"density_n{n}"
    )
