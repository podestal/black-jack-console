# Console Black Jack game built in python

import random

print('Welcome to Jack Black')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealerCardOne = cards[random.randint(0, len(cards) - 1)]
dealerCardTwo = cards[random.randint(0, len(cards) - 1)]

playerCardOne = cards[random.randint(0, len(cards) - 1)]
playerCardTwo = cards[random.randint(0, len(cards) - 1)]

dealer = [dealerCardOne, dealerCardTwo]
player = [playerCardOne, playerCardTwo]

dealerSum = 0
playerSum = 0

for card in player:
    playerSum += card

print(dealer[0], 'x')
print('These are your cards', playerSum)
print(player)

def isHit(playerSum):
    newCard = cards[random.randint(0, len(cards) - 1)]
    player.append(newCard)
    playerSum += newCard
    return playerSum

playerSum = isHit(playerSum)
print('These are your cards', playerSum)
print(player)
