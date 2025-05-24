import unittest

from python.main import (
    soma,
    concat
)


class TestStringMethods(unittest.TestCase):

    def test_soma(self):
        x = 4
        y = 8

        result = soma(x, y)

        self.assertEqual(result, 12)

    
    def test_concat(self):
        x = "Rodrigo"
        y = "Amandio"

        result = concat(x,y)

        self.assertEqual(result, "Rodrigo-Amandio")