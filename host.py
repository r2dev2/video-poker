from time import sleep
from threading import Thread
import sys

from IO import IO
from client import P1, P2, HOST
from game import PokerGame, getNameInput
from common import rmtouch
from translation import python_to_fics

VERBOSE = len(sys.argv) == 2 and sys.argv[1] == "--verbose"

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
    game(P1, FICS)

def nameFix(server: IO) -> None:
    userInput("What is your name? ", server, P1)

def game(user: str, server: IO) -> None:
    rmtouch("1.game")
    f = open("1.game", "a+")
    out = Thread(target = fileUserOutput, args = (server, "1.game", user))
    main = Thread(target = PokerGame, args = (f, lambda p: userInput(p, server, user)))
    out.daemon = True
    main.daemon = True
    out.start()
    main.start()
    if VERBOSE: print("Use keyboard interrupt to exit")
    while True:
        try:
            gameIsOver([main])
        except KeyboardInterrupt:
            print("\nCaught signal, exiting")
            exit()

def gameIsOver(gameThread: list):
    gameThread[0].join()
    print("Game is over")
    exit()

def userInput(prompt: str, server: IO, user: str) -> str:
    if prompt[-1] == '\n':
        prompt = prompt[:-1]
    if prompt[:3] == "fi\n":
        prompt = prompt[3:]
    sleep(.3)
    server.tell(user, encodeStr(prompt))
    while True:
        name, msg = server.receive_tell()
        if msg is None:
            sleep(.1)
            continue
        return msg.upper()

def fileUserOutput(server: IO, filename = "1.game", recepient = P1) -> None:
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