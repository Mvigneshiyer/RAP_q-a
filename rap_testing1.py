# -*- coding: utf-8 -*-
"""RAP_testing1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15VyJeSyGsqSOdi2fjVSDajJj3M93ZVXH
"""

from array import *
import re
import pandas as pd
import numpy as np
#input the value of N (where N is a natural number)
mylist = []
n=int(input("enter a number : "))
for i in range (1,n+1):
   mylist.append(i)
pass
for j in range(len(mylist)):
  if(j%3 == 0):
    print("Fizz")
    continue
  elif(j%5 == 0):
    print("Buzz")
    continue
  elif(j%3==0 & j%5==0):
    print("FizzBuzz")
    continue
  print(j)

