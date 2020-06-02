s = 'azcbobobegghakl'

longest_substring = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

L = []
counter = 0
for letter in s[:-1]:
    substring = ""
    considered_string = s[counter : ]
    iteration_number = 0
    substring += letter

    comparison_number = 1
    boolean_expression = True
    while boolean_expression:

        counter1 = 0
        for i in alphabet:
            counter1 += 1
            if i == considered_string[iteration_number]:
                break

        counter2 = 0
        for j in alphabet:
            counter2 += 1
            if j == considered_string[iteration_number + 1]:
                break

        if counter2 > counter1:
            if comparison_number == len(considered_string) - 1:
                substring += considered_string[iteration_number + 1]
                break
            else:
                substring += considered_string[iteration_number + 1]
                iteration_number += 1
        else:
            boolean_expression = False

        comparison_number += 1



    if len(substring) > len(longest_substring):
        longest_substring = substring


    counter += 1


print("Longest substring in alphabetical order is: %s" % longest_substring)


