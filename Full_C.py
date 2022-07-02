from Variebles import empty_columns, Board

def full_columns():
  if 0 in empty_columns:
    if (Board[0, 0]) != 0:
      empty_columns.remove(0)
  if 1 in empty_columns:
    if (Board[0, 1]) != 0:
      empty_columns.remove(1)
  if 2 in empty_columns:
    if (Board[0, 2]) != 0:
      empty_columns.remove(2)
  if 3 in empty_columns:
    if (Board[0, 3]) != 0:
      empty_columns.remove(3)
  if 4 in empty_columns:
    if (Board[0, 4]) != 0:
      empty_columns.remove(4)
  if 5 in empty_columns:
    if (Board[0, 5]) != 0:
      empty_columns.remove(5)
  if 6 in empty_columns:
    if (Board[0, 6]) != 0:
      empty_columns.remove(6)