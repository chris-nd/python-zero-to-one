from collections import namedtuple
import math

def distance(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2

    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(distance((0, 0), (3, 4)))

# 2ème approche avec la fonction namedtuple du module collection
# Point = namedtuple("Point", ['x', 'y'])

# def distance(p1, p2):
#     return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

# print(distance(Point(0, 0), Point(3, 4)))