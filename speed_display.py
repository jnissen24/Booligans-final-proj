import pygame
import random

# creates Card class
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{}{}".format(self.value, self.suit))

# creates Deck class
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.computer_cards = []
        self.player_cards = []
        self.standby1 = []
        self.standby2 = []
        self.wrkcard1 = []
        self.wrkcard2 = []
        self.shuffle()
        self.deal()

    # assigns each card a suit and a value
    # labels for cards now match labels of images
    def build(self):
        for ii in ["S", "C", "D", "H"]:
            for jj in ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(ii, jj))

    # Shuffles the deck by switching the card at index ii with a card at a random index
    def shuffle(self):
        for ii in range(len(self.cards)):
            r = random.randint(0, ii)
            self.cards[ii], self.cards[r] = self.cards[r], self.cards[ii]

    # Display the shuffled deck
    def show(self):
        for c in self.cards:
            c.show()

    # Deals cards to player and computer and also sets up standby decks and the middle cards
    def deal(self):
        self.computer_cards = self.cards[:20]
        self.player_cards = self.cards[20:40]
        self.standby1 = self.cards[40:45]
        self.standby2 = self.cards[45:50]
        self.wrkcard1 = self.cards[50]
        self.wrkcard2 = self.cards[51]

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
