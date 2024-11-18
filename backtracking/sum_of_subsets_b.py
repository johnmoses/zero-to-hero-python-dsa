""" 
Sum of subsets
https://medium.com/@dillihangrae/sum-of-subsets-problem-dynamic-programming-e682940730cb
"""

def sum_of_sub(w, m):
    n = len(w)
    x = [0] * n
    solutions = []

    def sum_of_sub_recursive(s, k, r, prefix="", is_left=True):
        # Determine the prefix for branches
        connector = "├── " if is_left else "└── "
        print(f"{prefix}{connector}({s}, {k}, {r})")

        # Check if the current sum equals the target sum
        if s == m:
            solutions.append([w[i] for i in range(n) if x[i] == 1])
            print(f"{prefix}    Solution: {[w[i] for i in range(n) if x[i] == 1]}")
            return

        # Continue with the recursive exploration
        if k < n:
            # Include w[k]
            x[k] = 1
            if s + w[k] <= m:
                sum_of_sub_recursive(s + w[k], k + 1, r - w[k], prefix + ("│   " if is_left else "    "), True)

            # Exclude w[k]
            x[k] = 0
            if s + r - w[k] >= m:
                sum_of_sub_recursive(s, k + 1, r - w[k], prefix + ("│   " if is_left else "    "), False)

    # Start recursive call with the root node
    print("(0, 0, {})".format(sum(w)))
    sum_of_sub_recursive(0, 0, sum(w))
    return solutions

# Example usage
w = [1, 9, 7, 5, 18, 12, 20, 15]
# w = [3, 34, 4, 12, 5, 2]
# m = 30
m = 35

solutions = sum_of_sub(w, m)

print("\nSolutions:")
for sol in solutions:
    print(sol)

# Print the total number of solutions
print(f"\nTotal number of solutions: {len(solutions)}")

# Code explanation
code_explain = """
Tree Branching Symbols:

├── represents a branch going left.
└── represents the end of a branch going right.
│ is used to continue vertical lines from previous levels.
Recursive Calls:

The prefix is updated in each call to align subsequent nodes correctly.
The structure dynamically builds the tree as the recursion progresses.
Visual Representation:

This method allows for a visual tree that mirrors the hierarchical branching of the recursive function exactly.
"""
# print(code_explain)