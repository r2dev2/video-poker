from copy import deepcopy

from stack_of_cards import StackOfCards
from game import WINNING_HANDS
from common import *

WINNING_HANDS = [ "Royal Flush", \
                  "Straight Flush", \
                  "Four of a Kind", \
                  "Full House", \
                  "Flush", \
                  "Straight", \
                  "3 of a Kind", \
                  "Two Pairs", \
                  "Pair (Jacks or better)" ]

#===========================================================================
# Description: A list of Card; used for a player's hand or a deck of cards
#
# State Attributes
#     - cards - list of card; starts out empty
# Methods
#     - shuffle() - randomly shuffle all the card in the list
#     - deal() - deal the 'top' card from the hand/deck
#     - add(card) - add Card to the list of cards
#     - remove(pos) - remove and return Card at pos number
#     - size() - size of hand
#     - getCard(pos) - returns a Card at the 'pos'
#     - __str__() - returns string of all the cards in the hand like '4♣ 10♥ A♠'
#     - sort() - sorts cards according to rank
#     - handType() - returns if hand is of typing found in pdf eg. royal flush
#===========================================================================

class PokerHand(StackOfCards):
    # TODO
    def sort(self) -> None:
        pass
    
    # TODO
    def handType(self) -> str:
        # Sorts a copy to avoid modifying self
        clone = deepcopy(self)
        clone.sort()
        # convert cards to str
        strcards = ''.join([str(int(c)) for c in cards])

        # Classify hand by rank
        rankclassification = countMaxOccurences(strcards)
        if rankclassification == 2 and numPairs(strcards) == 2:
            return "Two Pairs"
        
        
