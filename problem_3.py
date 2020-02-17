import pandas as pd, numpy, matplotlib

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

# x%(range(1,x)) == 0 to find factors
# put those factors in a list
# check to see if those factors are prime

list = [0]
for i in range(2,13195):
  if 13195%i == 0:          #if i is a factor
    for n in range(2,i-1):  #check to see if i is prime
      prime = True
      if i%n == 0:          #i is not prime 
        prime = False
      if prime == True:
        list.append(i)      #add i to a list
         
print(list)    
       