"""
Person is the super class of Player and Dealer
"""
class Person:
    def __init__(self, name):
        self.name = name
    
    """
    Method to add a deck obejct 
    """
    def add_deck(self, deck):
        self.hand.append(deck)
     
    """
    Method to record a hand's points to a Person
    """
    def hand_value(self, hand_value):
        self.hand_value.append(hand_value)