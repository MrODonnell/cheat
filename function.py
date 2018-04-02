""" To define a function, use the keywork "def" and put in a series of statements.
    Subsequent to the definition of a function, each line must be indented until the end
    The definition of a function must be before the call to the function in your code"""

def lyricsPrint():
    print("I'm a lumberjack and I'm ok")
    print("I sleep all night and I work all day")

def return_lyrics():
    lyrics = "I'm a lumberjack, and I'm okay."
    lyrics = lyrics + "I sleep all night and I work all day."
    return lyrics

lyricsPrint()
print(return_lyrics())

name = "Fredo"
def returnGreeting(name):
    greeting = "Hello, " + name
    return greeting
	
	
print(returnGreeting("James"))
print(name)

