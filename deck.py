import card
import random

class Deck:
    def __init__(self, owner):
        self.owner = owner
        self.deck = []
        
    def create_deck():
        #print(deck)
        for x in range(0, 4):
            for y in range(0, 13):
                add_card(card.Card(x, y))
        
        #print(deck[1])
        #print([deck[1].suit, deck[1].card_num])
        #print(deck)
        
    def add_card(self, hand):
        hand.append(hand)
    
    def remove_card(self, card):
        card.remove(random_card)
        
    def empty_hand(self, card):
        card.clear()
        
    # input is either playerhand or dealerhand
    def deal_card(self, deck, hand):
        random_card = random.choice(deck)
        print(random_card)
        len(deck)
        deck.remove(random_card)
        len(deck)
        hand.append([random_card])
        print(hand)