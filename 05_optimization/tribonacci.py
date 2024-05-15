""" 
Tribonacci sequence using Dynamic Programming
"""

def tribonacci(num:int) -> list[int]:
    """ 
    Return first n tribonacci numbers
    """
    dp = [0] * num
    dp[2] = 1

    for i in range(3, num):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp

print(tribonacci(8))