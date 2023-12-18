with open("test") as f:
  plan = f.read().splitlines()

print(plan)

#For each row, find the start and end points of each chunk of "#" and for every pair, mark out  a trench
#This is a bad idea that will end poorly on certain edge cases like thickness one walls.
#Figure something better out. 