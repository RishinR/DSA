# leetcode 2013
from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point[0], point[1]
        result = 0

        for (x, y), cnt in self.points.items():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            result += cnt*self.points.get((px, y), 0)*self.points.get((x, py), 0)
        return result
