import math
import random

class Deck:
    myDeck = []
    
    def __init__(self): # constructor
        # produces an ordered deck
        self.myDeck = [0] * 10
        for i in range(10):
            self.myDeck[i] = i
    
    def swap(self, i, j):
        # i and j are expected to be index values for myDeck list
        if ((not i == None) and (not j == None)):
            temp = self.myDeck[i]
            self.myDeck[i] = self.myDeck[j]
            self.myDeck[j] = temp
                
    def shuffle(self):
        # Shuffles the deck.
        # Maintain the actual items, but randomly change the order of them.
        index = -1
        for i in range(9, -1, -1):
            index = math.floor(random.random() * (i + 1))
            self.swap(i, index)
            
    def showDeck(self):
        # show the deck in its current state
        return self.myDeck
    
    def __str__(self):
        # invoked when programmer attempts to print the object
        return str(self.showDeck())
