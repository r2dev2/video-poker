'''
Edited on Feb 4, 2020

@author: mark_kwong
'''

#===========================================================================
# Description: a card player with money and a hand of stack_of_cards
#
# State Attributes
#    name - string - the name of the player
#    hand - StackOfCards - a bunch of cards
#    money - integer - how much money player has
# Methods
#    introduce() - prints out message "Hi, my name is ..."
#    __str__() - returns a string ex. 'Joe: 4d 7c 10s Ah'
#    getName() - returns the name of the player
#    getMoney() - returns the money balance
#    getCard(pos) - returns a Card at the pos number
#    addCard(card) - add card to the player's hand of stack_of_cards
#    removeCard(pos) - removes a card at the pos number
#    addMoney(amt) - add amt to player's money
#===========================================================================
class Player:

    # inputs:
    #    name - string for the player's name
    #    amount - integer for how much money the player has
    #    cards - a StackOfCards
    def __init__(self, name, amount, cards):
        '''
        Constructor
        '''
        self.name = name
        self.money = amount
        self.hand = cards
     
    # prints out name and the hand of stack_of_cards    
    def __str__(self):
        return("{}: {}".format(self.name, self.hand))
    
    def introduce(self):
        print("Hi, my name is {}".format(self.name))
        
    def getName(self):
        return(self.name)
    
    def getMoney(self):
        return self.money

    # add (or subtract) player's money    
    def addMoney(self, amount):
        self.money += amount
    
    # when player given another card, add it it player's hand    
    def addCard(self, card):
        self.hand.add(card)
        
    def getCard(self, pos):
        return self.hand.getCard(pos)
    
    def removeCard(self, pos):
        return self.hand.remove(pos)