"""
 Deck is a list that stores Card object(s)
"""
import card
import random

class Deck(list):
    def __init__(self):
        # stores whether a player has chose to double down in a hand, default set to False
        self.double = False
        
    def create_full_deck(self):
        """
        This method creates a full deck of 52 unique Card objects and append it to the deck
        """
        # x represents suits and y represents
        for x in range(0, 4):
            for y in range(0, 13):
                # card points from A to K, respectively
                card_point = [1,2,3,4,5,6,7,8,9,10,10,10,10]
                # call card_reaader() to generate the english name of the card
                card_eng_name = self.card_reader(x, y)
                # creates and adds 1 card to deck
                self.add_card(card.Card(x+1, y+1, card_point[y], card_eng_name))
        
    def add_card(self, card):
        """
        This method adds a card to a deck
        """
        self.append(card)
    
    def remove_card(self, card):
        """
        This method removes a card from a deck
        """
        self.remove(card)
        
    def empty_deck(self):
        """
        This method empties a deck
        """
        self.clear()
    
    def draw_card(self):
        """
        This method randomly select a card from a deck
        """
        random_card = random.choice(self)
        return random_card
        
    #works for both dealing card from main_deck and spliting card into seperate decks    
    def move_random_card(self, from_deck):
        """
        This method removes a random card from from_deck and append it to the deck which called the method
        """
        # select a random card
        random_card = from_deck.draw_card()
        # remove the selected card from from_deck
        from_deck.remove_card(random_card)
        # add the selected card to the deck which called the method
        self.add_card(random_card)
        
    def card_reader(self, suit, card_num):
        """
        This method returns the english name of a card base on the input
        """
        eng_suit = ["Diamond", "Club", "Heart", "Spade"]
        eng_num = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
        card_eng_name = (str(eng_num[card_num]) + " of " + eng_suit[suit])
        return card_eng_name
        
    def hand_reader(self):
        """
        This method prints the english name of the card(s) in a deck
        """
        for i in self:
            print(i.card_eng_name)
