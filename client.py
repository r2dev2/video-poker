from threading import Thread
from time import sleep

from IO import IO
from game import intinput

# Name constants
P1 = "guestKA"
P2 = "guestKB"
HOST = "guestKH"

def main() -> None:
    username = getUser()
    FICS = IO("freechess.org", 5000)
    FICS.login(username)

def shouldExit(filename = "lock.conf") -> bool:
    return False

def printOutput(msg: str) -> None:
    print(msg)

def client_receive(server: IO, ) -> None:
    server.receive_tell()
    while True:
        if shouldExit():
            break
        msg = server.receive_tell()
        if msg is None:
            sleep(.1)
            continue
    printOutput(msg)

def getUser() -> str:
    ipt = intinput(
        "Player 1 or 2?",
        lambda x: x == 1 or x == 2,
        "Please enter 1 or 2"
    )
    if ipt == 1:
        return P1
    return P2