import pygame, sys
import deck
#import drawCard
from pygame.locals import QUIT

#create starting objects
cardDeck = deck.initializedeck()
player1 = {"hand" : deck.createhand(cardDeck), "balance" : 1000}
cardDeck = [e for e in cardDeck if e not in player1["hand"]]
player2 = {"hand" : deck.createhand(cardDeck), "balance" : 1000}
cardDeck = [e for e in cardDeck if e not in player2["hand"]]
pot = 0
tableCards = deck.dealTablecards(cardDeck)

#start pygame vars
pygame.init()
window = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 10)

#create card rects
p1card1 = {"shape": pygame.Rect(200-38,300-70,36,58), "color": (255,0,0), "value": player1["hand"][0]}
p1card2= {"shape": pygame.Rect(200+2, 300-70, 36,58),"value":player1["hand"][1], "color":(255,0,0)}
p2card1={"shape":pygame.Rect(200-38,22,36,58),"color":(255,0,0),"value": player2["hand"][0]}
p2card2={"shape":pygame.Rect(200+2,22,36,58),"color":(255,0,0),"value": player2["hand"][1]}

#while True:
window.fill((255,255,255))
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
pygame.draw.rect(window, p1card1["color"], p1card1["shape"])
pygame.draw.rect(window, p1card1["color"], p1card1["shape"])
#drawCard.drawCardFace(window, p1card1["shape"],p1card1['value'], font)
#drawCard.drawCardFace(window, p1card2["shape"],p1card2['value'], font)
#drawCard.drawCardBack(window,p2card1["shape"])
#drawCard.drawCardBack(window,p2card2["shape"])
pygame.display.update()