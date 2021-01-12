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
    Veggie("Lettuce", 6, "Green"),
    Veggie("Tomato", 2, "Red"),
    Veggie("Carrot", 2, "Orange"),
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
cardStackTwo = []
cardStackThree = []

Def dealStack:
   createStack(cardStackOne)
   createStack(cardStackTwo)
   createStack(cardStackThree)

DealStack()

printStack(cardStackOne, "One")
printStack(cardStackTwo, "Two")
printStack(cardStackThree, "Three")

