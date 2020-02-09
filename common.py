# counts the highest duplicity reached eg. countMaxOccurences("11222") -> 3
def countMaxOccurences(istr: str) -> int:
    if len(istr) <= 1:
        return 1
    if len(istr) == 2:
        return istr[0] == istr[1]
    times = 0
    for i in range(2, len(istr) - 1):
        ocurrencesofi = istr[0].count(istr[0] * i)
        if ocurrencesofi > times:
            times = ocurrencesofi
    return max([times, countMaxOccurences(istr[1:])])

