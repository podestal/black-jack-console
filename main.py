# Console Black Jack game built in python

import random

def evaluate(playerSum, dealer):
    if playerSum == 21:
        print('You win')
    elif playerSum > 21: 
        print('You lost')
    else:
        playerHit = input('Hit? y/n')
        if playerHit == 'y':
            return playerHit
        else:
            print('Dealer cards: ', dealer[0], dealer[1])
            if playerSum > dealerSum:
                print('You win')
            elif playerSum == dealerSum:
                print('even')
            else:
                print('You lost')
            return playerHit
    
def game(dealer, playerSum, player):
    print(dealer[0], 'x')
    print('These are your cards', playerSum)
    print(player)

def isHit(playerSum, player, cards):
    newCard = cards[random.randint(0, len(cards) - 1)]
    player.append(newCard)
    playerSum += newCard
    return playerSum

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

for card in dealer:
    dealerSum += card


game(dealer, playerSum, player)

playerHit = evaluate(playerSum, dealer)

while playerHit == 'y':
    playerSum = isHit(playerSum, player, cards)
    game(dealer, playerSum, player)
    playerHit = evaluate(playerSum, dealer)

print(playerSum)
    