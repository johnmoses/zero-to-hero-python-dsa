""" 
20. Valid Parentheses
Easy

Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
def is_valid(s: str) -> bool:
    # Map closing brackets to corresponding open brackets
    pairs = {')': '(', ']': '[', '}': '{'}
    
    # Stack to track open brackets
    stack = []
    
    for char in s:
        # If closing bracket
        if char in pairs:
            # Check if matches top of stack
            if not stack or stack.pop() != pairs[char]:
                return False
        # If opening bracket    
        else:
            stack.append(char)
            
    # Check if any unclosed brackets
    return len(stack) == 0

print(is_valid("()[]{}"))