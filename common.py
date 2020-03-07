import os
from string import digits
from time import sleep
from typing import Callable, Generic

import vlc

from translation import fics_to_python, python_to_fics


# Returns indexes of all occurences within a list
def find_all(value: Generic, biglist: list) -> list:
    indexes = []
    for i, v in enumerate(biglist):
        if v == value:
            indexes.append(i)
    return indexes

# Returns the integer value of the number inside a string
# Ex: numInStr("hello123hello123") -> 123123
def numInStr(string: str) -> int:
    def strnumInStr(string: str) -> str:
        if len(string) == 0:
            return ''
        n = str(string[0]) if string[0] in digits else ''
        return n + strnumInStr(string[1:])
    return int(strnumInStr(string)) if string != '' else 0

# returns if a list is found in a bigger list
def is_in(small: list, big: list) -> bool:
    if len(small) > len(big):
        return False
    if len(small) == len(big):
        return small == big
    return big[:len(small)] == small or is_in(small, big[1:])

# counts the highest duplicity reached 
# eg. countMaxOccurences(list("11222")) -> 3, countMaxOccurences(list("123")) -> 1
def countMaxOccurences(ilst: list) -> int:
    # Edge case
    if len(ilst) <= 1:
        return 1
    # Base case
    if len(ilst) == 2:
        return int(ilst[0] == ilst[1]) + 1
    # Count maximum duplicity of first character
    times = 1
    for i in range(2, 5):
        ioccurs = is_in([ilst[0]] * i, ilst)
        if not ioccurs:
            break
        times = i
    # Get the highest between the current max duplicity and the max duplicity of
    # everything but the first character
    return max(times, countMaxOccurences(ilst[1:]))

# count number of pairs
def numPairs(ilst: list) -> int:
    pair = 0
    blacklist = []
    for c in ilst:
        # if the character isn't in blacklist
        # increment pair based upon whether there is a pair
        if c not in blacklist:
            haspair = is_in([c, c], ilst)
            pair += int(haspair)
            blacklist.append(c)
    # if there are 4 occurences of anything, should return 2
    for c in blacklist:
        if ilst.count(c*4) == 1:
            return 2
    return pair

# returns a generator; I don't know how to type annotate that
# format of (returned value, pass status)
def testCountMaxOccurences() -> Generic:
    tests = [
        list("1222331"),
        list("123421"),
        list("736122"),
        ['12', '12', '12', '12', '10'],
        ['11', '13', '13', '13', '13']
    ]
    expectedresults = [
        3,
        1,
        2,
        4,
        4
    ]

    for index, t in enumerate(tests):
        result = countMaxOccurences(t)
        yield result, result == expectedresults[index] 

def commonmain():
    for ispass in testCountMaxOccurences():
        print(ispass)

# Removes a file and does equivalent of ``touch filename``
def rmtouch(filename: str) -> None:
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    finally:
        with open(filename, 'a+') as fin:
            pass

def encodeStr(msg: str) -> str:
    try:
        for k, v in python_to_fics.items():
            msg = msg.replace(k, v)
    except UnicodeEncodeError:
        raise NotImplementedError(
                "Your current computer can't handle unicode keys in hashmaps"
                )
    return msg

def findDifference(oglines: list, newlines: list) -> list:
    if len(oglines) >= len(newlines):
        return []
    return findDifference(oglines, newlines[:-1]) + [newlines[-1]]

# Checks if a filepath exists
def doesItExist(path: str) -> bool:
    try:
        open(path, 'rb').close()
        exists = True
    except FileNotFoundError:
        exists = False
    finally:
        return exists

# Plays an audio file, returns pause and stop methods
def playAudio(path: str) -> tuple:
    player = vlc.MediaPlayer(path)
    player.play()
    return player.pause, player.stop

if __name__ == "__main__":
    commonmain()
