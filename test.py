import unittest
from main import kelv_cell, farr_cell


class TestConverter(unittest.TestCase):
    def test_temp_type(self):
        self.assertTrue(isinstance(farr_cell(10, 'c'), float))
        self.assertTrue(isinstance(kelv_cell(10, 'c'), float))

    def test_kelv_cell(self):
        self.assertEqual(kelv_cell(10, 'c'), -263.15)
        self.assertEqual(kelv_cell(10, 'f'), 283.15)

    def test_farr_cell(self):
        self.assertEqual(farr_cell(10, 'c'), -12.222222222222223)
        self.assertEqual(farr_cell(10, 'K'), 50.0)
