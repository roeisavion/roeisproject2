from unittest import TestCase,mock
from random import randint
from  CardsGame.CardGame import CardGame
from CardsGame.Player import Player
from CardsGame.DeckOfCards import DeckOfCards



class TestCardGame(TestCase):

    def test_newGame(self):
        game=CardGame(14)
        self.assertEqual(game.newGame(),'not enough cards or illigal number of cards')
        game1 = CardGame(-1)
        self.assertEqual(game1.newGame(),'not enough cards or illigal number of cards')
        game2 = CardGame('a')
        self.assertEqual(game2.newGame(), 'illigal number of cards')



    @mock.patch('CardsGame.CardGame.CardGame.newGame', return_value=None)
    def test_init_(self,mock_game):
        game3=CardGame(4)
        self.assertEqual(game3.num_of_cards,4)
        self.assertEqual(game3.newGame(),None)
        for i in range (len(game3.players)):
            self.assertTrue(type(game3.players[i])==Player)

