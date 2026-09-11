"""
Filename: errors.py

Description:
    Defines the errors classes
    to ensure descriptive error
    messages.
"""

# Generic Errors
class ManagerError(ValueError):
    """ Exception for Material Manager error """
    CODE = "PM001"

    def __init__(self, error: str):
        """ Returns a custom error message """
        msg = f"[{self.CODE}] Material Manager raised error: {error}. "
        super().__init__(msg)
