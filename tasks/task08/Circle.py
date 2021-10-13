from Shape2D import Shape2D, Point2D
import math


class Circle(Shape2D):
    def __init__(self, center: Point2D, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def __contains__(self, point: Point2D) -> bool:
        return (point.x - self.center.x)**2 + (point.y - self.center.y)**2 <= self.radius**2

    def __str__(self) -> str:
        return f"Center: [x: {self.center.x}, y: {self.center.y}] and Radius: {self.radius}"