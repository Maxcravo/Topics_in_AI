import cartesianPlane
import pygame
import random

# fazer um plano cartesiano com váriios pontos, onde vamos traçar uam reta, que vai dividir o plano e classificar os pontos caso estejam acima
# da reta devem ser um objeto caso estjam abaixo, devem ser outro.
# O programa deve calcular. A inclinação da reta, que vai a partir dessa equação saber se o valro de x está acima ou abaixo da reta.

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Set up the window

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Plano Cartesiano")

plane = cartesianPlane.CartesianPlane(screen)

circle = cartesianPlane.Circle(plane, RED,(0,0),0.5) 
line = cartesianPlane.Line(plane, BLUE, [0,0], [4500,4500]) # usa o padrão [x,y]
# path = cartesianPlane.Path(plane, YELLOW, [0, 0], [10, 10], [20, 20])


i=0
while i < 10:
  i=i+1
  random_cordenateX = random.randrange(0,100)
  random_cordenateY = random.randrange(0,100)
  cartesianPlane.Circle(plane, RED, (random_cordenateX,random_cordenateY), 1)
  

w=0
while w < 10:
  w = w+1
  random_cordenateX = random.randrange(0,100)
  random_cordenateY = random.randrange(0,100)
  cartesianPlane.Circle(plane, YELLOW,(random_cordenateX,random_cordenateY), 1)


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      pygame.quit()
      quit()
    plane.event_handling(event)

  # Update the plane
  plane.update()

  pygame.display.update()