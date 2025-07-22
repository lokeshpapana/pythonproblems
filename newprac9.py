def is_sorted(values):
    for i in range(0, len(values) - 1):
        if(values[i] > values[i + 1]):
            return False
    return True
print(is_sorted(['b', 'c']))
