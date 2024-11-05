"""
Bit manipulation operations
"""
def set_bit(number: int, position: int) -> int:
    """
    Set the bit at position to 1
    """
    return number | (1 << position)

def clear_bit(number: int, position: int) -> int:
    """
    Set the bit at position to 0.

    Details: perform bitwise and for given number and X.
    Where X is a number with all the bits - ones and bit on given
    position - zero.
    """
    return number & ~(1 << position)

def flip_bit(number: int, position: int) -> int:
    """
    Flip the bit at position.

    Details: perform bitwise xor for given number and X.
    Where X is a number with all the bits - zeroes and bit on given
    position - one.
    """
    return number ^ (1 << position)

def is_bit_set(number: int, position: int) -> bool:
    """
    Is the bit at position set?

    Details: Shift the bit at position to be the first (smallest) bit.
    Then check if the first bit is set by anding the shifted number with 1.
    """
    return ((number >> position) & 1) == 1

def get_bit(number: int, position: int) -> int:
    """
    Get the bit at the given position

    Details: perform bitwise and for the given number and X,
    Where X is a number with all the bits - zeroes and bit on given position - one.
    If the result is not equal to 0, then the bit on the given position is 1, else 0.

    """
    return int((number & (1 << position)) != 0)

print(set_bit(0b1111, 1))
print(clear_bit(0b0, 5))
print(flip_bit(0b101, 0))
print(is_bit_set(0b0, 17))
print(get_bit(0b1010, 3))