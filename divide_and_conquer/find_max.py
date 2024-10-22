def find_max(data):
    #return
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest

listData = [1,2,6,4,3,5,8,14,7]
print(find_max(listData))