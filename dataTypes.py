""" Data types including strings """

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


blah = "blahblahblah"
print(blah[4:8])

for i in range(12, 18):
    print(i)


colors = ['red', 'gold', 'green']
color = colors[1]
print(color)

#why does this not print "red"?
colors.append('black')

#add only takes one argument
#colors.append('blue', 'white')  -- not valid

colors.append('blue')
colors.append('white')
print(colors)

#slice

print(colors[:3])
print(colors[2:3])
print(colors[2:])

print("slice also works for a string")
print(color[1:])


favorite_colors = {'Graham': 'blue', 'Eric': 'green', 'Terry': 'orange'}
print(favorite_colors)
grahams_favorite = favorite_colors['Graham']
print(grahams_favorite)
