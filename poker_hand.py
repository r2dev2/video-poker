from copy import deepcopy

from stack_of_cards import StackOfCards
from game import WINNING_HANDS
from common import *

WINNING_HANDS = [ "Royal Flush", 
                  "Straight Flush", 
                  "Four of a Kind", 
                  "Full House", 
                  "Flush", 
                  "Straight", 
                  "3 of a Kind", 
                  "Two Pairs", 
                  "Pair (Jacks or better)",
                  "Nothing" ]

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
        classification = "Nothing"
        # Sorts a copy to avoid modifying self
        clone = deepcopy(self)
        clone.sort()
        # convert cards to str
        listcards = [str(int(c)) for c in clone.cards]
        strcards = ''.join(listcards)

        # Classify hand by rank
        rankclassification = countMaxOccurences(strcards)
        if rankclassification == 2 and numPairs(strcards) == 2:
            return "Two Pairs"
        if rankclassification == 2:
            jacksorbetter = [11, 11] in listcards or [12, 12] in listcards or \
                [13, 13] in listcards or [14, 14] in listcards:
            if not jacksorbetter:
                rankclassification = 1
        classification = WINNING_HANDS.index(
            ["Nothing", "Pair (Jacks or better", "3 of a Kind", "Four of a Kind"][rankclassification - 1]
            )
        
        # Classify hand by flush
        # Straight, not a flush
        isstraight = True
        for i, rank in enumerate(listcards):
            if i == 4:
                break
            trueforcurrentcard = rank + 1 == listcards[i + 1]
            if not trueforcurrentcard and i == 3 and listcards[4] == 14:
                trueforcurrentcard = listcards[0] == 2
            if not trueforcurrentcard:
                isstraight = False
                break

        # Flush
        # List -> set removes duplicates
        isflush = len(set([c.suit for c in clone.cards])) == 1
        if isflush and classification > 4:
            classification = 4
        
        # 
