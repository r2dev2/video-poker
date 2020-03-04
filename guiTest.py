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
import subprocess
import sys
from pathlib import Path
from threading import Thread
from time import sleep

from common import numInStr, rmtouch, findDifference
from game import PokerGame

# Just because you might not have it installed

try:
    from easygui import *
except ImportError:
    subprocess.call([sys.executable, '-m', "pip", "install", "easygui"])



FILEOUT = "gui.out"
VERBOSE = True if len(sys.argv) == 2 and sys.argv[1] == "--verbose" else False
timeforinput = False
money = 0
askheld = False
hand = ''

# Based on prompt change the gui
def userInput(prompt):
    global VERBOSE, timeforinput, askheld, hand, money
    if VERBOSE: print(prompt)
    while not timeforinput:
        sleep(.1)
    timeforinput = False
    if any([s in prompt for s in ("name?", "you have?", "bet?")]):
        return getStr(prompt)
    elif "Shall" in prompt:
        if VERBOSE: print("Printing")
        if ccbox(title="Video Poker", msg="You have %d money" % money):
            return 'Y'
        print("You have finished with %d money." % money)
        raise KeyboardInterrupt("Finish stuff")
    elif "hold?" in prompt:
        askheld = True
        return hand_prompt(hand)
    else:
        raise RuntimeError("prompt not found")

# Based on output change the gui
def retrieveOutput():
    global timeforinput, askheld, hand, VERBOSE, money
    with open(FILEOUT, 'r') as fin:
        prev = fin.readlines()
    while True:
        sleep(.1)
        with open(FILEOUT, 'r') as fin:
            new = fin.readlines()
        diff = findDifference(prev[:], new[:])
        if diff != []:
            for s in diff:
                # Don't care about You held: messages
                if "You held" in s:
                    continue
                # Checks if hand stuff is needed at all
                elif any([c in s for c in ('♠', '♥', '♦', '♣', '@', '#', '&', '%')]):
                    if not askheld:
                        hand = s.split('\t')[1]
                        continue
                    n = True
                    while n:
                        with open(FILEOUT, 'r') as fin:
                            new = fin.readlines()
                        if "won" in new[-2] or "lost" in new[-2]:
                            show_hand(s + new[-2])
                            n = False
                            new = new[:-1] 
                    askheld = False
                elif "money left" in s:
                    money = numInStr(s)
                    timeforinput = True
                # Fixes bug of seeing this again
                elif "won" in s or "lost" in s:
                    continue
                # Generic output
                else:
                    if s.strip() != '': indexbox(title="Video Poker", msg=s, choices=("Next",))
                    timeforinput = True
        prev = new[:]
# r"C:\users\labuser\Documents\video-poker\img\2C.gif"
def getStr(msg: str) -> str:
    return enterbox(msg=msg, title="Video Poker")

def handToFilePaths(hand: str) -> tuple:
    img = Path(os.getcwd()) / "img"
    translations = {
        '♥': 'H',
        '♦': 'D', 
        '♣': 'C',
        '♠': 'S',
        '@': 'H ',
        '#': 'D ',
        '&': 'C ',
        '%': 'S '
        }
    for k, v in translations.items():
        hand = hand.replace(k, v)
    new = []
    for s in hand.split(' '):
        if s.strip() == '':
            continue
        new.append(s)
    return tuple(getRealPaths([str(img / "{}.gif".format(s)) for s in new]))

def getRealPaths(paths: list) -> list:
    if len(paths) <= 1:
        return paths if doesItExist(paths[0]) else [] 
    val = paths[0] if doesItExist(paths[0]) else []
    return [val] + getRealPaths(paths[1:])

def doesItExist(path):
    try:
        open(path, 'rb').close()
        exists = True
    except FileNotFoundError:
        exists = False
    finally:
        return exists

# Displays the cards
# msg consists of {name}: {hand}\n{result}
#=> for Karthik
def show_hand(msg: str):
    hand = msg[:msg.find('\n')]
    filetuple = handToFilePaths(hand)[1:]
    filelist = list(filetuple)
    try:
        indexbox(msg=msg[msg.find('\n')+1:], 
            image = filetuple, 
            choices = ("Next",)
            )
    except AssertionError:
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
# def genericOutput(msg: str) -> None:
#     tocontinue = ccbox(msg=msg, title="Video Poker")
#     if not tocontinue:
#         raise KeyboardInterrupt("Yeetus the threads")

# def testing():
#     hand_prompt("7♣ 7♠ 5♠ 9♦ J♦ ")
#     genericOutput("Kartrhritis")

def main():
    # PokerGame(cout, cin)
    rmtouch(FILEOUT)
    userOut = Thread(target=retrieveOutput, daemon=True)
    mainGame = Thread(target=PokerGame, args=(open(FILEOUT, 'a+'), userInput, True), daemon=True)
    userOut.start()
    mainGame.start()
    while True:
        try:
            mainGame.join()
        except KeyboardInterrupt:
            print()
            exit()
        
if __name__ == "__main__":
    # testing()
    main()

# from gui import *
# video = r"C:\Users\labuser\Documents\poker\img\2C.gif"
# reply = buttonbox(msg = "Exam", iamge = img, choices = ["Next"])