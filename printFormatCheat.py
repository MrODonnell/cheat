"""This cheatsheet demonstrates basic uses of string formatting
for more complete information see:
https://docs.python.org/3.1/library/string.html#format-examples
"""

# This is the basic example of how to use the format function
# curly brackets are used to indicate a replacement field within the string
# The format function supplies the input
# the replacement field optionally indicates the position of the input
# and then some formatting information (the part after the colon)

print('    #######  first example  #######')
print('The word "{0:s}" occurs {1:2.2f}  times'.format('special', 12))

print('\n    #######  table output example  #######')
# padding can display like a table

for x in range(1, 9):
    print('{0:5d} {1:5d} {2:5d}'.format(x, x*x, x*x*x))


print('\n    #######  time example  #######')
# here are several alternative examples for fomatting some numbers
# note that the datetime module provides advanced ways to handle time
hours = 2
seconds = 9
minutes = 34
# outputs with leading zeros
print('{0:02d}:{1:02d}:{2:02d}'.format(hours, seconds, minutes))
# no leading zeros
print('{0:2d}:{1:2d}:{2:2d}'.format(hours, seconds, minutes))
# demonstrates that position parameter is optional
print('{:02d}:{:02d}:{:02d}'.format(hours, seconds, minutes))
# this is the old way to format -- you might encounter this is legacy code
print('%.2d:%.2d:%.2d' % (hours, minutes, seconds))

# shortens long float numbers
average = 23.343245698
print("The average is: {0:0.2f}".format(average))

# it will round; however rounding is very complicated and not always accurate
another_average = 23.34999
print("The average is: {0:0.2f}".format(another_average))


# old style string formatting
# not used for new code very often, but you will see it in legacy code
# so it is a good idea to know what it is doing
# that s stands for string

name = "Juliette"
print("Hello %s, how are you?" % name)

