class Solution(object):
    def reverse(self, x):
        if x in range(-2**31, 2**31):
           result = 0
           while x != 0:
               rem = x % 10
               result = (result * 10) + rem
               x = x // 10
           return result
        else:
           return 0

print(Solution().reverse(123))
