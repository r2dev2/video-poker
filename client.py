import os
from threading import Thread
from time import sleep

from IO import IO
from game import intinput
from common import ascii_to_unicode

# Name constants
P1 = "geustKA"
P2 = "geustKB"
HOST = "geustKS"

def main() -> None:
    username, other = getUser()
    FICS = IO("freechess.org", 5000)
    FICS.login(username)
    send = Thread(target = client_send, args = (FICS, HOST))
    receive = Thread(target = client_receive, args = (FICS,))
    send.start()
    receive.start()
    send.join()
    receive.join()
    resetLock()
    print("Ended")

# Returns if the lock file is found
def shouldExit(filename = "lock.lock") -> bool:
    try:
        with open(filename, 'r') as fin:
            pass
    except FileNotFoundError:
        return False
    return True

# Gives Signal to all threads to stop
def stopAllThreads(filename = "lock.lock") -> None:
    with open(filename, 'w+') as fout:
        fout.write("yeet the threads")

# Deletes the lock file
def resetLock(filename = "lock.lock") -> None:
    os.remove(filename)

def printOutput(msg: str) -> None:
    print(msg)

def client_receive(server: IO) -> None:
    server.receive_tell()
    while not shouldExit():
        name, msg = server.receive_tell()
        if msg is None:
            sleep(.1)
            continue
        # Don't read messages from each individual guest
        if "KA(U)" in msg or "KB(U)" in msg or '*' in msg:
            continue
        for k, v in ascii_to_unicode.items():
            msg = msg.replace(k, v)
        printOutput(msg)

def client_send(server: IO, other: str):
    print("Sending has started")
    while not shouldExit():
        msg = input('')
        if msg == "$QUIT":
            stopAllThreads()
            continue
        print()
        server.tell(other, msg)

def getUser() -> (str, str):
    ipt = intinput(
        "Player 1 or 2? ",
        lambda x: x == 1 or x == 2,
        "Please enter 1 or 2"
    )
    if ipt == 1:
        return P1, P2
    return P2, P1

if __name__ == "__main__":
    main()