# pylint: skip-file
"""
Filename: Introduction.py

Descriptions:
    Introduces the mechanics of picomats via a few examples
"""

from picomats import mm
from picomats import Materials


Materials.info()
Materials.abstract.info()

copper = Materials.abstract.pure.copper

copper.info()
density = copper.physical.density

volume = 100 * mm ** 3
mass = volume * density
print(f"object mass: {mass}")