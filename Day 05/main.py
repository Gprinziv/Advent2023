import re
#First thought is to pass each seed in. For each step:
#Find the nearest map point that doesn't go over the origin number (Index 0), find the difference, and add that to the to the Destination number (Index 1) 
def main():
    with open("test") as f:
        seeds, *maps = f.read().split("\n\n")
    seeds = [int(seed) for seed in seeds.split()[1:]]

    #This nightmare code block pre-sorts the instructions for each map by origin number to cheese the logic later.
    for i, mp in enumerate(maps):
        coords = [m.split() for m in mp.split("\n")[1:]]
        newCoords = []
        for coord in coords:
            newCoords.append([int(coord[1]), int(coord[0]), int(coord[2])])
        maps[i] = [x for coord in sorted(newCoords) for x in coord]
        
    #Do each seed completely one step at a time.
    for mp in maps:
        print(f"Our Origin Points are {mp[::3]}")
        newSeeds = []
        
        for seed in seeds:
            print(f"Our seed is {seed}")
            
            #If the "seed" is before any of the modified origin points, it remains unmodified. 
            if seed < mp[0]:
                print(f"Seed {seed} is less than min {mp[0]}")
                newSeeds.append(seed)
            #If it's beyond the end of the modification table, it's also unmodified.
            elif seed >= mp[-3]:
                if mp[-3] + mp[-1] > seed:
                    print(f"Seed {seed} is in range of {mp[-3]} (Range: {mp[-1]})")
                    print(f"New seed value is: {mp[-2] - mp[-3] + seed}")
                    newSeeds.append(mp[-2] - mp[-3] + seed)
                else:
                    print(f"Seed {seed} greater than max {mp[-3]} (Range: {mp[-1]})")
                    newSeeds.append(seed)
            else:
                for i in range(3, len(mp), 3):
                    if mp[i] > seed:
                        print(f"Seed {seed} is between {mp[i-3]} and {mp[i]}")
                        #then we need to look at i-3 and see if it's in range
                        if mp[i-3] + mp[i-1] > seed:
                            print(f"Seed in range of {mp[i-3]} (Range:{mp[i-1]})")
                            print(f"New seed value is: {mp[i-2] - mp[i-3] + seed}")
                            newSeeds.append(mp[i-2] - mp[i-3] + seed)
                        else:
                            print(f"Seed out of range of {mp[i-3]} (Range:{mp[i-1]})")
                            newSeeds.append(seed)
                        break
        print(newSeeds)
        print()
        seeds = newSeeds
main()