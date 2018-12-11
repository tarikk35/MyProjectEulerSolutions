# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:36:26 2018

@author: Dell

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# first i declared i variable
# then i created a loop that will iterate while i variable squared is smaller than given number
# another loop iterates while given number is divisible to i variable without remainder.
# if divisible, divide it.
# at the end, increase i variable.
# this process continues until the given number is not divisible( number becomes largest prime factor )
# this solution works for any properly given number.

def PrimeFactor(number):
    i=2
    while i * i < number:
        while number%i == 0:
            number = int(number / i)
        i = i + 1
    return number
            
maxPrime=PrimeFactor(101)
print(maxPrime)