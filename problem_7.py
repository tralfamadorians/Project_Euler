import pandas as pd, numpy, matplotlib


#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

# brute force
num_primes = 1
for b in range(3,1000000,2):
  if num_primes < 10002:             
    num_primes += 1 
    for n in range(2,b//2):  # prime?
      if b%n == 0:
        #num_primes -= 1
        #break
  if num_primes == 10001:
    print('The 10,001st prime number is', b)   
    break   

#algorithm- Sieve of Eratosthenes
upper_limit = 200000
num_primes = 0 
goal = 10001
list = [True for i in range(upper_limit+1)] #default prime
for n in range(2,upper_limit+1):
  if list[n] == True and n <= upper_limit*2: #if prime
    for i in range(n**2,upper_limit+1,n): #remove multiples
      list[i] = False
    n += 1
list[0] = False
list[1] = False  
for p in range(upper_limit+1):
  if list[p] == True:
    num_primes += 1
    if num_primes == goal:
      print('The 10,001st prime number is', p)
      break
if num_primes < goal:
  print('Upper range not high enough.')

    



  
   


