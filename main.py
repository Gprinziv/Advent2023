def findNext(cur, x, y):
    if cur == "7":
        return [[x-1, y], [x, y+1]]
    elif cur == "J":
        return [[x-1, y], [x, y-1]]
    elif cur == "F":
        return [[x+1, y], [x, y+1]]
    elif cur == "L":
        return [[x+1, y], [x, y-1]]
    elif cur == "-":
        return [[x-1, y], [x+1, y]]
    elif cur == "|":
        return [[x, y+1],[x, y-1]]

with open("test4") as f:
    pipes = f.read().splitlines()

for i in range(len(pipes)):
    if "S" in pipes[i]:
        start = [pipes[i].index('S'), i]

print(start)
stepmap = [['.'] * len(pipe) for pipe in pipes]
stepmap[start[1]][start[0]] = 0
steps, curQueue, nextQueue = 1, [], []

#Need to do some work to figure out what nextQueue is for start
if pipes[start[1]][start[0] - 1] in ["F", "L", "-"]:
    curQueue.append((start[0]-1, start[1]))
if pipes[start[1]][start[0] + 1] in ["J", "7", "-"]:
    curQueue.append((start[0]+1, start[1]))
if pipes[start[1] - 1][start[0]] in ["F", "7", "|"]:
    curQueue.append((start[0], start[1]-1))
if pipes[start[1]+1][start[0]] in ["J", "L", "|"]:
    curQueue.append((start[0], start[1]+1))

while curQueue:
    x, y = curQueue.pop()
    stepmap[y][x] = pipes[y][x]
    nextSteps = findNext(pipes[y][x], x, y)
    for step in nextSteps:
        if stepmap[step[1]][step[0]] == ".":
            nextQueue.append(step)

    if not curQueue:
        curQueue = nextQueue
        nextQueue = []
        steps += 1

#This version doesn't take care of "junk pipe bits"
curQueue = [[0,0]]
while curQueue:
    x, y = curQueue.pop()
    stepmap[y][x] = "O"
    try:
        if stepmap[y][x-1] == ".":
            curQueue.append([x-1, y])
    except: pass
    try:
        if stepmap[y][x+1] == ".":
            curQueue.append([x+1, y])
    except:pass
    try:
        if stepmap[y+1][x] == ".":
            curQueue.append([x, y+1])
    except:pass
    try:
        if stepmap[y-1][x] == ".":
            curQueue.append([x, y-1])
    except:pass

for line in stepmap:
    print(" ".join([str(x) for x in line]))
print(steps-1)
print(sum(line.count(".") for line in stepmap))