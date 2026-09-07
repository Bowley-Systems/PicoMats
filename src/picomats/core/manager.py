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
from picomats.constants.picomats import ONTOLOGY, DERIVED_UNITS, UNIT_FRAME


class Material(DynamicLoader):
    """ Defines the Material structure via inheritance """
    def __repr__(self) -> str:
        """ Returns the material name and attributes """
        attributes = self._attributes()

        items = ', '.join(attributes)
        return f'{self.lx_name}({items})'


class Manager:
    """ Manages material structural & values boundary """
    def __init__(self, ontology: Node | None = None) -> None:
        """ Initializes the manager """
        self.ontology: Node = None

        if ontology is None:
            self._load_from_package()
        else:
            self.ontology = ontology

        # Attaches the attributes to the Manager.
        self._manger_attributes()

    def info(self) -> None:
        """ Displays the material ontology """
        if isinstance(self.ontology, Node):
            self.ontology.info()
            return

        msg = "Failed to display ontology due to loading error."
        raise ImportError(msg)

    def _manger_attributes(self) -> None:
        """ Imports all attributes from the nodal representation """
        # Attach child directories as nested Manager instances
        for child in self.ontology.children:
            setattr(self, child.name, Manager(ontology=child))

    def _material_attributes(self, endpoint: str) -> None:
        """ Imports all attributes from the dynamic loader representation """
        attributes = Parser.open(Path(endpoint), loader=Material)

        for name in dir(attributes):
            if name.startswith('_') or name.startswith('lx_'):
                # Skips private/magic attributes and loader internals
                continue

            try:
                # Set it as an attribute on this instance
                node = getattr(attributes, name)
                setattr(self, name, node)

            except AttributeError:
                # Attempts to set next attribute
                continue

    def __getattr__(self, key: str) -> Any:
        """ Allows dynamic attribute accesses """
        if self.ontology is None:
            raise AttributeError(f"{key!r} not found within material library.")

        msg = f"{key!r} not found within material library."
        raise AttributeError(msg)

    def _load_material_from_package(self) -> None:
        return

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
