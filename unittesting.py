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
        1,
        2,
        3
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
        2,
        2
    ]
    for t, e in zip(tests, expected):
        result = common.numPairs(t)
        yield result, result == e

# Runs a testing function
def runTest(f, name):
    print(name, "testing")
    gen = f()
    for result, ispass in testCountMaxOccurences():
        print(result, ispass)
    print()

def main():
    runTest(testCountMaxOccurences, "Max Occurences testing")
    runTest(testFindAll, "Find All testing")
    runTest(testNumInStr, "Num in Str testing")
    runTest(testIsIn, "Is in testing")
    runTest(testNumPairs, "Num Pairs testing")

if __name__ == "__main__":
    main()