def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    v = 0
    for letter in hand:
        v += hand[letter]
    return v



print(calculateHandlen({'k': 1, 'w': 1, 'j': 1, 'i': 2, 'b': 1, 'o': 1}))