def buyin(users):
  while round == 0:#establishes this is the start and the only time the buyin is established
      print("How much wouldd you like the buyin to be?")
      buyin = input()
      #the players can decide how much the buyin should be but it has to be an integer, more than 0 and less than balance or either player
      while isint(buyin) == False or buyin < 0 or buyin > player1["balance"] or buyin > player2["balance"]:
        buyin = input()
  
    #asks player one eiof they want to pay the buyin
    print("It is player1's turn.")
    print("Would you like to buyin?")
    #loop so it only happens durting the buyin
    while round == 0:
      #mkaes it so the only potions ofe the player are a variation of "yes" or "no"
      player1response =  str(input()).upper()
      while player1response != ("YES" or "NO"):
        player1response = str(input()).upper()
      player1["balance"] = player1["balance"] - buyin
      #same process for player2 because hardcoding it seems easier
      print("It is player2's turn.")
      print("Would you like to buyin?")
      player2response =  str(input()).upper()
      while player2response != ("YES" or "NO"):
        player2response = str(input()).upper()
      player2["balance"] = player2["balance"] - buyin
      round += 1
    #buyin is complete so the round went upo by onme so it shouldn't happen agin but the round variuab;le has to be outside the function so when betting is called again it doens't repeat the buyin
  return(buyin)

players = [player1, player2]

player1 = {
    "hand" : [],
    "balance" : 1000
}

player2 = {
    "hand" : [],
    "balance" : 1000
}
round = 0