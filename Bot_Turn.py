import os
from Variebles import empty_columns, Board
from secrets import choice

def Bot():
  Column_Input = choice(empty_columns)
  (Board[0, Column_Input]) = 2