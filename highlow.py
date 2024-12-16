# TODO
# - REVAMP THE GOD DAMNED PRESET SYSTEM
# - CODE FORMATTING BESIDES FUNCTIONS


# IMPORTS
from random import *  # requirement for program function
from time import sleep as wait  # required for polish

import matplotlib.pyplot as plt  # not my usual style, for plotting
import numpy as np  # matplotlib dependency

# get save id
saveIdFile = open("current_save_id.txt", "r")  # open the file
saveId = int(saveIdFile.read())  # read the file, it contains the save id number
saveIdFile.close()  # in case.

# ask user for configuration
print("highLow with analytics by Spade1345")
print("Would you like to set up your own game config or use a preset?")
print("> Type 'custom' to set up your own config")
print("> [broken] Type 'presets' for presets")
print("> Leave BLANK for default\n")
option = input("Enter your choice: ").strip()
print("-" * 50)  # seperator bar in short(er) form

# backup config
highNumber = 100
lowNumber = 0
coins = 1000

# config set
if option == "":
    # DEFAULT CONFIG
    print("Using default configuration.")
    highNumber = 100  # high end of the RNG Randint
    lowNumber = 0  # low end of the RNG Randint
    coins = 1000  # money to start with
    def bet():
        return 10  # amount of money to win/lose every round

elif option == "presets":
    # Implementation of presets
    print("""Preset List:
> standard - Standard 0-100 gameplay, start with 1000 coins.
> hardcore - Same as standard, but you always bet all your money.
> baby - TOO EASY. 0-5 gameplay, start 100 coins.
> rng-hell - Contains negative numbers. -1000 to 1000 gameplay, same as standard.""")
    option = input("Enter preset code:").strip()
    if option == "standard":  # Average Gameplay Moment
        highNumber = 100
        lowNumber = 0
        coins = 1000
        def bet():
            return 10

    elif option == "hardcore":  # hardcore mode (bet always returns coins)
        highNumber = 100
        lowNumber = 0
        coins = 10
        def bet(): # this is the way hardcore mode works
            return coins

    elif option == "baby":  # baby mode
        highNumber = 5
        lowNumber = 0
        coins = 100
        def bet():
            return 10

    elif option == "rng-hell": # mode that contains negative numbers
        highNumber = 1000
        lowNumber = -1000
        coins = 100
        def bet():
            return 10

    else:
        def bet():
            return 10

elif option == "custom":
    print("Custom Configuration")
    highNumber = int(input("RNG Highest number: ").strip())
    lowNumber = int(input("RNG Lowest number: ").strip())
    coins = int(input("Starting coins: ").strip())
    bet = int(input("Bet amount: ").strip())

else:
    # DEFAULT CONFIG
    print("Using default configuration.")
    highNumber = 100  # high end of the RNG Randint
    lowNumber = 0  # low end of the RNG Randint
    coins = 1000  # money to start with
    def bet():
        return 10  # amount of money to win/lose every round

# SCRIPTS
roundCount = 0  # Counts current round
roundCountList = [0]  # Start at 0, make it an array
statusList = [1]  # Accuracy starter at 100, also an array
rovingAccuracy = [1.0]  # set up accuracy, begin at 100% accurate, in float for consistency

while True:  # game loop
    realNumber = randint(lowNumber, highNumber)
    hintNumber = randint(lowNumber, highNumber)

    if realNumber > hintNumber:  # yes, this program calculates the answer ahead of time
        correctAns = "+"

    elif realNumber == hintNumber:
        correctAns = "="

    elif realNumber < hintNumber:
        correctAns = "-"

    else:
        raise TypeError("Somehow the system melted down. correctAns is undefined.")  # raise error if something breaks

    print("-" * 50)  # seperator bar in short form (the - symbol times 50)
    print(f"Round {roundCount + 1} | {coins} coins\n")
    print(f"I have chosen a number between {lowNumber} and {highNumber}.")
    print(f"Is the number lower, higher, or equal to {hintNumber}?")
    print("""Type '+' for higher.
Type '-' for lower.
Type '=' if it's equal.""")
    key = input("Choose answer - 'quit' to quit: ")
    while not (key == "+" or key == "-" or key == "=" or key == "quit"):
        print("Input a valid answer.")
        key = input("Choose answer - 'quit' to quit: ").strip()

    print("-----------------")

    if key == correctAns:
        print("CORRECT; +10 coins")
        coins += bet()
        correct = 1
    elif key == "quit":
        break
    else:
        print("INCORRECT; -10 coins")
        coins -= bet()
        correct = 0

    print("--------------------------------------")
    print(f"The hint you got was {hintNumber}")
    print(f"The actual number was {realNumber}")
    roundCount += 1
    roundCountList.append(roundCount)
    statusList.append(correct)
    rovingAccuracy.append(np.mean(statusList))

    if coins <= 0:
        print("-" * 50)
        print("YOU HAVE LOST!")
        print("Press ENTER to save your stats.")
        dumped = input("[PRESS ENTER]")
    elif coins > 0:
        wait(0.5)

# result file generation
result_file = open(f"highLow-result-{saveId}.txt", "w")
result_file.write(f"""highLow game #{saveId}
AUTOGENERATED RESULT FILE

> RESULTS
{roundCount} rounds played
Left with {coins} coin(s)
End accuracy: {(rovingAccuracy[len(rovingAccuracy) - 1]) * 100}%


> RAW DATA
This is the raw data from the program graph generation.
    - Round list and Accuracy Tracker are used as X and Y respectively in the end-of-game graph
    - Note that the floats are in raw float64s from numpy

     Accuracy track: {rovingAccuracy}
         Round list: {roundCountList}
Correct status list: {statusList}
   Accuracy tracker: {rovingAccuracy}""") # write the new file
result_file.close() # CLOSE IT

# increase the save ID by 1 and store it in current_save_id.txt
saveIdFile = open("current_save_id.txt", "w") # open file
saveIdFile.write(f"{saveId + 1}") # change save ID
saveIdFile.close() # DOOR STUCK! DOOR STUCK!

# set up for graph display
roundCountList = np.array(roundCountList) # array the list so matplotlib can use it
rovingAccuracy = np.array(rovingAccuracy) # array the other list

# set up and display graph
plt.title("highLow game accuracy by round") # main title
plt.scatter(roundCountList, rovingAccuracy) # form the scatterplot
plt.xlabel(f"Round - played {roundCount} rounds") # x axis label
plt.ylabel(f"Accuracy - end accuracy: {rovingAccuracy[len(rovingAccuracy) - 1] * 100}%") # y axis label w/ accuracy
plt.grid() # g r i d
plt.show() # show the graph
