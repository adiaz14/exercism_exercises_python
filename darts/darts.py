import math


def score(x, y):
    score = 0
    distance = math.sqrt((x**2)+(y**2))
    if(distance >= 0 and distance <= 1):
        score = 10
    elif(distance > 1 and distance <= 5):
        score = 5
    elif(distance > 5 and distance <= 10):
        score = 1
    else:
        score = 0
    return score
