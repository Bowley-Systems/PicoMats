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

        if self.lx_name is not None:
            # Removes ordering when lx_name is not none
            self.lx_name = Node.remove_ordering(self.lx_name)

        # Removes attributes not needed during runtime
        self.non_mapped_attributes()

    def non_mapped_attributes(self):
        """ Attributes not required for runtime """
        if hasattr(self, 'version'):
            # Removes version attribute from material
            del self.version

        if hasattr(self, 'sources'):
            # Removes source attributes from material
            del self.sources

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
