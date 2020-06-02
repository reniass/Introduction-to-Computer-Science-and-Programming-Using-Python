def isTriangular(k):
    L = []
    total_score = 0
    for number in range(1,k+1):
        total_score += number
        L.append(total_score)
    if k in L:
        return True
    else:
        return False



print(isTriangular(15))

