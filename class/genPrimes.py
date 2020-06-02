def genPrimes():
    n = 1
    while True:
        n += 1
        dividers = []
        for d in range(1, n + 1):
            if n % d == 0:
                dividers.append(d)
        if len(dividers) == 2:
            yield n

prime = genPrimes()
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
