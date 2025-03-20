""" 
Tribonacci sequence using dynamic programming

Return first n tribonacci numbers
"""

def tribonacci1(n):
    """
    Calculates the first n Tribonacci numbers.

    Args:
        n (int): The number of Tribonacci numbers to calculate.

    Returns:
        list: A list containing the first n Tribonacci numbers.
    """
    # Initialize the list with the first three Tribonacci numbers
    trib = [0, 0, 1]

    # If n is less than or equal to 3, return the first n elements of the list
    if n <= 3:
        return trib[:n]

    # Calculate the remaining Tribonacci numbers using dynamic programming
    for i in range(3, n):
        # The next Tribonacci number is the sum of the previous three numbers
        trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])

    return trib

def tribonacci2(num:int) -> list[int]:
    """ 
    Return first n tribonacci numbers
    """
    dp = [0] * num
    dp[2] = 1

    for i in range(3, num):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp

print(tribonacci1(5))
print(tribonacci2(5))