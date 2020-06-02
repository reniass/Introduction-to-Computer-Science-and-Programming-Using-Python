def largest_odd_times(L):
    max_number = 0
    Numbers = []
    for n in L:
        for m in L:
            if m == n:
                Numbers.append(m)
        if not len(Numbers) % 2 == 0 and n > max_number:
            max_number = n
        Numbers = []
    if max_number == 0:
        return None
    else:
        return max_number

print(largest_odd_times([2,2,4,4]))