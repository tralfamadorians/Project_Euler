import pandas as pd, numpy, matplotlib

#The sum of the squares of the first ten natural numbers is, 12+22+...+102=385
#The square of the sum of the first ten natural numbers is, (1+2+...+10)2=552=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

total = 0
sum_square = 0
for n in range(1,101):
  sum_square += n ** 2
  total += n
square_sum = total ** 2

print(square_sum - sum_square)