# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 20:12:05 2018

@author: Dell
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# easy pythagorean triplet generator : u^2-v^2 , 2uv , u^2+v^2 works like magic
# low cost, no brute forcing, my computer thanks me ! but u always has to be bigger than v
# this solution can work for every properly given number

def FindTriplet(number):
    result=[]
    for i in range(2,number):
        for j in range(1,i):
            a=(i*i)-(j*j)
            b=(2*i*j)
            c=(i*i)+(j*j)
            if a+b+c == number:
                result.append(a)
                result.append(b)
                result.append(c)
    return result

result=FindTriplet(1000)
print(result[0]*result[1]*result[2])
