dr# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:19:55 2018

@author: Dell

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
 find the sum of the even-valued terms.
"""

# first i declared previous fibonacci, current fibonacci, next fibonacci numbers and 
# summary for even-valued fibonacci terms 
# then created an endless loop
# next fibonacci term will be previous + current
# then i checked if fibonacci is passing the maximum (limit)
# then assigned previous value and current value
# checked if fibonacci is even
# if yes, added to summary
# this solution works for any properly given number.

def EvenFibonacci(maximum):
    prevNumber,currNumber,nextNumber,summary=1,1,0,0
    while(maximum):
        nextNumber=prevNumber+currNumber
        if(nextNumber>maximum):
            break        
        prevNumber=currNumber
        currNumber=nextNumber
        if(nextNumber%2==0):
            summary=summary+nextNumber
            print(nextNumber)
            
    return summary

result=EvenFibonacci(4000000)
print(result)