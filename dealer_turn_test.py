import deck
import gameplay_method
import card
import random

main_deck = deck.Deck()
    
while True:
    try:            
        player_hand = deck.Deck()
        dealer_hand = deck.Deck()
        
        for y in range(0, 10):
            card_point = [1,2,3,4,5,6,7,8,9,10]
            card_eng_name = main_deck.card_reader(0, y)
            main_deck.add_card(card.Card(1, y+1, card_point[y], card_eng_name))
        
        random_card_1 = random.choice(main_deck)
        random_card_2 = random.choice(main_deck)
        random_card_3 = random.choice(main_deck)
        random_card_4 = random.choice(main_deck)
        print("wtf")
        player_hand.append(random_card_1)
        player_hand.append(random_card_2)
        
        dealer_hand.append(random_card_3)
        dealer_hand.append(random_card_4)
        
        gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)
    
    except:
        break