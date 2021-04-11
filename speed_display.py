import pygame

# Margins
margin_left = 250
margin_top = 150

# window size
width = 800
height = 600

# colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (110, 110, 110)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(gray)
pygame.display.set_caption("Speed!")

#back_of_card = pygame.image.load('gray_back.png')
# scale image
#back_of_card = pygame.transform.scale(back_of_card, (100, 150))

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False