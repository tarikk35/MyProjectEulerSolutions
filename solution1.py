# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:39:08 2018

@author: Dell

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
# first i declared a summary variable
# then first loop iterates until it hit its maximum value
# second loop iterates through numbers given (you can give any amount of numbers,for this problem, its 2)
# i check if number is multiple of any given number
# if yes, add it to total summary and exit the second loop
# this solution can work for any properly given number and any amount.

def SumOfIsDividedBy(maximum,*args):
    summary=0
    for i in range(maximum):
        for arg in args:
            if i>0 and (i%arg == 0):
                summary=summary+i
                break
    return summary

result=SumOfIsDividedBy(1000,3,5)
print(result)