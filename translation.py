python_to_fics = {
    '♥ ': "@", 
    '♦ ': "#", 
    '♣ ': "&", 
    '♠ ': "%",
    "What is your name? ": "$NA",
    "Please enter a valid integer.": "$I",
    "Please enter an integer greater than 0": "$G0I",
    "How many credits do you have? ": "$AC",
    "How much would you like to bet? ": "$B",
    "Royal Flush": "$RF",
    "Straight Flush": "$SF",
    "Four of a Kind": "$FAK",
    "3 of a Kind": "$K3",
    "(Jacks or better)": "$JB",
    "Nothing :( You lost.": "$L",
    "You won": "$W",
    "Which cards would you like to hold?": "$HC",
    "You should have 5 entries at max": "$5E",
    "Your numbers should be integers between 1 and 5 inclusive": "$1&5",
    '\t': '^'
}

fics_to_python = {value: key for key, value in python_to_fics.items()}