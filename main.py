import pygame, sys
import deck
import drawCard
from pygame.locals import QUIT
import buyin
import betting
#import showdown

#create starting objects
cardDeck = deck.initializedeck()
print(cardDeck)
player1 = {"hand": deck.createhand(cardDeck), "balance": 1000}
cardDeck = [e for e in cardDeck if e not in player1["hand"]]
player2 = {"hand": deck.createhand(cardDeck), "balance": 1000}
cardDeck = [e for e in cardDeck if e not in player2["hand"]]
pot = 0
tableCards = deck.dealTablecards(cardDeck)
round = 0

#start pygame vars
pygame.init()
window = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 10)

#create card rects
p1card1 = {
    "shape": pygame.Rect(200 - 38, 300 - 70, 36, 58),
    "color": (255, 0, 0),
    "value": player1["hand"][0]
}
p1card2 = {
    "shape": pygame.Rect(200 + 2, 300 - 70, 36, 58),
    "value": player1["hand"][1],
    "color": (255, 0, 0)
}
p2card1 = {
    "shape": pygame.Rect(200 - 38, 22, 36, 58),
    "color": (255, 0, 0),
    "value": player2["hand"][0]
}
p2card2 = {
    "shape": pygame.Rect(200 + 2, 22, 36, 58),
    "color": (255, 0, 0),
    "value": player2["hand"][1]
}
tableCardRects = {
    0: pygame.Rect(200 - 80 - 18, 150 - 29, 36, 58),
    1: pygame.Rect(200 - 18 - 40, 150 - 29, 36, 58),
    2: pygame.Rect(200 - 18, 150 - 29, 36, 58),
    3: pygame.Rect(200 + 22, 150 - 29, 36, 58),
    4: pygame.Rect(200 + 22 + 36 + 4, 150 - 29, 36, 58)
}

#money money money
moneyRects = {
    "p1Bal": pygame.Rect(75, 230, 50, 20),
    "p2Bal": pygame.Rect(75, 70, 50, 20),
    "pot": pygame.Rect(325, 150, 50, 20)
}

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    drawCard.drawGame(round, window, moneyRects, [player1["balance"],player2["balance"],pot], tableCardRects, tableCards, [p1card1,p1card2,p2card1,p2card2], font)
    pygame.display.update()
    if round == 0:
      buyin.buyin([player1, player2])
      round += 1
    elif round ==3:
      #showdown.showdown()
      print("over")
    else:
      betting.betting([player1,player2], pot)
      round += 1