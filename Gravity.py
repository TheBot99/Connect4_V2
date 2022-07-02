from Variebles import Board
import os
import time
def Gravity_alg():
  os.system('clear')
  print(Board)
  time.sleep(0.2)
  falling_User = True
  y = 0  
  y2 = 1
  x = 0
  while falling_User == True:
    if (Board[y, x]) == 1:
      if (Board[y2, x]) == 0:
        (Board[y, x]) = 0
        (Board[y2, x]) = 1
        os.system('clear')
        print(Board)
        time.sleep(0.2)
        if y < 5:
          y = y + 1
        else:
          if x < 6 :
            x = x + 1
          else:
            falling_User = False
            y = 0  
            y2 = 1
            x = 0
            falling_Bot = True
        if y2 < 5:
          y2 = y2 + 1
        else:
          if x < 6 :
            x = x + 1
          else:
            falling_User = False
            y = 0  
            y2 = 1
            x = 0
            falling_Bot = True
      else:
        if x < 6 :
          x = x + 1
        else:
          falling_User = False
          y = 0  
          y2 = 1
          x = 0
          falling_Bot = True
    else:
      if x < 6 :
        x = x + 1
      else:
        falling_User = False
        y = 0  
        y2 = 1
        x = 0
        falling_Bot = True
        
  while falling_Bot == True:
    if (Board[y, x]) == 2:
      if (Board[y2, x]) == 0:
        (Board[y, x]) = 0
        (Board[y2, x]) = 2
        os.system('clear')
        print(Board)
        time.sleep(0.2)
        if y < 5:
          y = y + 1
        else:
          if x < 6 :
            x = x + 1
          else:
            falling_Bot = False
            y = 0  
            y2 = 1
            x = 0
            falling_User = True
        if y2 < 5:
          y2 = y2 + 1
        else:
          if x < 6 :
            x = x + 1
          else:
            falling_Bot = False
            y = 0  
            y2 = 1
            x = 0
            falling_User = True
      else:
        if x < 6 :
          x = x + 1
        else:
          falling_Bot = False
          y = 0  
          y2 = 1
          x = 0
          falling_User = True
    else:
      if x < 6 :
        x = x + 1
      else:
        falling_Bot = False
        y = 0  
        y2 = 1
        x = 0
        falling_User = True  