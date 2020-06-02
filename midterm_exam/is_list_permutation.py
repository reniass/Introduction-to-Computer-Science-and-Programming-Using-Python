def is_list_permutation(L1, L2):
    v = 0
    copy_L2 = L2.copy()
    for e in L1:
        if e in L2:
            v += 1
            L2.remove(e)

    if v == len(L1):

        most_common_sign = ''
        how_many_most_common_sign = []
        for m in L1:
            L3 = []
            for n in copy_L2:
                if n == m:
                    L3.append(n)

            if len(L3) > len(how_many_most_common_sign):
                how_many_most_common_sign = L3
                most_common_sign = how_many_most_common_sign[0]

        return (most_common_sign, len(how_many_most_common_sign), type(most_common_sign))
    elif len(L1) == len(L2) == 0:
        return (None, None, None)
    else:
        return False



print(is_list_permutation([1, 'b', 1, 'c', 'c', 1],['c', 1, 'b', 1, 1, 'c']))