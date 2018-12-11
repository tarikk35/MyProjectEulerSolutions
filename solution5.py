# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 22:17:59 2018

@author: Dell

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# primelist returns prime list for given range
# lowestcommonmultiple 
# first i declared variables
# i made a loop creating a number list for given range
# created a loop iterates while prime list iteration index is bigger than prime list size
# created an inside loop ranges from zero to number list length
# checked all numbers if they are divisible without remainder by prime number
# if yes, divide it
# if there is at least one divisible number, multiply prime number by previous multiplication
# if there is zero divisible number, increase prime list index.
# multiplication is our lowest common multiple number.
# this solution can work for any properly given range.
 
def PrimeList(minNumber,maxNumber):
    primeList=[]
    for i in range(minNumber,maxNumber):
        divCount=0
        for j in range(minNumber,maxNumber-1):
            if(i%j==0):
                divCount=divCount+1       
        if(divCount==1):
            primeList.append(i)
    return primeList

def LowestCommonMultiple(minRange,maxRange):
    numbers,primeNumbers,primeIndex,lcm,divCount= [],[],0,1,0
    for i in range(minRange,maxRange):
        numbers.append(i)
    primeNumbers=PrimeList(minRange,maxRange)
    while(primeIndex<len(primeNumbers)):
        divCount=0
        for i in range(0,len(numbers)):            
            if(numbers[i]%primeNumbers[primeIndex]==0):
                numbers[i]=int(numbers[i]/primeNumbers[primeIndex])
                divCount=1
        if(divCount>0):
            lcm=lcm*(primeNumbers[primeIndex])
        else:
            primeIndex+=1
                        
    return lcm

lcm=LowestCommonMultiple(2,21)
print(lcm)
