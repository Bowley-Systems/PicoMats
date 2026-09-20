"""
Filename: constants.py

Description:
    Physical constants defined
    based on ontology unit frame (Metric).
"""

from picomats.physical.units import (
    meter,
    second,
    joule,
    kilogram,
    coulomb,
    henry,
    farad
)


# =============== Fundamental physical constants =================


c = speed_of_light = 299792458 * (meter / second)
h = plank_constant = 6.62607015e-34 * (joule * second)
G = gravitational_constant  = 6.67430e-11 * meter**3 / (kilogram * second**2)
e = elementary_charge = 1.602176634e-19 * coulomb
mu_0 = vacuum_permeability = 1.25663706212e-6 * henry / meter
eps_0 = vacuum_permittivity = 8.8541878128e-12 * farad / meter
k_e = coulomb_constant = 1 / (4 * 3.141592653589793 * eps_0)


# ================================================================
