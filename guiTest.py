import os
from pathlib import Path
import subprocess
import sys
from threading import Thread
# Just because you might not have it installed

try:
    from easygui import *
except ImportError:
    subprocess.call([sys.executable, '-m', "pip", "install", "easygui"],)


from game import PokerGame
from common import rmtouch

FILEOUT = "gui.out"
VERBOSE = True if len(sys.argv) == 2 and sys.argv[1] == "--verbose" else False

'''
choices = ["Yes","No","Only on Friday"]
reply = choicebox("Do you like to eat fish?", choices=choices)

vos_choix = ["Yes", "Definitely", "Hai"]
reply = choicebox("Are you a weeb?", choices = vos_choix)
if reply == "Yes" or reply == "Definitely":
    confirmation_of_lie = msgbox("Weeb janai desu :(")
    if confirmation_of_lie == None:
        exit()
else:
    truth = msgbox("Eh! Sugoi desu ne!")
    if truth == None:
        exit()
'''

rmtouch(FILEOUT)

# Based on prompt change the gui
def userInput(prompt):
    return input(prompt)

# Based on output change the gui
def retrieveOutput():
    pass

#PokerGame(
#    cout = open(FILEOUT, "a+"),
#    cin = userInput
#)

userin = Thread(target = userInput)
dispout = Thread(target = retrieveOutput)

# userin.start()
# dispout.start()

# for i in range(5):
#     hold_curr_card = ynbox("Do you want to hold card " + str(i))
#     arr[i] = hold_curr_card
# hold_cards = enterbox()

# hold1 = True
# hold2 = True
# hold3 = True
# hold4 = True
# hold5 = True
# arr = [hold1, hold2, hold3, hold4, hold5]
# image = Path(os.getcwd()) / "img" / "KS.gif"
# img2 = Path(os.getcwd()) / "img" / "2C.gif"
# msg   = "Do you like this picture?"
# choices = ["Smash", "Pass"]
# reply=buttonbox(msg,image=(str(img2),str(image)),choices=choices)
# reply2=buttonbox(msg,image=str(img2),choices=choices)
#pseudocode:
#Ask for name(enterbox)
#Ask for the amount of credits the player has(integerbox)
#Ask the player how much they want to bet(integerbox)
#Show the player the cards they have received(buttonbox)
#Have them click on the cards they want to hold
# -> have a set of images
# -> have them click on ONE, SINGLE CARD
# -> if they want to hold another card, have them click "continue"
# -> if they don't want to hold another card(or any cards) have them click "I'm done"
#Show them their new cards 
#Show them what type of hand it is
#Show them how much money they have left
#Ask them if they want to continue(ccbox)
#GOOD IDEA: use a ccbox for asking if you want to continue
#pseudocode continued: what to use for each part
#
def handToFilePaths(hand: str) -> tuple:
    img = Path(os.getcwd()) / "img"
    translations = {
        '♥': 'H',
        '♦': 'D', 
        '♣': 'C',
        '♠': 'S'
    }
    new = []
    for s in hand.split(' ')[:-1]:
        news = s
        for k, v in translations.items():
            news = news.replace(k, v)
        if VERBOSE: print(news)
        new.append(news)
    return tuple(str(img / "{}.gif".format(s)) for s in new)

filetuple = handToFilePaths("10♠ J♣ J♠ K♣ A♣ ")
filelist = list(filetuple)

# how the hand prompt will work
uin = []
reply = None
while True:
    reply = buttonbox(image = filetuple, choices = ["I'm done"])
    if reply == "I'm done":
        break
    uin.append(str(filelist.index(reply) + 1))
uinstr = ' '.join(uin)
print(uinstr)

'''
# A nice welcome message
ret_val = msgbox("Hello, World!")
if ret_val is None: # User closed msgbox
    exit()
test = msgbox("Close this if you are not a weeb")
if test is None:
    yeet = msgbox("weeb janai desu")
    exit()

msg ="What is your favorite flavor?\nOr Press <cancel> to exit."
title = "Ice Cream Survey"
choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
while 1:
    choice = choicebox(msg, title, choices)
    if choice is None:
        exit()
    msgbox("You chose: {}".format(choice), "Survey Result")
'''
