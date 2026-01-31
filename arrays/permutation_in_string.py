# leetcode 567
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        if len1 > len2:
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:len1])

        if c1 == c2:
            return True

        for i in range(len1, len2):
            c2[s2[i]] += 1
            c2[s2[i - len1]] -= 1
            if c2[s2[i - len1]] == 0:
                del c2[s2[i - len1]]
            if c1 == c2:
                return True

        return False