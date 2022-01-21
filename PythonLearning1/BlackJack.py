#	Carleton-Code-Gym
#   Ahmads BlackJack game
#	A game of blackjack
#	Created by:  Ahmad Osman (Co-Founder CCG)
#	Date: March 29 2016

#-------------------------------------------------------------------------------------------------
"""
Want to determine if you will win the next black jack game. Well, the program below attached with
the best BlackJack verifier will tell you the output of such.
"""
#-------------------------------------------------------------------------------------------------

player1 = int(input("enter a value for player 1: "))
player2 = int(input("enter a value for player 2: "))

if player1 > player2 and player1 < 21 or player2 > 21:              #Set's a must do if statement. Sets an and statement that leads to two different options that follow the first statement rule, the output will appear if one of those rules has been followed.
    print("player one wins")