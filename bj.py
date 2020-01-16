# create object "card", which stores the index value of suit and number of cards. [x, y] x 1 - 4 for the 4 suits & y 1 - 13
import card
import deck
import user
import dealer
import gameplay_method

player = user.User()
print(player)
player.input_name()
print(player.name)
player.input_chip()
print(player.acct_balance)
print(player.bet)
print(player.hand)
player.create_empty_hands()
print(player.hand[1].deck)
print(len(player.hand))
dealer = dealer.Dealer("bj")
dealer.create-empty_hand()
print(dealer.game)
main_deck = deck.Deck("main_deck")
print(main_deck.id)
print(main_deck.deck)
main_deck.create_full_deck()
print(main_deck.deck)
print(len(main_deck.deck))

player_hand_counter = 0
# infinite loop until player answer "N" in newgame.py 
while True:
    
    # adding this layer to allow breaking as soon as someone bust without also eliminating the import of "new_game.py"
    while True:
        # deal 1st card to player
        player.hand[1].deal_card()
        # deal 1 card to dealer
        dealer.hand[1].deal_card()
        # deal 2nd card to player | import all outcomes and ask for player decision until playerbust or dealer's turn
        for i in player.hand:
            gameplay_method.player_turn()

        if playerbust == True:
            break
            
        import deal_dealer
        
        if dealerbust == True:
            break
        
        import check_winner
        break
            
    # ask player if they want to keep playing | if yes, reset deck, hands, and bet(s) | else, return FALSE to break from loop
    import new_game
    if newgame == FALSE:
        break
print("Thank you for playing^_^!") 