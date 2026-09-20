# pylint: skip-file
"""
Filename: Introduction.py

Descriptions:
    Introduces the mechanics of 
    picomats via a few examples
"""

def next_step(title: str, first: bool = False):
    """ Helper functions for examples (Doesn't relate to library) """
    notation = "" if first else "\n"
    print(f"{notation}{'='*10} {title} {'='*10}")
    input(">>> Press Enter to see this example...")
    
next_step("0: How to view the materials in the ontology", True)

from picomats import Materials

# .info() to view the entries
Materials.info()

next_step("1: How to view entries within entry", True)


from picomats import Materials

# .info() to view the entries
Materials.abstract.pure.copper.info()




next_step("2: How to use values from entry", True)

from picomats import m
from picomats import Materials

# Pulls materials into the simulation
copper = Materials.abstract.pure.copper

# Pulls the density & Calculates mass
density = copper.physical.density

volume = 0.1 * m ** 3
mass = volume * density

print(mass)

print("\n" + "=" * 30)
print("Tutorial Complete!")