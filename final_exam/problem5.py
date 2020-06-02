def cipher(map_from, map_to, code):
    key_code = {}
    k = 0
    for e in map_from:
        key_code[e] = map_to[k]
        k += 1
    decoded = ''
    for el in code:
        decoded += key_code[el]
    return (key_code, decoded)


print(cipher("abcd", "dcba", "dab"))