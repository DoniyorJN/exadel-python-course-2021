from Shape2D import Shape2D, Point2D

class ShapeCollection(Shape2D):

    def __init__(self, stores: list[Shape2D]):
        self._stores = stores

    def area(self) -> float:
        sum_area: float = 0
        for shape in self._stores:
            sum_area += shape.area()
        return sum_area
    
    def __contains__(self, point: Point2D) -> bool:
        for shape in self._stores:
            if point in shape:
                return True
        return False

    def __str__(self) -> str:
        all_str: str = ""
        for shape in self._stores:
            all_str += shape.__str__() + "\n"
        return all_str