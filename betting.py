def betting(players, pot):
  allin = False
  player1 = players[0]
  player2 = players[1]
  highbet = None
  playernumber = 2
  turncounter = 0
  player1bet = 0
  player2bet = 0
  #NOTE: don't mod playernumber by 1; it will always be zero. Change it.
  

#end conditions for betting: player1bet and player2 but must be equal to each other and highbet
  while player1bet != highbet or player2bet != highbet:

    if playernumber % 2 == 0:
      print("It is player 1's turn.")

    else:
      print("It is player 2's turn.")
      
    #outer if statement check: if first turn, only actions are bet and fold; otherwise, call, raise, and fold are availible as actions.
    
    if turncounter == 0:
      actions = ("bet", "fold")
      action = input("Would you like to bet or fold?")
      #function that checks for invalid responses placeholder


      #fold mechanics on the first turn
      if action in actions and action == "fold":
        players[playernumber % 2]["hand"] = []
        players[(playernumber + 1) % 2]["balance"] += pot
        pot = 0
        return(player1["balance"], player2["balance"])



      #betting on the first turn 
      elif action in actions and action == "bet":
        bet = input("How much would you like to bet?")
        while bet.isnumeric() == False:
          bet = input("please bet an integer amount")
        #check if bet is a valid input using a function
        
        
        if playernumber % 2 == 0:
          player1bet = int(bet)
          if player1bet >= player1["balance"]:
            allin = True
            player1bet = player1["balance"]
            highbet = player1bet                           
            pot += player1bet
            turncounter += 1
            playernumber += 1
            players[0]["balance"] -= player1bet
          else:
            players[0]["balance"] -= player1bet
            highbet = player1bet
            pot += player1bet
            turncounter += 1
            playernumber += 1
          
        else:
          player2bet = int(bet)
          if player2bet >= player2["balance"]:
            allin = True
            player2bet = player2["balance"]
            player2["balance"] -= player2bet
            pot += player2bet
            turncounter += 1
            playernumber += 1
          else:
            players[1]["balance"] -= player2bet
            highbet = player2bet
            pot += player2bet
            turncounter += 1
            playernumber += 1

      else: #since I added a loop to make it an int I don't think this is needed anymore
          print("Invalid Input. Please try again.")


    #if it isn't the first turn, call, raise, and fold are avalible as actions (see outer loop check)
    else:
      actions = ("call", "raise", "fold") 
      action = input("Would you like to call, raise, or fold?")



      #fold
      if action in actions and action == "fold":
        players[playernumber % 2]["hand"] = []
        players[(playernumber + 1) % 2]["balance"] += pot
        pot = 0
        return(player1["balance"], player2["balance"])


      
      #raise
      elif action in actions and action == "raise":
        bet = input("How much would you like to raise?")
        while bet.isnumeric() == False:
          bet = input("please raise an integer amount")
        #check if bet is a number, not a letter, and is greater than 0 (Placeholder) #should be fixed by the while loop
        if playernumber % 2 == 0:
          if bet >= players[0]["balance"]:
            allin = True
            bet = players[0]["balance"]
            players[0]["balance"] -= bet
            player1bet += bet
            highbet += bet
            playernumber += 1
            turncounter += 1
          
          else:
            players[0]["balance"] -= bet
            pot += bet
            player1bet += bet
            highbet += bet
            playernumber += 1
            turncounter += 1

        else:
          if bet >= players[1]["balance"]:
            allin = True
            bet = player1["balance"]
            pot+= bet
            highbet += bet
            playernumber += 1
            turncounter += 1
            player2bet += bet
            
          else:
            players[1]["balance"] -= bet
            pot += bet
            player2bet += bet
            highbet += bet
            playernumber += 1
            turncounter += 1

      #call
      elif action in actions and action == "call": 
        
        if playernumber % 2 == 0 and player1bet < highbet:
          callamount = highbet - player1bet
          player1bet += callamount
          players[0]["balance"] -= callamount
          pot += callamount

        elif playernumber % 2 != 0 and player2bet < highbet:
          callamount = highbet - player2bet
          player2bet += callamount
          players[1]["balance"] -= callamount
          pot += callamount
        


  return(players[0]["balance"], players[1]["balance"])

#NOTE: initial version will not have check as an action. 
#I will make a function to check if keyboard inputs are numbers or letters so that no invalid inputs result in errors.
