# pylint: skip-file
# picomats/__init__.py

from picounits import inject_unit_frame
from importlib import resources

# Now "ontology" is a proper package that can be found
library = resources.files("ontology")
unit_frame = library / ".picounits"

inject_unit_frame(unit_frame)