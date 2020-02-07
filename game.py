'''
Created on Feb 6, 2019

@author: My Name, Other name

Description: Classes are done

'''
from card import Card
from stack_of_cards import StackOfCards
from player import Player

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

# make a PokerCard Class inherit from Card
# class PokerCard(Card):

# make a PokerHand Class
        
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
    
def main():
    PokerGame()
    
if __name__ == "__main__":
    main()
    
        

