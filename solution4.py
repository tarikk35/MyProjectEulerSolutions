# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:16:59 2018

@author: Dell

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# ispalindrome checks if given number is palindrome
# multiplier multiplys values starting from min ending at max
# first loop starts from maximum because we are looking for biggest palindrome
# second loop starts from previous iteration index because computers have feelings,too !
# and then i check if multiplication of two numbers is palindrome and is it biggest
# if yes, change it!
# this solution can work for any properly given ranges.

def IsPalindrome(number):
    number=str(number)
    return (False,True)[number==number[::-1]]
    
def Multiplier(minValue=99,maxValue=999):
    maxPalindrome=0
    for i in range(maxValue,minValue,-1):
        for j in range(i,minValue,-1):
            if IsPalindrome(i*j) and (i*j)>maxPalindrome:
                maxPalindrome=(i*j)
    return maxPalindrome

p=Multiplier(99,999)
print(p)