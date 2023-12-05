import re
#First thought is to pass each seed in. For each step:
#Find the nearest map point that doesn't go over the origin number (Index 1), find the difference, and add that to the to the Destination number (Index 0) 
def main():
    with open("test") as f:
        seeds, *maps = f.read().split("\n\n")
    maps = [re.findall("[0-9]+", map) for map in maps]
    
    #Do each seed completely one step at a time.
    for map in maps:
        print(map[1::3])
        #Once the seeds are tep-converted, save them and start the next step
        #newSeeds = []
        for seed in seeds:
            pass
            #Find the Origin closest to but not over ours. If we fail to find, it meanns the conversion has no change.
            #map[1::3] is the slice we want?
            #calculate the difference between the original and "seed", if it's greated than the Range, ignore.
        #seeds = newSeeds

    print(seeds)
    print(maps)
    
main()