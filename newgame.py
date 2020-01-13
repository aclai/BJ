def newgame():
    deck.clear()
    dealerhand.clear()
    playerhand.clear()
    
    if account_balance < 800:
        answer = input("You only have $ " + account_balance + " million dollars left. Would you like to add fund to your account_balance? [Y/N]")
        if answer == "Y":
            import add_fund
        elif answer == "N":
            ?
        else:
            
            