Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Solution

Approach 1: Bit by Bit

Intuition

Though the question is not difficult, it often serves as a warm-up question to kick off the interview. The point is to test one's basic knowledge on data type and bit operations.

As one of the most intuitive solutions that one could come up during an interview, one could reverse the bits one by one.

The key idea is that for a bit that is situated at the index i, after the reversion, its position should be 31-i (note: the index starts from zero).
We iterate through the bit string of the input integer, from right to left (i.e. n = n >> 1). To retrieve the right-most bit of an integer, we apply the bit AND operation (n & 1). 

For each bit, we reverse it to the correct position (i.e. (n & 1) << power). Then we accumulate this reversed bit to the final result. 

When there is no more bits of one left (i.e. n == 0), we terminate the iteration. 

