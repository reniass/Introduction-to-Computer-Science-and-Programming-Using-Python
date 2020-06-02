def sum_digits(s):

    import string
    digits = string.digits
    sum = 0
    how_many_numbers = 0
    for el in s:
        if el in digits:
            how_many_numbers += 1
            sum += int(el)
    if how_many_numbers == 0:
        raise ValueError


    return sum



print(sum_digits('mother'))