from copy import deepcopy

from stack_of_cards import StackOfCards
from pokercard import PokerCard
from common import *

# For reference
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
#     - handType() - returns what hand eg. royal flush
#===========================================================================

class PokerHand(StackOfCards):
    def __str__(self):
        return super().__str__() + ' '
        
    def sort(self) -> None:
        self.cards.sort()
    
    def handType(self) -> str:
        classification = "Nothing"

        # Sorts a copy to avoid modifying self
        clone = deepcopy(self)
        clone.sort()
        
        # convert cards to str and list of str
        listcards = [str(int(c)) for c in clone.cards]
        strcards = ''.join(listcards)

        # Classify hand by rank
        rankclassification = countMaxOccurences(listcards)

        # Full house
        if rankclassification == 3:
            if [listcards[2]] * 2 == listcards[:2] and listcards[3] == listcards[4] or \
                [listcards[2]]* 2 == listcards[3:] and listcards[0] == listcards[1]:
                return "Full House"

        # Two Pairs
        if rankclassification == 2 and numPairs(strcards) == 2:
            return "Two Pairs"

        # Change pair to pair (Jacks or better)
        if rankclassification == 2:
            jacksorbetter = is_in([11, 11], listcards) or is_in([12, 12], listcards) or \
                is_in([13, 13], listcards) or is_in([14, 14], listcards)
            if not jacksorbetter:
                rankclassification = 1

        # Classification is now the index of the Winning hand
        classification = WINNING_HANDS.index(
            ["Nothing", "Pair (Jacks or better", "3 of a Kind", "Four of a Kind"][rankclassification - 1]
            )
        
        # Classify hand by flush
        # Straight, not a flush
        isstraight = True
        for i, card in enumerate(listcards):
            rank = int(card)
            # avoid index out of bounds
            if i == len(listcards) - 1:
                break
            # see if cards are sequential
            trueforcurrentcard = rank + 1 == int(listcards[i + 1])
            if not trueforcurrentcard and i == len(listcards) - 2 and int(listcards[-1]) == '14':
                trueforcurrentcard = listcards[0] == 2
            if not trueforcurrentcard:
                isstraight = False
                break
        if isstraight and classification > 5:
            classification = 5

        # Flush
        # List -> set removes duplicates
        isflush = len(set([c.suit for c in clone.cards])) == 1
        if isflush and classification > 4:
            classification = 4
        
        # Straight Flush
        if isflush and isstraight:
            classification = 1

        # Royal Flush
        if classification == 1:
            allroyals = len([int(c) for c in clone.cards if int(c) >= 10]) == len(clone.cards)
            classification -= int(allroyals)

        return WINNING_HANDS[classification]


def main():
    #suits: SUIT = ['♥', '♦', '♣', '♠']
    #RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    hand = PokerHand()
    hand.cards = [
        PokerCard("10", '♥'),
        PokerCard("J", '♥'),
        PokerCard("Q", '♥'),
        PokerCard("K", '♥'),
        PokerCard("A", '♥')
    ]
    #four of a kind
    hand2 = PokerHand()
    hand2.cards = [
        PokerCard("K", '♥'),
        PokerCard("K", '♦'),
        PokerCard("K", '♣'),
        PokerCard("K", '♠'),
        PokerCard("J", '♥'), 
    ]
    print("hand 1s type is", hand.handType(), "it should be royal flush")
    print("hand 2's type is", hand2.handType(), "it should be 'four of a kind'")
    #full house: 
    # A full house, also known as a 
    # full boat or a boat (and originally called a full hand), 
    # is a hand that contains three cards of one rank and two 
    # cards of another rank
    hand3 = PokerHand()
    hand3.cards = [
        PokerCard("10", '♥'),
        PokerCard("10", '♦'),
        PokerCard("10", '♣'),
        PokerCard("3",'♥' ),
        PokerCard("3", '♣')
    ]
    '''
    "Royal Flush" : 250
    "Straight Flush" : 50
    "Four of a Kind" : 25
    "Full House" : 9
    "Flush" : 6
    "Straight" : 4
    "3 of a Kind" : 3
    "Two Pairs" : 2
    "Pair (Jacks or better)" : 1
    '''

    # Karthik, it should be full house, 1 triple and 1 double
    print("hand3's type is ", hand3.handType(), "it should be 'full house'")

if __name__ == "__main__":
    main()
