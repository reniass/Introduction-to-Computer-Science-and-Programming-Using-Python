'''
def max_val(t):
    maxValue = 0
    for el in t:
        if type(el) == int:
           if el > maxValue:
                maxValue = el
        elif type(el) == tuple:
            for k in range(len(el)):
                if el[k] > maxValue:
                    maxValue = el[k]
        else:
            for l in range(len(el)):
                if el[l][0] > maxValue:
                    maxValue = el[l][0]
    return maxValue

print(max_val((9, [3, 8, 2]))
'''

def max_val(t):
    import string
    digits = string.digits
    maxValue = 0
    s = str(t)
    for el in range(len(s)):
        string_number = ''
        if s[el] in digits:
            string_number += s[el]
            part_s = s[el + 1:]
            for ele in range(len(part_s)):
                if part_s[ele] in digits:
                    string_number += part_s[ele]
                else:
                    break
        if string_number != '':
            if int(string_number) > maxValue:
                maxValue = int(string_number)



    return maxValue

print(max_val((4, 20, 3, 1, 7, 7, 20, 3)))