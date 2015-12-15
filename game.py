print "Welcome to the Memory Game"

#initiate a new game

# choice1 = 0
# choice2 = 0

# def new_game():
#     global Variables, location, turns, isDiscovered
#     turns = 0
#    isDiscovered = [False for i in range(16)]
    

# x = BoardSize
# difficulty = "Choose which level: easy, medium or hard"

# def Diff(difficulty):
#     if difficulty = "easy":
#         x = 4
#     elif difficult = "medium":
#         x = 6
#     else:
#         x = 8

##assuming total = 16 tiles, 8 pairs

#shuffle letters
import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
random.shuffle(Letters, random.random)
realValues = random.sample(Letters, 8)

#generate pairs of values
Variables = realValues + realValues
random.shuffle(Variables)

#create display board 
def displayBoard(Values):
    for i in range(0,4):
        for j in range(0,4):
            location = i*4 + j
            if (location<10):
                location = " " +str(location)
            print location,
        print
displayBoard(Variables)

#create dictionary to access values?
tiles = {"0": Variables[0], "1": Variables[1], "2": Variables[2], "3": Variables[3], "4": Variables[4], "5": Variables[5], "6": Variables[6], "7": Variables[7], "8": Variables[8], "9": Variables[9], "10": Variables[10], "11": Variables[11], "12": Variables[12], "13": Variables[13], "14": Variables[14], "15": Variables[15], "16": Variables[16]}

#create class to reference values?

# class Tile(object):
#     def __init__(self, location, value, isDiscovered):
#         self.location = location
#         self.value = value
#     def match(self, choice1, choice2):
#         if Variables(choice1) = Variables(choice2):
#             isDiscovered = True
#         else: 
#             isDiscovered = False    

print """
Instructions: Flip over two tiles. 
If your tiles match, the tiles will be revealed permenantly.
If your tiles do not match, the tiles will be covered again.
Try to match all of the tiles until all tiles are revealed.
Good Luck!"""

#allow the user to choose tiles based on location to turn over
choice1 = int(raw_input("Choose your first tile: "))
print Variables[choice1]

choice2 = int(raw_input("Choose your second tile: "))
print Variables[choice2]

def match(choice1, choice2):
    if Variables[choice1] = Variables[choice2]:
        print "You've got a match!"
        return Variables[choice1]
        location = Variables[choice1]
    else:
        print "Sorry, try again."

    #replace display value with letter - how??

# if matching values, flip over; else displayboard






