# pylint: skip-file
# picomats/__init__.py

from picounits import Q, Parser, expects
from picounits.utilities.errors import UnitError
from picounits.utilities.validation import strip_quantity, check_quantity

from picomats.physical.units import *
from picomats.physical.constants import *

from picomats.core.manager import Manager
from picomats.core.modules.material import Material


# References the parser & Quality
_, _ = Q, Parser

# References the UnitError, Expect Decorator & Checking functions
_ = UnitError
_ = expects
_, _ = strip_quantity, check_quantity 

# Referenced the manager as material.
Materials = Manager()
_ = Material

# API Promises
__all__ = [
    # Quality & Parser
    "Q",
    "Parser",
    
    # Unit Validation
    "UnitError",
    "expects",
    "strip_quantity",
    "check_quantity",    
    
    # Materials
    "Materials", "Material",
    
    # Base units
    "second", "s",
    "meter", "m",
    "kilogram", "kg",
    "ampere", "A",
    "kelvin", "K",
    "mole", "mol",
    "candela", "cd",
    "dimensionless", "nullset",
    
    "TIME",
    "LENGTH",
    "MASS",
    "CURRENT",
    "TEMPERATURE",
    "AMOUNT",
    "LUMINOSITY",
    "NULLSET",
    
    # Scales
    "GIGA", "gi",
    "MEGA", "me",
    "KILO", "ki",
    "CENTI", "ce",
    "MILLI", "mi", 
    "MICRO", "ui",
    "NANO", "na",
    "PICO", "pi",
    
    # Scaled length units
    "kilometer", "km",
    "centimeter", "cm",
    "millimeter", "mm",
    "micrometer", "um",
    "nanometer", "nm",
    "picometer", "pm",
    
    # Scaled time units
    "millisecond", "ms",
    "microsecond", "us",
    "nanosecond", "ns",
    
    # Mass units
    "gram", "g", 
    "milligram", "mg",
    
    # Derived unit definitions (constants)
    "FORCE",
    "ENERGY",
    "POWER",
    "PRESSURE",
    "FREQUENCY",
    "CHARGE",
    "VOLTAGE",
    "RESISTANCE",
    "CAPACITANCE",
    "INDUCTANCE",
    "MAGNETIC_FLUX",
    "MAGNETIC_FIELD",
    "CONDUCTANCE",
    "VOLUMETRIC_HEAT_CAPACITY",
    "VOLUMETRIC_HEATING",
    
    # Derived named units
    "newton", "N",
    "joule", "J",
    "watt", "W",
    "pascal", "Pa",
    "hertz", "Hz",
    "coulomb", "C",
    "volt", "V",
    "ohm", "R",
    "farad", "F",
    "henry", "H",
    "tesla", "T",
    "weber", "Wb",
    "siemens", "S",
    
    # Heat transfer units
    "volumetric_capacity", 
    "volumetric_heating", 
    "convection_coefficient",
    
    # Fundamental physical constants
    "c", "speed_of_light",
    "h", "plank_constant",
    "hbar", "reduced_plank_constant",
    "G", "gravitational_constant",
    "e", "elementary_charge",
    "mu_0", "vacuum_permeability",
    "eps_0", "vacuum_permittivity",
    "k_e", "coulomb_constant",
    "N_A", "avogadro_constant",
    "k_B", "boltzmann_constant",
    "R", "gas_constant",
]