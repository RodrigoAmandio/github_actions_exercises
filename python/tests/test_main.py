import unittest

from python.main import soma

class TestStringMethods(unittest.TestCase):

    def test_soma(self):
        x = 5
        y = 8

        result = soma(x,y)

        self.assertEqual(result,12)