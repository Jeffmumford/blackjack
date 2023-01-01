import random

symbols = {'clubs': "\u2663", 'hearts': "\u2665",'diamonds': "\u2666",'spades': "\u2660"}

suits = ['diamonds', 'hearts', 'spades', 'clubs']
ranks = ['ace', 'two', 'three', 'four', 'five','six','seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
values = {'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5,'six' : 6,'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10, 'jack' : 10, 'queen' : 10, 'king' : 10, 'ace' : 11}


class Card:
    """set up individual cards"""

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        self.symbol = symbols[suit]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
    

       



class Deck:

    """set up a list to store the deck of cards and loop through ranks and suits to set up deck"""

    def __init__(self):
        self.all_cards = []

        for rank in ranks:
            for suit in suits:
                self.all_cards.append(Card(rank,suit))

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    #deal a single card out of the deck/remove it from the deck
    def deal_one(self):
        card = self.all_cards.pop()
        return card
    
  




class Hand:

    """Create a list that can hold a players hand"""

    def __init__(self):
        self.all_cards = []
        self.cash = 500

    #to add a single card to a hand
    def add_card(self,card):
        self.all_cards.append(card)
    
    #plays a card out of the player hand and removes it from the hand
    def play_card(self):
        card = self.all_cards.pop()
        return card

    def clear_hand(self):
        for i in range(len(self.all_cards)):
            self.all_cards.pop()

    def place_bet(self, bet):
        self.cash -= bet
    def win_bet(self, bet):
        self.cash += bet

    #to print out the cards in a players hand
    def __str__(self):
        output = ''
        for i in self.all_cards:
            output += str(i) + "\n"
        return output