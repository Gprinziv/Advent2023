def main():
    with open("test") as f:
        seeds, *maps = f.read().split("\n\n")
    seeds = [int(seed) for seed in seeds.split()[1:]]

    for i, mp in enumerate(maps):
        coords = [m.split() for m in mp.split("\n")[1:]]
        newCoords = []
        for coord in coords:
            newCoords.append([int(coord[1]), int(coord[0]), int(coord[2])])
        maps[i] = [x for coord in sorted(newCoords) for x in coord]
        
    for mp in maps:
        newSeeds = []
        
        for seed in seeds:
            if seed < mp[0]:
                newSeeds.append(seed)
            elif seed >= mp[-3]:
                if mp[-3] + mp[-1] > seed:
                    newSeeds.append(mp[-2] - mp[-3] + seed)
                else:
                    newSeeds.append(seed)
            else:
                for i in range(3, len(mp), 3):
                    if mp[i] > seed:
                        if mp[i-3] + mp[i-1] > seed:
                            newSeeds.append(mp[i-2] - mp[i-3] + seed)
                        else:
                            newSeeds.append(seed)
                        break
        print(newSeeds)
        print()
        seeds = newSeeds

#Take your range, find its origin point and see if it crosses into or out of ranges. 
def part2():
    #Generates a list of seed ranges with values inclusive
    #[[Start, End], ...]
    with open("input") as f:
        seeds, *maps = f.read().split("\n\n")
    seed = seeds.split()[1:]
    seeds = [[int(seed[i]), int(seed[i+1]) + int(seed[i]) - 1] for i in range(0, len(seed), 2)]
    
    #Generates each conversion table where values in that range are modified by the third value.
    #Appends a minimum range (zero to the first number) in order to make later functions work.
    #[[startRange, endRange, offset], ...]
    conMap = []
    for i, mp in enumerate(maps):
        coords = [m.split() for m in mp.split("\n")[1:]]
        newCoords = []
        for coord in coords:
            newCoords.append([int(coord[1]), int(coord[1]) + int(coord[2]) - 1, int(coord[0]) - int(coord[1])])
        newCoords.sort()
        zero = [] if newCoords[0][0] == 0 else [[0, newCoords[0][0] - 1, 0]]
        conMap.append(zero + newCoords)
    
    #Run the seed ranges through each conversion table. If it splits, then two seed ranges will form.
    #I could merge ranges that are contiguous if necessary to save space, but I think that's more trouble than it's worth.
    for mp in conMap:
        newSeeds = []
        for seed in seeds:
            for m in mp:
                if seed[0] in range(m[0], m[1]):
                    #If the seed is completely in a range, then stop here.
                    if seed[1] <= m[1]:
                        newSeed = [seed[0] + m[2], seed[1] + m[2]]
                    #Otherwise, modify all valid values and check the remaining against the next rule.
                    else:
                        newSeed = [seed[0] + m[2], m[1] + m[2]]
                        seed[0] = m[1] + 1
                    newSeeds.append(newSeed)
            #Then, if the seed exceeds the final rule, simply append it as-is.
            if seed[0] > mp[-1][-2]:
                newSeeds.append(seed)   
        seeds = newSeeds
    print(f"lowest value: {sorted(seeds)[0][0]}")

part2() 