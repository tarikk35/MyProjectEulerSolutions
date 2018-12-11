# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:17:07 2018

@author: Dell

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.
"""
# sum of squares is calling itself (recursive) while minimum is smaller than maximum
# multiplies minimum value by itself , adds to total and increases minimum value
# sum of numbers is also calling itself while minimum is smaller than maximum
# adds minumum to total and increases minimum value
# this solution can work for any properly given range

def SumOfSquares(minNumber,maxNumber):
    if(minNumber<=maxNumber):
        sumOfSquares=(minNumber*minNumber)+SumOfSquares(minNumber+1,maxNumber)
        return sumOfSquares
               
    else:
        return 0
        
        
def SumOfNumbers(minNumber,maxNumber):
    if(minNumber<=maxNumber):
        summary=minNumber+SumOfNumbers(minNumber+1,maxNumber)
        return summary
    else:
        return 0

sumOfSquares=SumOfSquares(1,5)
print(sumOfSquares)
squareOfSum=SumOfNumbers(1,5)
squareOfSum=squareOfSum*squareOfSum
print(squareOfSum)
difference=squareOfSum-sumOfSquares
print(difference)