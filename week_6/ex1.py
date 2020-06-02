def foo(L):
    val = L[0]
    while (True):
        val = L[val]
        print(val)
        



print(foo([1, 2, 3, 4, 0]))