from CardsGame.CardGame import CardGame

game=CardGame()
print(game.players)

for i in range (game.num_of_cards):
    max_value=0
    max_suit=0
    winner=0
    bank=0
    dropped_cards=[]
    for a in range (len(game.players)):
        bank+=(1+i)*100
        game.players[a].reduceAmount((1+i)*100)
        dropped_cards.append(game.players[a].dropCard())
    winner=dropped_cards.index(max(dropped_cards))
    print(dropped_cards)
    game.players[winner].addAmount(bank)
    print(f'game winner:{game.players[winner]}')
    print('*********************************************************************************************************')
money_list=[]
for i in range (len(game.players)):
    money_list.append(game.players[i].money)

winnerOfTheGame_index=money_list.index(max(money_list))
print(f'winner of the game is {game.players[winnerOfTheGame_index]}')



# if dropped_card.value>max_value :
#     max_value=dropped_card.value
#     max_suit=dropped_card.suit
#     winner=a
# if dropped_card.value==max_value:
#     if dropped_card.suit>max_suit:
#         max_value = dropped_card.value
#         max_suit = dropped_card.suit
#         winner = a