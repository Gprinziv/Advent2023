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
    cards = set(hand)

    if len(cards) == 5: high.append(hand)
    elif len(cards) == 4: one.append(hand)
    elif len(cards) == 3:
      if any(hand.count(card) == 3 for card in cards): three.append(hand)
      else: two.append(hand)
    elif len(cards) == 2:
      if any(hand.count(card) == 1 for card in cards): four.append(hand)
      else: full.append(hand)
    else: five.append(hand)

  ranks = sorted(high) + sorted(one) + sorted(two) + sorted(three)\
      + sorted(full) + sorted(four) + sorted(five)

  total = sum((i+1) * bids[hand] for i, hand in enumerate(ranks))
  print(total)

def p2():
  #Performing some simple replacement operations to make the sorting process painless.
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
    jokers = hand.count("0")
    cards.discard("0")

    #Jokers have been discarded, so this is high card.
    if len(cards) == 5: high.append(hand)  
    #Regardless of the 5th card, only one pair is possible (ABCDx)  
    elif len(cards) == 4: one.append(hand)
    #If the jokers plus any card reach 3, it's a three of a kind, otherwise pair.
    elif len(cards) == 3:
      if any([hand.count(card) + jokers == 3 for card in cards]): three.append(hand)
      else: two.append(hand)
    #With two unique cards, the options are a full house (AABBx) or four of a kind
    elif len(cards) == 2:
      if any([hand.count(card) == 1 for card in cards]): four.append(hand)
      else: full.append(hand)
    #If only one card appears, it must be 5 of a kind!
    else: five.append(hand)

  ranks = sorted(high) + sorted(one) + sorted(two) + sorted(three)\
      + sorted(full) + sorted(four) + sorted(five)

  total = sum((i+1) * bids[hand] for i, hand in enumerate(ranks))
  print(total)

p1()
p2()