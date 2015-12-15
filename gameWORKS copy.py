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
Letters = [' a',' b',' c',' d',' e',' f',' g',' h',' i',' j',' k',' l',' m',' n',' o',' p',' q',' r',' s',' t',' u',' v',' w',' x',' y',' z'] 
random.shuffle(Letters, random.random)
realValues = random.sample(Letters, 8)

#generate pairs of values
Variables = realValues + realValues
random.shuffle(Variables)

#create display board 
def displayBoard(tiles):
    for i in range(0,4):
        for j in range(0,4):
            location = i*4 + j
            if tiles[str(location)].isDiscovered == True:
                print tiles[str(location)].value,
            else:
                if (location<10):
                    location = " " +str(location)
                print location,
        print

#create class to reference values?
class Tile(object):
    def __init__(self, location, value, isDiscovered):
        self.location = location
        self.value = value
        self.isDiscovered = isDiscovered

#create dictionary to access values?
tiles = {}
for i in range(len(Variables)):
    tiles[str(i)] = Tile(i, Variables[i], False)

print """
Instructions: Flip over two tiles. 
If your tiles match, the tiles will be revealed permenantly.
If your tiles do not match, the tiles will be covered again.
Try to match all of the tiles until all tiles are revealed.
Good Luck!"""

#allow the user to choose tiles based on location to turn over

def Discovered():
    for loc,tile in tiles.items():
        if tile.isDiscovered == False:
            return False
    return True

while not Discovered():    
    displayBoard(tiles)
    choice1 = raw_input("Choose your first tile: ")
    choice2 = raw_input("Choose your second tile: ")
    print tiles[choice1].value
    print tiles[choice2].value
    if tiles[choice1].value == tiles[choice2].value:
        print "You've got a match!"
        location = tiles[choice1].value
        tiles[choice1].isDiscovered = True
        tiles[choice2].isDiscovered = True
    else:
        print "Sorry, try again."

displayBoard(tiles)

# def match(choice1, choice2):
#     if tiles[choice1].value == tiles[choice2].value:
#         print "You've got a match!"
#         return tiles[choice1].value
#         location = tiles[choice1].value
#     else:
#         print "Sorry, try again."

# if matching values, flip over; else displayboard


