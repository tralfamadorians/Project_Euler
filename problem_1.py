import pandas as pd, numpy, matplotlib

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

#don't double count the multiples of 3 and 5!
total = 0
for i in range(0,1000):
  if i%3 == 0 and i%5 == 0:
    total += i
  if i%3 == 0 and i%5 != 0:
    total += i
  if i%3 != 0 and i%5 == 0:
    total += i     

print()
print()
print('The total is ' + str(total))

