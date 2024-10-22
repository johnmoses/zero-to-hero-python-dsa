"""
Nth Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        two_p, five_p, three_p = 0, 0, 0
        n-=1

        while n:
            two, three, five = 2*res[two_p], 3*res[three_p], 5*res[five_p]
            #print(res, two, three, five)
            min_num = min(two, min(three, five))

            res.append(min_num)

            if two==min_num:
                two_p+=1
            if three==min_num:
                three_p+=1
            if five==min_num:
                five_p+=1

            n-=1
        return res[-1]

n = 10
sn = Solution()
print(sn.nthUglyNumber(n))
# Output: 12