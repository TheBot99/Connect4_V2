import os
import time

def User():
  from Variebles import Board
  os.system('clear')
  print(Board) 
  Column_Input = input("What column do you want to drop a coin into: ")
  if Column_Input == "1"or Column_Input == "2" or Column_Input == "3" or Column_Input == "7" or Column_Input == "4" or Column_Input == "6" or Column_Input == "5":
    Column_Input = int(Column_Input)
    Column_Input = Column_Input - 1
    if (Board[0, Column_Input]) == 0:
      (Board[0, Column_Input]) = 1
    else:
      print("That Column is full")
      time.sleep(2)
      User()
  else:
    print("That is not a valid number")
    time.sleep(2)
    User()