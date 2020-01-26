import deck
import gameplay_method
import card

while True:
    try:
        main_deck = deck.Deck()
    
        for y in range(0, 10):
            card_point = [1,2,3,4,5,6,7,8,9,10]
            card_eng_name = main_deck.card_reader(0, y)
            main_deck.add_card(card.Card(1, y+1, card_point[y], card_eng_name))
            
        player_hand = deck.Deck()
        dealer_hand = deck.Deck()
        
        player_hand.append(main_deck[0])
        player_hand.append(main_deck[8])
        
        dealer_hand.append(main_deck[0])
        dealer_hand.append(main_deck[5])
        
        gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)
    
    except:
        break