deck = ["Ah", "Ad", "Ac", "As",
    "2h", "2d", "2c", "2s",
    "3h", "3d", "3c", "3s",
    "4h", "4d", "4c", "4s",
    "5h", "5d", "5c", "5s",
    "6h", "6d", "6c", "6s",
    "7h", "7d", "7c", "7s",
    "8h", "8d", "8c", "8s",
    "9h", "9d", "9c", "9s",
    "10h", "10d", "10c", "10s",
    "Jh", "Jd", "Jc", "Js",
    "Qh", "Qd", "Qc", "Qs",
    "Kh", "Kd", "Kc", "Ks"]

import random
# # player1_stack = 500
# # player2_stack = 500
# pot_size = 0

# def money_won(): 
#     player1_stack = 500
#     player2_stack = 500
#     won = False
#     player1_hand = 100
#     player2_hand = 50
#     money_won = 0

#     if player1_hand > player2_hand: 
#         won = True
#         money_won = player1_stack + player2_stack
#         return money_won
#     else:
#         print('The pot will be chopped')

# print(money_won())  

def initialize_deck(arr):
    return random.choice(arr)


print(initialize_deck(deck))
    

# print(f'Player 1 stack is {player1_stack}')
# print(f'Player 2 stack is {player2_stack}')

# player1_card1 = []
# player1_card2 = []

# player2_card1 = []
# player2_card2 = []


# flop = []

# #initialize player 1 hand
# player1_card1 = random.choice(deck)
# deck.remove(player1_card1)
# player1_card2 = random.choice(deck)
# deck.remove(player1_card2)
# player1_hand = [player1_card1, player1_card2]
# print('\nPlayer 1 hand is:')
# print(player1_hand)

# #need to find away to remove these deck from array

# #initialize player 2 hand
# player2_card1 = random.choice(deck)
# deck.remove(player2_card1)
# player2_card2 = random.choice(deck)
# deck.remove(player2_card2)
# player2_hand = [player2_card1, player2_card2]
# print('\nPlayer 2 hand is:')
# print(player2_hand)

# # ADD : initialize bet fold options, player 1 starts first.

# #initialize flop
# card_1 = random.choice(deck)
# card_2 = random.choice(deck)
# card_3 = random.choice(deck)
# flop.append(card_1)
# deck.remove(card_1)
# flop.append(card_2)
# deck.remove(card_2)
# flop.append(card_3)
# deck.remove(card_3)
# print('\nFlop is:')
# print(flop)

# #Program prompts player 1 with the following actions: bet, check. If player bets,
# #program will add amount to potsize and remove from stack. If player checks, program 
# #prompts player 2

