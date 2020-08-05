from unittest import TestCase
from CardsGame.Card import Card

class TestCard(TestCase):
    def test_init(self):
        card1=Card(15,5)
        print(card1)
        self.assertTrue(card1.__repr__() == '2 diamond')
