print("Hello World")
# To get started you need to be aware of three data types:
# int is an Integer
# float is a decimal
# sting is letters, words, whitespace, and special characters including numbers
pageDivider = '#####################\n'
print(pageDivider)

# Addition uses the + operator
addition = 2 + 2

print("The sum of 2 and 2 is: ")
print(addition)
print(pageDivider)

# Subtraction uses the - operator
subtraction = 4 - 2
print("The differnce of 4 minus 2 is: ")
print(subtraction)
print(pageDivider)

# Multiplication uses the * operator
multiplication = 4 * 8
print("The produce of 4 times 8 is: ")
print(multiplication)
print(pageDivider)

# exponent uses ** as the operator
exponent = 2 ** 3
print("2 to the power of 3 is: ")
print(exponent)
print(pageDivider)

# Division is more tricky than you might think.
# Be aware that in Python 3 division results in a float

someFloat = 7 / 3
# Division uses / as the operator and returns a float
print("In Python3 division results in a 'float' :")
print(someFloat)
print(pageDivider)

# Even if the division results in an integer division returns a float
anotherFloat = 8 / 2
print("8 divided by 2 will also result in a 'float' :")
print(anotherFloat)
print(pageDivider)

# With floor division the result is truncated, not rounded.
floorDivision = 7 // 3
print("7 divided by 3 using floor divistion:")
print(floorDivision)
print(pageDivider)

#Modulus essentially the remainder

mod = 7 % 3
print("""Modulus is the amount left over after the
      first number is divided by the second number""")
print ("mod 7 % 3 is:")
print(mod)
print(pageDivider)


#### day two ####


def lyricsPrint():
    print("I'm a lumberjack and I'm ok")
    print("I sleep all night and I work all day")

def return_lyrics():
    lyrics = "I'm a lumberjack, and I'm okay."
    lyrics = lyrics + "I sleep all night and I work all day."
    return lyrics

lyricsPrint()
print(return_lyrics())

 
#### Day Three ####

name = "Fredo"
def returnGreeting(name):
    greeting = "Hello, " + name
    return greeting
	
	
print(returnGreeting("James"))
print(name)

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

numb = 1
if numb == 1:
    print("one")
elif numb == 2:
    print("two")
else:
    print("bigger number")

i = 0
while i < 5:
    print('hello')
    i += 1

for number in range(12, 20):
    print(number)

i = 0
j = 0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print('\n###############')
    j = 0
    i += 1

# Day four

# Lists

fruits = ['apple', 'orange', 'banana', 'grape', 'grapefruit']

firstFruit = fruits[0]  # lists are zero indexed, so the first element is 0
print(firstFruit)

lastFruit = fruits[-1] # negative number count back from the last item
print(lastFruit)

# There is a shortcut for loop through a list

for fruit in fruits:    # The keyword "for" loops through a list
    print(fruit)        # The keywork "in" will assign each value
                        # To the variable name that comes before "in"

# List slice

twoFruits = fruits[1:3] # Returns a list including "organge" and "banana"
for fruit in twoFruits:
    print(fruit)

# Dictionaries

favFoods = {'cheese': 'camembert', 'meat': 'beef', 'vegitable': 'carrot'}
# As directed by pep 8 do not exceed 80 characters per line

for foodType, food in favFoods.items():
    print('My favorite ' + foodType + ' is: ' + food)

print(favFoods['meat'])

# The hanging indentation helps keep 80 char limit and improve readability
favFoods = {'cheese': 'camembert',
            'meat': 'beef',
            'vegetable': 'carrot',
            'desert': 'pie',
            'meat product': 'spam'
            }

# string functions

# find function
# use when the index of the sub string is needed

string = "It will be easy to catch my catatonic cat."
subString = "cat"
stringIndex = string.find(subString)
print(stringIndex)

# when you only need "True" if the sub string is present use "in"
if(subString in string):
    print("yes")
else:
    print("no")

# change string to lower case
# this if helpful because "A" is not the same as "a"

crazyString = "I will be easy to cAtch my cAtAtonic cat."
stringIndex = crazyString.find(subString)
print(stringIndex)
stringIndex = crazyString.lower().find(subString)
print(stringIndex)

print(crazyString.lower())
print(crazyString)

if crazyString > string:
    print("crazy")
else:
    print("lowercase is greater than uppercase")

if "Z" < "a":
    print("uppercase letters come first")

# parameter is the value you pass to a function
# they do into the parentheses
# like this: ( parameter, anotherParameter)
# in the docs optional parameters are indicated by square brackets
# like this function(required, [optional])
# find takes optional begin and end index parameters

stringIndex = string.find(subString, 19)
print(stringIndex)

# any string can be "split" on any character, or characters
# the result is a list (sometimes called an array)
# you may not realize it now, but this can be very handy
someValues = "Laconia Gilford Belmont"
listOfValues = someValues.split()
print(listOfValues[1])
#here is a more complex example
keyValuePairs = "Bill: Laconia, Jane: Gilford, Tom: Belmont"
listOfPairs = keyValuePairs.split(", ")
count = 0
while count < len(listOfPairs):
    fname, town = listOfPairs[count].split(": ")
    print("first name is: " + fname + "\n town is: " + town)
    count += 1

# string functions
