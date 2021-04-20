import pygame
import random


# creates Card class
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{}{}".format(self.value, self.suit))

    def getstr(self):
        str = '{}{}'.format(self.value, self.suit)
        return str


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
            for jj in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
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


def card_value(card):
    if card == "AD":
        value = 1
    elif card == "AC":
        value = 1
    elif card == "AH":
        value = 1
    elif card == "AS":
        value = 1
    elif card == "2D":
        value = 2
    elif card == "2C":
        value = 2
    elif card == "2H":
        value = 2
    elif card == "2S":
        value = 2
    elif card == "3D":
        value = 3
    elif card == "3C":
        value = 3
    elif card == "3H":
        value = 3
    elif card == "3S":
        value = 3
    elif card == "4D":
        value = 4
    elif card == "4C":
        value = 4
    elif card == "4H":
        value = 4
    elif card == "4S":
        value = 4
    elif card == "5D":
        value = 5
    elif card == "5C":
        value = 5
    elif card == "5H":
        value = 5
    elif card == "5S":
        value = 5
    elif card == "6D":
        value = 6
    elif card == "6C":
        value = 6
    elif card == "6H":
        value = 6
    elif card == "6S":
        value = 6
    elif card == "7D":
        value = 7
    elif card == "7C":
        value = 7
    elif card == "7H":
        value = 7
    elif card == "7S":
        value = 7
    elif card == "8D":
        value = 8
    elif card == "8C":
        value = 8
    elif card == "8H":
        value = 8
    elif card == "8S":
        value = 8
    elif card == "9D":
        value = 9
    elif card == "9C":
        value = 9
    elif card == "9H":
        value = 9
    elif card == "9S":
        value = 9
    elif card == "10D":
        value = 10
    elif card == "10C":
        value = 10
    elif card == "10H":
        value = 10
    elif card == "10S":
        value = 10
    elif card == "JD":
        value = 11
    elif card == "JC":
        value = 11
    elif card == "JH":
        value = 11
    elif card == "JS":
        value = 11
    elif card == "QD":
        value = 12
    elif card == "QC":
        value = 12
    elif card == "QH":
        value = 12
    elif card == "QS":
        value = 12
    elif card == "KD":
        value = 13
    elif card == "KC":
        value = 13
    elif card == "KH":
        value = 13
    elif card == "KS":
        value = 13
    else:
        value = 0
    return value


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

# Load and scale back of card images
back_of_card = pygame.image.load('./Playing Cards/PNG-cards-1.3/gray_back.png')
back_of_card = pygame.transform.scale(back_of_card, (100, 150))

deck = Deck()

computer_hand = []
player_hand = []
for i in range(0, 5):
    computer_hand.append(deck.computer_cards[i])
    player_hand.append(deck.player_cards[i])  # this used to be deck.computer_cards but should be this maybe?

deck.computer_cards.pop(0)
deck.computer_cards.pop(0)
deck.computer_cards.pop(0)
deck.computer_cards.pop(0)
deck.computer_cards.pop(0)
deck.player_cards.pop(0)
deck.player_cards.pop(0)
deck.player_cards.pop(0)
deck.player_cards.pop(0)
deck.player_cards.pop(0)

wrkcard1_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard1.getstr() + '.png')
wrkcard1_pic = pygame.transform.scale(wrkcard1_pic, (100, 150))
wrkcard2_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard2.getstr() + '.png')
wrkcard2_pic = pygame.transform.scale(wrkcard2_pic, (100, 150))

player_hand_pic1 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[0].getstr() + '.png')
player_hand_pic1 = pygame.transform.scale(player_hand_pic1, (100, 150))
player_hand_pic2 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[1].getstr() + '.png')
player_hand_pic2 = pygame.transform.scale(player_hand_pic2, (100, 150))
player_hand_pic3 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[2].getstr() + '.png')
player_hand_pic3 = pygame.transform.scale(player_hand_pic3, (100, 150))
player_hand_pic4 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[3].getstr() + '.png')
player_hand_pic4 = pygame.transform.scale(player_hand_pic4, (100, 150))
player_hand_pic5 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[4].getstr() + '.png')
player_hand_pic5 = pygame.transform.scale(player_hand_pic5, (100, 150))

running = True
while running:
    # Load images of player hand
    screen.blit(player_hand_pic1, (200, 550))
    screen.blit(player_hand_pic2, (330, 550))
    screen.blit(player_hand_pic3, (460, 550))
    screen.blit(player_hand_pic4, (590, 550))
    screen.blit(player_hand_pic5, (720, 550))
    pygame.display.update()

    # Load images of working cards and standby decks
    screen.blit(wrkcard1_pic, (375, 250))  # working card 1
    screen.blit(wrkcard2_pic, (525, 250))  # working card 2
    screen.blit(back_of_card, (120, 250))  # standby deck 1
    screen.blit(back_of_card, (780, 250))  # standby deck 2

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
