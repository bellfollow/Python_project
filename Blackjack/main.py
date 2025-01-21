from random import choice
import art
import random

#카드 뽑기
def card_choice(num,user_cards,user_cards_symbol):

    for i in range(num):
        user = random.choice(list(deck.keys()))
        user_card = random.choice(deck[user])
        user_cards_symbol.append(user)
        user_cards.append(user_card)
    return user_cards, user_cards_symbol



# def deck_choice():
#     user_cards = []
#     user_cards_symbol = []
#     dealer_cards = []
#     dealer_cards_symbol = []
#     used_cards = set()  # 중복 방지를 위한 집합
#
#     for i in range(2):
#         #딕셔너리에 각 키와 값을 저장
#         user = random.choice(list(deck.keys()))
#         user_card = random.choice(deck[user])
#         user_cards_symbol.append(user)
#         user_cards.append(user_card)
#
#         dealer = random.choice(list(deck.keys()))
#         dealer_card = random.choice(deck[dealer])
#         dealer_cards_symbol.append(dealer)
#         dealer_cards.append(dealer_card)
#     return user_cards,user_cards_symbol,dealer_cards, dealer_cards_symbol

print(art.logo)
print("\n"*20)

deck = {
    "ace":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "clobber":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "heart":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "diamond":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
}
while True:
    user_cards = []
    user_cards_symbol = []
    dealer_cards = []
    dealer_cards_symbol = []

    user_cards,user_cards_symbol = (card_choice(2,user_cards,user_cards_symbol))
    dealer_cards,dealer_cards_symbol = (card_choice(2,dealer_cards,dealer_cards_symbol))
    print("user_card :")
    for i in range(len(user_cards_symbol) - 1):
        print(f" {user_cards_symbol[i]} : {user_cards[i]}")
    print(f"dealer card : \n {dealer_cards_symbol[0]} : {dealer_cards[0]}")

    if sum(user_cards) > 21:
        print("Bust! You Draw")
        game_set = input("Try Again? or Stop?").lower()
        if game_set =="again":
            continue
        elif game_set == "stop":
            print("Thanks for Playing this game")
            break
    elif sum(user_cards) == 21:
        print("You Win!")
        game_set = input("Try Again? or Stop?").lower()
        continue
    else:
        hit_stand = input("Hit or Stand?").lower()
        if hit_stand == 'hit':
            print("User Say", """Hit!""")
            user_cards, user_cards_symbol = (card_choice(1,user_cards,user_cards_symbol))
            for i in range(len(user_cards_symbol) - 1):
                print(f" {user_cards_symbol[i]} : {user_cards[i]}")
            if sum(user_cards) > 21:
                print("You Draw")
                game_set = input("Try Again? or Stop?").lower()
                if game_set =="again":
                    continue
                elif game_set == "stop":
                    print("Thanks for Playing this game")
                    break
            else:
                if sum(dealer_cards) <= 16:
                    print("Dealer Say ","""Hit!""")
                    dealer_cards, dealer_cards_symbol = (card_choice(1, dealer_cards, dealer_cards_symbol))
                elif sum(dealer_cards) > 16:
                    print("Dealer Say", """Stand""")
                
                if sum(dealer_cards) > 21 or sum(user_cards) > sum(dealer_cards):
                    print("You win!")
                    game_set = input("Try Again? or Stop?").lower()
                elif sum(user_cards) < sum(dealer_cards):
                    print("Dealer wins!")
                    game_set = input("Try Again? or Stop?").lower()
                else:
                    print("user draw!")
                    game_set = input("Try Again? or Stop?").lower()
                if game_set =="again":
                    continue
                elif game_set == "stop":
                    print("Thanks for Playing this game")
                    break
                    
        