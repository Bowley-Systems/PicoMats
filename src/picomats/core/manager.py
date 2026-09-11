"""
Filename: manager.py

Description:
    Managers the materials 
    within the ontology.
"""

from typing import Any

from pathlib import Path
from importlib import resources
from picounits import Parser, inject_unit_frame

from picomats.core.modules.structure import Node, NodalRepresentation
from picomats.core.modules.material import Material

from picomats.configuration.picomats import ONTOLOGY, DERIVED_UNITS, UNIT_FRAME
from picomats.utilities.errors import ManagerError


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
        raise ManagerError(msg)

    def __getattr__(self, key: str) -> Any:
        """ Allows dynamic attribute accesses """
        if self.ontology is None:
            msg = f"{key!r} not found within material ontology."
            raise ManagerError(msg)

        for child in self.ontology.children:
            # Checks if the key is a child and builds the sub-manager.
            if Node.remove_ordering(child.name) == key:
                sub_manager = Manager(ontology=child)
                setattr(self, key, sub_manager)
                return sub_manager

        for endpoint in self.ontology.endpoint:
            # Checks if the key is an endpoint and imports the material.
            if Node.remove_ordering(endpoint.stem) == key:
                material = Parser.open(Path(endpoint), loader=Material)
                setattr(self, key, material)
                return material

        msg = f"{key!r} not found within material ontology."
        raise ManagerError(msg)

    @classmethod
    def _remove_ordering(cls, name: str) -> str:
        """ Removes the non-semantic ordering prefix from a name. """
        return name.split("-", 1)[-1]

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
            msg = f"Failed to load ontology from package resources: {err!r}"
            raise ManagerError(msg) from err
