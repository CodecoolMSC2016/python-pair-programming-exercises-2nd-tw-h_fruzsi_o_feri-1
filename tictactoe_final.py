import random
import os

os.system('cls' if os.name == 'nt' else 'clear')
Symbol = ""
board = []

def rules():
      print("\033[91m"+ "Rules: " + "\033[0m" + "\nThe numbers represent the places where you can put your character.")
      print("In order to win you have to put three of your characters next to each other.\n(vertically, horizontally, or diagonally)")
      print("\n 7 | 8 | 9\n-----------\n 4 | 5 | 6\n-----------\n 1 | 2 | 3\n")
rules()


play_with_comp = input("Do you want to play against the computer? (Y/N)    ")
if play_with_comp[0] == "N" or play_with_comp[0] == "n":
      user_name1 = input("What is name of player one?   ")
      user_name2 = input("What is name of player two?   ")
elif play_with_comp[0] == "Y" or play_with_comp[0] == "y":
      human_name = input("What is your name?    ")
      comp_name = ("Computer")
else:
      print("The game quits now, restart the game, and please enter a valid answer! (Y/N) or (y/n)")
      quit()      



def drawBoard():
    print("\n")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("~~~~~~~~~~~")                          
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("~~~~~~~~~~~")
    print(" " + board[1] + " | " + board[2] + " | " + board[3], "\n")


def whoStarts():
      iTurn = random.randint(1, 2)
      if iTurn == 1:
            print(user_name1,("can start."))
            print("You are with: " + "\033[92m" + "X" + "\033[0m" + ".")
            return "\033[92m" + "X" + "\033[0m"
      else:
            print(user_name2,("can start."))
            print("You are with: " + "\033[94m" +  "O" + "\033[0m" + ".")
            return "\033[94m" +  "O" + "\033[0m"

def whoStarts_comp():
      iTurn = random.randint(1, 2)
      if iTurn == 1:
            print(human_name,("can start."))
            print("You are with: " + "\033[92m" + "X" + "\033[0m" + ".")
            return "\033[92m" + "X" + "\033[0m"
      else:
            return "\033[94m" +  "O" + "\033[0m"


def doMove(Symbol,move):
      nums = [i for i in range(1, 10)]
      while not move in nums:
            try:
                 print("Choose a number between 1 and 9")
                 if Symbol == "O":
                        iTurn = 1
                        while iTurn == 1:
                              move_string = int(input(": "))
                              if move_string != "":
                                    move = int(move_string)
                                    if board[move] == " ":
                                          board[move] = Symbol
                                          iTurn -= 1
                                    else:
                                          print("Choose an empty bracket!")
                                          drawBoard()
                 else:
                       iTurn = 0
                       while iTurn == 0:
                             move_string = str(input(": "))
                             if move_string != "":
                                   move = int(move_string)
                                   if board[move] == " ":
                                         board[move] = Symbol
                                         iTurn += 1
                                   else:
                                         print("Choose an empty bracket!")
            except (ValueError, IndexError):
                  pass

def doMove_comp(Symbol,move):
      nums = [i for i in range(1, 10)]
      while not move in nums:
            try:
                 print("Choose a number between 1 and 9")
                 if Symbol == "\033[94m" +  "O" + "\033[0m":
                        iTurn = 1
                        while iTurn == 1:
                              move_string = random.randint(1, 10)
                              if move_string != "":
                                    move = int(move_string)
                                    if board[move] == " ":
                                          board[move] = Symbol
                                          iTurn -= 1
                                    else:
                                          print("Choose an empty bracket!")
                                          drawBoard()
                 else:
                       iTurn = 0
                       while iTurn == 0:
                             move_string = str(input(": "))
                             if move_string != "":
                                   move = int(move_string)
                                   if board[move] == " ":
                                         board[move] = Symbol
                                         iTurn += 1
                                   else:
                                         print("Choose an empty bracket!") 
            except (ValueError, IndexError):
                  pass


def isWinner():
      winValues = ([7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1])
      for value in winValues:
            if (board[(value[0])] == board[(value[1])] == board[(value[2])] == "\033[92m" + "X" + "\033[0m"):
                  drawBoard()
                  print("%s is the winner!" % user_name1)
                  rematch()
            elif (board[(value[0])] == board[(value[1])] == board[(value[2])] == "\033[94m" +  "O" + "\033[0m"):
                  drawBoard()
                  print("%s is the winner!" % user_name2)
                  rematch()
            else:
                  pass

def isWinner_comp():
      winValues = ([7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [9, 5, 1])
      for value in winValues:
            if (board[(value[0])] == board[(value[1])] == board[(value[2])] == "\033[92m" + "X" + "\033[0m"):
                  drawBoard()
                  print("%s is the winner!" % human_name)
                  rematch_comp()
            elif (board[(value[0])] == board[(value[1])] == board[(value[2])] == "\033[94m" +  "O" + "\033[0m"):
                  drawBoard()
                  print("%s is the winner!" % comp_name)
                  rematch_comp()
            else:
                  pass


def rematch():
      global board
      global Symbol
      re_match = input("Rematch?(y/n): ")
      if re_match == "y" or re_match == "yes":
            board = [' '] * 10
            if Symbol == "\033[92m" + "X" + "\033[0m":
                  print("\n%s, it is your turn." % user_name1)
            else:                                           
                  print("\n%s, it is your turn." % user_name2)            
      else:
            quit()

def rematch_comp():
      global board
      global Symbol
      re_match = input("Rematch?(y/n): ")
      if re_match == "y" or re_match == "yes":
            board = [' '] * 10
            if Symbol == "\033[92m" + "X" + "\033[0m":
                  print("\n%s, it is your turn." % human_name)
            else:                                           
                  print("\n%s picks now." % comp_name)            
      else:
            quit()


def isFull():
      global Symbol
      if ' ' in board[1:10]:
            os.system('cls' if os.name == 'nt' else 'clear')
            if Symbol == "\033[92m" + "X" + "\033[0m":
                  print("\n%s, it is your turn." % user_name2)
                  Symbol = "\033[94m" +  "O" + "\033[0m"
            else:
                  print("\n%s, it is your turn." % user_name1)
                  Symbol = "\033[92m" + "X" + "\033[0m"
      else:
            print("\nIt's a tie!")
            drawBoard()
            rematch()

def isFull_comp():
      global Symbol
      if ' ' in board[1:10]:
            os.system('cls' if os.name == 'nt' else 'clear')
            if Symbol == "\033[92m" + "X" + "\033[0m":
                  print("\n%s picks now." % comp_name)
                  Symbol = "\033[94m" +  "O" + "\033[0m"
            else:
                  print("\n%s, it is your turn." % human_name)
                  Symbol = "\033[92m" + "X" + "\033[0m"
      else:
            print("\nIt's a tie!")
            drawBoard()
            rematch_comp()


            
while play_with_comp[0] == "N" or play_with_comp[0] == "n":
      board = [' '] * 10
      Symbol = whoStarts()
      gameIsOn = True
      while gameIsOn:
            drawBoard()
            move = None
            doMove(Symbol, move)
            if isWinner():
                  drawBoard(board)
            elif isFull():
                  drawBoard()

while play_with_comp[0] == "Y" or play_with_comp[0] == "y":
      board = [' '] * 10
      Symbol = whoStarts_comp()
      gameIsOn = True
      while gameIsOn:
            drawBoard()
            move = None
            doMove_comp(Symbol, move)
            if isWinner_comp():
                  drawBoard(board)
            elif isFull_comp():
                  drawBoard()