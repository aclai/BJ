# create object "card", which stores the index value of suit and number of cards. [x, y] x 1 - 4 for the 4 suits & y 1 - 13
import Card

# starting chips in millions of dollars
account_balance = 10000

# infinite loop until player answer "N" in newgame.py 
while True:
    
    # adding this layer to allow breaking as soon as someone bust without also eliminating the importution of "new_game.py"
    while True:
        # generate a list of a single deck of cards
        import deck
        deck = deck.create_deck()
        print (deck)
        
        # a list to save the dealer's hand
        dealerhand = []
        # a list to save the player's hand
        playerhand = []
        
        # ask player for bet amount
        import bet            
        bet_amount = bet.bet()
        
        print(account_balance)
        account_balance = account_balance + bet_amount
        print(account_balance)
        
        
        import deal_card
        # deal 1st card to player
        deal_card.deal_card(playerhand)
        # deal 1 card to dealer
        deal_card.dealcard(dealerhand)
        # deal 2nd card to player | import all outcomes and ask for player decision until playerbust or dealer's turn
        deal_card.dealcard(playerhand)

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