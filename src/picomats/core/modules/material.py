"""
Filename: material.py

Description:
    Defines the Material class within
    the ontology based on picounits
    DynamicLoader.
"""

from picounits import DynamicLoader

from picomats.core.modules.structure import Node


class Material(DynamicLoader):
    """ Defines the Material structure via inheritance """
    def __init__(self, dictionary, name=None):
        """ Removes the ontology ordering from material name """
        super().__init__(dictionary, name)

        if name is not None:
            # Removes ordering when name is not none
            self.lx_name = Node.remove_ordering(name)
    
        if self.lx_name is not None:
            # Removes ordering when lx_name is not none
            self.lx_name = Node.remove_ordering(self.lx_name)

    def __repr__(self) -> str:
        """ Returns the material name and attributes """
        attributes = self._attributes()

        filtered_attributes = []
        for attribute in attributes:
            # Removes the required version in `.uiv` tag from materials.
            if str(attribute).lower() == "version":
                continue

            filtered_attributes.append(attribute)

        items = ', '.join(filtered_attributes)
        return f'{self.lx_name}({items})'
