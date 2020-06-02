'''
def flatten(aList):
    alist_as_a_string = str(aList)
    copy_aList = []
    for sign in alist_as_a_string:
        if sign != '[' and sign != ']':
            copy_aList.append(sign)

    return copy_aList
'''

'''
def flatten(aList):
    s = ''
    L1 = []
    v = 0
    for e in str(aList):
        v += 1
        if e != ',' :
            s += e
            if v == len(str(aList)):
                L1.append(s)
        else:
            L1.append(s)
            s = ''
    return L1
'''

def flatten(aList):
    copy_aList = []
    for e in aList:
        #print(e)
        if type(e) == int:
            copy_aList.append(e)
        elif type(e) == str:
            copy_aList.append(e)
        else:
            for el in e:
                if type(el) == int:
                    copy_aList.append(el)
                elif type(el) == str:
                    copy_aList.append(el)
                else:
                    for ele in el:
                        if type(ele) == int:
                            copy_aList.append(ele)
                        elif type(ele) == str:
                            copy_aList.append(ele)
                        else:
                            for elem in ele:
                                if type(elem) == int:
                                    copy_aList.append(elem)
                                elif type(elem) == str:
                                    copy_aList.append(elem)
                                else:
                                    for eleme in elem:
                                        if type(eleme) == int:
                                            copy_aList.append(eleme)
                                        elif type(eleme) == str:
                                            copy_aList.append(eleme)
                                        else:
                                            continue
    return copy_aList



print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))