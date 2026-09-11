# pylint: skip-file
# picomats/__init__.py

from picomats.physical.units import *
from picomats.physical.constants import *

from picomats.core.manager import Manager

# Referenced the manager as material.
Materials = Manager()


# API Promises
__all__ = [
    # Materials
    "Materials",
    
    # Base units
    "second", "s", "meter", "m", "kilogram", "kg", "ampere", "A",
    "kelvin", "K", "mole", "mol", "candela", "cd", 
    "dimensionless", "nullset",
    
    "TIME", "LENGTH", "MASS", "CURRENT", "TEMPERATURE",
    "AMOUNT", "LUMINOSITY", "NULLSET",
    
    # Scales
    "GIGA", "gi", "MEGA", "me", "KILO", "ki", "CENTI", "ce",
    "MILLI", "mi", "MICRO", "ui", "NANO", "na", "PICO", "pi",
    
    # Scaled length units
    "kilometer", "km", "centimeter", "cm", "millimeter", "mm",
    "micrometer", "um", "nanometer", "nm", "picometer", "pm",
    
    # Scaled time units
    "millisecond", "ms", "microsecond", "us", "nanosecond", "ns",
    
    # Mass units
    "gram", "g", "milligram", "mg",
    
    # Derived unit definitions (constants)
    "FORCE", "ENERGY", "POWER", "PRESSURE", "FREQUENCY",
    "CHARGE", "VOLTAGE", "RESISTANCE", "CAPACITANCE", "INDUCTANCE",
    "MAGNETIC_FLUX", "MAGNETIC_FIELD", "CONDUCTANCE",
    "VOLUMETRIC_HEAT_CAPACITY", "VOLUMETRIC_HEATING",
    
    # Derived named units
    "newton", "N", "joule", "J", "watt", "W", "pascal", "Pa",
    "hertz", "Hz", "coulomb", "C", "volt", "V", "ohm", "R",
    "farad", "F", "henry", "H", "tesla", "T", "weber", "Wb",
    "siemens", "S",
    
    # Heat transfer units
    "volumetric_capacity", "volumetric_heating", "convection_coefficient",
]