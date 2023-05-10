import random

#initialize deck, create deck as a list of cards with format numsuit; shuffle deck
def initializedeck():
  deck = []
  card = ""
  suitdictionary = {1 : "s", 2 : "c", 3 : "d", 4 : "h"}
  royals = {11 : "j", 12 : "q", 13: "k", 14: "a"}
  for suit in range(1, 5):
      for num in range(2, 11):
          card += str(num)
          card += suitdictionary[suit]
          deck.append(card)
          card = ""
      for num in range(11, 15):
          card += royals[num]
          card += suitdictionary[suit]
          deck.append(card)
          card = ""
  
  random.shuffle(deck)
  return(deck)

#assign two cards to each player for the preflop (note: "player" argument takes player1 or player2)
def createhand(deck):
  hand =[]
  for i in range(2):
    card = deck[0]
    deck.pop(0)
    hand.append(card)
  return(hand)

#flop/turn/river function
def dealTablecards(deck):
  middle = []
  for i in range(0, 5):
      card = random.choice(deck)
      middle.append(card)
      
  return middle


#showdown functions (check for each type of hand, all the way down to high card. If high card is the same, check suit of each high card)

