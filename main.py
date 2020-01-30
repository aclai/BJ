"""
This is the main game. Run this file to play the game
"""
import card             
import deck            
import person         
import dealer          
import player          
import gameplay_method

"""
Create player and ask for name and buy in amount
"""
player = player.Player()
player.input_name()
print("Hi, " + player.name)
player.input_chip()
print("Your bankroll is $ " + str(player.acct_balance))

dealer = dealer.Dealer("bj")

"""
Loop until player chooice, "N", not to have another game
"""
while True:
    """
    Ask player to bet, reduce the amount from player's bankroll, and save the amount in player.bet
    """
    player.input_bet()
    print("you bet $" + str(player.bet))
    
    """
    Create an empty deck and put 52 unique cards in it
    """
    main_deck = deck.Deck()
    main_deck.create_full_deck()
    
    """
    Create an empty deck and save it in dealer object
    """
    dealer_hand = deck.Deck()
    dealer.add_deck(dealer_hand)
    
    """
    Create an empty deck and save it in player object
    """
    player_hand = deck.Deck()
    player.add_deck(player_hand)
    
    """
    Remove a random card from main_deck and append into player_hand, and then the same to dealer_hand
    """
    player_hand.move_random_card(main_deck)
    print("Your first card is " + player_hand[0].card_eng_name)
    dealer_hand.move_random_card(main_deck)
    print("The dealer's first card is " + dealer_hand[0].card_eng_name)
    
    """
    Loop through player's hand and have player make decisions. There is only 1 hand atm, more hands may
    be created and appended during player_turn if player split his current hand
    """
    for i in player.hand:
        gameplay_method.player_turn(player, i, main_deck)
    
    """
    No cards will be dealt if player's hand is bursted. Loop through player.hand in case player's 1st hand bursted
    while 2nd hand did not
    """
    for i in player.hand:
        gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)
        
    """
    Loop through player.hand and compare each hand to dealer_hand to determine payout and adjust player's bankroll accordingly
    """
    for i in player.hand:
        gameplay_method.check_winner(player, i, dealer_hand)

    """
    Ask if player want another game. If "Y" let while loop continue, if "N", game will end
    Note that user_choice return either "Y" or "N" and filtered out all other input
    """
    new_game_choice = gameplay_method.user_choice("do you want another game?[Y/N]")       
    # ask player if they want to keep playing | if yes, reset deck, hands, and bet(s) | else, return FALSE to break from loop
    if new_game_choice == "Y":
        gameplay_method.new_game(new_game_choice, player, dealer)
        continue
    else:
        break
print("Thank you for playing^_^!") 