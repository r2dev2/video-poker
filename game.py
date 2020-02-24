'''
Created on Feb 6, 2019

@author: My Name, Other name

Description: Classes are done

'''

# Ronak Badhe, Karthik Bhattaram
# Snapshot comment: finished base classes, base snarf
from poker_hand import PokerHand
from pokercard import PokerCard
from pokerplayer import PokerPlayer

# These are the winning hands in order of strength
WINNING_HANDS = [ "Royal Flush", \
                  "Straight Flush", \
                  "Four of a Kind", \
                  "Full House", \
                  "Flush", \
                  "Straight", \
                  "3 of a Kind", \
                  "Two Pairs", \
                  "Pair (Jacks or better)" ]

# make a PokerGame function
def valid_continue_input(inpt):
    return inpt == 'Y' or inpt == 'N'
    
def PokerGame():
    credits_for_hand = {
        "Royal Flush" : 250,
        "Straight Flush" : 50,
        "Four of a Kind" : 25,
        "Full House" : 9,
        "Flush" : 6,
        "Straight" : 4,
        "3 of a Kind" : 3,
        "Two Pairs" : 2,
        "Pair (Jacks or better)" : 1,
        "Nothing": 0
        }
    # make the player
    #player = PokerPlayer("Player", 1)
    
    # make a deck of cards
    deck = PokerHand()
    SUIT = ['♥', '♦', '♣', '♠']
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for s in SUIT:
        for r in RANK:
            deck.add(PokerCard(r, s))
    # shuffle
    deck.shuffle()
    # make rest of the game
    #pseudocode for the game
    #
    print("Poker Game!! Let's Go!")
    name = input("What is your name? ")
    print("Hello %s, let's begin" % name)
    money = int(input("How many credits do you have?"))
    print("You have %d credits" % money)
    print("%s:" % name, money)
    #deal 5 cards
    hand = PokerHand()
    for i in range(5):
        hand.add(deck.deal())
    player = PokerPlayer(name, money, hand)
    #PokerRound(player, deck)
    inpt = input("Shall we play?")
    while not valid_continue_input(inpt):
        print("please enter a valid input, ('Y' or 'N') ")
        inpt = input("Shall we play?")
    
    #PokerRound()
# add any other helper functions to organize your code nicely
    
# plays one round of the game
# return string of results
# update player's money
def PokerRound(player: PokerPlayer, deck: PokerHand) -> str:
    
    '''
    explanation of program logic
    Take in the poker player's hand from the 52 card deck
    Ask for what cards they want to hold
    Add cards from the deck to said card
    Check hand type
    Output the hand type
    
    '''
    print("{}: {}".format(player.name, player.hand))
    rawcards = player.askHoldChoice().split(' ')
    cardsToHold = [player.getCard(int(c) - 1) for c in rawcards]
    #player hand = cardstohold

    #now add additional cards
    while len(cardsToHold) < 5:
        dealtcard = deck.deal()
        cardsToHold.append(dealtcard)
    newHand = PokerHand()
    newHand.cards = cardsToHold[:]
    #make a new poker_hand
    player.hand = newHand
    hand_type = player.hand.handType()
    return hand_type

def main():
    hand = PokerHand()
    hand.cards = [
        PokerCard("10", '♥'),
        PokerCard("J", '♥'),
        PokerCard("Q", '♥'),
        PokerCard("K", '♥'),
        PokerCard("A", '♥')
    ]
    
    deck = PokerHand()
    for i in ['A', '1', '2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K']:
        for j in ['♥', '♦', '♣', '♠']:
            deck.cards.append(PokerCard(i, j))
    p = PokerPlayer("Yudachi", 100000000, hand)
    print(PokerRound(p, hand))
    
if __name__ == "__main__":
    main()
    
        

