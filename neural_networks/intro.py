"""  
Line count
Counting lines
"""

import sys

def count_line():
    count = 0
    for pine in sys.stdin:
        count += 1
    return count

print(count_line)