from unittest import TestCase,mock
from CardsGame.Card import Card
from CardsGame.DeckOfCards import DeckOfCards

class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck1 = DeckOfCards()
        self.deck2 = DeckOfCards()
        self.deck3 = DeckOfCards()
        self.deck3.newGame()

    def test_dealOne(self):
        self.assertTrue(self.deck1.deck[-1]==self.deck1.dealOne())
        self.deck1.deck=[]
        self.assertEqual(self.deck1.dealOne(),None)


    def test_newGame(self):
        self.assertTrue(len(self.deck1.deck)==52)
        print(self.deck1)
        print(self.deck2)
        print(self.deck3)
        self.assertTrue(self.deck1==self.deck2)
        self.assertTrue(self.deck3!=self.deck2)

    def test_show(self):
        pass

    def test_shuffle(self):
        self.deck1._DeckOfCards__shuffle_deck()
        self.assertTrue(self.deck2!=self.deck1)

        self.deck1.dealOne()
        self.deck2.deck=self.deck1.deck.copy()
        self.deck1._DeckOfCards__shuffle_deck()
        self.assertTrue(self.deck2==self.deck1)

