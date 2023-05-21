from typing import List
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        q = deque()
        for i in range(len(temperatures)):
            while q and temperatures[i] > temperatures[q[-1]]:
                x = q.pop()
                output[x] = i - x
            q.append(i)
        return output
    
s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))