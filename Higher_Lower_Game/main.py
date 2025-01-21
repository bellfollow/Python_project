import art
import game_data
import random

print(art.logo)

print("\n" * 5)
score = 0 

while True:
    result = ''
    random_a = random.randrange(0,50)
    print(f"Compare A: {game_data.data[random_a]["name"]} {game_data.data[random_a]["description"]} from {game_data.data[random_a]["country"]}" )
    a_follower = game_data.data[random_a]["follower_count"]
    
    print(art.vs)

    random_b = random.randrange(0,50)
    b_follower = game_data.data[random_b]["follower_count"]
    
    print(f"Against A: {game_data.data[random_b]["name"]} {game_data.data[random_b]["description"]} from {game_data.data[random_b]["country"]}" )
    
    if random_a > random_b:
        result = 'a'
    else:
        result = 'b'
    
    who_more = input("Who has more followers? Type 'A' or 'B' ").lower()
    if who_more == result:
        score += 1
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        break
