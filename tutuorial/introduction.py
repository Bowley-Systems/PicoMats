# pylint: skip-file
"""
Filename: Introduction.py

Descriptions:
    Introduces the mechanics of picomats via a few examples
"""

from picomats import m
from picomats import Materials

# Pulls materials into the simulation
copper = Materials.abstract.pure.copper

density = copper.physical.density
volume = 0.1 * m ** 3

mass = volume * density
print(mass)