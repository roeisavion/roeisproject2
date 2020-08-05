from CardsGame.Card import Card
from random import shuffle
class DeckOfCards():

    def __init__(self):
        'builds a deck of 54 cards'
        self.deck =[]
        for i in range (4):
            for a in range (13):
                self.deck.append(Card(a,i))

    def __eq__(self, other):
        if self.deck==other.deck :
            return True
        else: return False

    def __repr__(self):
        return f'this is the deck \n{self.deck}'

    def __shuffle_deck(self):
        if len(self.deck)==52:
            shuffle(self.deck)

    def dealOne(self):
        'give a card from the top of the deck '
        if len(self.deck)>0:
            return self.deck.pop()

    def newGame(self):
        self.__init__()
        self.__shuffle_deck()

    def show(self):
        print(self)



