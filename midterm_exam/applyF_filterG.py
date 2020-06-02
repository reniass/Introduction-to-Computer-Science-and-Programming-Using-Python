def f(i):
    return i + 5

def g(i):
    return  i > 5

def applyF_filterG(L, f, g):
    copy_L = L.copy()
    new_elements_of_L = []
    number_elements_in_new_L = 0
    for e in range(len(copy_L)):
        copy_L[e] = f(copy_L[e])
        if g(copy_L[e]) == True:
            new_elements_of_L.append(L[e])
            number_elements_in_new_L += 1
    del L[:]
    for el in range(len(new_elements_of_L)):
        L.append(new_elements_of_L[el])
    if len(L) == 0:
        return -1
    else:
        return max(L)




L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
