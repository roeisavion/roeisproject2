from CardsGame.DeckOfCards import DeckOfCards
from random import shuffle
from CardsGame.Card import Card

class Player():
    def __init__(self,name,money,num_of_cards=5):
        if type(name)==str:
            self.name=name
        if type(money)==int and money>1:
            self.money=money
        if type(num_of_cards) == int and num_of_cards<0:
            self.num_of_cards=num_of_cards
        else: self.num_of_cards=5
        self.cards=[]

    def setHand(self, deck):
        'adds 5 cards to a player hand'
        if self.num_of_cards<=len(deck.deck):
            for i in range (self.num_of_cards):
                if type(deck.deck[-1])== Card:
                    self.addCard(deck.dealOne())


    def addCard(self, card):
        'add 1 card to a player hand'
        if type(card)==Card:
            self.cards.append(card)

    def dropCard(self):
        if len(self.cards)>0:
            shuffle(self.cards)
            return self.cards.pop()

    def reduceAmount(self,amount):
        if 0<=amount<=self.money and type(amount)==int:
            self.money-=amount


    def addAmount(self,amount):
        if amount>0 and type(amount)==int:
            self.money+=amount

    def __repr__(self):
        return f'{self.name}, money:{self.money}, cards:{self.cards}\n'
