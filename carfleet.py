from typing import List
from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        q = deque()
        for i in range(len(position)):
            cars.append((position[i], speed[i], (target-position[i])/speed[i]))
        cars.sort(reverse=True)
        # print(cars)
        q.append(cars[0])
        for i in range(1, len(cars)):
            if q and q[-1][2] < cars[i][2]:
                q.append(cars[i])
        return len(q)

s = Solution()

print(s.carFleet(100, [0,2,4], [4,2,1]))