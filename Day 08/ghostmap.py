import re

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

  #When you reach a Z, you can calculate the frequency it will appear.
  #Once you have all 6 frequencies, you can find the least common multiple
  steps = 0
  while True:
    for move in moves:
      if move == "R":
        for i, l in enumerate(locations):
          locations[i] = nodes[l][1]
      else:
        for i, l in enumerate(locations):
          locations[i] = nodes[l][0]
      steps += 1
      input(f"Step {steps}: {locations}")
      if all(l[2] == "Z" for l in locations): 
        print(steps)
        return


#p1()
p2()