# create an object "player", which stores the name, bankroll, hand(s), and bet(s) of the player.
import Player

# infinite loop until player answer "N" in newgame.py 
while TRUE:
    
    # adding this layer to allow breaking as soon as someone bust without also eliminating the importution of "new_game.py"
    while TRUE:
        # generate a list of a single deck of cards
        import deck
        
        # a list to save the dealer's hand
        dealerhand = []
        
        # ask player for bet amount
        import bet
        
        # deal 1st card to player
        import deal_player
        # deal 1 card to dealer
        import deal_dealer
        # deal 2nd card to player | importute all outcomes and ask for player decision until playerbust or dealer's turn
        import deal_player

        if playerbust == TRUE:
            break
            
        import deal_dealer
        
        if dealerbust == TRUE:
            break
        
        import check_winner
  
    # ask player if they want to keep playing | if yes, reset deck, hands, and bet(s) | else, return FALSE to break from loop
    import new_game
    if newgame == FALSE:
        break
print("Thank you for playing^_^!")