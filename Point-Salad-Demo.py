  
import random
# need to add scoring style and point card/resource bool.
#
class Card:
  def __init__(self, type, resource):
    self.type = type
    self.resource = resource

class Veggie:
  def __init__(self, name, points, color):
    self.name = name
    self.points = points
    self.color = color
    
resourceTypes = [
    Veggie("Lettuce", 1, "Green"),
    Veggie("Lettuce", 2, "Green"),
    Veggie("Lettuce", 3, "Green"),
    Veggie("Lettuce", 4, "Green"),
    Veggie("Lettuce", 5, "Green"),
    Veggie("Tomato", 1, "Red"),
    Veggie("Tomato", 2, "Red"),
    Veggie("Tomato", 3, "Red"),
    Veggie("Tomato", 4, "Red"),
    Veggie("Tomato", 5, "Red"),
    Veggie("Carrot", 1, "Orange"),
    Veggie("Carrot", 2, "Orange"),
    Veggie("Carrot", 3, "Orange"),
    Veggie("Carrot", 4, "Orange"),
    Veggie("Carrot", 5, "Orange"),
    Veggie("Mystery", random.randint(1, 10), "Rainbow" )
  ]

board = [[],[],[],[],[],[],[],[],[]]

stackSize = 5

######################################################

#create and add a card
def addCard(targetStack):
  randNum = random.randint(0, len(resourceTypes)-1)
  resource = resourceTypes[randNum]
  card = Card("resource", resource)
  targetStack.append(card)

#populate a stack
def createStack(targetStack):
  for x in range(stackSize):
    addCard(targetStack)

#print the stack contents
def printStack(targetStack, stackName):
  print('------ Stack ' + stackName + ' ------')
  for x in targetStack:
    print(x.resource.name, x.resource.points, x.resource.color)
 
def dealStack():
    createStack(board[0])
    createStack(board[1])
    createStack(board[2])

#check if value is in market list and fill
def dealMarket(y,x):
    if len(board[x]) < 1:
        board[x].append(board[y][0])
        board[y].pop(0)

#fill entire market
def beginTurn():
    dealMarket(0,3)
    dealMarket(1,4)
    dealMarket(2,5)
    dealMarket(0,6)
    dealMarket(1,7)
    dealMarket(2,8)

#data check full board
def callStacks():
    print("---------------------")
    printStack(board[0], "One")
    printStack(board[3], "Market One")
    printStack(board[6], "Market One")
    printStack(board[1], "Two")
    printStack(board[4], "Market Two")
    printStack(board[7], "Market Two")
    printStack(board[2], "Three")
    printStack(board[5], "Market Three")
    printStack(board[8], "Market Three")

dealStack()

callStacks()

beginTurn()

callStacks()









