def dict_invert(d):
    print(d)
    new_d = {}
    for k,v in d.items():
        if v in new_d.keys():
            new_d[v].append(k)
        else:
            new_d[v] = [k]
    print(new_d)





dict_invert({4:True, 2:True, 0:True})