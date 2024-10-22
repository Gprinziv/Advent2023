import math

def main():
    with open ("input") as f:
        times, *distance = f.read().split("\n")
    times = [int(x) for x in times.split()[1:]]
    distance = [int(x) for x in distance[0].split()[1:]]

    totals = []
    for i in range(len(times)):
        beaten = 0
        print(f"Race time: {times[i]}, Record distance: {distance[i]}")
        for x in range(1, times[i]):
            if (x * (times[i] - x)) > distance[i]:
                beaten += 1
        totals.append(beaten)
    print(totals)
    print(math.prod(totals))

#Math! The range of faliv values is symmetrical
#If we take the total number of times (plus 0) and subtract 
#the invalid times (i) twice, we get the remaining valid times.
def part2():
    with open ("input") as f:
        times, *distance = f.read().split("\n")
    time = int("".join([x for x in times.split()[1:]]))
    distance = int("".join([x for x in distance[0].split()[1:]]))

    i = 1
    while (time - i) * i < distance:
        i += 1
    print(time + 1 - 2*i)

part2()