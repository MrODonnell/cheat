greeting = "Hello world"
print(greeting)
# To get started you need to be aware of three data types:
# int is an Integer
# float is a decimal
# sting is letters, words, whitespace, and special characters including numbers
pageDivider = '\n#####################\n\n'
print(pageDivider)

# Addition uses the + operator
addition = 2 + 2

print("The sum of 2 and 2 is: ")
print(addition, end = pageDivider)


# Subtraction uses the - operator
subtraction = 4 - 2

print("The differnce of 4 minus 2 is: ")
print(subtraction, end = pageDivider)

# Multiplication uses the * operator
multiplication = 4 * 8

print("The produce of 4 times 8 is: ")
print(multiplication, end = pageDivider)

# exponent uses ** as the operator
exponent = 2 ** 3
print("2 to the power of 3 is: ")
print(exponent, end = pageDivider)

# Division is more tricky than you might think.
# Be aware that in Python 3 division results in a float

someFloat = 7 / 3
# Division uses / as the operator and returns a float
# this is a change from Python2
print("In Python3 division results in a 'float' :")
print(someFloat, end = pageDivider)


# Even if the division results in an integer division returns a float
anotherFloat = 8 / 2
print("8 divided by 2 will also result in a 'float' :")
print(anotherFloat, end = pageDivider)

# With floor division the result is truncated, not rounded.
floorDivision = 7 // 3
print("7 divided by 3 using floor divistion:")
print(floorDivision, end = pageDivider)

#Modulus essentially the remainder

mod = 7 % 3
print("""Modulus is the amount left over after the
      first number is divided by the second number""")
print ("mod 7 % 3 is:")
print(mod, end = pageDivider)
