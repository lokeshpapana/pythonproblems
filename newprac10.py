def swap(values):
    temp = values[0]
    values[0] = values[len(values) - 1]
    values[len(values) - 1] = temp
    return values
print(swap([1,2,3,4,5]))
