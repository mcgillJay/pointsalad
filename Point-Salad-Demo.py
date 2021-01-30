
import random

class Player:
    def __init__(self, player, score, hand):
        self.player = player
        self.score = score
        self.hand = hand

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

class Game:
    x, y = (3, 3)
    stackSize = 5
    board = []

    def __init__(self):
        self.board = [[0]*3]*3
        print(self.board)

    #create and add a card
    def addCard(self, targetStack):
        randNum = random.randint(0, len(resourceTypes)-1)
        resource = resourceTypes[randNum] 
        card = Card("resource", resource)
        targetStack.append(card)

    #populate a stack
    def createStack(self, targetStack):
        ###
        stackSize = self.stackSize
        ###
        for x in range(stackSize):
            self.addCard(targetStack)

    def dealStack(self):
        ### have a problem here not sure how best to move forward
        self.createStack(self.board[0][0])
        self.createStack(self.board[1][0])
        self.createStack(self.board[2][0])

    def printBoard(self):
        print('Current Board')
        print(self.board)

    def updateBoardPos(self, newValue,  x , y):
        self.board[x][y] = newValue
        

new_game = Game()

new_game.printBoard()

new_game.updateBoardPos(6, 1, 2)

new_game.printBoard()



'''

def dealMarket(y,x):
    if len(board[x]) < 1:
        board[x].append(board[y][0])
        board[y].pop(0)







#veggieBuyers = []
#players = Input("enter player number? (2-6)")
#players = 2

######################################################

def gameSet(players):
    for x in players:
        score = 
        playerScore = Player("score", score[x])
        veggieBuyers.append(playerScore)
        players = players - 1 
        






#print the stack contents
def printStack(targetStack, stackName):
  print('------ Stack ' + stackName + ' ------')
  for x in targetStack:
    print(x.resource.name, x.resource.points, x.resource.color)
 


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



'''




