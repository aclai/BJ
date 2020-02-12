"""
Card is a poker card with its number, suit, point, and english name
"""
class Card:
    #done
    def __init__ (self, suit, card_num, card_point, card_eng_name):
        self.suit = suit
        # A, 2, ..., J, Q, K
        self.card_num = card_num
        # A = 1, 2 = 2, ..., 10/J/Q/K = 10
        self.card_point = card_point
        self.card_eng_name = card_eng_name