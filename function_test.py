"""
Use this to test functions in gameplay_method.py
"""

import deck
import gameplay_method
import card
import random
import player

"""
Create parameters that only need to be created once for the functions
"""
main_deck = deck.Deck()
player = player.Player()
player.bet = 100

"""
Infinite loop to test the functions until tester hit ctrl + c
"""
while True:
    """
    Create parameters that needs to be recreated for every run
    """
    player_hand = deck.Deck()
    dealer_hand = deck.Deck()
    
    """
    Put diamond Ace to 10 into main_deck, which is sufficient for the test
    """
    for y in range(0, 10):
        card_point = [1,2,3,4,5,6,7,8,9,10]
        card_eng_name = main_deck.card_reader(0, y)
        main_deck.add_card(card.Card(1, y+1, card_point[y], card_eng_name))
    
    """
    Pick 4 random cards to put in player_hand and dealer_hand without removing them from main_deck
    """
    random_card_1 = random.choice(main_deck)
    random_card_2 = random.choice(main_deck)
    random_card_3 = random.choice(main_deck)
    random_card_4 = random.choice(main_deck)
    
    player_hand.append(random_card_1)
    player_hand.append(random_card_2)
    
    dealer_hand.append(random_card_3)
    dealer_hand.append(random_card_4)
    
    """
    Functions to be tested. Delete the # in front of the function to test. Code that immediately follow a function without a blank line
    are for printing the necessary output to determine whether the function is working as intended
    """
    #gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)
    
    #dealer_point = gameplay_method.calculate_hand(dealer_hand)
    #dealer_hand.hand_reader()
    #print(dealer_point)
    
    #gameplay_method.check_winner(player, player_hand, dealer_hand)
    
    #gameplay_method.hit_decision("Y", player, player_hand, main_deck)
    #player_hand.hand_reader()
    #print(len(player_hand))
    
    #gameplay_method.
    #gameplay_method.
    #gameplay_method.
    #gameplay_method.
    
