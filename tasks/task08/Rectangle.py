from Shape2D import Shape2D, Point2D

class Rectangle(Shape2D):
    def __init__(self, bottom_left: Point2D, width: float, length: float):
        self.bottom_left = bottom_left
        self.width = width
        self.length = length

    def area(self) -> float:
       return self.width * self.length
 
    def __contains__(self, point: Point2D) -> bool:
        if(self.bottom_left.x <= point.x <= self.bottom_left.x + self.length and self.bottom_left.y - self.width <= point.y <= self.bottom_left.y):
            return True
        return False
 
    def __str__(self) -> str:
        return f"Bottom left[x: {self.bottom_left.x}, y: {self.bottom_left.y}], Width: {self.width}, Length: {self.length}"