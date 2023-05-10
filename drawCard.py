import pygame
pygame.init()
place = {"A":[[0,0]],"2":[[0, 10],[0,-10]],"3":[[0,10],[0,0],[0,-10]],"4":[[-5,-10],[-5,10],[5,-10],[5,10]],"5":[[0,0],[-5,10], [-5, -10], [5, 10], [5, -10]],"6":[[-5,-10],[-5,0],[-5,10], [5, 10], [5, 0], [5, -10]],"7":[[0,5],[-5,10], [-5, 0], [-5, -10], [5, 10], [5, 0], [5, -10]],"8":[[0,5],[0,-5],[-5, 10],[-5,0],[-5,-10],[5,-10],[5,0],[5,10]],"9":[[0,0],[-5,15],[-5,7],[-5,-7],[-5,-15],[5,7],[5,15],[5,-7],[5,-15]],"10":[[0,10],[0,-10],[-5,15],[-5,7],[-5,-7],[-5,-15],[5,7],[5,15],[5,-7],[5,-15]]}


def drawCardFace(window, rect, value, font):
  color = (255, 0, 0) if value[1] == "d" or value[1] == "h" else (0,0,0)
  cx, cy = rect.centerx, rect.centery
  front= pygame.image.load("assets/front.png")
  front = pygame.transform.scale(front, rect.size)
  window.blit(front, rect)
  tx,ty = cx - 12, cy - 23
  bx,by = cx + 9, cy+20
  text = font.render(value[0], True, color)
  window.blit(text, (bx, by))
  window.blit(text, (tx,ty))
  suit = pygame.image.load("assets/" + value[1] + ".png")
  suit = pygame.transform.scale(suit, (rect.width/5, rect.height/9))
  cw, ch = suit.get_rect().width/2, suit.get_rect().height/2
  
  if value[0] != "k" and value[0] != "q" and value[0] != "j": 
    i = 0
    while i < len(place[value[0]]):
      #print(place[value[0]][i][0])
      window.blit(suit,(cx+place[value[0]][i][0]-cw, cy+place[value[0]][i][1]-ch)) 
      i += 1

def drawCardBack(window, rect):
  back=pygame.image.load("assets/back.png")
  back=pygame.transform.scale(back, rect.size)
  window.blit(back, rect)