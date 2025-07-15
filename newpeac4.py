def odd_finds(a, b):
    values = []
    count = 0
    for i in range(a, b):
        if(i % 2 == 1):
            values.append(i)
            count += 1
    return values, count,
a = int(input("Enter any number"))
b = int(input("Enter any number"))
print(odd_finds(a, b))
