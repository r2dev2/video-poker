import telnetlib

#===========================================================================
# Description: A telnet handler, specifically for FICS
#
# State Attributes
#     - tel = Telnet object
# Methods
#     - login(user) = logs in to telnet connection, initializes connection
#     - close() = closes telnet connection
#     - receive_tell() = returns tell message and sender if a tell was sent or else None
#     - tell(receiver, msg) = sends a tell to a user
#===========================================================================

class IO:
    def __init__(self, host: str, port: int):
        self.tel = telnetlib.Telnet(host, port)

    def close(self) -> None:
        self.tel.close()

    def receive_tell(self) -> (str, str):
        back = self.tel.read_eager().decode("utf-8").split("fics%")
        for s in back:
            if "(U)" in s:
                return s[2:9], s[24:-2]
        return None, None

    def tell(self, receiver: str, msg: str) -> None:
        self.tel.write("tell {who} {msg}\r\n".format(who=receiver, msg=msg).encode("ascii"))

    def login(self, user: str) -> None:
        self.tel.read_until(b"login: ")
        self.tel.write(user.encode("ascii") + b'\n')
        self.tel.read_until(b"Press return to enter the server")
        self.tel.write(b"\r\n")
        # Ignore all of the game requests
        self.tel.write(b"set seek 0\r\n")