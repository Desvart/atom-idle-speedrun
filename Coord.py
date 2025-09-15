from typing import Self

from pyscreeze import Box, Point


class Coord:

    def __init__(self, x: int = 0, y: int = 0):
        self.left: int = x
        self.top: int = y


    @classmethod
    def from_box(cls, box: Box) -> Self:
        return cls(box.left, box.top)


    @classmethod
    def from_point(cls, point: Point) -> Self:
        return cls(point.x, point.y)


    def add(self, other: Self) -> Self:
        return Coord(self.left + other.left, self.top + other.top)


    def __str__(self) -> str:
        return f'(left = {self.left},top = {self.top})'