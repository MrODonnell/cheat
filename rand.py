"""
This is a very simple function that will return
a random number from one to 6 by default
and a demonstration of how to use it
You must import random
"""

import random

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven']

def rtn_rand(beg=1, end=6):
        return random.randint(beg,end)

count = 0
while count < 100:
    x = rtn_rand()
    print(numbers[x])
    count += 1
