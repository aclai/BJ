#Python 3.7.5

import deck
import card
import gameplay_method

main_deck = deck.Deck()
print("length of main_deck after creating deck object:")
print(len(main_deck))
main_deck.create_full_deck()
print("length of main_deck after create_full_deck:")
print(len(main_deck))

player_hand = deck.Deck()
dealer_hand = deck.Deck()

player_hand.move_random_card(main_deck)
dealer_hand.move_random_card(main_deck)
print("player hand with 1 card:")
print(player_hand[0].card_eng_name)
print("dealer hand with 1 card:")
print(dealer_hand[0].card_eng_name)
print("length of main_deck aftter dealing 2 cards")
print(len(main_deck))

gameplay_method.player_turn(player_hand, main_deck)
print("player_hand after player is done:")
for i in player_hand:
    print(i.card_eng_name)
	
gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)

print("dealer_hand after dealer is done")
for i in dealer_hand:
    print(i.card_eng_name)

outcome = gameplay_method.check_winner(player_hand, dealer_hand)
print("the multiplier for payout base of the bet amount - 2.5 for bj, 2 for win, 1 for draw, and 0 for lose")
print(outcome)



	