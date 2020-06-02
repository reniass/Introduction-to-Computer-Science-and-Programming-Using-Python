def f(a, b):
    return a + b

def dict_interdiff(d1, d2):

    dict1 = {}
    dict2 = {}
    for k in d1.keys():
        if k in d2.keys():
            dict1[k] = f(d1[k], d2[k])
        elif k not in d2.keys():
            dict2[k] = d1[k]
        else:
            continue

    for k in d2.keys():
        if k not in d1.keys():
            dict2[k] = d2[k]
    return (dict1, dict2)

print(dict_interdiff({1:30, 2:20, 3:30, 5:80}, {1:40, 2:50, 3:60, 4:70, 6:90}))





