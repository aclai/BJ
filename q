[1mdiff --git a/project_design b/.project_design.txt[m
[1msimilarity index 100%[m
[1mrename from project_design[m
[1mrename to .project_design.txt[m
[1mdiff --git a/.user.py b/.user.py[m
[1mdeleted file mode 100644[m
[1mindex bcc2b66..0000000[m
[1m--- a/.user.py[m
[1m+++ /dev/null[m
[36m@@ -1,77 +0,0 @@[m
[31m-import deck[m
[31m-[m
[31m-class User:[m
[31m-    #done[m
[31m-    def __init__(self, version=1, user_id=1):[m
[31m-        self.version = version[m
[31m-        self.user_id = user_id[m
[31m-        self.name = ""[m
[31m-        self.password = ""[m
[31m-        self.acct_balance = 0[m
[31m-        self.bet = 0[m
[31m-        self.hand = [][m
[31m-        self.hand_value = [][m
[31m-    [m
[31m-    #done[m
[31m-    def input_name(self):[m
[31m-        self.name = input("Please enter your name:")[m
[31m-[m
[31m-    def input_bet(self):[m
[31m-        while True:[m
[31m-            try:[m
[31m-                bet_amount = int(input ("please enter your bet in millions of dollars:"))[m
[31m-            except ValueError:[m
[31m-                print("integer please")[m
[31m-                continue[m
[31m-            if bet_amount <= 0 or bet_amount > 100:[m
[31m-                print("table limit is $1 - 100 million dollars")[m
[31m-                continue[m
[31m-            elif bet_amount > acct_balance:[m
[31m-                print("insufficinet funds")[m
[31m-                add_fund[m
[31m-                continue[m
[31m-            else:[m
[31m-                break    [m
[31m-        self.bet = bet_amount[m
[31m-        bet_amount = bet_amount*(-1)[m
[31m-        add_fund(bet_amount)       [m
[31m-        [m
[31m-    def hand_value(self, value):[m
[31m-        self.hand_value.append(value)[m
[31m-    [m
[31m-    #done[m
[31m-    def input_chip(self):[m
[31m-        while True:[m
[31m-            try:[m
[31m-                input_chip = int(input ("please enter the number of chips in millions of dollars you would like to buy:"))[m
[31m-            except ValueError:[m
[31m-                print("integer please")[m
[31m-                continue[m
[31m-            if input_chip <= 1000:[m
[31m-                print("the minimum you can buy is 1 billion / 1000 1-million-dollar chips")[m
[31m-                continue[m
[31m-            else:[m
[31m-                self.acct_balance = self.acct_balance + input_chip[m
[31m-                break[m
[31m-    #done        [m
[31m-    def create_empty_hands(self):[m
[31m-        for i in [1,2,3,4]:[m
[31m-            self.hand.append(deck.Deck("player_hand_" + str(i)))[m
[31m-            [m
[31m-    [m
[31m-    [m
[31m-    #later when branch off blackjack and become universal & save user[m
[31m-    #def change_version(self, version_num):[m
[31m-    #def add_attribute(self, attribute_name):[m
[31m-    #def disable_attribute(self, attribute_name):[m
[31m-    #def enable_attribute(self, attribute_name):[m
[31m-    #def change_name(self, new_name):[m
[31m-    #def change_password(self, new_password):[m
[31m-    [m
[31m-    [m
[31m-    [m
[31m-        [m
[31m-[m
[31m-    [m
[31m-    [m
[31m-[m
[1mdiff --git a/README.MD b/README.MD[m
[1mindex 0b33de9..d902b8e 100644[m
[1m--- a/README.MD[m
[1m+++ b/README.MD[m
[36m@@ -1,8 +1,8 @@[m
[31m-Written in Python 3.7.5[m
[32m+[m[32m*Written in Python 3.7.5*[m[41m[m
 [m
[31m-Blackjack [m
[32m+[m[32m**Blackjack**[m[41m[m
 [m
[31m-Rules:[m
[32m+[m[32m#Rules:[m[41m[m
 1 deck[m
 1 player[m
 Shuffle after every game[m
[36m@@ -11,45 +11,45 @@[m [mUnlimited split within 1 deck[m
 Double on hard 10/11[m
 Dealer stops at hard 17[m
 [m
[31m-Instruction:[m
[32m+[m[32m#Instruction:[m[41m[m
 Run main.py with Python[m
 [m
[31m-Game-play: [m
[31m-Enter your preferred name[m
[31m-Enter the amount of chips in millions of dollars you would like to buy (1 = 1 million dollars) and you have to at least buy 1000 (only accept integers)[m
[31m-Place your bet (min = 1, max = 100) (only accept integers)[m
[32m+[m[32m#Game-play:[m[41m [m
[32m+[m[32m1. Enter your preferred name[m[41m[m
[32m+[m[32m2. Enter the amount of chips in millions of dollars you would like to buy (1 = 1 million dollars) and you have to at least buy 1000 (only accept integers)[m[41m[m
[32m+[m[32m3. Place your bet (min = 1, max = 100) (only accept integers)[m[41m[m
 [m
[31m-*The game will deal you 2 and the deal 1 card alternatively[m
[32m+[m[32m*-->The game will deal you 2 and the dealer 1 card alternatively[m[41m[m
 [m
[31m-Player Decision Phrase - A (PDPA)[m
[31m-The game will print your hand and its points[m
[31m-If you get a bj, the game will not ask for your decision[m
[32m+[m[32m4. Player Decision Phrase - A (PDPA)[m[41m[m
[32m+[m	[32mThe game will print your hand and its points[m[41m[m
[32m+[m	[32mIf you get a bj, the game will not ask for your decision[m[41m[m
 [m
[31m-Else, if your two cards are of equal points, the game will ask if you want to split (only accept "Y" as yes or "N" as no, without the quotation marks)[m
[31m-	if you choose to split, it will split your 2 cards into 2 seperate hands, deal you 1 card for your first hand and start at the PDPA[m
[31m-	until you finish both PDPA and PDPB for your first hand, and then move on to your second hand. (Same process applies to further spliting)[m
[32m+[m	[32mElse, if your two cards are of equal points, the game will ask if you want to split (only accept "Y" as yes or "N" as no, without the quotation marks)[m[41m[m
[32m+[m		[32mif you choose to split, it will split your 2 cards into 2 seperate hands, deal you 1 card for your first hand and start at the PDPA[m[41m[m
[32m+[m		[32muntil you finish both PDPA and PDPB for your first hand, and then move on to your second hand. (Same process applies to further spliting)[m[41m[m
 	[m
[31m-	if you choose not to split, it will continue to check if you are allowed to double down[m
[32m+[m		[32mif you choose not to split, it will continue to check if you are allowed to double down[m[41m[m
 [m
[31m-Else, if your hand has a hard 9 or hard 10 points, the game will ask if you want to double down (only accept "Y" as yes or "N" as no, without the quotation marks)[m
[31m-	if you choose to double down, it will deal you an additional card and double your bet amount, and you will skip PDPB[m
[32m+[m	[32mElse, if your hand has a hard 9 or hard 10 points, the game will ask if you want to double down (only accept "Y" as yes or "N" as no, without the quotation marks)[m[41m[m
[32m+[m		[32mif you choose to double down, it will deal you an additional card and double your bet amount, and you will skip PDPB[m[41m[m
 	[m
[31m-	if you choose not to double down, it will continue to take you to PDPB[m
[32m+[m		[32mif you choose not to double down, it will continue to take you to PDPB[m[41m[m
 [m
[31m-Player Decision Phrase - B (PDPB)[m
[31m-The game will ask if you want to hit another card[m
[31m-	if you choose to have another card, the game will deal you an additional card[m
[31m-	it will check and display your new hand and its points[m
[32m+[m[32m5. Player Decision Phrase - B (PDPB)[m[41m[m
[32m+[m	[32mThe game will ask if you want to hit another card for your hand(s)[m[41m[m
[32m+[m		[32mif you choose to have another card, the game will deal you an additional card[m[41m[m
[32m+[m		[32mit will check and display your new hand and its points[m[41m[m
 	[m
[31m-	if your hand has greater than 21 (burst) you will be taken to the reset phrase[m
[31m-	else it will go through PDPB again, until you choose not to have another card, reach 21 points, or burst[m
[32m+[m		[32mif your hand has greater than 21 (burst) you will be taken to the reset phrase[m[41m[m
[32m+[m		[32melse it will go through PDPB again, until you choose not to have another card, reach 21 points, or burst[m[41m[m
 	[m
[31m-The game will now complete and display the outcome[m
[32m+[m[32m6. The game will now complete and display the outcome[m[41m[m
 [m
[31m-The game will ask if you want another bj(only accept "Y" as yes or "N" as no, without the quotation marks)[m
[31m-	if you choose to have another bj, the game will start at *[m
[32m+[m[32m7. The game will ask if you want another bj(only accept "Y" as yes or "N" as no, without the quotation marks)[m[41m[m
[32m+[m		[32mif you choose to have another bj, the game will start at *-->[m[41m[m
 	[m
[31m-	if you choose not to have another bj, the game will end[m
[32m+[m		[32mif you choose not to have another bj, the game will end[m[41m[m
 	[m
 [m
 [m
[1mdiff --git a/dealer_turn_test.py b/dealer_turn_test.py[m
[1mdeleted file mode 100644[m
[1mindex 392f5d1..0000000[m
[1m--- a/dealer_turn_test.py[m
[1m+++ /dev/null[m
[36m@@ -1,32 +0,0 @@[m
[31m-import deck[m
[31m-import gameplay_method[m
[31m-import card[m
[31m-import random[m
[31m-[m
[31m-main_deck = deck.Deck()[m
[31m-    [m
[31m-while True:[m
[31m-    try:            [m
[31m-        player_hand = deck.Deck()[m
[31m-        dealer_hand = deck.Deck()[m
[31m-        [m
[31m-        for y in range(0, 10):[m
[31m-            card_point = [1,2,3,4,5,6,7,8,9,10][m
[31m-            card_eng_name = main_deck.card_reader(0, y)[m
[31m-            main_deck.add_card(card.Card(1, y+1, card_point[y], card_eng_name))[m
[31m-        [m
[31m-        random_card_1 = random.choice(main_deck)[m
[31m-        random_card_2 = random.choice(main_deck)[m
[31m-        random_card_3 = random.choice(main_deck)[m
[31m-        random_card_4 = random.choice(main_deck)[m
[31m-        print("wtf")[m
[31m-        player_hand.append(random_card_1)[m
[31m-        player_hand.append(random_card_2)[m
[31m-        [m
[31m-        dealer_hand.append(random_card_3)[m
[31m-        dealer_hand.append(random_card_4)[m
[31m-        [m
[31m-        gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)[m
[31m-    [m
[31m-    except:[m
[31m-        break[m
\ No newline at end of file[m
[1mdiff --git a/function_test.py b/function_test.py[m
[1mnew file mode 100644[m
[1mindex 0000000..aff82cf[m
[1m--- /dev/null[m
[1m+++ b/function_test.py[m
[36m@@ -0,0 +1,46 @@[m
[32m+[m[32mimport deck[m[41m[m
[32m+[m[32mimport gameplay_method[m[41m[m
[32m+[m[32mimport card[m[41m[m
[32m+[m[32mimport random[m[41m[m
[32m+[m[32mimport player[m[41m[m
[32m+[m[41m[m
[32m+[m[32mmain_deck = deck.Deck()[m[41m[m
[32m+[m[32mplayer = player.Player()[m[41m[m
[32m+[m[32mplayer.bet = 100[m[41m[m
[32m+[m[41m[m
[32m+[m[32mwhile True:[m[41m[m
[32m+[m[32m    player_hand = deck.Deck()[m[41m[m
[32m+[m[32m    dealer_hand = deck.Deck()[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    for y in range(0, 10):[m[41m[m
[32m+[m[32m        card_point = [1,2,3,4,5,6,7,8,9,10][m[41m[m
[32m+[m[32m        card_eng_name = main_deck.card_reader(0, y)[m[41m[m
[32m+[m[32m        main_deck.add_card(card.Card(1, y+1, card_point[y], card_eng_name))[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    random_card_1 = random.choice(main_deck)[m[41m[m
[32m+[m[32m    random_card_2 = random.choice(main_deck)[m[41m[m
[32m+[m[32m    random_card_3 = random.choice(main_deck)[m[41m[m
[32m+[m[32m    random_card_4 = random.choice(main_deck)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    player_hand.append(random_card_1)[m[41m[m
[32m+[m[32m    player_hand.append(random_card_2)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    dealer_hand.append(random_card_3)[m[41m[m
[32m+[m[32m    dealer_hand.append(random_card_4)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    #gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    #dealer_point = gameplay_method.calculate_hand(dealer_hand)[m[41m[m
[32m+[m[32m    #dealer_hand.hand_reader()[m[41m[m
[32m+[m[32m    #print(dealer_point)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    #gameplay_method.check_winner(player, player_hand, dealer_hand)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    gameplay_method.hit_decision("Y", player, player_hand, main_deck)[m[41m[m
[32m+[m[32m    print(len(player_hand))[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m    #gameplay_method.[m[41m[m
[32m+[m[32m    #gameplay_method.[m[41m[m
[32m+[m[32m    #gameplay_method.[m[41m[m
[32m+[m[32m    #gameplay_method.[m[41m[m
[32m+[m[41m    [m
[1mdiff --git a/gameplay_method.py b/gameplay_method.py[m
[1mindex cf9dac1..baec13d 100644[m
[1m--- a/gameplay_method.py[m
[1m+++ b/gameplay_method.py[m
[36m@@ -67,7 +67,7 @@[m [mdef check_winner(player, player_hand, dealer_hand):[m
         else:[m
             payout = 2.5[m
             outcome = "you won 1.5x with a bj"[m
[31m-    elif player_point > 21:[m
[32m+[m[32m    elif player_point > 21 or dealer_point == "bj":[m[41m[m
         payout = 0[m
         outcome = "you lose"[m
     elif player_point == dealer_point:[m
[36m@@ -82,7 +82,8 @@[m [mdef check_winner(player, player_hand, dealer_hand):[m
     if player_hand.double == True:[m
         payout = payout * 2[m
     print(outcome)[m
[31m-    player.acct_balance = player.acct_balance + player.bet * payout[m
[32m+[m[32m    adjust_fund = player.bet * payout[m[41m[m
[32m+[m[32m    player.adjust_fund(adjust_fund)[m[41m[m
     print("your bankroll is now " + str(player.acct_balance))[m
         [m
 def new_game(user_answer, player, dealer):[m
