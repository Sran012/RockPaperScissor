from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (R, P or S)")
print()

player1_score = 0
player2_score = 0

while True :
  player1move = input("Player 1 > ")
  player2move = input("Player 2 > ")


  if player1move == "R":
    if player2move == "R":
      print("You both have picked Rock, DRAW !")
    elif player2move == "S":
      print("Player1 smashed player2's Scissor into dust with their Rock")
      player1_score += 1
    elif player2move == "P":
      print("Player1's Rock is smothered by Player2's Paper!")
      player2_score += 1
    else:
      print("invalid move player2 !")

  
  
  elif player1move == "P":
    if player2move == "P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
    elif player2move == "R":
      print("Player2's Rock is smothered by Player1's Paper!")
      player1_score += 1
    elif player2move == "S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2_score += 1
    else:
      print("Invalid Move Player 2!")


  
  
  elif player1move == "S":
    if player2move == "S":
      print("Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif player2move == "R":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2_score += 1
    elif player2move == "P":
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1_score += 1
    else:
      print("Invalid Move Player 2!")

  print("player 1 has", player1_score, "wins")
  print("player 2 has", player2_score, "wins")

  if player1_score == 3 or player2_score == 3 :
    print("tanks for playing !")
    exit()
  
  else:
    continue 