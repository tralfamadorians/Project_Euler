import pandas as pd, numpy, matplotlib

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a = 1
b = 1
total_even = 0
while a <= 4000000 or b <= 4000000:
  a = a + b
  if a >= 4000000:
    break
  else:
    if a%2 == 0:
      total_even += a
  b = b + a
  if b >= 4000000:
    break
  else:
    if b%2 == 0:
      total_even += b  
print(total_even)  
