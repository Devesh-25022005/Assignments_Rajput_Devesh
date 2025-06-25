import random
p1_score = 0
p2_score = 0
print("Welcome to Rock, Paper, Scissor Game")
choices = ["Rock", "Paper", "Scissor"]
while True:
   
    print("Enter 'exit' to quit the game")

    player1 = input("Player 1 - Rock, Paper or Scissor: ")
    player2 = random.choice(choices)  # Randomly select for Player 2
    print(f"Player 2 (Computer) chose: {player2}")

    if player1.lower() == "exit" or player2.lower() == "exit":
        print("Thanks for playing!")
        break

    if (player1 == "Rock" and player2 == "Scissor") or \
       (player1 == "Scissor" and player2 == "Paper") or \
       (player1 == "Paper" and player2 == "Rock"):

        
        p1_score += 1
        print("Player 1 wins this round!")

    elif (player2 == "Rock" and player1 == "Scissor") or \
         (player2 == "Scissor" and player1 == "Paper") or \
         (player2 == "Paper" and player1 == "Rock"):

        print("Player 2 wins this round!")
        p2_score += 1

    elif player1 == player2:
        print("It's a tie!")

    else:
        print("Invalid input! Please enter Rock, Paper or Scissor.")

    print(f" Player 1: {p1_score} | Player 2: {p2_score}\n")


# Final result after exit
if p1_score > p2_score:
    print("Player 1 wins with score =",p1_score)
elif p2_score > p1_score:
    print("Player 2 wins with score =", p2_score)
else:
    print("It's an tie with score =", p1_score)
