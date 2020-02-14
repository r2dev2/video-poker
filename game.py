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
def PokerGame():
        
    # make the player
    #player = PokerPlayer("Player", 1)
    
    # make a deck of card
    # deck = PokerHand()  # make empty deck
    # add the 52-cards and shuffle
    
    # make rest of the game
    #pseudocode for the game
    #
    print("Poker Game!! Let's Go!")
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
    
# add any other helper functions to organize your code nicely
    
# plays one round of the game
# return string of results
# update player's money
def PokerRound(player: PokerPlayer, deck: PokerHand) -> str:
    
    '''
    explanation of program logic
    Take in the poker player's hand from the 52 card deck
    Ask for what cards they want to hold
    Remove the cards that they do not want to hold
    Fill in the blanks with cards from the shuffled deck
    Check hand type
    Output the hand type
    
    '''
    print("{}: {}".format(player.name, player.hand))
    rawcards = player.askHoldChoice().split(' ')
    cardstohold = map(int, rawcards)
    #now add additional cards
    dealtcard = deck.deal()
    player.addCard(dealtcard)

def main():
    PokerGame()
    
if __name__ == "__main__":
    main()
    
        

