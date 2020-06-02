def updateHand(hand, word):

    for letter in word:
        hand[letter] -= 1

    return hand

print(updateHand({'a' : 2, 'm' : 2, 'o' : 1, 't' : 2}, 'mama'))