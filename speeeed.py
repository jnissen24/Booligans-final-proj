# -*- coding: utf-8 -*-
"""speeeed.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XV5tjgkJfA4O0Bf3Gx6KB42UnU9LBqOs

<a href="https://colab.research.google.com/github/jnissen24/Booligans-final-proj/blob/main/speeeed.ipynb"
target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

# PSUEDOCODE/OUTLINE:
# display rules/object of game
# set up game board
# create deck of cards; shuffle/randomize
# deal two stacks of 20 and two stacks of 5 all face down, two individual cards face up/displayed
# assign one stack of 20 to computer, the other to active player
# start game
# each player gets the first 5 cards of their 20 face-up
# variables: computer_cards, player_cards, standby1, standby2, wrkcard1, wrkcard2, computer_hand + player_hand
# can play a card from their 5 if it is +1 or -1 of either of the two face-up cards;
# this card becomes the new face-up card
# when a card is played, player then replenishes hand of 5 by drawing from personal pile
# this occurs until no cards are left - player wins by getting rid of cards first
# exceptions
# if neither player can use their in-hand cards to be +1 or -1 of the two working face-up cards,
# then two new working cards can be flipped, one from each of the two waiting piles of 5
# once all of these have been used, all of the previous working cards (except the two on top)
# are shuffled and used to draw from once more

import random
import pygame

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
            for jj in range(1, 14):  # ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
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

def showDeck(mydeck):
    mystr = ''
    for c in mydeck:
        mystr = mystr + ',' + c.getstr()
    print(mystr)


def displayStatus(deck, computer_hand):
    print('Standby1 : ')
    showDeck(deck.standby1)

    print('Standby2 : ')
    showDeck(deck.standby2)

    print('Wrkcard1 : ')
    deck.wrkcard1.show()

    print('Wrkcard2 : ')
    deck.wrkcard2.show()

    print('Computer Hand:')
    showDeck(computer_hand)

    print('Computer Cards: ')
    showDeck(deck.computer_cards)

### ACTUAL GAME STARTS ###
deck = Deck()

# print statement for wrkcard since only has one object
#print(deck.wrkcard1.show())
#print(deck.wrkcard2.show())
# print statement for all other piles
#print([x.show() for x in deck.computer_cards])
#print([x.show() for x in deck.player_cards])

pygame.init()

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

#fonts
small_font = pygame.font.Font(None, 32)
large_font = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((width, height))
screen.fill(gray)
pygame.display.set_caption("Speed!")

back_of_card = pygame.image.load('./Playing Cards/PNG-cards-1.3/gray_back.png')
back_of_card = pygame.transform.scale(back_of_card, (100, 150))
# take first 5 cards of each player's stack to be in active hand
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

print(deck.wrkcard1.show())
print(deck.wrkcard2.show())
import time
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# loop for game play
    def computer_gameplay():
        pygame.time.wait(3000)
        count = 0
        count_player = 0
        displayStatus(deck, computer_hand)
        #while len(computer_hand) > 0 and (count < len(computer_hand)):
        for item in range(0,5):
            if len(computer_hand) > 0 and count < len(computer_hand):
                item = computer_hand[count]
                count = count + 1
                length_comp = len(computer_hand)
                if (item.value == (deck.wrkcard1.value + 1)) or (item.value == (deck.wrkcard1.value - 1)) or (item.value == 13 and (deck.wrkcard1.value == 1)) or (item.value == 1 and (deck.wrkcard1.value == 13)):
                    deck.standby1.append(deck.wrkcard1)  # keeps deck.wrkcard1 at holding one thing
                    deck.wrkcard1 = item
                    wrkcard1_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard1.getstr() + '.png')
                    wrkcard1_pic = pygame.transform.scale(wrkcard1_pic, (100, 150))
                    pygame.display.update()
                    computer_hand.pop(count-1)
                    if len(deck.computer_cards) > 0:
                        computer_hand.append(deck.computer_cards[0])
                        deck.computer_cards.pop(0)
                        count = 0
                    else:
                        count = 0
                    print('Replace working card 1')
                    displayStatus(deck, computer_hand)
                    break
                elif (item.value == (deck.wrkcard2.value + 1)) or (item.value == (deck.wrkcard2.value - 1)) or (item.value == 13 and (deck.wrkcard2.value == 1)) or (item.value == 1 and (deck.wrkcard2.value == 13)):
                    deck.standby2.append(deck.wrkcard2)
                    deck.wrkcard2 = item
                    wrkcard2_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard2.getstr() + '.png')
                    wrkcard2_pic = pygame.transform.scale(wrkcard2_pic, (100, 150))
                    pygame.display.update()
                    computer_hand.pop(count-1)
                    if len(deck.computer_cards) > 0:
                        computer_hand.append(deck.computer_cards[0])
                        deck.computer_cards.pop(0)
                        count = 0
                    else:
                        count = 0
                    print('Replace working card 2')
                    displayStatus(deck, computer_hand)
                    break
                elif count == length_comp:
                    count = 0
                    break
                else:
                    pass


    def quit_game():
        pygame.quit()
        quit()


    def player_gameplay():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("number one")
                    print(player_hand[0].value)
                    if (player_hand[0].value == (deck.wrkcard1.value + 1)) or (player_hand[0].value == (deck.wrkcard1.value - 1)) or (player_hand[0].value == 13 and (deck.wrkcard1.value == 1)) or (player_hand[0].value == 1 and (deck.wrkcard1.value == 13)):
                        deck.standby1.append(deck.wrkcard1)
                        deck.wrkcard1 = player_hand[0]
                        player_hand.pop(0)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    elif (player_hand[0].value == (deck.wrkcard2.value + 1)) or (player_hand[0].value == (deck.wrkcard2.value - 1)) or (player_hand[0].value == 13 and (deck.wrkcard2.value == 1)) or (player_hand[0].value == 1 and (deck.wrkcard2.value == 13)):
                        deck.standby2.append(deck.wrkcard2)
                        deck.wrkcard2 = player_hand[0]
                        player_hand.pop(0)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    else:
                        print('Error - this card cannot be played')
                elif event.key == pygame.K_2:
                    print("number 2")
                    if (player_hand[1].value == (deck.wrkcard1.value + 1)) or (player_hand[1].value == (deck.wrkcard1.value - 1)) or (player_hand[1].value == 13 and (deck.wrkcard1.value == 1)) or (player_hand[1].value == 1 and (deck.wrkcard1.value == 13)):
                        deck.standby1.append(deck.wrkcard1)
                        deck.wrkcard1 = player_hand[1]
                        player_hand.pop(1)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    elif (player_hand[1].value == (deck.wrkcard2.value + 1)) or (player_hand[1].value == (deck.wrkcard2.value - 1)) or (player_hand[1].value == 13 and (deck.wrkcard2.value == 1)) or (player_hand[1].value == 1 and (deck.wrkcard2.value == 13)):
                        deck.standby2.append(deck.wrkcard2)
                        deck.wrkcard2 = player_hand[1]
                        player_hand.pop(1)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    else:
                        print('Error - this card cannot be played')
                elif event.key == pygame.K_3:
                    print("number 3")
                    if (player_hand[2].value == (deck.wrkcard1.value + 1)) or (player_hand[2].value == (deck.wrkcard1.value - 1)) or (player_hand[2].value == 13 and (deck.wrkcard1.value == 1)) or (player_hand[2].value == 1 and (deck.wrkcard1.value == 13)):
                        deck.standby1.append(deck.wrkcard1)
                        deck.wrkcard1 = player_hand[2]
                        player_hand.pop(2)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    elif (player_hand[2].value == (deck.wrkcard2.value + 1)) or (player_hand[2].value == (deck.wrkcard2.value - 1)) or (player_hand[2].value == 13 and (deck.wrkcard2.value == 1)) or (player_hand[2].value == 1 and (deck.wrkcard2.value == 13)):
                        deck.standby2.append(deck.wrkcard2)
                        deck.wrkcard2 = player_hand[2]
                        player_hand.pop(2)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    else:
                        print('Error - this card cannot be played')
                elif event.key == pygame.K_4:
                    print("number 4")
                    if (player_hand[3].value == (deck.wrkcard1.value + 1)) or (player_hand[3].value == (deck.wrkcard1.value - 1)) or (player_hand[3].value == 13 and (deck.wrkcard1.value == 1)) or (player_hand[3].value == 1 and (deck.wrkcard1.value == 13)):
                        deck.standby1.append(deck.wrkcard1)
                        deck.wrkcard1 = player_hand[3]
                        player_hand.pop(3)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    elif (player_hand[3].value == (deck.wrkcard2.value + 1)) or (player_hand[3].value == (deck.wrkcard2.value - 1)) or (player_hand[3].value == 13 and (deck.wrkcard2.value == 1)) or (player_hand[3].value == 1 and (deck.wrkcard2.value == 13)):
                        deck.standby2.append(deck.wrkcard2)
                        deck.wrkcard2 = player_hand[3]
                        player_hand.pop(3)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)

                        break
                    else:
                        pygame.draw.rect(screen, white, [270, 40, 255, 90])
                        error_text = small_font.render("Error - this card cannot be played", True, black)
                        error_text_rect = error_text.get_rect()
                        error_text_rect.center = (width // 2, 85)
                        screen.blit(error_text, error_text_rect)
                        pygame.display.update()
                elif event.key == pygame.K_5:
                    print("number 5")
                    if (player_hand[4].value == (deck.wrkcard1.value + 1)) or (player_hand[0].value == (deck.wrkcard1.value - 1)) or (player_hand[4].value == 13 and (deck.wrkcard1.value == 1)) or (player_hand[4].value == 1 and (deck.wrkcard1.value == 13)):
                        deck.standby1.append(deck.wrkcard1)
                        deck.wrkcard1 = player_hand[4]
                        player_hand.pop(4)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)
                        break
                    elif (player_hand[4].value == (deck.wrkcard2.value + 1)) or (player_hand[4].value == (deck.wrkcard2.value - 1)) or (player_hand[4].value == 13 and (deck.wrkcard2.value == 1)) or (player_hand[4].value == 1 and (deck.wrkcard2.value == 13)):
                        deck.standby2.append(deck.wrkcard2)
                        deck.wrkcard2 = player_hand[4]
                        player_hand.pop(4)
                        if len(deck.player_cards) > 0:
                            player_hand.append(deck.player_cards[0])
                            deck.player_cards.pop(0)
                        break
                    else:
                        print('Error - this card cannot be played')
                elif event.key == pygame.K_6:
                    print("number 6")
                    deck.wrkcard1 = deck.standby1[0]
                    card = deck.standby1.pop(0)
                    deck.standby1.append(card)
                    print('Flip')
                    deck.wrkcard2 = deck.standby2[0]
                    card = deck.standby2.pop(0)
                    deck.standby2.append(card)
                    break
                else:
                    print('Invalid key - try again!')

    game_over = False
    while not game_over:

        if len(player_hand) == 4:
            screen.fill(gray)
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
            screen.blit(player_hand_pic1, (200, 550))
            screen.blit(player_hand_pic2, (330, 550))
            screen.blit(player_hand_pic3, (460, 550))
            screen.blit(player_hand_pic4, (590, 550))

            screen.blit(wrkcard1_pic, (375, 250))  # working card 1
            screen.blit(wrkcard2_pic, (525, 250))  # working card 2
            screen.blit(back_of_card, (120, 250))  # standby deck 1
            screen.blit(back_of_card, (780, 250))  # standby deck 2
            pygame.display.update()

        elif len(player_hand) == 3:
            screen.fill(gray)
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
            screen.blit(player_hand_pic1, (200, 550))
            screen.blit(player_hand_pic2, (330, 550))
            screen.blit(player_hand_pic3, (460, 550))

            screen.blit(wrkcard1_pic, (375, 250))  # working card 1
            screen.blit(wrkcard2_pic, (525, 250))  # working card 2
            screen.blit(back_of_card, (120, 250))  # standby deck 1
            screen.blit(back_of_card, (780, 250))  # standby deck 2
            pygame.display.update()

        elif len(player_hand) == 2:
            screen.fill(gray)
            wrkcard1_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard1.getstr() + '.png')
            wrkcard1_pic = pygame.transform.scale(wrkcard1_pic, (100, 150))
            wrkcard2_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard2.getstr() + '.png')
            wrkcard2_pic = pygame.transform.scale(wrkcard2_pic, (100, 150))

            player_hand_pic1 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[0].getstr() + '.png')
            player_hand_pic1 = pygame.transform.scale(player_hand_pic1, (100, 150))
            player_hand_pic2 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[1].getstr() + '.png')
            player_hand_pic2 = pygame.transform.scale(player_hand_pic2, (100, 150))
            screen.blit(player_hand_pic1, (200, 550))
            screen.blit(player_hand_pic2, (330, 550))

            screen.blit(wrkcard1_pic, (375, 250))  # working card 1
            screen.blit(wrkcard2_pic, (525, 250))  # working card 2
            screen.blit(back_of_card, (120, 250))  # standby deck 1
            screen.blit(back_of_card, (780, 250))  # standby deck 2
            pygame.display.update()

        elif len(player_hand) == 1:
            screen.fill(gray)
            wrkcard1_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard1.getstr() + '.png')
            wrkcard1_pic = pygame.transform.scale(wrkcard1_pic, (100, 150))
            wrkcard2_pic = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + deck.wrkcard2.getstr() + '.png')
            wrkcard2_pic = pygame.transform.scale(wrkcard2_pic, (100, 150))

            player_hand_pic1 = pygame.image.load('./Playing Cards/PNG-cards-1.3/' + player_hand[0].getstr() + '.png')
            player_hand_pic1 = pygame.transform.scale(player_hand_pic1, (100, 150))
            screen.blit(player_hand_pic1, (200, 550))

            screen.blit(wrkcard1_pic, (375, 250))  # working card 1
            screen.blit(wrkcard2_pic, (525, 250))  # working card 2
            screen.blit(back_of_card, (120, 250))  # standby deck 1
            screen.blit(back_of_card, (780, 250))  # standby deck 2
            pygame.display.update()

        elif len(player_hand) > 4:
            screen.fill(gray)
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

            # Load images of player hand
            screen.blit(player_hand_pic1, (200, 550))
            screen.blit(player_hand_pic2, (330, 550))
            screen.blit(player_hand_pic3, (460, 550))
            screen.blit(player_hand_pic4, (590, 550))
            screen.blit(player_hand_pic5, (720, 550))

        # Load images of working cards and standby decks
            screen.blit(wrkcard1_pic, (375, 250))  # working card 1
            screen.blit(wrkcard2_pic, (525, 250))  # working card 2
            screen.blit(back_of_card, (120, 250))  # standby deck 1
            screen.blit(back_of_card, (780, 250))  # standby deck 2
            pygame.display.update()

        computer_gameplay()
        player_gameplay()

        if len(deck.computer_cards) == 0 and len(computer_hand) == 0:
            print('Computer has won the game!')
            screen.fill(gray)
            pygame.display.update()
            pygame.time.wait(5000)
            game_over = True
            running = False
        elif len(deck.player_cards) == 0 and len(player_hand) == 0:
            game_over = True
            running = False
        else:
            game_over = False
##