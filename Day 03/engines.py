import math

#Returns all numbers adjacent to an "Engine Part" as a string
#Searchers the row above, of, and below a part.
def findNumbers(parts, j, i):
    for row in [j-1, j, j+1]:
        if parts[row][i].isnumeric():
            start, end = i, i+1
            while start > 0 and parts[row][start-1].isnumeric():
                start -= 1
            while end <= len(parts[row]) and parts[row][end].isnumeric():
                end += 1
            yield int(parts[row][start:end])
        else:
            if parts[row][i-1].isnumeric():
                start = i
                while start > 0 and parts[row][start-1].isnumeric():
                    start -= 1
                yield int(parts[row][start:i])
            if parts[row][i+1].isnumeric():
                end = i+2
                while end < len(parts[row]) and parts[row][end].isnumeric():
                    end += 1
                yield int(parts[row][i+1:end])


def p1():
    with open("input") as f:
        parts = f.read().splitlines()

    numbers = []
    misses = "0123456789."
    for j in range(len(parts)):
        for i in range(len(parts[j])):
            if parts[j][i] not in misses:
                numbers += findNumbers(parts, j, i)

    print(sum(numbers))

#just need to look forthe gear symbol, the fndNumbers algo will work just fine, and then we can filter only those with two numbers 
def p2():
    with open("input") as f:
        parts = f.read().splitlines()

    numbers = 0
    for j in range(len(parts)):
        for i in range(len(parts[j])):
            if parts[j][i] == "*":
                gear = list(findNumbers(parts, j, i))
                if len(gear) == 2:
                    numbers += math.prod(gear)

    print(numbers)

p1()
p2()