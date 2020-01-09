def bet():
    while True:
        try:
            bet_amount = int(input ("please enter your bet in millions of dollars:"))
        except ValueError:
            print("integer please")
            continue
        if bet_amount <= 0 or bet_amount > 100:
            print("table limit is $1 - 100 million dollars")
            continue
        else:
            break    
    
    print("wtf")
    print(bet_amount)
    return bet_amount
    
