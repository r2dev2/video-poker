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


import os
from pathlib import Path
import subprocess
import sys
from threading import Thread
# Just because you might not have it installed

try:
    from easygui import *
except ImportError:
    subprocess.call([sys.executable, '-m', "pip", "install", "easygui"])


from game import PokerGame
from common import rmtouch

FILEOUT = "gui.out"
VERBOSE = True if len(sys.argv) == 2 and sys.argv[1] == "--verbose" else False

# Based on prompt change the gui
def userInput(prompt):
    if "name?" in prompt:
        return getStr(prompt)
    elif "credits?" in prompt or "bet?" in prompt:
        return getInt(prompt)


# Based on output change the gui
def retrieveOutput():
    pass

def getInt(msg: str) -> int:
    return integerbox(msg=msg, title="Video Poker")

def getStr(msg: str) -> str:
    return enterbox(msg=msg, title="Video Poker")

def handToFilePaths(hand: str) -> tuple:
    img = Path(os.getcwd()) / "img"
    translations = {
        '♥': 'H',
        '♦': 'D', 
        '♣': 'C',
        '♠': 'S'
    }
    new = []
    for s in hand.split(' '):
        if s == '':
            continue
        news = s
        for k, v in translations.items():
            news = news.replace(k, v)
        if VERBOSE: print(news)
        new.append(news)
    return tuple(str(img / "{}.gif".format(s)) for s in new)

# Displays the cards
def show_hand(hand: str):
    pass

# Prompt which cards to hold in hand
def hand_prompt(hand: str) -> str:
    filetuple = handToFilePaths(hand)
    filelist = list(filetuple)
    uin = []
    reply = None
    while True:
        reply = buttonbox(
            msg = "You are holding cards: %s" % ' '.join(uin),
            image = filetuple, 
            choices = ["I'm done"]
            )
        if reply == "I'm done":
            break
        choice = str(filelist.index(reply) + 1)
        if choice not in uin: 
            uin.append(choice)
        else:
            uin.pop(uin.index(choice))
    uinstr = ' '.join(uin)
    if VERBOSE: print(uinstr)
    return uinstr

# outputs a message, keyboard interrupts if no desire to continue
def genericOutput(msg: str) -> None:
    tocontinue = ccbox(msg=msg, title="Video Poker")
    if not tocontinue:
        raise KeyboardInterrupt("Yeetus the threads")

def main():
    hand_prompt("7♣ 7♠ 5♠ 9♦ J♦ ")
    genericOutput("Kartrhritis")

if __name__ == "__main__":
    main()
