'''
def sort(L):
    for i in range(len(L)):
        min_x = L[i][0]
        print(min_x)
        y = L[i][1]
        print(y)
        print('\n')
        for j in range(i+1, len(L)):
            if L[j][0] < min_x:
                temp_x = L[j][0]
                temp_y = L[j][1]
                min_x = L[j][0]
                print(min_x)
                y = L[j][1]
                print(y)
                print('\n')
                L[j][0] = L[i][0]
                print(L[j][0])
                L[j][1] = L[i][1]
                print(L[j][1])
                print(L)
        print('\n')
    return L
'''


def sort(L):
    for i in range(len(L)):

        for j in range(i+1, len(L)):
            if L[j][0] < L[i][0]:
                temp_x = L[i][0]
                temp_y = L[i][1]
                L[i][0] = L[j][0]
                L[i][1] = L[j][1]
                L[j][0] = temp_x
                L[j][1] = temp_y
        L[i] = '<'+str(L[i][0])+','+str(L[i][1])+'>'
    return L




print(sort([[5,2],[3,4],[1,3]]))