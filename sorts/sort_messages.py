""" 
Sort messages threads from server in chronological order

messages = [['root',1], [2,3], [3,0]]
"""

messages = [['root',1], [2,3], [3,0]]

def sort_messages(messages):
    res = []
    for i in messages:
        for j in i:
            if j == 'root':
                res.append(i[1])

    return res
print(sort_messages(messages))