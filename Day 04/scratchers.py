import re

def p1():
    #Use 6 for the test case and 11 for the main case.
    ENTRIES = 11

    with open("input") as f:
        cards = f.read().splitlines()

    total = 0
    for card in cards:
        raw = re.findall("[0-9]+", card)
        nums, win = raw[1:ENTRIES], raw[ENTRIES:]
        total += int(2 ** (sum(i in win for i in nums) - 1))
    print(total)
    

def p2():
    #Use 6 for the test case and 11 for the main case.
    ENTRIES = 11

    with open("input") as f:
        cards = f.read().splitlines()

    instances = [0] * len(cards)

    for i in range(len(cards)):
        instances[i] += 1

        raw = re.findall("[0-9]+", cards[i])
        nums, win = raw[1:ENTRIES], raw[ENTRIES:]
        wins = sum(i in win for i in nums)
        for j in range(1, wins+1):
            if i+j < len(instances):
                instances[i+j] += instances[i]
    print(sum(instances))

p1()
p2()