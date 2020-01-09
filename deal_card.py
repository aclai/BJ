import random

# input is either playerhand or dealerhand
def deal_card(hand):
    random_card = random.choice(deck)
    print(random_card)
    len(deck)
    deck.remove(random_card)
    len(deck)
    hand.append(random_card)
    print(hand)