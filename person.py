class Person:

    def __init__(self):
        self.hand = []
        self.hand_value = []
     
    def add_deck(self, deck):
        self.hand.append(deck)
     
    def hand_value(self, hand_value):
        self.hand_value.append(hand_value)