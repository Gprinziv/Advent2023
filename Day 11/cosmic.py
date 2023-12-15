import re, itertools

with open("input") as f:
    galaxy = f.read().splitlines()

verticals, horizontals, stars = [], [], []
for i, _ in enumerate(galaxy[0]):
    if all(space[i] == "." for space in galaxy):
        verticals += [i]
for j, line in enumerate(galaxy):
    if all(space == "." for space in line):
        horizontals += [j]
    else:
        stars += [[star.start(), j] for star in re.finditer("#", galaxy[j])]

total = 0
for a, b in itertools.combinations(stars, 2):
    x = sorted([a[0], b[0]])
    y = sorted([a[1], b[1]])
    total += (x[1] - x[0]) + (y[1] - y[0])
    for ver in verticals:
        if ver in range(x[0], x[1]):
            total += 999999
    for hor in horizontals:
        if hor in range(y[0], y[1]):
            total += 999999
print(total)