""" This is a cool effect Patrick Deegan found
in a video by Bryan Tong, aka tbong.
It displays text with a short delay, as if someone were typing to you.
I have demonstrated the technique, then created a function.
The function has a default time delay which allows you to
call the function using only the string as an argument,
or to specify a time delay other than the default
This technique requires that you import the time
"""

import time

display_string = "hello world slowly typed out"
for letter in display_string:
    print(letter, end='')
    time.sleep(0.1)
print('')

def display(s, t = 0.05):
    for letter in s:
        print(letter, end='')
        time.sleep(t)
    print('')


s = "Hello, would you like to play an interactive game?"
display(s)
display(s, 0.1)
display(s, 0.01)


