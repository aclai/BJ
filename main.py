#classes
import card             #
import deck            #
import person         #
import dealer          #sub-class of person
import player          #sub-class of person
#functions
import gameplay_method


#***********************************************************************program starts here***********************************************************************
player = player.Player()
player.input_name()
player.input_chip()

dealer = dealer.Dealer("bj")

while True:
    player.input_bet()
    
    main_deck = deck.Deck()
    print("length of main_deck after creating deck object:")
    print(len(main_deck))
    main_deck.create_full_deck()
    print("length of main_deck after create_full_deck:")
    print(len(main_deck))
    
    dealer_hand = deck.Deck()
    dealer.add_deck(dealer_hand)
    
    player_hand = deck.Deck()
    player.add_deck(player_hand)
    
    player_hand.move_random_card(main_deck)
    dealer_hand.move_random_card(main_deck)
    
    for i in player.hand:
        gameplay_method.player_turn(player, i, main_deck)
            
    gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)
    
    for i in player.hand:
        gameplay_method.check_winner(player, i, dealer_hand)
        
    new_game_choice = gameplay_method.new_game(player, dealer)       
    # ask player if they want to keep playing | if yes, reset deck, hands, and bet(s) | else, return FALSE to break from loop
    if new_game_choice == "Y":
        continue
    else:
        break
print("Thank you for playing^_^!") 