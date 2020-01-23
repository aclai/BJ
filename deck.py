import card
import random

class Deck(list):
    def __init__(self):
        self.id = ""
        
    def create_full_deck(self):
        #print(deck)
        for x in range(0, 4):
            for y in range(0, 13):
                card_point = [1,2,3,4,5,6,7,8,9,10,10,10,10]
                card_eng_name = self.card_reader(x, y)
                self.add_card(card.Card(x+1, y+1, card_point[y], card_eng_name))
        #print(deck[1])
        #print([deck[1].suit, deck[1].card_num])
        #print(deck)
        
    def add_card(self, card):
        self.append(card)
    
    def remove_card(self, card):
        self.remove(card)
        
    def empty_deck(self):
        self.clear()
    
    def draw_card(self):
        random_card = random.choice(self)
        return random_card
        
    #works for both dealing card from main_deck and spliting card into seperate decks    
    def move_random_card(self, from_deck):
        random_card = from_deck.draw_card()
        #print(random_card)
        from_deck.remove_card(random_card)
        #len(self.deck)
        self.add_card(random_card)
        
    def card_reader(self, suit, card_num):
        eng_suit = ["Diamond", "Club", "Heart", "Spade"]
        eng_num = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
        
        #print (card_num)
        #print (suit)
        #print (eng_num[card_num])
        #print (eng_suit[suit])
        #print (str(eng_num[card_num]) + " of " + eng_suit[suit])   
        card_eng_name = (str(eng_num[card_num]) + " of " + eng_suit[suit])
        return card_eng_name
        
