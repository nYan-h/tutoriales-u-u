import random

def dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    return a, b

print(dice())
