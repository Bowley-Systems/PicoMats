"""
Filename: manager.py

Description:
    Managers the materials within the ontology.
"""


from typing import Any
from importlib import resources
from picounits import Parser, DynamicLoader, inject_unit_frame

from picomats.core.structure import Node, NodalRepresentation
from picomats.constants.picomats import ONTOLOGY_LOCATION, DERIVED_UNITS_LOCATION


class Material(DynamicLoader):
    """ Defines the Material structure via inheritance """
    def __repr__(self) -> str:
        """ Returns the material name and attributes """
        attributes = self._attributes()

        items = ', '.join(attributes)
        return f'{self.lx_name}({items})'


class Manager:
    """ Manages material structural & values boundary """
    def __init__(self) -> None:
        """ Initializes the manager """
        self.ontology: Node = None

        # Loads the package ontology & attaches attributes
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
        msg = f"{key!r} not found within material library."
        raise AttributeError(msg)

    def _load_from_package(self) -> None:
        """ Loads the material ontology """
        try:
            ontology = resources.files(ONTOLOGY_LOCATION)

            # Injects unit frame and scans ontology
            inject_unit_frame(ontology / DERIVED_UNITS_LOCATION)
            self.ontology = NodalRepresentation.scan(ontology)

        except Exception as err:
            msg = f"Failed to load library from package resources: {err!r}"
            raise RuntimeError(msg) from err
