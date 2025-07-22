def find(values):
    max = values[0]
    for i in range(0, len(values)):
        if(values[i] > max):
            max = values[i]
    secondlargest = values[0]
    for i in range(0, len(values)):
        if(values[i] < max and values[i] > secondlargest):
            secondlargest = values[i]
    return secondlargest
print(find([1,2,3,8,5,6,9]))
