from CardsGame.Player import Player
from random import randint
from CardsGame.DeckOfCards import DeckOfCards

class CardGame():
    def __init__(self,num_of_cards=5):
        money=randint(5000,10000)
        self.num_of_cards=num_of_cards
        self.players=[]
        self.players.append(Player('moshe',money,self.num_of_cards))
        self.players.append(Player('gill', money,self.num_of_cards))
        self.players.append(Player('david', money,self.num_of_cards))
        self.players.append(Player('yosi', money,self.num_of_cards))
        self.newGame()



    def newGame(self):
        deck=DeckOfCards()
        deck.newGame()                                 ### creats and shuffles a deck
        if type(self.num_of_cards) == int:
            if  0< len(self.players)*self.num_of_cards <=52:
                for i in range(len(self.players)):
                    self.players[i].setHand(deck)
            else:
                return 'not enough cards or illigal number of cards'
        else: return 'illigal number of cards'






