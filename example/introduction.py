# pylint: skip-file
"""
Filename: Introduction.py

Descriptions:
    Introduces the mechanics of picomats via a few examples
"""

from picomats import mm
from picomats import Materials

Materials.info()

copper = Materials.abstract.pure.copper
density = copper.physical.density

copper.info()

volume = 100 * mm ** 3
mass = volume * density

mass.info()

print(f"\nobject mass: {mass}")
