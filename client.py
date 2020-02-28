from threading import Thread
from time import sleep

from IO import IO
from game import intinput

# Name constants
P1 = "guestKA"
P2 = "guestKB"
HOST = "guestKS"

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
    print("Ended")

def shouldExit(filename = "lock.lock") -> bool:
    return False

def stopAllThreads(filename = "lock.lock") -> None:
    pass

def printOutput(msg: str) -> None:
    print(msg)

def client_receive(server: IO) -> None:
    print("Receiving tells")
    server.receive_tell()
    while not shouldExit():
        name, msg = server.receive_tell()
        if msg is None:
            sleep(.1)
            continue
        if "KA(U)" in msg or "KB(U)" in msg or '*' in msg:
            continue
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