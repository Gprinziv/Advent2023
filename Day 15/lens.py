def computeHash(string):
  total = 0
  for char in string:
      total = (total + ord(char)) * 17 % 256
  return total

def p1():
  bigtotal = 0
  for string in instructions:
    bigtotal += computeHash(string)
  return bigtotal

with open("input") as f:
  instructions = f.read().split(",")

hshmap = [[] for _ in range(256)]

for inst in instructions:
  if inst[-1] == "-":
    addr = computeHash(inst[:-1])
    try:
      lens = [x[0] for x in hshmap[addr]].index(inst[:-1])
      hshmap[addr].pop(lens)
    except ValueError:
      #print(f"Remove {inst} failed!")
      pass
  else:
    addr = computeHash(inst[:-2])
    try: 
      lens = [x[0] for x in hshmap[addr]].index(inst[:-2])
      hshmap[addr][lens][1] = inst[-1]
    except ValueError:
      hshmap[addr].append([inst[:-2], inst[-1]])


focus = 0
for j, addr in enumerate(hshmap):
  for i, val in enumerate(addr):
    #print(val)
    focus += (j+1) * (i+1) * int(val[1])
print(focus)