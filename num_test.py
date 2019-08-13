# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:22:58 2019

@author: jim
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”
"""
enter_a_number=int(input('enter a number : '))
if 10>enter_a_number:
    print('Too low')
elif enter_a_number in range(10,20):
    print('correct')
else:
    print('Too high')


