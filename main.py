import random
from time import sleep

options = ('rock','paper','scissor')
player_score = 0
pc_score = 0

emojis = ['😏' , '🧐' , '😎' , '🤫' , '😂' , '👻' , '🤨' , '😘']

print()
print(f"---- Welcome {random.choice(emojis)}----")
sleep(0.8)


max_score = int(input("Enter maximum score (1 to 10) : "))
if max_score > 10:
    print("Looks like you set maximum score more 10 ")
    print("Setting maximum score to 10")
    max_score = 10

while True:
    user_input = input("Enter rock/paper/scissor : ").lower()
    while user_input not in options:
        print("Invalid input, please choose 'rock', 'paper', or 'scissor'.")
        user_input = input("Enter rock/paper/scissor : ").lower()

    pc_input = random.choice(options)
    print(f"PC's chose : {pc_input}")

    if user_input == pc_input:
        print("It's a tie 🙁")

    elif (user_input == 'rock' and pc_input == 'scissor') or \
         (user_input == 'paper' and pc_input == 'rock') or \
         (user_input == 'scissor' and pc_input == 'paper'):
        player_score = player_score + 1

    else:
        pc_score = pc_score + 1

    if player_score == max_score or pc_score == max_score:
        print()
        print('----- Game Over ----')
        print(f'your score {random.choice(emojis)}: {player_score}')
        print(f"PC's score {random.choice(emojis)}: {pc_score}")
        print("--------------------")
        break

sleep(1)
if(player_score == max_score):
    print(f'You won {random.choice(emojis)}')
else:
    print(f'PC won {random.choice(emojis)}')
    print('Better luck next time........')
