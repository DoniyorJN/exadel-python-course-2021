from Point2D import Point2D
from Rectangle import Rectangle
class Square(Rectangle):
   def __init__(self, bottom_left: Point2D, width: float):
       super().__init__(bottom_left, width, width)
        