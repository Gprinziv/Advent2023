import re, math

def p1():
  with open("input") as f:
    moves, *paths = f.read().splitlines()
  paths = [re.findall("[A-Z]+", p) for p in paths]
  nodes = {}
  for path in paths[1:]:
    nodes[path[0]] = path[1:]
  location = "AAA"
  steps = 0
  while location != "ZZZ":
    for move in moves:
      if move == "R":
        location = nodes[location][1]
      else:
        location = nodes[location][0]
      steps += 1
      if location == "ZZZ": break
  print(steps)



def p2():
  with open("input") as f:
    moves, *paths = f.read().splitlines()
  paths = [re.findall("[A-Z0-9]+", p) for p in paths]
  locations, nodes = [], {}

  for path in paths[1:]:
    nodes[path[0]] = path[1:]
    if path[0][-1] == "A":
      locations.append(path[0])

  #For each starting location, find the Z frequency, then calc LCM.
  #it's possible z loops to a different than A, so this could be a royal cock up.
  locSteps = []
  for l in locations:
    thisLoc = l
    steps = 0
    while thisLoc[2] != "Z":
      for move in moves:
        if move == "R":
          thisLoc = nodes[thisLoc][1]
        else:
          thisLoc = nodes[thisLoc][1]
        steps += 1
    locSteps.append(steps)

  while len(locSteps) > 1:
    a = locSteps.pop()
    b = locSteps.pop()
    lcm = (a * b) // math.gcd(a, b)
    locSteps.append(lcm)
  print(locSteps.pop())

#p1()
p2()