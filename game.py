'''
Created on Feb 6, 2019

@author: My Name, Other name

Description: Classes are done

'''
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
    print("Poker Game!! Let's Go!")
    
# add any other helper functions to organize your code nicely
    
# plays one round of the game
# return string of results
# update player's money
def PokerRound(player: PokerPlayer, deck: PokerHand) -> str:
    pass

def main():
    PokerGame()
    
if __name__ == "__main__":
    main()
    
        

