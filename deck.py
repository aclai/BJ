import Card

deck = []

deck.append(deck)
print(deck)

for x in range(1, 4):
    for y in range(1, 13):
        deck.append(Card.Card(x, y))
        
print(deck[1])
print([deck[1].suit, deck[1].card_num])