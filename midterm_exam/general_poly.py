
def general_poly(L, x):

    exponent = len(L) - 1
    function_value = 0
    s = 'F(%r)= ' %x

    for i in range(len(L)):
        function_value += L[i] * x ** exponent
        exponent -= 1
        if i == len(L) - 1:
            s1 = ' ' + str(L[i]) + ' *' ' ' + str(x ** exponent) + ' ='
        else:
            s1 = ' ' + str(L[i]) + ' *' ' ' + str(x ** exponent) + ' ='
        s += s1

    return function_value, s

#print(general_poly([1, 2, 3, 4], 10))

def print_general_poly(f):
    print_string = f
    value = f
    print(print_string + value)

print_general_poly(general_poly([1, 2, 3, 4], 10))