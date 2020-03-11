import pandas as pd, numpy, matplotlib

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallest = 0
test = 0
multiple = 19*17*13*11*7*5*3*2 #19,17,13,7,5,3,2 are prime
while smallest == 0:
  divisible = True
  test += multiple  
  for r in range(11,21):
    if test%r != 0:
      divisible = False
      print('Not ',test)
      break
  if divisible == True:
    smallest = test
print(smallest)      