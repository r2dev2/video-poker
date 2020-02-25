from player import Player
from poker_hand import PokerHand

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
#    askHoldChoice() - returns players choice of cards to hold with input validation
#===========================================================================

class PokerPlayer(Player):
    def askHoldChoice(self) -> str:
        cards_to_hold = input("Which cards would you like to hold?\n")
        if len(cards_to_hold) == 0:
            return ''
        holdlist = cards_to_hold.split(' ')
        # If there are more than 5 cards, try again (input validation)
        if len(holdlist) > 5:
            print("You should have 5 entries at max")
            return self.askHoldChoice()
        # Input Validation by splitting by ' ' and checking if each value is an integer between 1 and 5
        for s in holdlist:
            try:
                ints = int(s)
            except ValueError:
                print("Your numbers should be integers between 1 and 5 inclusive")
                return self.askHoldChoice()
            if not 1 <= ints <= 5:
                print("Your numbers should be integers between 1 and 5 inclusive")
                return self.askHoldChoice()
        return cards_to_hold


if __name__ == "__main__":
    player = PokerPlayer("Kwarthik", 42069, PokerHand())
    print(player.askHoldChoice())