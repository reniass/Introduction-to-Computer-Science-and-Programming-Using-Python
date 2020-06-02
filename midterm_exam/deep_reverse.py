"""
L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
def deep_reverse(L):
    reverse_L = L[::-1]
    final_L = []
    print(L)
    for e1 in reverse_L:
        reverse_list_inside_reverse_L = e1[::-1]
        final_L.append(reverse_list_inside_reverse_L)
    L = final_L

    #return  final_L

#print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))




#L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)
"""

def deep_reverse(L):
    L.reverse()
    for n in range(len(L)):
        L[n].reverse()






#print(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]))

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)