import random

name = input('Enter your name: ')

print("Hello, " + name)

choose_option = input().split(",")

print(choose_option)

game_options = []
game_dictionary = {}

rock_dictionary = {'rock' : ['sponge' ,'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']}
gun_dictionary = {'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock']}
lightning_dictionary = {'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']}
devil_dictionary = {'devil': ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning']}
dragon_dictionary = {'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil']}
water_dictionary = {'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon']}
air_dictionary = {'air': ['fire','rock', 'gun', 'lightning', 'devil', 'dragon', 'water']}
paper_dictionary = {'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air']}
sponge_dictionary = {'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper']}
wolf_dictionary = {'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge']}
tree_dictionary = {'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf']}
human_dictionary = {'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree']}
snake_dictionary = {'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human']}
scissors_dictionary = {'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake']}
fire_dictionary = {'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors']}

for i in choose_option:
    if choose_option == ['']:
        game_options = ['paper', 'scissors', 'rock']
        game_dictionary = {'rock' : 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    else:
        if i == "rock":
            game_options.append(i)
            game_dictionary.update(rock_dictionary)
        elif i == "gun":
            game_options.append(i)
            game_dictionary.update(gun_dictionary)
        elif i == "lightning":
            game_options.append(i)
            game_dictionary.update(lightning_dictionary)
        elif i == "devil":
            game_options.append(i)
            game_dictionary.update(devil_dictionary)
        elif i == "dragon":
            game_options.append(i)
            game_dictionary.update(dragon_dictionary)
        elif i == "water":
            game_options.append(i)
            game_dictionary.update(water_dictionary)
        elif i == "air":
            game_options.append(i)
            game_dictionary.update(air_dictionary)
        elif i == "paper":
            game_options.append(i)
            game_dictionary.update(paper_dictionary)
        elif i == "sponge":
            game_options.append(i)
            game_dictionary.update(sponge_dictionary)
        elif i == "wolf":
            game_options.append(i)
            game_dictionary.update(wolf_dictionary)
        elif i == "tree":
            game_options.append(i)
            game_dictionary.update(tree_dictionary)
        elif i == "human":
            game_options.append(i)
            game_dictionary.update(human_dictionary)
        elif i == "snake":
            game_options.append(i)
            game_dictionary.update(snake_dictionary)
        elif i == "scissors":
            game_options.append(i)
            game_dictionary.update(scissors_dictionary)
        elif i == "fire":
            game_options.append(i)
            game_dictionary.update(fire_dictionary)
        else:
            pass

print(game_options)
print(game_dictionary)
print("Okay, let's start")

while True:
    user_option = input()
    computer_option = random.choice(game_options)
    if user_option != computer_option:
        if user_option not in game_options:
            if user_option == "!exit":
                print("Bye!")
                break
            else:
                print("Invalid input")
                continue
        else:
            if computer_option in game_dictionary.get(user_option) and user_option in game_options:
                print(f'Well done. The computer chose {computer_option} and failed')
                continue
            elif computer_option not in game_dictionary.get(user_option) and user_option in game_options:
                print(f'Sorry, but the computer chose {computer_option}')
                continue
            else:
                pass
                continue

    elif user_option == computer_option:
        print(f"There is a draw {computer_option}")
        continue

    else:
        pass
        continue