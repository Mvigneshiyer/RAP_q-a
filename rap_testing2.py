# -*- coding: utf-8 -*-
"""RAP_testing2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cVQEabsOBcpJ_M2seYXzP5bKh36bnA57
"""

import collections
def CountFrequency(arr):
  return collections.Counter(arr)
N = int(input("enter an integer : "))
for i in range(N):
  arr.append(int(input()))       
# Driver function 
if __name__ == "__main__":  
    freq = CountFrequency(arr) 
  
    
    for key, value in freq.items():
        print(key, " - ", value)

