import re

def p1():
  with open("input") as f:
    text = f.read()
    text = re.sub("J", "W", text)
    text = re.sub("Q", "X", text)
    text = re.sub("K", "Y", text)
    text = re.sub("A", "Z", text)
    bids = {}
    hands = []
    for hand in text.splitlines():
      cards, *bid = hand.split()
      hands.append(cards)
      bids[cards] = int(bid[0])

  five, four, full, three, two, one, high = [], [], [], [], [], [], []

  for hand in hands:
    pairFlag = False
    tripFlag = False
    if len(set(hand)) == 5:
      high.append(hand)
    else:
      for card in set(hand):
        if hand.count(card) == 5:
          five.append(hand)
          break
        elif hand.count(card) == 4:
          four.append(hand)
          break
        elif hand.count(card) == 3:
          tripFlag = True
          if pairFlag == True:
            full.append(hand)
            break
        elif hand.count(card) == 2:
          if pairFlag == True:
            pairFlag = False
            two.append(hand)
            break
          else:
            pairFlag = True

            if tripFlag == True:
              full.append(hand)
              break
      if tripFlag == True and pairFlag == False:
        three.append(hand)
      elif pairFlag == True and tripFlag == False:
        one.append(hand)

  ranks = sorted(high) + sorted(one) + sorted(two) + sorted(three)\
      + sorted(full) + sorted(four) + sorted(five)

  print(ranks)

  total = 0
  for i, hand in enumerate(ranks):
    total += (i+1) * bids[hand]
  print(total)

def p2():
  with open("input") as f:
    text = f.read()
    text = re.sub("J", "0", text)
    text = re.sub("Q", "X", text)
    text = re.sub("K", "Y", text)
    text = re.sub("A", "Z", text)
    bids = {}
    hands = []
    for hand in text.splitlines():
      cards, *bid = hand.split()
      hands.append(cards)
      bids[cards] = int(bid[0])

  five, four, full, three, two, one, high = [], [], [], [], [], [], []

  for hand in hands:
    cards = set(hand)
    if len(cards) == 5:
      high.append(hand)
    else:
      cards.discard("0")
      if len(cards) == 1: #Five of a kind!
        five.append(hand)
      elif len(cards) == 4: #We know no jokers, so one pair.
        one.append(hand)
      elif len(cards) == 2: #If the count of one of the cards is one, it's a four of a kind. Otherwise it's Full House
        isFull = True
        for card in cards:
          if hand.count(card) == 1:
            isFull = False
            four.append(hand)
            break
        if isFull:
          full.append(hand)
      else: #Two Pair or Three of a Kind. The only valid two pair has no jokers.
        numOfOnes = sum(hand.count(card) == 1 for card in cards)
        if numOfOnes == 1:
          two.append(hand)
        else:
          three.append(hand)

  ranks = sorted(high) + sorted(one) + sorted(two) + sorted(three)\
      + sorted(full) + sorted(four) + sorted(five)

  print(sorted(five))


  total = 0
  for i, hand in enumerate(ranks):
    total += (i+1) * bids[hand]
    #print(f"hand {i}: {hand}")
  print(total)

#p1()
p2()