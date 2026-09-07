"""
Filename: units.py

Description:
    Defines unit notation based on ontology
    unit frame (Metric). 
"""

from picounits import PrefixScale
from picounits.constants import TIME, LENGTH, MASS, CURRENT,TEMPERATURE, AMOUNT, LUMINOSITY, NULLSET


# =============== Base units (SI names) ===============

second          = s         = TIME
meter           = m         = LENGTH
kilogram        = kg        = MASS
ampere          = A         = CURRENT
kelvin          = K         = TEMPERATURE
mole            = mol       = AMOUNT
candela         = cd        = LUMINOSITY
dimensionless   = nullset   = NULLSET


# =============== Predefined scales for quantities ===============

GIGA    = gi  = PrefixScale.GIGA
MEGA    = me  = PrefixScale.MEGA
KILO    = ki  = PrefixScale.KILO
CENTI   = ce  = PrefixScale.CENTI
MILLI   = mi  = PrefixScale.MILLI
MICRO   = ui  = PrefixScale.MICRO
NANO    = na  = PrefixScale.NANO
PICO    = pi  = PrefixScale.PICO


# =============== Scaled length units ===============

kilometer   = km = 1 * KILO  * meter
centimeter  = cm = 1 * CENTI * meter
millimeter  = mm = 1 * MILLI * meter
micrometer  = um = 1 * MICRO * meter
nanometer   = nm = 1 * NANO  * meter
picometer   = pm = 1 * PICO  * meter


# =============== Scaled time units ===============

millisecond = ms = 1 * MILLI * second
microsecond = us = 1 * MICRO * second
nanosecond  = ns = 1 * NANO  * second


# =============== Mass units ===============


gram        = g  = 1 * MILLI * kilogram
milligram   = mg = 1 * MICRO * kilogram


# =============== Derived unit definitions ===============


# Mechanical units
FORCE           = kilogram * meter / second**2
ENERGY          = FORCE * meter
POWER           = ENERGY / second
PRESSURE        = FORCE / meter**2
FREQUENCY       = 1 / second

# Electrical units
CHARGE          = ampere * second
VOLTAGE         = POWER / ampere
RESISTANCE      = VOLTAGE / ampere
CAPACITANCE     = CHARGE / VOLTAGE
INDUCTANCE      = VOLTAGE * second / ampere
MAGNETIC_FLUX   = VOLTAGE * second
MAGNETIC_FIELD  = FORCE / (ampere * meter)
CONDUCTANCE     = 1 / RESISTANCE

# Heat transfer units
VOLUMETRIC_HEAT_CAPACITY = ENERGY / (meter**3 * kelvin)
VOLUMETRIC_HEATING      = POWER / meter**3

# =============== Derived named units ===============

newton          = N     = FORCE
joule           = J     = ENERGY
watt            = W     = POWER
pascal          = Pa    = PRESSURE
hertz           = Hz    = FREQUENCY
coulomb         = C     = CHARGE
volt            = V     = VOLTAGE
ohm             = R     = RESISTANCE
farad           = F     = CAPACITANCE
henry           = H     = INDUCTANCE
tesla           = T     = MAGNETIC_FIELD
weber           = Wb    = MAGNETIC_FLUX
siemens         = S     = CONDUCTANCE

# =============== Heat transfer units ===============

volumetric_capacity     = VOLUMETRIC_HEAT_CAPACITY
volumetric_heating      = VOLUMETRIC_HEATING
convection_coefficient  = watt/(meter ** 2 * kelvin)

# ===================================================
