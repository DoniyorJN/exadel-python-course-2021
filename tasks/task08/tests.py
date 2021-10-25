import unittest
import math
from Square import *
from Circle import *


class TestRectangle(unittest.TestCase):
    __rectangle = Rectangle(Point2D(5, 5), 10, 20)

    def test_area(self):
        self.assertEqual(self.__rectangle.area(), 200)

    def test_contains(self):
        self.assertEqual(Point2D(5,5) in self.__rectangle, True)


class TestSquare(unittest.TestCase):
    __square = Square(Point2D(10, 10), 10)

    def test_area(self):
        self.assertEqual(self.__square.area(), 100)

    def test_contains(self):
        self.assertEqual(Point2D(5, 10) in self.__square, False)


class TestCircle(unittest.TestCase):
    __circle = Circle(Point2D(15, 15), 10)

    def test_area(self):
        self.assertEqual(self.__circle.area(), math.pi*10**2)

    def test_contains(self):
        self.assertEqual(Point2D(15, 10) in self.__circle, True)


if __name__ == '__main__':
    unittest.main()