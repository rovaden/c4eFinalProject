
def buyin(players):
  player1= players[0]
  player2 = players[1]
  pot = 0
  print("How much would you like the buyin to be?")
  #the players can decide how much the buyin should be but it has to be an integer, more than 0 and less than balance or either player
  gotvalidvalue = False
  while not gotvalidvalue:
    buyin = input()
    if buyin.isnumeric() == True:
      buyin = int(buyin)
      if (buyin >= player1["balance"] or buyin >= player2["balance"]):
        print("please enter an integer buyin that's less than your balance")
      else:
        print("thanks")
        gotvalidvalue=True
        break
    else:
      print("please enter a numeric value")
  #asks player one eiof they want to pay the buyin
  print("It is player1's turn.")
  print("Would you like to buyin? YES or NO")
  #mkaes it so the only potions ofe the player are a variation of "yes" or "no"
  player1response =  str(input()).upper()
  while player1response != "YES" and player1response != "NO":
    print("please say yes or no")
    player1response = str(input()).upper()
  if player1response == "YES":  
    player1["balance"] = player1["balance"] - buyin
    pot += buyin
  else:
    print("player one does not want to pay this buyin")
    return("player1's balance is", player1["balance"], "player2's balance is",player2["balance"])
  #same process for player2 because hardcoding it seems easier
  print("It is player2's turn.")
  print("Would you like to buyin? Yes or NO")
  player2response =  str(input()).upper()
  while player2response != "YES" and player2response != "NO":
    player2response = str(input("please say yes or no")).upper()
  if player2response == "YES": 
    player2["balance"] = player2["balance"] - buyin
    pot += buyin
  else:
    print("player 2 does not want to pay this buyin")
    return("player1's balance is",player1["balance"],"player2's balance is",player2["balance"])
  #buyin is complete so the round went upo by onme so it shouldn't happen agin but the round variuab;le has to be outside the function so when betting is called again it doens't repeat the buyin
  return("buyin is",buyin,"player1's balance is",player1["balance"],"player2's balance is",player2["balance"])
