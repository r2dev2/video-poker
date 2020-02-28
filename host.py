from time import sleep

from IO import IO
from client import P1, P2, HOST

def main() -> None:
    FICS = IO("freechess.org", 5000)
    FICS.login(HOST)
    FICS.receive_tell()
    print("Host server has started up")
    while True:
        name, msg = FICS.receive_tell()
        if msg is None:
            sleep(.1)
            continue
        FICS.tell(other_user(name), msg)

def other_user(user: str) -> str:
    if user == P2:
        return P1
    return P2

if __name__ == "__main__":
    main()