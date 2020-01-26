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
print("Hi, " + player.name)
player.input_chip()
print("Your bankroll is $ " + str(player.acct_balance))

dealer = dealer.Dealer("bj")

while True:
    player.input_bet()
    print("you bet $" + str(player.bet))
    
    main_deck = deck.Deck()
    main_deck.create_full_deck()
    
    dealer_hand = deck.Deck()
    dealer.add_deck(dealer_hand)
    
    player_hand = deck.Deck()
    player.add_deck(player_hand)
    
    player_hand.move_random_card(main_deck)
    print("Your first card is " + player_hand[0].card_eng_name)
    dealer_hand.move_random_card(main_deck)
    print("The dealer's first card is " + dealer_hand[0].card_eng_name)
    
    for i in player.hand:
        gameplay_method.player_turn(player, i, main_deck)
            
    for i in player.hand:
        gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)
    
    for i in player.hand:
        gameplay_method.check_winner(player, i, dealer_hand)
        
    new_game_choice = gameplay_method.user_choice("do you want another game?[Y/N]")       
    # ask player if they want to keep playing | if yes, reset deck, hands, and bet(s) | else, return FALSE to break from loop
    if new_game_choice == "Y":
        gameplay_method.new_game(new_game_choice, player, dealer)
        continue
    else:
        break
print("Thank you for playing^_^!") 