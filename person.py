"""
Person is the super class of Player and Dealer
"""
class Person:
    """
    This class contains methods shared by Player and Dealer
    """
    def __init__(self, name):
        self.name = name

    def add_deck(self, deck):
        """
        Method to add a deck obejct to a Person's .hand
        """
        self.hand.append(deck)
     
    def hand_value(self, hand_value):
        """
        Method to record a hand's points to a Person .hand_value
        """
        self.hand_value.append(hand_value)