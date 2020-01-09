def newgame():
    deck.clear()
    dealerhand.clear()
    playerhand.clear()
    
    if bankroll < 100:
        answer = input("You only have $ " + bankroll + " million dollars left. Would you like to add fund to your bankroll? [Y/N]")
        if answer == "Y":
            import add_fund
        elif answer == "N":
            ?
        else:
            