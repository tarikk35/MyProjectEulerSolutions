# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:27:30 2018

@author: Dell

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

def PrimeFinder(index):
    currIndex,number,prime=0,2,0
    while(currIndex<=index):
        dividedCount=0
        for i in range(2,int(math.sqrt(number)+1)):
            if number%i==0:
                dividedCount+=1
        if dividedCount==0:
            prime=number
            currIndex+=1
        number+=1
    return prime       

prime=PrimeFinder(10000)
print(prime)