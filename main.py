import numpy as np

from physics import (
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
    compute_density,
    radial_wavefunction
)

from visualization import (
    plot_all_radial_functions,
    plot_all_probabilities,
    plot_density_subplots,
    plot_isosurface_3d
)

def main():
    # Radial functions
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

    def validate_radial_functions():

        r = np.linspace(0, 30, 1000)

        functions = {
            (1, 0): R10,
            (2, 0): R20,
            (2, 1): R21,
            (3, 0): R30,
            (3, 1): R31,
            (3, 2): R32,
            (4, 0): R40,
            (4, 1): R41,
            (4, 2): R42,
            (4, 3): R43
        }

        tolerance = 1e-12

        for (n, l), function in functions.items():

            analytical = function(r)
            general = radial_wavefunction(n, l, r)

            difference = np.max(np.abs(analytical - general))

            status = "PASS" if difference < tolerance else "FAIL"

            print(
            f"R{n}{l}: max difference = {difference:.3e}",
            "PASS" if np.allclose(analytical, general, atol=1e-12) else "FAIL"
    )

    validate_radial_functions()


    
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

    # 2D density grids
    x = np.linspace(-30,30,500)
    z = np.linspace(-30,30,500)

    X, Z = np.meshgrid(x,z)

    r_grid = np.sqrt(X**2 + Z**2)


    theta = np.arccos(
        np.where(r_grid == 0, 1, Z/r_grid)
    )

    phi = np.where(X >= 0, 0, np.pi)

    # Calculate and plot densities
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

                # print("max:", np.max(density))
                # print("min:", np.min(density))

                densities[(l, m)] = density

        plot_density_subplots(
            X,
            Z,
            densities,
            n,
            f"density_n{n}"
        )


    # 3D density grid

    x = np.linspace(-30, 30, 100)
    y = np.linspace(-30, 30, 100)
    z = np.linspace(-30, 30, 100)

    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

    r_grid = np.sqrt(X**2 + Y**2 + Z**2)

    theta = np.arccos(
        np.clip(
            Z / np.where(r_grid == 0, 1, r_grid),
            -1,
            1
        )
    )

    phi = np.mod(np.arctan2(Y, X), 2*np.pi)

    for n in range(1, 5):

        densities = {}

        for l in range(n):
            for m in range(-l, l + 1):

                density = compute_density(
                    n,
                    l,
                    m,
                    r_grid,
                    theta,
                    phi
                )

                densities[(l, m)] = density

        plot_isosurface_3d(
            x,
            y,
            z,
            densities,
            n,
            threshold=0.15,
            filename=f"isosurface_n{n}"
        )

if __name__ == "__main__":
    main()