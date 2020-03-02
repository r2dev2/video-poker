import os
from pathlib import Path
import subprocess

# Just because you might not have it installed

try:
    from easygui import *
except ImportError:
    subprocess.call([sys.executable, '-m', "pip", "install", "easygui"],)
'''
choices = ["Yes","No","Only on Friday"]
reply = choicebox("Do you like to eat fish?", choices=choices)

vos_choix = ["Yes", "Definitely", "Hai"]
reply = choicebox("Are you a weeb?", choices = vos_choix)
if reply == "Yes" or reply == "Definitely":
    confirmation_of_lie = msgbox("Weeb janai desu :(")
    if confirmation_of_lie == None:
        exit()
else:
    truth = msgbox("Eh! Sugoi desu ne!")
    if truth == None:
        exit()
'''
hold1 = True
hold2 = True
hold3 = True
hold4 = True
hold5 = True
arr = [hold1, hold2, hold3, hold4, hold5]
for i in range(5):
    hold_curr_card = ynbox("Do you want to hold card " + str(i))
    arr[i] = hold_curr_card

hold_cards = enterbox()

image = Path(os.getcwd()) / "img" / "python_and_check_logo.gif"
img2 = Path(os.getcwd()) / "img" / "2C.gif"
msg   = "Do you like this picture?"
choices = ["Yes","No","No opinion"]
reply=buttonbox(msg,image=str(image),choices=choices)
reply2=buttonbox(msg,image=str(image),choices=choices)
'''
# A nice welcome message
ret_val = msgbox("Hello, World!")
if ret_val is None: # User closed msgbox
    exit()
test = msgbox("Close this if you are not a weeb")
if test is None:
    yeet = msgbox("weeb janai desu")
    exit()

msg ="What is your favorite flavor?\nOr Press <cancel> to exit."
title = "Ice Cream Survey"
choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
while 1:
    choice = choicebox(msg, title, choices)
    if choice is None:
        exit()
    msgbox("You chose: {}".format(choice), "Survey Result")
'''
