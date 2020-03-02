from time import sleep
from threading import Thread
import sys

from IO import IO
from client import P1, P2, HOST
from game import PokerGame, getNameInput
from common import rmtouch, numInStr, find_all
from translation import python_to_fics

VERBOSE = len(sys.argv) == 2 and sys.argv[1] == "--verbose"
UIN = "user.in"
FILE1 = "1.game"
FILE2 = "2.game"

def main() -> None:
    FICS = IO("freechess.org", 5000)
    FICS.login(HOST)
    FICS.receive_tell()
    nameFix(FICS)
    print("Host server has started up")
    # while True:
    #     name, msg = FICS.receive_tell()
    #     if msg is None:
    #         sleep(.1)
    #         continue
    #     FICS.tell(other_user(name), msg)
    mainui = Thread(target = mainUserInput, args = (FICS, UIN), daemon = True)
    mainui.start()
    main = [game(P1, FILE1, FICS), game(P2, FILE2, FICS)]
    if VERBOSE: print("Use keyboard interrupt to exit")
    while True:
        try:
            gameIsOver(main, [FILE1, FILE2], FICS)
        except KeyboardInterrupt:
            print("\nCaught signal, exiting")
            exit()

def nameFix(server: IO) -> None:
    server.tell(P1, encodeStr("What is your name? "))
    server.tell(P2, encodeStr("What is your name? "))
    server.receive_tell()

def game(user: str, gamefile: str, server: IO) -> Thread:
    rmtouch(gamefile)
    f = open(gamefile, "a+")
    out = Thread(
        target = fileUserOutput, 
        args = (server, gamefile, user), 
        daemon = True
        )
    main = Thread(
        target = PokerGame,
        args = (f, lambda p: userInput(p, server, user, UIN)),
        daemon = True
        )
    out.start()
    main.start()
    return main
    
def gameIsOver(gameThread: list, filenames: list, server: IO) -> None:
    scores = []
    for gt in gameThread:
        gt.join()
    for filename in filenames:
        with open(filename, 'r') as fin:
            lastLine = fin.readlines()[-1]
        scores.append(numInStr(lastLine))
    winners = find_all(max(scores), scores)
    winstr = ["Player {} has won with a balance of {} money".format(w+1, scores[w]) for w in winners]
    server.tell("geustKDEV", "Yolo")
    for w in winstr:
        server.tell(P1, w)
        server.tell(P2, w)
        server.tell("geustKDEV", "Yolo")
        print(w)
    print("Game is over")
    exit()

def userInput(prompt: str, server: IO, user: str, filename: str) -> str:
    if prompt[-1] == '\n':
        prompt = prompt[:-1]
    if prompt[:3] == "fi\n":
        prompt = prompt[3:]
    sleep(.3)
    server.tell(user, encodeStr(prompt))
    with open(filename, 'r') as fin:
        prev = fin.readlines()[:]
    while True:
        sleep(.1)
        with open(filename, 'r') as fin:
            new = fin.readlines()[:]
        differences = findDifference(prev[:], new[:])
        if differences != []:
            for s in differences:
                if s != '' and user in s:
                    if VERBOSE: print(s)
                    return s[len(user + ": "):-1]
        prev = new[:]

def mainUserInput(server: IO, filename: str) -> None:
    rmtouch(filename)
    while True:
        name, msg = server.receive_tell()
        if msg is None:
            sleep(.1)
            continue
        with open(filename, 'a+') as fout:
            print("{}: {}".format(name, msg), file = fout, flush = True)

def fileUserOutput(server: IO, filename = "1.game", recepient = P1) -> None:
    if VERBOSE: print(filename)
    server.tell(recepient, "Poker Game!! Let's Go!")
    if VERBOSE: print("Poker Game!! Let's Go!")
    with open(filename, 'r') as fin:
        prev = fin.readlines()[:-1]
    while True:
        with open(filename, 'r') as fin:
            new = fin.readlines()[:]
        differences = findDifference(prev[:], new[:])
        if differences != []:
            for s in differences:
                if "Let's Go!" in s:
                    continue
                if VERBOSE: print(s[:-1], flush = True)
                safestring = s[:-1]
                safestring = encodeStr(safestring)
                if VERBOSE: print("Safestring=", safestring)
                server.tell(recepient, safestring)
        prev = new[:]

def encodeStr(msg: str) -> str:
    for k, v in python_to_fics.items():
        msg = msg.replace(k, v)
    return msg

def findDifference(oglines: list, newlines: list) -> list:
    if len(oglines) >= len(newlines):
        return []
    return findDifference(oglines, newlines[:-1]) + [newlines[-1]]

def other_user(user: str) -> str:
    if user == P2:
        return P1
    return P2

if __name__ == "__main__":
    main()