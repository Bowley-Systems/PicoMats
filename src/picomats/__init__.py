# pylint: skip-file
# picomats/__init__.py

from picounits import inject_unit_frame
from importlib import resources

# Injects the ontology unit frame into the system.
inject_unit_frame(resources.files("ontology") / ".picounits")

from importlib import resources


def scan_ontology_tree(traversable, indent=0):
  """Recursively scans and prints the contents of a Traversable path."""
  for item in traversable.iterdir():
    # Print with indentation to show hierarchy
    prefix = "  " * indent
    if item.is_dir():
      print(f"{prefix}📁 {item.name}/")
      # Recurse deeper into the subdirectory
      scan_ontology_tree(item, indent + 1)
    else:
      print(f"{prefix}📄 {item.name}")


# Start scanning from the root of the "ontology" package
root_dir = resources.files("ontology")
print("Scanning ontology package structure:")
scan_ontology_tree(root_dir)