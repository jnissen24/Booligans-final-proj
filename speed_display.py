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

# Load and scale card images
back_of_card = pygame.image.load('./Playing Cards/PNG-cards-1.3/gray_back.png')
back_of_card = pygame.transform.scale(back_of_card, (100, 150))
_AH = pygame.image.load('./Playing Cards/PNG-cards-1.3/AH.png')
_AH = pygame.transform.scale(_AH, (100, 150))
_AD = pygame.image.load('./Playing Cards/PNG-cards-1.3/AD.png')
_AD = pygame.transform.scale(_AD, (100, 150))
_AC = pygame.image.load('./Playing Cards/PNG-cards-1.3/AC.png')
_AC = pygame.transform.scale(_AC, (100, 150))
_AS = pygame.image.load('./Playing Cards/PNG-cards-1.3/AS.png')
_AS = pygame.transform.scale(_AS, (100, 150))
_2H = pygame.image.load('./Playing Cards/PNG-cards-1.3/2H.png')
_2H = pygame.transform.scale(_2H, (100, 150))
_2D = pygame.image.load('./Playing Cards/PNG-cards-1.3/2D.png')
_2D = pygame.transform.scale(_2D, (100, 150))
_2C = pygame.image.load('./Playing Cards/PNG-cards-1.3/2C.png')
_2C = pygame.transform.scale(_2C, (100, 150))
_2S = pygame.image.load('./Playing Cards/PNG-cards-1.3/2S.png')
_2S = pygame.transform.scale(_2S, (100, 150))
_3H = pygame.image.load('./Playing Cards/PNG-cards-1.3/3H.png')
_3H = pygame.transform.scale(_3H, (100, 150))
_3D = pygame.image.load('./Playing Cards/PNG-cards-1.3/3D.png')
_3D = pygame.transform.scale(_3D, (100, 150))
_3C = pygame.image.load('./Playing Cards/PNG-cards-1.3/3C.png')
_3C = pygame.transform.scale(_3C, (100, 150))
_3S = pygame.image.load('./Playing Cards/PNG-cards-1.3/3S.png')
_3S = pygame.transform.scale(_3S, (100, 150))
_4H = pygame.image.load('./Playing Cards/PNG-cards-1.3/4H.png')
_4H = pygame.transform.scale(_4H, (100, 150))
_4D = pygame.image.load('./Playing Cards/PNG-cards-1.3/4D.png')
_4D = pygame.transform.scale(_4D, (100, 150))
_4C = pygame.image.load('./Playing Cards/PNG-cards-1.3/4C.png')
_4C = pygame.transform.scale(_4C, (100, 150))
_4S = pygame.image.load('./Playing Cards/PNG-cards-1.3/4S.png')
_4S = pygame.transform.scale(_4S, (100, 150))
_5H = pygame.image.load('./Playing Cards/PNG-cards-1.3/5H.png')
_5H = pygame.transform.scale(_5H, (100, 150))
_5D = pygame.image.load('./Playing Cards/PNG-cards-1.3/5D.png')
_5D = pygame.transform.scale(_5D, (100, 150))
_5C = pygame.image.load('./Playing Cards/PNG-cards-1.3/5C.png')
_5C = pygame.transform.scale(_5C, (100, 150))
_5S = pygame.image.load('./Playing Cards/PNG-cards-1.3/5S.png')
_5S = pygame.transform.scale(_5S, (100, 150))
_6H = pygame.image.load('./Playing Cards/PNG-cards-1.3/6H.png')
_6H = pygame.transform.scale(_6H, (100, 150))
_6D = pygame.image.load('./Playing Cards/PNG-cards-1.3/6D.png')
_6D = pygame.transform.scale(_6D, (100, 150))
_6C = pygame.image.load('./Playing Cards/PNG-cards-1.3/6C.png')
_6C = pygame.transform.scale(_6C, (100, 150))
_6S = pygame.image.load('./Playing Cards/PNG-cards-1.3/6S.png')
_6S = pygame.transform.scale(_6S, (100, 150))
_7H = pygame.image.load('./Playing Cards/PNG-cards-1.3/7H.png')
_7H = pygame.transform.scale(_7H, (100, 150))
_7D = pygame.image.load('./Playing Cards/PNG-cards-1.3/7D.png')
_7D = pygame.transform.scale(_7D, (100, 150))
_7C = pygame.image.load('./Playing Cards/PNG-cards-1.3/7C.png')
_7C = pygame.transform.scale(_7C, (100, 150))
_7S = pygame.image.load('./Playing Cards/PNG-cards-1.3/7S.png')
_7S = pygame.transform.scale(_7S, (100, 150))
_8H = pygame.image.load('./Playing Cards/PNG-cards-1.3/8H.png')
_8H = pygame.transform.scale(_8H, (100, 150))
_8D = pygame.image.load('./Playing Cards/PNG-cards-1.3/8D.png')
_8D = pygame.transform.scale(_8D, (100, 150))
_8C = pygame.image.load('./Playing Cards/PNG-cards-1.3/8C.png')
_8C = pygame.transform.scale(_8C, (100, 150))
_8S = pygame.image.load('./Playing Cards/PNG-cards-1.3/8S.png')
_8S = pygame.transform.scale(_8S, (100, 150))
_9H = pygame.image.load('./Playing Cards/PNG-cards-1.3/9H.png')
_9H = pygame.transform.scale(_9H, (100, 150))
_9D = pygame.image.load('./Playing Cards/PNG-cards-1.3/9D.png')
_9D = pygame.transform.scale(_9D, (100, 150))
_9C = pygame.image.load('./Playing Cards/PNG-cards-1.3/9C.png')
_9C = pygame.transform.scale(_9C, (100, 150))
_9S = pygame.image.load('./Playing Cards/PNG-cards-1.3/9S.png')
_9S = pygame.transform.scale(_9S, (100, 150))
_10H = pygame.image.load('./Playing Cards/PNG-cards-1.3/10H.png')
_10H = pygame.transform.scale(_10H, (100, 150))
_10D = pygame.image.load('./Playing Cards/PNG-cards-1.3/10D.png')
_10D = pygame.transform.scale(_10D, (100, 150))
_10C = pygame.image.load('./Playing Cards/PNG-cards-1.3/10C.png')
_10C = pygame.transform.scale(_10C, (100, 150))
_10S = pygame.image.load('./Playing Cards/PNG-cards-1.3/10S.png')
_10S = pygame.transform.scale(_10S, (100, 150))
_JH = pygame.image.load('./Playing Cards/PNG-cards-1.3/JH.png')
_JH = pygame.transform.scale(_JH, (100, 150))
_JD = pygame.image.load('./Playing Cards/PNG-cards-1.3/JD.png')
_JD = pygame.transform.scale(_JD, (100, 150))
_JC = pygame.image.load('./Playing Cards/PNG-cards-1.3/JC.png')
_JC = pygame.transform.scale(_JC, (100, 150))
_JS = pygame.image.load('./Playing Cards/PNG-cards-1.3/JS.png')
_JS = pygame.transform.scale(_JS, (100, 150))
_QH = pygame.image.load('./Playing Cards/PNG-cards-1.3/QH.png')
_QH = pygame.transform.scale(_QH, (100, 150))
_QD = pygame.image.load('./Playing Cards/PNG-cards-1.3/QD.png')
_QD = pygame.transform.scale(_QD, (100, 150))
_QC = pygame.image.load('./Playing Cards/PNG-cards-1.3/QC.png')
_QC = pygame.transform.scale(_QC, (100, 150))
_QS = pygame.image.load('./Playing Cards/PNG-cards-1.3/QS.png')
_QS = pygame.transform.scale(_QS, (100, 150))
_KH = pygame.image.load('./Playing Cards/PNG-cards-1.3/KH.png')
_KH = pygame.transform.scale(_KH, (100, 150))
_KD = pygame.image.load('./Playing Cards/PNG-cards-1.3/KD.png')
_KD = pygame.transform.scale(_KD, (100, 150))
_KC = pygame.image.load('./Playing Cards/PNG-cards-1.3/KC.png')
_KC = pygame.transform.scale(_KC, (100, 150))
_KS = pygame.image.load('./Playing Cards/PNG-cards-1.3/KS.png')
_KS = pygame.transform.scale(_KS, (100, 150))

deck = Deck()

wrkcard1_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard1.getstr() + '.png')
wrkcard1_pic = pygame.transform.scale(wrkcard1_pic, (100, 150))
wrkcard2_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard2.getstr() + '.png')
wrkcard2_pic = pygame.transform.scale(wrkcard2_pic, (100, 150))

#player_hand_pics = []
#for i in range(0, 5):
   # player_hand_pics[i] = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.player_cards[i].getstr() + '.png')
    #player_hand_pics[i] = pygame.transform.scale(player_hand_pics[i], (100, 150))

running = True
while running:
    for i in range(0, 5):
        screen.blit(_KS, (190 + 130 * i, 550))
        pygame.display.update()

    screen.blit(wrkcard1_pic, (375, 250))  # working card 1
    screen.blit(wrkcard2_pic, (525, 250))  # working card 2
    screen.blit(back_of_card, (120, 250))  # standby deck 1
    screen.blit(back_of_card, (780, 250))  # standby deck 2
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
