from time import sleep
from threading import Thread

from IO import IO
from client import P1, P2, HOST
from game import PokerGame
from common import touch

def main() -> None:
    # FICS = IO("freechess.org", 5000)
    # FICS.login(HOST)
    # FICS.receive_tell()
    # print("Host server has started up")
    # while True:
    #     name, msg = FICS.receive_tell()
    #     if msg is None:
    #         sleep(.1)
    #         continue
    #     FICS.tell(other_user(name), msg)
    game(P1)

def game(user: str) -> None:
    f = open("1.game", "a+")
    out = Thread(target = fileUserOutput, args = ("1.game",))
    main = Thread(target = PokerGame, args = (f, userInput))
    out.start()
    main.start()
    

def userInput(prompt: str) -> str:
    sleep(.5)
    print(prompt, end = '')
    return input('')

def fileUserOutput(filename = "1.game") -> None:
    with open(filename, 'r') as fin:
        prev = fin.readlines()[:-1]
    sleep(.1)
    while True:
        with open(filename, 'r') as fin:
            new = fin.readlines()[:]
        differences = findDifference(prev[:], new[:])
        if differences != []:
            for s in differences:
                print(s[:-1], flush = True)
        prev = new[:]

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