import pandas as pd, numpy, matplotlib

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

# x%(range(1,x)) == 0 to find factors
# put those factors in a list
# check to see if those factors are prime

list = []
number = 600851475143
for factor in range(2,number//2): #divide by 2 to save time
  if number%factor == 0:          
    list.append(factor) 
    for n in range(2,factor//2):  #are the factors prime?
      if factor%n == 0:
        list.remove(factor)
        break

print()         
print(list)  
  
       