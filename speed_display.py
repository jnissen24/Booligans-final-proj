import pygame

# Margins
margin_left = 250
margin_top = 150

# window size
width = 1000
height = 700

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

back_of_card = pygame.image.load('./Playing Cards/PNG-cards-1.3/gray_back.png')
# scale image
back_of_card = pygame.transform.scale(back_of_card, (100, 150))

pygame.display.flip()
running = True

# Right now what this does is put the image "back_of_card" along the bottom left side of the screens
while running:
    for i in range(0, 5):
        screen.blit(back_of_card, (100 * i, 550))
        pygame.display.update()
    # Not sure exactly what this does right now, but it is needed to avoid an infinite loop and for stuff to appear
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
