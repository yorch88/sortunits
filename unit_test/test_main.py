import unittest
from main import SortUnits

class TestSortingUnits(unittest.TestCase):
    def test__sort__standard_units(self):
        self.assertEqual(SortUnits.sort(100, 100, 100, 10), "STANDARD")
        self.assertEqual(SortUnits.sort(50, 50, 50, 5), "STANDARD")
    
    def test__sort__special_units(self):
        self.assertEqual(SortUnits.sort(200, 50, 50, 10), "SPECIAL")  # Bulky
        self.assertEqual(SortUnits.sort(100, 100, 100, 25), "SPECIAL")  # Heavy
        self.assertEqual(SortUnits.sort(150, 100, 50, 19), "SPECIAL")  # Bulky
    
    def test__sort__rejected_units(self):
        self.assertEqual(SortUnits.sort(200, 200, 200, 30), "REJECTED")  # Bulky & Heavy
        self.assertEqual(SortUnits.sort(150, 150, 150, 20), "REJECTED")  # Bulky & Heavy

if __name__ == "__main__":
    unittest.main()