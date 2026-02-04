# leetcode 150

from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = set(['-', '+', '*', '/'])
        for i in tokens:
            if i in symbols:
                param2 = stack.pop()
                param1 = stack.pop()
                stack.append(str(int(eval(param1+i+param2))))
            else:
                stack.append(i)
        return int(stack[0])