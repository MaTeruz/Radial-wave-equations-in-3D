import numpy as np

from scipy.special import sph_harm_y
from math import factorial
from scipy.special import assoc_laguerre


a0 = 1.0

def R10(r):
    return 2*a0**(-3/2)*np.exp(-r/a0)

def R20(r):
    return (1/np.sqrt(2))*a0**(-3/2)*(1 - 1/2*r/a0)*np.exp(-r/(2*a0))

def R21(r):
    return (1/(2*np.sqrt(6))*a0**(-3/2)*(r/a0)*np.exp(-r/(2*a0)))

def R30(r):
    return (2/(3*np.sqrt(3))*a0**(-3/2)*(1- 2/3*r/a0+2/27*(r/a0)**2)*np.exp(-r/(3*a0)))

def R31(r):
    return (8/(27*np.sqrt(6))*a0**(-3/2)*(1- 1/6*(r/a0)**2)*np.exp(-r/(3*a0)))

def R32(r):
    return (4/(81*np.sqrt(30))*a0**(-3/2)*((r/a0)**2)*np.exp(-r/(3*a0)))

def R40(r) :
    return (2/(3*np.sqrt(3))*a0**(-3/2)*(1- 3/4 + 1/8*(r/a0)**2 - 1/192*(r/a0)**3)*np.exp(-r/(4*a0)))

def R41(r) :
    return (5/(16*np.sqrt(15))*a0**(-3/2)*(1 - 1/4 + 1/8*r/a0 + 1/80*(r/a0)**2)*(r/a0)*np.exp(-r/(4*a0)))

def R42(r) :
    return (1/(64*np.sqrt(5))*a0**(-3/2)*(1 - 1/12 * r/a0)*(r/a0)*np.exp(-r/(4*a0)))

def R43(r) :
    return (1/(768*np.sqrt(35))*a0*(r/a0)**3*np.exp(-r/(4*a0)))

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
