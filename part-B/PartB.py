import unittest
from PartA import House

class PartB(unittest.TestCase):
    def test_instance(self):
        house = House()
        self.assertTrue(isinstance(house, House))

    def test_notInstance(self):
        number = 2
        self.assertFalse(isinstance(number, House))

    def test_identical(self):
        h1 = House()
        h2 = House()
        self.assertEqual(print(h1), print(h2))

    def test_setHouseNo(self):
        house = House()
        house.setHouseNo(456)
        self.assertEqual(house.houseNo, 456)

    def test_setStreet(self):
        house = House()
        house.setStreet("Small Street")
        self.assertEqual(house.street, "Small Street")

    def test_setArea(self):
        house = House()
        house.setArea("D02")
        self.assertEqual(house.area, "D02")


if __name__ == '__main__':
    unittest.main()