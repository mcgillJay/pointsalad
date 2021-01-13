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

stackSize = 5

#create and add a card
def addCard(targetStack):
  randNum = random.randint(0, len(resourceTypes)-1)
  resource = resourceTypes[randNum]
  #what does Card("resource", resource) do? 
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

#print the stack contents
def printMarket(targetMarket, marketName):
  print('------ Market ' + marketName + ' ------')
  for x in targetMarket:
    print(x.resource.name, x.resource.points, x.resource.color)

board = [[],[],[],[],[],[],[],[],[]]  


         
def dealStack():
   createStack(board[0])
   createStack(board[1])
   createStack(board[2])
   
dealStack()

printStack(board[0], "One")
#printStack(board[1], "Two")
#printStack(board[2], "Three")
pause = input("pause")
print(pause)

#def beginTurn(zone):
    #will this work for moving point cards to resources? should probably be moved to a turnBegin/play function
   # if len(board[3]) < 1:
         Board[3].append(board[0][0])
  #      while x < 2:
   #        markets[x].append(stacks[x].pop)



while len(marketOne) <= 1:
    marketOne.append(cardStackOne[0])
    cardStackOne.pop(0)

printStack(cardStackOne, "One")
printMarket(marketOne, "One")
