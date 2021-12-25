import pygame
pygame.init()
a=int(input())
b=int(input())
win=pygame.display.set_mode((a,a))
color=(255,255,255)
win.fill(color)
pygame.display.update()

for j in range(3):
  for i in range(3):
    pygame.draw.rect(win,(0,0,0),(i*100+50,j*100+50,50,50))
    pygame.draw.rect(win,(0,0,0),(i*100,j*100,50,50))
pygame.display.update()




while True:
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
       exit()