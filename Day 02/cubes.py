import re
import math

def p1():
    limits = {"red": 12, "green": 13, "blue": 14}
    with open("input") as f:
        games = [re.split("[:;,] ", game) for game in f.read().splitlines()]

    total = 0
    for game in games:
        if all(int(draw.split()[0]) <= limits[draw.split()[1]] for game in games for draw in game[1:]):
            total += int(game[0].split()[1]) 
    print(total)

def p2():
    with open("input") as f:
        games = [re.split("[:;,] ", game)[1:] for game in f.read().splitlines()]

    total = 0
    for game in games:
        fewest = {"red": 0, "green": 0, "blue": 0}
        for draw in game:
            c = draw.split()
            fewest[c[1]] = max([fewest[c[1]], int(c[0])])
        total += math.prod(val for val in fewest.values())
    print(total)

p1()
p2()