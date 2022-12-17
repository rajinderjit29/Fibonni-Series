numbers = [1, 1]
for i in range (10):
    c = numbers[-1]+numbers[-2]
    numbers.append(c)
for i in numbers :
    print(i, end = " ")