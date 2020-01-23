#4 classes - card objects in deck objects, deck objects in user objects and dealer objects, plus a main_deck object
import card
import deck
import user
import dealer
#for drawing cards from main_deck
import random

#*****************************************************************************functions*****************************************************************************

#deal 1 card into deck objects (hand_name) in the form of user.hand.[i]   
#def move_random_card(hand_name):                           
#    random_card = random.choice(main_deck.deck)
#    #print(random_card)
#    main_deck.deck.remove(random_card)
#    #len(main_deck.deck)
#    hand_name.add_card([random_card])
#
#def player_turn(player, player_hand):
#    move_random_card(player_hand)
#    print(player_hand)
#    print(player_hand.deck)
#    print(player)
#    hand_value = calculate_hand(player, player_hand)
#    if len(player.hand) == 2:
#        #check bj
#        if hand_value == "bj":
#            pass
#        #check split        
#        #wrong here, elif will take player out of this condition without evaluating the possibililty to double down 
#        #if split is possible and player choose N
#        elif player_hand[0] == player_hand[1]:
#            split_decision()
#        #check double
#        elif hand_value == 19 or 20 and 1 in hand and hand_value == 19 or 20 or hand_value == 9 or 10:
#            double_decision()
#        else:
#            hit_decision(player_hand)
#    else:
#        hit_decision(player_hand)
#        
#def calculate_hand(owner, hand):
#    print(owner)
#    print(hand)
#    print(hand.deck.count)
#    if hand.deck.count == 2 and 1 in hand and 10 in hand or 11 in hand or 12 in hand or 13 in hand:
#        hand_value = "bj"
#    else:
#        hand_value = 0
#        for i in len(hand.deck):
#            hand_value = hand_value + hand.deck[i].card_num
#    if hand_value != "bj" and 1 in hand and points <= 11:
#        hand_value = hand_value + 10        
#        
#def compare_hand():
#    if player.hand_value == dealer.hand_point:
#        player.acct_balance = player.acct_balance + player.bet
#    elif player.hand_value == "bj":
#        player.acct_balance = player.acct_balance + player.bet*2.5
#    elif player.hand_value > dealer.hand_value:
#        player.acct_balance = player.acct_balance + player.bet*2
#    else:
#        pass
#        
#def new_game():
#    deck.clear()
#    dealerhand.clear()
#    playerhand.clear()
#    #ask player if they want to a new game
#            
#def hit_decision(hand):
#    user_choice = input("do you want an additional card?[Y/N]")
#    if user_choice == "Y":
#        move_random_card(player.hand[0])
#        hand_value = calculate_hand(player, hand)
#        print(hand_value)
#        if hand_value < 21:
#            hit_decision()
#        else:
#            pass               
#    elif user_choice == "N":
#        pass
#    else:
#        print("please answer [Y/N]")
#        hit_decision(hand)
#
#def split_decision():
#    user_choice = input("do you want to split?[Y/N]")
#    if user_choice == "Y":
#        removed_card = player.deck[0].remove_card(player)
#        player.deck[1].add_card(removed_card)
#        for i in num_of_hands:
#            deck.move_random_card(player.hand[i-1])
#            player_turn(player.hand[i-1])
#    elif user_choice == "N":
#        hit_decision()
#    else:
#        print("please answer [Y/N]")
#        split_decision()
#
#def double_decision():
#    user_choice = input("do you want to double down?[Y/N]")
#    if user_choice == "Y":
#        player.acct_balance = player.acct_balance - player.bet
#        player.bet = player.bet * 2
#        deck.move_random_card(player.hand)
#    elif user_choice == "N":
#        hit_decision()
#    else:
#        print("please answer [Y/N]")
#        double_decision()            
#           
#def dealer_turn():
#    dealer_hand = calculate_hand(dealer, hand)
#    if dealer_hand == "bj" or dealer_hand  > 17 or dealer_hand  == 17 and 1 not in hand:
#        pass
#    else:
#        dealer_turn()


#***********************************************************************program starts here***********************************************************************
player = player.Player()
#print(player)
player.input_name()
#print(player.name)
player.input_chip()
#print(player.acct_balance)
#print(player.bet)
#print(player.hand)
player.create_empty_hands()
#print(player.hand[0].deck)
#print(len(player.hand))
dealer = dealer.Dealer("bj")
dealer.create_empty_hand()
#print(dealer.game)
main_deck = deck.Deck("main_deck")
#print(main_deck)
#print(main_deck.id)
#print(main_deck.deck)
main_deck.create_full_deck()
#print(main_deck.deck)
#print(len(main_deck.deck))

player_hand_counter = 0
# infinite loop until player answer "N" in newgame.py 
while True:
    
    # adding this layer to allow breaking as soon as someone bust without also eliminating the import of "new_game.py"
    while True:
        # deal 1st card to player
        move_random_card(player.hand[0])
        #print(player.hand)
        #print(player.hand[0].deck[0][0].card_reader(player.hand[0].deck[0][0].suit, player.hand[0].deck[0][0].card_num))
        #print(player.hand[0].deck[0].card_num)
        # deal 1 card to dealer
        move_random_card(dealer.hand[0])
        #print(dealer.hand)
        #print(dealer.hand[0].deck[0][0].card_reader(dealer.hand[0].deck[0][0].suit, dealer.hand[0].deck[0][0].card_num))
        # deal 2nd card to player | import all outcomes and ask for player decision until playerbust or dealer's turn
        for i in player.hand:
            #print(i)
            #print(i.deck[0])
            #print(i.deck[0][0].card_num)
            hand_value = player_turn(i, main_deck)
            player.hand_value(hand_value)

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