import pandas as pd, numpy, matplotlib

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#n = 43365644
#[int(d) for d in str(n)]
#[4, 3, 3, 6, 5, 6, 4, 4]
#Find the largest palindrome made from the product of two 3-digit numbers.

largest_palindrome = 0
for number1 in range(999,900,-1):
  for number2 in range(999,900,-1):
    product = number1 * number2
    digits = [int(d) for d in str(product)] #split digits of product
    first_digit = digits[0]
    second_digit = digits[1]
    third_digit = digits[2]
    fourth_digit = digits[3]
    fifth_digit = digits[4]
    last_digit = digits[len(digits)-1]
    if first_digit == last_digit and second_digit == fifth_digit and third_digit == fourth_digit:
      if product > largest_palindrome:
        largest_palindrome = product              
if largest_palindrome == 0:
  print('there is no palindrome')
else:
  print(largest_palindrome, 'is the largest palindrome')




