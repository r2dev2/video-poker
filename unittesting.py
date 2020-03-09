import os
from pathlib import Path

import client
import common
import game
import gui
import host
import IO
import poker_hand
import pokercard
import pokerplayer
import translation


YEET = True

class charStream():
    def __init__(self):
        self.contents = ''

    def write(self, msg):
        self.contents += msg

    def flush(self):
        pass
    
    def read(self, lineno):
        return self.contents.split('\n')[lineno]

    def readlines(self):
        return self.contents.split()('\n')

# returns a generator
# format of (returned value, pass status)
def testCountMaxOccurences():
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

    for t, e in zip(tests, expectedresults):
        result = common.countMaxOccurences(t)
        yield result, result == e

# Tests common.find_all
def testFindAll():
    tests = [
        (1, [1, 2, 3, 4, 5]),
        (2, [1, 2, 3, 3, 2]),
        (3, [3, 3, 3])
    ]
    expected = [
        [0],
        [1, 4],
        [0, 1, 2]
    ]
    for t, e in zip(tests, expected):
        result = common.find_all(t[0], t[1])
        yield result, result == e

# tests common.numInStr
def testNumInStr():
    tests = [
        "hello123helo12",
        "Joe has 10 money left",
        "Karthik has finished the game with 100 money"
    ]
    expected = [
        12312,
        10,
        100
    ]
    for t, e in zip(tests, expected):
        result = common.numInStr(t)
        yield result, result == e

# tests common.is_in
def testIsIn():
    tests = [
        ([1, 2], list(range(10))),
        ([1, 0, 2], list(range(10))),
        ([1, 1], [1,2]),
        ([1, 1], [1, 1])
    ]
    expected = [
        True,
        False,
        False,
        True
    ]
    for t, e in zip(tests, expected):
        result = common.is_in(t[0], t[1])
        yield result, result == e

# tests common.numPairs
def testNumPairs():
    tests = [
        [1, 2, 2],
        [1, 2, 2, 1],
        [1, 1, 2, 2, 3]
    ]
    expected = [
        1,
        1, # function assumes that the list is sorted
        2
    ]
    for t, e in zip(tests, expected):
        result = common.numPairs(t)
        yield result, result == e

# Client exiting support
def testClientExit():
    client.stopAllThreads()
    result = client.shouldExit()
    yield result, result
    client.resetLock()

# Test intinput
def testIntInput():
    stream = charStream()
    def cin(prompt):
        global YEET
        if YEET:
            YEET = False
            return '9'
        return '0'
    result = game.intinput(
        "Test this please",
        lambda x: x == 0,
        cinput = cin,
        cout = stream
    )
    print(stream.contents)
    yield result, result == 0

# Tests gui.handToFilepaths
def testHandToFilePaths():
    PWD = Path(os.getcwd())
    tests = [
        "10@ 3# ",
        "10# 5& "
    ]
    expected = [
        (str(PWD / "img" / "10H.gif"), str(PWD / "img" / "3D.gif")),
        (str(PWD / "img" / "10D.gif"), str(PWD / "img" / "5C.gif"))
    ]
    for t, e in zip(tests, expected):
        result = gui.handToFilePaths(t)
        yield result, result == e

# Runs a testing function
def runTest(f, name):
    print(name, "testing")
    gen = f()
    for result, ispass in f():
        print(result, ispass, sep = '\t')
    print()

def main():
    print("Testing:")
    print("Returned value\texpected")
    print("Push enter for next test")
    runTest(testCountMaxOccurences, "Max Occurences")
    runTest(testFindAll, "Find All")
    runTest(testNumInStr, "Num in Str")
    runTest(testIsIn, "Is in")
    runTest(testNumPairs, "Num Pairs")
    runTest(testClientExit, "Client exit")
    runTest(testIntInput, "Int input")
    runTest(testHandToFilePaths, "Hand to filepaths")

if __name__ == "__main__":
    main()
