"""
Filename: structure.py

Description:
    Searches the ontology for .uiv 
    files and creates a structural
    scheme for the manager.
"""

from __future__ import annotations
from dataclasses import dataclass
from importlib.resources.abc import Traversable


@dataclass(frozen=True, slots=True)
class LoaderContext:
    """ Stores the context of the loader structure """
    indent: str = ""
    in_last: bool = True

    def next_level(self) -> LoaderContext:
        """ Creates context for the next level of nesting """
        new_indent = self.indent + ("    " if self.in_last else "│   ")
        return LoaderContext(new_indent, True)

    def with_last(self, is_last: bool) -> LoaderContext:
        """ Creates context with updated last flag """
        return LoaderContext(self.indent, is_last)

    def connector(self) -> str:
        """ Returns the tree connector character """
        return "└── " if self.in_last else "├── "


class Node:
    """ Nodal Representation of Ontology """
    def __init__(self, name: str) -> None:
        """ Initializes the node """
        self.name: str = name
        self.children: list[Node] = []
        self.endpoint: list[Traversable] = []

    def info(self) -> None:
        """ Recursively prints the structure of the node as a tree. """
        context = LoaderContext()
        print(f"{self.name}:.")

        # Prints the tree structure
        self.print_contents(context)

    def print_contents(self, context: LoaderContext) -> None:
        """ Prints endpoints and child nodes with proper formatting. """
        items = self._get_items()
        for index, item in enumerate(items):
            # Constructs the formatting for that item
            last_item = index == len(items) - 1
            item_context = context.with_last(last_item)
            connector = item_context.connector()

            if isinstance(item, str):
                # returns the endpoint
                print(f"{item_context.indent}{connector}{item}")

            else:
                # Returns the children
                print(f"{item_context.indent}{connector}{item.name}")
                item.print_contents(item_context.next_level())

    def _get_items(self) -> list[str | Node]:
        """ Gets node endpoints and children as a list. """
        items = []
        for endpoint in self.endpoint:
            items.append(endpoint.name)

        return items + self.children


class NodalRepresentation:
    """ Represents the file structure as a nodal network """
    @classmethod
    def scan(cls, parent: Traversable, target: str =".uiv") -> Node:
        """ Scans the library resources and creates ontology network """
        node = Node(parent.name)

        for item in parent.iterdir():
            if item.name == "__pycache__" or item.name.startswith("."):
                # Skips hidden items or pycache folders.
                continue

            if item.is_dir():
                # Adds a sub_nodes as children
                sub_node = NodalRepresentation.scan(item, target)
                node.children.append(sub_node)
                continue

            if item.name.endswith(target):
                # Adds nodal endpoints for items
                node.endpoint.append(item)
                continue

        return node
