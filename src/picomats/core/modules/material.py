"""
Filename: material.py

Description:
    Defines the Material class within
    the ontology based on picounits
    DynamicLoader.
"""

from picounits import DynamicLoader


class Material(DynamicLoader):
    """ Defines the Material structure via inheritance """
    def __repr__(self) -> str:
        """ Returns the material name and attributes """
        attributes = self._attributes()

        filtered_attributes = []
        for attribute in attributes:
            # Removes the required version in `.uiv` tag from materials.
            if str(attribute).lower() == "version": continue
            filtered_attributes.append(attribute)

        items = ', '.join(filtered_attributes)
        return f'{self.lx_name}({items})'
