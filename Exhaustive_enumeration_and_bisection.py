# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:29:17 2020

@author: bryan
"""

# Find the integer cube root of a perfect cube.  Print the cube root.  If not
# a perfect cube print that.  Use exuastive enumeration.  Start at zero anc ount upward
# by one.  Cube that number each time and compare to the inputed number.  If
# the computed value lands exactly on the input number it is a perfect cube.  If
# it overshoots the number it is not a perfect cube
#
#x = int(input('Enter an integer:>> '))
#ans = 0
#while ans**3 < abs(x):
#    ans += 1
#if ans**3 != abs(x):
#    print(x, "is not a perfect cube")
#else:
#    if x < 0:
#        ans = -ans
#    print(f'The cube root of {x} is {ans}')

# Find the square root of a number using bisection search

x = 25
epsilon = 0.01
num_guesses = 0
high = x
low = 0
ans = (high + low)/ 2

while abs(ans**2 - x) >= epsilon:
    print(f'low = {low} , high = {high} , ans = {ans}')
    num_guesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
print(f'The number of guesses = {num_guesses}')
print(f'The square root of {x} is close to {ans}')