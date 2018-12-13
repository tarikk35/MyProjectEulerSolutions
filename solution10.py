# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:52:42 2018

@author: Dell

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


"""
# no need to check even numbers because they can be divided by two

import math

def FindSumOfPrimes(minNumber,maxNumber):
    summary=2
    for number in range(3,maxNumber,2):
        if all(number%i!=0 for i in range(3,int(math.sqrt(number))+1, 2)):
            summary+=number
    return summary

summary=FindSumOfPrimes(0,2000000)
print(summary)