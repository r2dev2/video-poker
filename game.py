'''
Created on Feb 6, 2019

@author: My Name, Other name

Description: Classes are done

'''

# Ronak Badhe, Karthik Bhattaram
# IMPORTANT: won't work on python < 3.5 due to type annotations
# Snapshot 2 comment: finished text based version

from typing import Callable

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
def willContinue() -> bool:
    ipt = input("Shall we continue?(Y/N) ").upper()
    if ipt in ['Y', 'N']:
        return ipt == 'Y'
    return willContinue()


# creates a deck instance of type PokerHand by iterating through suits and ranks
def create_deck() -> PokerHand:
    deck = PokerHand()
    SUIT = ['♥', '♦', '♣', '♠']
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for s in SUIT:
        for r in RANK:
            deck.add(PokerCard(r, s))
    # shuffle
    deck.shuffle()
    return deck


# Creates game variables
# Returns (deck, player)
def gameinit(name: str, money: int) -> tuple:
    deck = create_deck()
    # deals 5 cards to deck
    hand = PokerHand()
    for i in range(5):
        hand.add(deck.deal())
    player = PokerPlayer(name, money, hand)
    return deck, player


# Gets name from user
def getNameInput() -> str:
    name = input("What is your name? ")
    return name


# Gets int inputs
# Ex: intinput("An integer please ", lambda x: 1<x<5, "Integer between 1 and 5") \
# Will keep asking until user inputs an int between 1 and 5
def intinput(prompt: str, condition: Callable, errmsg: str = "Please enter a valid integer.") -> int:
    # Checks if condition is callable
    if not callable(condition):
        raise TypeError("Condition should be a function")

    cin = input(prompt)
    # Sees if cin can be turned into an int following guidelines
    try:
        cin = int(cin)
    except ValueError:
        print(errmsg)
        return intinput(prompt, condition, errmsg)
    if not condition(cin):
        print(errmsg)
        return intinput(prompt, condition, errmsg)
    return cin


# Initial money with input validation
def getMoneyInput() -> str:
    errormsg = "Please enter an integer greater than 0"
    prompt = "How many credits do you have? "
    return intinput(
        prompt,
        lambda x: x > 0,
        errormsg
    )


# Returns amount of money to be bet
def getBetInput() -> int:
    return intinput(
        "How much would you like to bet? ",
        lambda x: x > 0,
        "Please enter an integer value greater than 0"
    )


# -------------------------------
# Poker Game text solo version
# Main game loop
# Game should look like:
# {name}: {hand}
# Which cards do u want to hold?
# You held {cards that held}
# {Hand type}!! You won {amount won}
# You have {money} left
# Would you like to continue?
# -------------------------------
def PokerGame() -> None:
    # Hash map for money gained per hand type
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
        "Nothing": -1
        }

    # Intro
    print("Poker Game!! Let's Go!")
    name = getNameInput()
    print("Hello %s, let's begin" % name)
    money = getMoneyInput()
    print("You have %d credits" % money)

    # Create Game variables
    deck, player = gameinit(name, money)

    # Main Game Loop
    while player.getMoney() > 0:
        print()
        bet = getBetInput()
        typeOfHand = PokerRound(player, deck)
        moneywon = bet * credits_for_hand[typeOfHand]
        player.addMoney(moneywon)
        if typeOfHand == "Nothing":
            print("Nothing :( You lost.")
        else:
            print(typeOfHand + "!!", "You won", moneywon)
        print("You have %d money left" % player.getMoney())
        if not willContinue():
            break
        deck, player = gameinit(name, player.getMoney())
    
    
# plays one round of the game
# return string of results
def PokerRound(player: PokerPlayer, deck: PokerHand) -> str:
    
    '''
    explanation of program logic
    Take in the poker player's hand from the 52 card deck
    Ask for what cards they want to hold
    Add cards from the deck to said card
    Check hand type
    Output the hand type
    
    '''
    print("{}:\t{}".format(player.getName(), player.hand))
    rawcards = player.askHoldChoice().split(' ')
    cardsToHold = []
    if rawcards != ['']:
        cardsToHold = [player.getCard(int(c) - 1) for c in rawcards]
    #player hand = cardstohold

    testhand = PokerHand()
    testhand.cards = cardsToHold
    print("You held:", testhand)

    #now add additional cards
    while len(cardsToHold) < 5:
        dealtcard = deck.deal()
        cardsToHold.append(dealtcard)
    newHand = PokerHand()
    newHand.cards = cardsToHold[:]
    #make a new poker_hand
    player.hand = newHand
    print("%s:" % player.getName(), player.hand)
    hand_type = player.hand.handType()
    return hand_type

def main():
    # hand = PokerHand()
    # hand.cards = [
    #     PokerCard("10", '♥'),
    #     PokerCard("J", '♥'),
    #     PokerCard("Q", '♥'),
    #     PokerCard("K", '♥'),
    #     PokerCard("A", '♥')
    # ]
    # 
    # deck = PokerHand()
    # for i in ['A', '1', '2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K']:
    #     for j in ['♥', '♦', '♣', '♠']:
    #         deck.cards.append(PokerCard(i, j))
    # p = PokerPlayer("Yudachi", 100000000, hand)
    # print(PokerRound(p, hand))
    PokerGame()
    
if __name__ == "__main__":
    main()
    
        

