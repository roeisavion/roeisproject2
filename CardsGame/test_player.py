from unittest import TestCase,mock
from CardsGame.Player import Player
from CardsGame.Card import Card
from CardsGame.DeckOfCards import DeckOfCards

class TestPlayer(TestCase):
    def setUp(self):
        self.player1=Player('gill',300)
        self.player1.money=50
        self.deck1=DeckOfCards()


    # @mock.patch('CardsGame.DeckOfCards.DeckOfCards.dealOne', return_value=Card(1,1))
    def test_setHand(self):
        cards1=self.player1.cards.copy()
        self.deck1.deck = [1, 2, 3, 4, 5]        #check if not cards
        self.player1.setHand(self.deck1)
        print(self.player1.cards)
        self.assertTrue(self.player1.cards==cards1)

        self.deck1.deck = [Card(5,3),Card(5,3),Card(5,3),Card(5,3)]    #check if deck<num of cards
        self.player1.setHand(self.deck1)
        print(self.player1.cards)
        self.assertTrue(self.player1.cards == cards1)

        self.deck1.deck = [Card(5, 3), Card(5, 3), Card(5, 3), Card(5, 3), Card(4,3)]
        self.player1.setHand(self.deck1)
        print(self.player1.cards)
        self.assertTrue(self.player1.cards != cards1)


    def test_addCard(self):
        player1_cards=self.player1.cards         ### check if only adding cards
        self.player1.addCard(5)
        self.assertTrue(player1_cards==self.player1.cards)


    def test_dropCard(self):
        self.player1.cards=[]
        self.assertEqual(self.player1.dropCard(),None)

    def test_reduceAmount(self):
        self.player1.reduceAmount(100)
        self.assertTrue(self.player1.money==50)             ### amount>money

        self.player1.reduceAmount(-40)                      ###negative amount
        self.assertEqual(self.player1.money,50)

    def test_addAmount(self):
        self.player1.addAmount(-100)
        self.assertEqual(self.player1.money,50)

