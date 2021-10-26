from typing import NamedTuple

class Point2D(NamedTuple):
    """
    A point in 2-dimensional space. Implemented as NamedTuple 
    (so it is immutable), but simple class can be used instead.
    """
    x: float
    y: float

    def __str__(self):
        return f"({self.x}, {self.y})" 