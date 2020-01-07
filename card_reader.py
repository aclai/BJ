def card_reader(suit, card_num):
    eng_suit = ["Diamond", "Club", "Heart", "Spade"]
    eng_num = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
    print (card_num)
    print (suit)
    
    print (eng_num[card_num])
    print (eng_suit[suit])
    print (str(eng_num[card_num]) + " of " + eng_suit[suit])