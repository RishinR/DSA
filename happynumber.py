class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n**2 < 49:
            return False
        else:
            n = n**2
        while n != 1:
            sum = 0
            s = str(n)
            for i in s:
                sum += int(i)
            if sum == 1:
                return True
            elif sum*sum < 49:
                return True
            else:
                n = n**2
if __name__ == "__main__":
    s = Solution()
    flag = s.isHappy(19)
    print(flag)
            
        
