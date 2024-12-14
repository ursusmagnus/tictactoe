import random 
import time

# Function declarations
def printgrid():
    for i in range(9):
        print( cells[i], " ", ".", " ", end="")
        if ((i+1)%3 == 0):
            print("")

def win() :
    for x in range(3) :
        if cells[3*x] == cells[3*x + 1] and cells[3*x] == cells[3*x + 2] :
            return True
        if cells[1*x] == cells[1*x + 3] and cells[1*x] == cells[1*x + 6] :
            return True
        if (cells[0] == cells[4] and cells[0] == cells[8]):
            return True
        if (cells[2] == cells[4] and cells[2] == cells[6]):
            return True

    return False

def draw():
    for x in range(9) :
        if cells[x] != "x" and cells[x] != "o" :
            return False
    return True 

def getMove(isAI):
    if isAI :
        return getMoveAI()
    else :
        return getMoveHuman()
   
def getMoveHuman() :
    moveStr=input("pick a cell 1-9 : ")
    if moveStr.isdigit() :
        move = int(moveStr)
        if move > 0 and move < 10 :
            return move 
    return 0

def getMoveAI() :
    while True :
        time.sleep(1)
        move = random.randint (1, 9)
        print("ai picked ", move)
        if (cells[move-1] != "x" and cells[move-1] != "o") :
            return move

def initializeGame():
    global playersAI
    mode = int(input("how many players? : "))
    match mode :
        case 0:
            playersAI = [ True , True]
        case 1 :
            playerschoose = input("chooseplayer_select x or o : ")
            if playerschoose == "x" :
                playersAI = [False, True]
            elif playerschoose == "o" :
                playersAI = [True ,False]
            else :
                print("Invalid entry")
                exit(1)
        case 2 :
            playersAI= [False, False]
        case _ :
            print("Invalid entry")
            exit(1)

def startGame() :
    printgrid()
    winning= False
    count = 0

    while not winning :
        p_index = count%2
        player = players[p_index]
        print ("ready player ", player )
        move = getMove(playersAI[p_index])

        if (move == 0):
            print("enter again")
            continue
        if  cells[move-1] == "x" or cells[move-1] == "o" :
            print("NO CHEATING >:( ")
            continue
        cells[move-1] = player
        printgrid()
        if win() :
            print("congratulations player ", player)
            winning = "yes"
        elif draw() :
            print("it'a a draw!")
            winning = "yes"

        count = count + 1

# Script execution
playersAI = [False, False]
cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ]
players = ["x", "o"]
initializeGame()
startGame()
