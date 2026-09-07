# pylint: skip-file
# picomats/__init__.py

from picounits import inject_unit_frame
from importlib import resources

# Injects the ontology unit frame into the system.
inject_unit_frame(resources.files("ontology") / ".picounits")