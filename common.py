from typing import Generic

# counts the highest duplicity reached 
# eg. countMaxOccurences("11222") -> 3, countMaxOccurences("123") -> 1
def countMaxOccurences(istr: str) -> int:
    # Edge case
    if len(istr) <= 1:
        return 1
    # Base case
    if len(istr) == 2:
        return int(istr[0] == istr[1]) + 1
    # Count maximum duplicity of first character
    times = 1
    for i in range(2, len(istr)):
        ocurrencesofi = istr.count(istr[0] * i)
        if ocurrencesofi == 0:
            break
        times = i
    # Get the highest between the current max duplicity and the max duplicity of
    # everything but the first character
    return max([times, countMaxOccurences(istr[1:])])

# returns a generator; I don't know how to type annotate that
# format of (returned value, pass status)
def testCountMaxOccurences() -> Generic:
    tests = [
        "1222331",
        "123421",
        "736122"
    ]
    expectedresults = [
        3,
        1,
        2
    ]

    for index, t in enumerate(tests):
        result = countMaxOccurences(t)
        yield result, result == expectedresults[index] 

def main():
    for ispass in testCountMaxOccurences():
        print(ispass)

if __name__ == "__main__":
    main()