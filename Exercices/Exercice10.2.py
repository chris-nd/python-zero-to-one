import random

def randomNbRange(count, start, end):
    for _ in range(count):
        print(random.randint(start, end))

randomNbRange(5, 1, 100)