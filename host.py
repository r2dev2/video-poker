from time import sleep
from threading import Thread

from IO import IO
from client import P1, P2, HOST
from game import PokerGame
from common import rmtouch, unicode_to_ascii

def main() -> None:
    FICS = IO("freechess.org", 5000)
    FICS.login(HOST)
    FICS.receive_tell()
    print("Host server has started up")
    # while True:
    #     name, msg = FICS.receive_tell()
    #     if msg is None:
    #         sleep(.1)
    #         continue
    #     FICS.tell(other_user(name), msg)
    game(P1, FICS)

def game(user: str, server: IO) -> None:
    rmtouch("1.game")
    f = open("1.game", "a+")
    out = Thread(target = fileUserOutput, args = (server, "1.game", user))
    main = Thread(target = PokerGame, args = (f, lambda p: userInput(p, server, user)))
    out.start()
    main.start()
    main.join()
    main = Thread(target=PokerGame, args = (f, lambda p: userInput(p, server, user)))
    main.start()
    main.join()
    out.join()
    print("Game has finished")
    

def userInput(prompt: str, server: IO, user: str) -> str:
    if prompt[-1] == '\n':
        prompt = prompt[:-1]
    sleep(.3)
    server.tell(user, prompt)
    while True:
        name, msg = server.receive_tell()
        if msg is None:
            sleep(.1)
            continue
        return msg

def fileUserOutput(server: IO, filename = "1.game", recepient = P1) -> None:
    server.tell(recepient, "Poker Game!! Let's Go!")
    print("Poker Game!! Let's Go!")
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
                print(s[:-1], flush = True)
                safestring = s[:-1]
                for k, v in unicode_to_ascii.items():
                    safestring = safestring.replace(k, v)
                print("Safestring=", safestring)
                server.tell(recepient, safestring)
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