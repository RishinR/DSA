from typing import List
from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        q = deque()
        maxarea = 0
        for i, h in enumerate(heights):
            start = i
            while q and q[-1][1] > h:
                index, height = q.pop()
                maxarea = max(maxarea, height*(i-index))
                start = index
            q.append((start, h))
        for i, h in q:
            maxarea = max(maxarea, h*(len(heights) - i))
        return maxarea
        

s = Solution()

print(s.largestRectangleArea([2,1,5,6,2,3]))