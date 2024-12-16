# highLow w/ analytics
This is a developed version of a classic number guessing game.

The objective of the game is to guess if the given hint number is higher or lower than an actual number.

It can't be that hard or complicated... right?

## running

install python. the python installers are at https://python.org if you need them

if you do not have matplotlib already, open a command line and install it:
`pip install matplotlib`

this will automatically install **numpy** which is a matplotlib dependency
## features

- Decently configurable game settings
- Analytics
- Result files (check the script dictionary)

## dependencies

highLow with analytics requires python 3.6 or higher. the latest version (as of writing, python **3.13**) is recommended

the following are also required
- matplotlib (`pip install matplotlib` if you need it)
- numpy (matplotlib needs it; automatically installed with matplotlib)
- random (comes with python)
- time (also comes with python)

## analytics

the main point of this highLow implementation is the analytics system. at the end of every game you play (losing all your coins or typing 'quit') you will be displayed a graph where you can see your accuracy!

## result files

the other point of this implementation, it will automatically save some data to a new file each time you play, including the data used for the graph!

## contributing

read CONTRIBUTING.md