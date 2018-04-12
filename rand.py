import random

def die():
        return random.randint(1,6)
count = 0
while count < 100:
    x = die()
    print(x)
    count += 1
