import random
# need to add scoring style and point card/resoirce bool.
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
    
cardStackOne = []
Market1 = []
cardStackTwo = []
Market2 = []
cardStackThree = []
Market3 = []

Def dealStack:
   createStack(cardStackOne)
   createStack(cardStackTwo)
   createStack(cardStackThree)
   If market1 < 2:
    Market1.append(CardStackOne.pop)

DealStack()

printStack(cardStackOne, "One")
printStack(cardStackTwo, "Two")
printStack(cardStackThree, "Three")

