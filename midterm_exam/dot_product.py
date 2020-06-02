def dot_product(listA, listB):
    sum = 0
    for n in range(len(listA)):
        sum += listA[n] * listB[n]
    return sum

print(dot_product([1, 2, 3],[4, 5, 6]))

