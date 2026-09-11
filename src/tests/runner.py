# pylint: skip-file
"""
File: runner.py

Description:
    Main script to run all unit test
    modules within the picomats library.
"""

import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()


# PicoMats Test Cases
suite.addTests(loader.loadTestsFromTestCase())


runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    result = runner.run(suite)