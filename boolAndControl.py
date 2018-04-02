""" Samples of boolean operators and control stuctures that use them.
    If statements selectively execute code based a boolean operation
    An "if statement" will execute for True
    """

# this is an assignement, NOT a comparision
# comparision (which follows) uses ==
x = 41
# Boolean operators

if x == 42: # equals
    print("equals")

if x != 42: # not equal 
    print("not equals")
    
if x > 42: # greater than
    print("greater than")
    
if x >= 42: # greater than or equal to
    print("greater than or equal to")
    
if x < 42: # less than
    print("less than")
    
if x <= 42: # less than or equal to
    print("less than or equal to")

# assign the value of 1 to the variable named "numb"

numb = 1
# elif executes ONLY if the if statement does not
if numb == 1:
    print("one")
elif numb < 2:
    print("two")
else:
    print("bigger number")

# A while look executes for as long as the comparision is True
i = 0
while i < 5:
    print('hello')
    i += 1
    
# a for loop operates on a range of numbers
for number in range(12, 20):
    print(number)

# This is a nested loop
# notice that is executes two loops, one inside the other
# i is commonly used as a variable that iterates
# for a nested loop you need two differnt iterator variables
# is it not uncommon to use j because it is the next letter after i
# it is unfortunate that they look so similar

i = 0
j = 0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print('\n###############')
    j = 0
    i += 1
