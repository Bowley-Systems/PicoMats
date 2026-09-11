"""
Filename: manager.py

Description:
    Managers the materials within the ontology.
"""


from typing import Any
from pathlib import Path
from importlib import resources
from picounits import Parser, DynamicLoader, inject_unit_frame

from picomats.core.structure import Node, NodalRepresentation
from picomats.configuration.picomats import ONTOLOGY, DERIVED_UNITS, UNIT_FRAME


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


class Manager:
    """ Manages material structural & values boundary """
    def __init__(self, ontology: Node | None = None) -> None:
        """ Initializes the manager """
        self.ontology: Node = ontology

        if ontology is None:
            # Imports the ontology for base manager.
            self._load_from_package()

    def info(self) -> None:
        """ Displays the material ontology """
        if isinstance(self.ontology, Node):
            self.ontology.info()
            return

        msg = "Failed to display ontology due to loading error."
        raise ImportError(msg)

    def __getattr__(self, key: str) -> Any:
        """ Allows dynamic attribute accesses """
        if self.ontology is None:
            msg = f"{key!r} not found within material library."
            raise AttributeError(msg)

        for child in self.ontology.children:
            # Checks if the key is a child and builds the sub-manager.
            if child.name == key:
                sub_manager = Manager(ontology=child)
                setattr(self, key, sub_manager)
                return sub_manager

        for endpoint in self.ontology.endpoint:
            # Checks if the key is an endpoint and imports the material.
            if endpoint.stem == key:
                material = Parser.open(Path(endpoint), loader=Material)
                setattr(self, key, material)
                return material

        msg = f"{key!r} not found within material library."
        raise AttributeError(msg)

    def _load_from_package(self) -> None:
        """ Loads the material ontology """
        try:
            ontology = resources.files(ONTOLOGY)

            # Injects unit frame & derived units
            inject_unit_frame(ontology / UNIT_FRAME)
            Parser.import_derived(ontology / DERIVED_UNITS)

            # Scans ontology structure
            self.ontology = NodalRepresentation.scan(ontology)

        except Exception as err:
            msg = f"Failed to load library from package resources: {err!r}"
            raise RuntimeError(msg) from err
