# pylint: skip-file
"""
Filename: Introduction.py

Descriptions:
    Introduces the mechanics of picomats via a few examples
"""

from picomats import mm
from picomats import Materials

Materials.info()

boron = Materials.fundamental.boron
boron.info()