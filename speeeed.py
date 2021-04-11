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
    

deck = Deck()
# print statement for wrkcard since only has one object
print(deck.wrkcard1.show())
print(deck.wrkcard2.show())
# print statement for all other piles
print([x.show() for x in deck.computer_cards])
print([x.show() for x in deck.player_cards])

# take first 5 cards of each player's stack to be in active hand
computer_hand = []
player_hand = []
for i in range(0, 5):
  computer_hand.append(deck.computer_cards[i])
  player_hand.append(deck.computer_cards[i])

print([x.show() for x in computer_hand])
print([x.show() for x in player_hand])