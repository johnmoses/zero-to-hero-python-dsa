"""
Bit manipulation

Design bit manipulation system for
- Checking if a number is even
- Checking if a number is odd
- Counting the number of set bits in a number
- Finding the number of trailing zeros in a number
- Reversing bits
"""
class BitManipulation:
    def is_even(self, num):
        return (num & 1) == 0

    def is_odd(self, num):
        return (num & 1) == 1

    def count_set_bits(self, num):
        count = 0
        while num:
            count += num & 1
            num >>= 1
        return count

    def find_trailing_zeros(self, num):
        count = 0
        while (num & 1) == 0:
            count += 1
            num >>= 1
        return count

    def reverse_bits(self, num):
        reversed_num = 0
        while num:
            reversed_num <<= 1
            reversed_num |= num & 1
            num >>= 1
        return reversed_num

bm = BitManipulation()
print(bm.is_even(4))  # True
print(bm.is_odd(5))   # True
print(bm.count_set_bits(7))  # 3
print(bm.find_trailing_zeros(16))  # 4
print(bm.reverse_bits(10))  # 5 (binary: 1010 -> 0101)
