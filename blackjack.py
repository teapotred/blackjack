# simple blackjack beginner style blackjack program in python. 

import random
import os
import sys

house_cards = []
player_cards = []

#deal house cards
while len(house_cards) != 2:
    house_cards.append(random.randint(1,11))
    if len(house_cards) == 2:
        print("house has: [x] & ",house_cards[1])
#deal players cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("You have: ",player_cards)

#checking if one or the other has a blackjack
if sum(house_cards) == 21:
    print("The house has a blackjack and has won!")
    sys.exit()
elif sum(house_cards) > 21:
    print("The deal BUST!")
    sys.exit()

if sum(player_cards) == 21:
    print("The player has a blacjack and has won")
elif sum(player_cards) >21:
    print("The player BUST!")


#game loop, checking for play again and if hit is true, checking if it doesn't go over 21, if not than hit again or stand until failure or stand
#if house has better cards, house wins, else, you win
i=0
while i == 0:
    if sum(player_cards) == 21:
        print("The player has a blacjack and has won")
        i += 1
    elif sum(player_cards) >21:
        print("The player BUST!")
        i += 1
    if sum(player_cards) <21:
        again = input("Would you like to [H]it or [S]Stand?").lower()
        if again == 'h':
            player_cards.append((random.randint(1,11)))
            print(player_cards)
            if sum(player_cards)>21:
                print("You went over 21 you BUST!")
                i+=1
                sys.exit()
        elif again == 's':
            print("Your card are", player_cards, "The house cards are", house_cards)
            i+=1

#last iteration of checking if player has better cards than the house
if sum(player_cards)<sum(house_cards):
    print("the house wins! BOZO")
elif sum(player_cards)>sum(house_cards):
    print("you win!")




