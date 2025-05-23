import random

"""
This code has now become a game of blackjack.

The cards could have been full-on unicode cards, but each unicode string would have
had to be coded one by one to make a deck. And then the images would be too small to
clearly make out. Whereas, a 2-character representation in the manner done here is
clear.
Deck will have an array (list) of 52 standard playing cards.
"""
def build_deck(deck: list) -> list:
    """
    Builds a standard card deck to start the game<br>
    Input Parameter (required):<br>
    deck: the deck to be built (should be empty)<br>
    <br>
    Suits_black and Suits_red are called globally, and represent the four card suits.
    values is another global list which are the 13 face values of the cards.<br>
    <br>
    This function will return a full deck of cards, in order.
    """
    for s in Suits_black:
        for v in values:
            deck.append(v+s)

    for s in Suits_red:
        for v in values:
            deck.append(v+RED+s+RESET)
    return Deck

def shuffle(deck: list) -> list:
    """
    This is a shuffling algorithm to scramble the cards without using Python's 
    built-in functions.<br>

    The input parameter is a non-empty list representing a deck of cards.<br>
    The return value is the same deck of cards, scrambled.
    """
    for i in range(len(deck)):
        temp = deck[i]
        rIdx = random.randint(0, len(deck)-1)
        deck[i] = deck[rIdx]
        deck[rIdx] = temp
    return deck

def printDeck(deck: list):
    """
    This routine prints a "deck" of cards to the console.<br>
    The "deck" can be an actual deck, or it can be a player's hand.<br>

    deck: an input parameter containing a list of cards.
    """
    C = 0
    for c in deck:
        print(c, end = "  ")
        C += 1
        if C % 13 == 0:
            print()
    print()

def deal(deck: list, numCards: int) -> list:
    """
    This function deals cards to the player or the dealer.<br>

    deck: the deck of cards to deal from.<br>
    numCards: the number of cards to deal out.<br>

    The function returns the hand of cards that was dealt.<br>

    The reason we have numCards, even though we expect to play out one card at a time, is 
    for reasons of flexibility and reusability. This same code can be used for a different 
    game where more cards can be dealt.<br>

    deck.pop() deals the top card and outputs that card. That output is sent immediately to
    hand.append(), where the dealt card is added to the player's hand.
    """
    hand = []
    for i in range(numCards):
        hand.append(deck.pop())
    if numCards == 1:
        return hand[0]
    else:
        return hand

def handTotal(deck):
    """
    Logic:
    check first digit. 
      If it is a 1, check the next digit, then (d1*10) + d2
      If it is an "A", add it last after you get the rest of the total
    """
    total = 0
    printDeck(deck)
    acePlayed = False
    for card in deck:
        totalc = 0
        try:
            d1 = int(card[0])
            d2 = 0
            if d1 == 1:
                d2 = int(card[1])
                totalc = d1*10 + d2
            if d1 != 1:
                totalc = d1
        except ValueError:
            if card[0] == "J" or card[0] == "Q" or card[0] == "K":
                totalc = 10
            elif card[0] == "A":
                acePlayed = True
        total += totalc
    if acePlayed:
        if total > 10:
            total += 1
        else:
            total += 11
    return total

def dealerPlay(deck, playerTotal):
    # deal two cards
    dealerHand = []
    dealerHand.append(deck.pop())
    dealerHand.append(deck.pop())
    dTotal = handTotal(dealerHand)
    while dTotal < playerTotal:
        dealerHand.append(deck.pop())
        printDeck(dealerHand)
        dTotal = handTotal(dealerHand)
        print("Dealer score so far: ", dTotal)
        if dTotal == 21:
            print("Blackjack! Dealer wins!")
            break
        elif dTotal > 21:
            print("Player wins!")
            break
    if (dTotal >= playerTotal) and (dTotal <= 21):
        print("Dealer's total: %d" % dTotal)
        print("Dealer wins!")

# MAIN CODE
# Initialize some variables
Suits_black = ['\u2660', '\u2663'] # spades, clubs
Suits_red = ['\u2665', '\u2666'] # hearts, diamonds
RED = '\u001B[31m' # red text
RESET = '\u001B[0m' # turns colour off
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Deck = []
Hand_player = []
Discards = []

print("Building deck ...")
Deck = build_deck(Deck)
print("Shuffling ...")
Deck = shuffle(Deck)
# printDeck(Deck)
quitting = False
cmd = ""
total = 0
while not quitting:
    cmd = input("""Commands are not case-sensitive: 
          Quit   : Quit the game
          hit    : deal a card
          deck   : show the deck (DEBUG)
          hand   : show my hand
          stay   : stay with your hand - dealer plays next\nCommand: """)
    cmd = cmd.lower()
    quitting = (cmd == "quit")
    if cmd == "hit":
        Hand_player.append(deal(Deck, 1))
        print("Cards in your hand: ", end = "")
        printDeck(Hand_player)
        total = handTotal(Hand_player)
        print("Your total is: %d" % total)
        if total > 21:
            print("Your total is too high! You lose!")
            quitting = True
        elif total == 21:
            print("Blackjack! You win!")
            quitting = True
    elif cmd == "hand":
        print("Cards in your hand: ")
        printDeck(Hand_player)
        total = handTotal(Hand_player)
        print("Your total is: %d" % total)
    elif cmd == "deck":
        print("Cards left in the deck:")
        printDeck(Deck)
    elif cmd == "stay":
        print("Your total is: %d" % total)
        print("Dealer's turn.")
        dealerPlay(Deck, total)
        quitting = True

