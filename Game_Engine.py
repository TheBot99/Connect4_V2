import numpy as np
import time
import os
from Gravity import Gravity_alg
from Variebles import empty_columns
from Full_C import full_columns

def Engine():
  Gravity_alg()
  full_columns()