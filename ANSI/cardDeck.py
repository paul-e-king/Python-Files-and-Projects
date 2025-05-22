Suits_black = ['\u2660', '\u2663'] # spades, clubs
Suits_red = ['\u2665', '\u2666'] # hearts, diamonds
RED = '\u001B[31m' # red text
RESET = '\u001B[0m' # turns colour off
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Deck = []
Deck_played = []

"""
The cards could have been full-on unicode cards, but each unicode string would have
had to be coded one by one to make a deck. And then the images would be too small to
clearly make out. Whereas, a 2-character representation in the manner done here is
clear.
Deck will have an array (list) of 52 standard playing cards.
"""

for s in Suits_black:
    for v in values:
        Deck.append(v+s)

for s in Suits_red:
    for v in values:
        Deck.append(v+RED+s+RESET)

C = 0
for c in Deck:
    print(c, end = "  ")
    C += 1
    if C % 13 == 0:
        print()
