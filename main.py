import random
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lists = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

game = True

user_ai = """


    _   ___          _           _ 
   /_\ |_ _| __ __ _(_)_ _  ___ | |
  / _ \ | |  \ V  V / | ' \(_-< |_|
 /_/ \_\___|  \_/\_/|_|_||_/__/ (_)
                                   


"""
user_one = """

  _   _               ___                    _           _ 
 | | | |______ _ _   / _ \ _ _  ___  __ __ _(_)_ _  ___ | |
 | |_| (_-< -_) '_| | (_) | ' \/ -_) \ V  V / | ' \(_-< |_|
  \___//__|___|_|    \___/|_||_\___|  \_/\_/|_|_||_/__/ (_)
                                                           


"""

user_two = """


  _   _              _____                     _           _ 
 | | | |______ _ _  |_   _|_ __ _____  __ __ _(_)_ _  ___ | |
 | |_| (_-< -_) '_|   | | \ V  V / _ \ \ V  V / | ' \(_-< |_|
  \___//__|___|_|     |_|  \_/\_/\___/  \_/\_/|_|_||_/__/ (_)
                                                             


"""

draw = """


  ___ _   _                _                   _ 
 |_ _| |_( )___  __ _   __| |_ _ __ ___ __ __ | |
  | ||  _|/(_-< / _` | / _` | '_/ _` \ V  V / |_|
 |___|\__| /__/ \__,_| \__,_|_| \__,_|\_/\_/  (_)
                                                 


"""


def ai_art(pos: int, user):
    global game
    game = False
    if user == 1:
        if lists[pos - 1] != 'O':
            lists[pos - 1] = 'X'

        else:
            new_pos = random.choice(list_of_numbers)
            print(f'AI chose {new_pos} instead')
            list_of_numbers.remove(new_pos)
            lists[new_pos - 1] = 'X'
    else:
        if lists[pos - 1] == 'O':
            new_pos = int(input(f'You already chose {pos}, pick again!\n'))
            lists[new_pos - 1] = 'O'
        elif lists[pos - 1] != 'X':
            lists[pos - 1] = 'O'
        else:
            new_pos = int(input("Space taken already!, Please pick another space.\n"))
            lists[new_pos - 1] = 'O'

    another = f"""
              |          |
         {lists[0]}    |    {lists[1]}     |   {lists[2]} 
    __________|__________|__________
              |          |
         {lists[3]}    |    {lists[4]}     |   {lists[5]}
    __________|__________|__________
              |          |
         {lists[6]}    |    {lists[7]}     |   {lists[8]}
              |          |

    """
    if lists[0] == "X" and lists[4] == "X" and lists[8] == "X":
        print(user_ai)
        game = True
    elif lists[0] == "O" and lists[4] == "O" and lists[8] == "O":
        print(user_two)
        game = True
    elif lists[2] == "X" and lists[5] == "X" and lists[8] == "X":
        print(user_ai)
        game = True
    elif lists[2] == "O" and lists[5] == "O" and lists[8] == "O":
        print(user_two)
        game = True
    elif lists[0] == "X" and lists[1] == "X" and lists[2] == "X":
        print(user_ai)
        game = True
    elif lists[0] == "O" and lists[1] == "O" and lists[2] == "O":
        print(user_two)
        game = True
    elif lists[3] == "X" and lists[4] == "X" and lists[5] == "X":
        print(user_ai)
        game = True
    elif lists[3] == "O" and lists[4] == "O" and lists[5] == "O":
        print(user_two)
        game = True
    elif lists[6] == "X" and lists[7] == "X" and lists[8] == "X":
        print(user_ai)
        game = True
    elif lists[6] == "O" and lists[7] == "O" and lists[8] == "O":
        print(user_two)
        game = True
    elif lists[0] == "X" and lists[3] == "X" and lists[6] == "X":
        print(user_ai)
        game = True
    elif lists[0] == "O" and lists[3] == "O" and lists[6] == "O":
        print(user_two)
        game = True
    elif lists[1] == "X" and lists[4] == "X" and lists[7] == "X":
        print(user_ai)
        game = True
    elif lists[1] == "O" and lists[4] == "O" and lists[7] == "O":
        print(user_two)
        game = True
    elif lists[2] == "X" and lists[4] == "X" and lists[6] == "X":
        print(user_ai)
        game = True
    elif lists[2] == "O" and lists[4] == "O" and lists[6] == "O":
        print(user_two)
        game = True
    else:
        if " " not in lists:
            print(draw)
            game = True
    print(another)
    return game


def art(pos: int, user):
    global game
    game = False
    if user == 1:
        if lists[pos - 1] == 'X':
            new_pos = int(input(f'You already chose {pos}, pick again!\n'))
            lists[new_pos - 1] = 'X'
        elif lists[pos - 1] != 'O':
            lists[pos - 1] = 'X'

        else:
            new_pos = int(input("Space taken already!, Please pick another space.\n"))
            lists[new_pos - 1] = 'X'
    else:
        if lists[pos - 1] == 'O':
            new_pos = int(input(f'You already chose {pos}, pick again!\n'))
            lists[new_pos - 1] = 'O'
        elif lists[pos - 1] != 'X':
            lists[pos - 1] = 'O'
        else:
            new_pos = int(input("Space taken already!, Please pick another space.\n"))
            lists[new_pos - 1] = 'O'

    another = f"""
              |          |
         {lists[0]}    |    {lists[1]}     |   {lists[2]} 
    __________|__________|__________
              |          |
         {lists[3]}    |    {lists[4]}     |   {lists[5]}
    __________|__________|__________
              |          |
         {lists[6]}    |    {lists[7]}     |   {lists[8]}
              |          |

    """
    if lists[0] == "X" and lists[4] == "X" and lists[8] == "X":
        print(user_one)
        game = True
    elif lists[0] == "O" and lists[4] == "O" and lists[8] == "O":
        print(user_two)
        game = True
    elif lists[2] == "X" and lists[5] == "X" and lists[8] == "X":
        print(user_one)
        game = True
    elif lists[2] == "O" and lists[5] == "O" and lists[8] == "O":
        print(user_two)
        game = True
    elif lists[0] == "X" and lists[1] == "X" and lists[2] == "X":
        print(user_one)
        game = True
    elif lists[0] == "O" and lists[1] == "O" and lists[2] == "O":
        print(user_two)
        game = True
    elif lists[3] == "X" and lists[4] == "X" and lists[5] == "X":
        print(user_one)
        game = True
    elif lists[3] == "O" and lists[4] == "O" and lists[5] == "O":
        print(user_two)
        game = True
    elif lists[6] == "X" and lists[7] == "X" and lists[8] == "X":
        print(user_one)
        game = True
    elif lists[6] == "O" and lists[7] == "O" and lists[8] == "O":
        print(user_two)
        game = True
    elif lists[0] == "X" and lists[3] == "X" and lists[6] == "X":
        print(user_one)
        game = True
    elif lists[0] == "O" and lists[3] == "O" and lists[6] == "O":
        print(user_two)
        game = True
    elif lists[1] == "X" and lists[4] == "X" and lists[7] == "X":
        print(user_one)
        game = True
    elif lists[1] == "O" and lists[4] == "O" and lists[7] == "O":
        print(user_two)
        game = True
    elif lists[2] == "X" and lists[4] == "X" and lists[6] == "X":
        print(user_one)
        game = True
    elif lists[2] == "O" and lists[4] == "O" and lists[6] == "O":
        print(user_two)
        game = True
    else:
        if " " not in lists:
            print(draw)
            game = True
    print(another)
    return game


description = """
 __      __   _                    _         _   _          _____ _      _____          _____            ___                
 \ \    / /__| |__ ___ _ __  ___  | |_ ___  | |_| |_  ___  |_   _(_)__  |_   _|_ _ __  |_   _|__  ___   / __|__ _ _ __  ___ 
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ |  _| ' \/ -_)   | | | / _|   | |/ _` / _|   | |/ _ \/ -_) | (_ / _` | '  \/ -_)
   \_/\_/\___|_\__\___/_|_|_\___|  \__\___/  \__|_||_\___|   |_| |_\__|   |_|\__,_\__|   |_|\___/\___|  \___\__,_|_|_|_\___|
                                                                                                                            
"""
logo = f"""
                      |          |
                      |          |
            __________|__________|__________
                      |          |
                      |          | 
            __________|__________|__________
                      |          |
                      |          |
                      |          |

            """
print(description)
print(logo)
ai_mode = True
while ai_mode:
    ai = input('Do you want to play with AI? Yes or No\n').title()
    if ai == 'Yes':
        game_is_on = True
        while game_is_on:
            rand_num = random.choice(list_of_numbers)
            print(f'AI chose {rand_num}')
            list_of_numbers.remove(rand_num)
            if ai_art(pos=rand_num, user=1):
                game_is_on = False
                ai_mode = False
            else:
                game_is_on = True
                user2_input = int(input("User 2, What position? 1-9\n"))
                if user2_input > 9 or user2_input < 1:
                    print('Pick a number between 1 and 9')
                    user2_input = int(input("User 2, What position? 1-9\n"))
                    if ai_art(pos=user2_input, user=2):
                        game_is_on = False
                        ai_mode = False
                    else:
                        game_is_on = True
                else:
                    game_is_on = True
                    if ai_art(pos=user2_input, user=2):
                        game_is_on = False
                        ai_mode = False
                    else:
                        game_is_on = True
    elif ai == 'No':
        game_is_on = True
        while game_is_on:
            user1_input = int(input("User 1, What position? 1-9\n"))
            if user1_input > 9 or user1_input < 1:
                print('Pick a number between 1 and 9')
                user1_input = int(input("User 1, What position? 1-9\n"))
                if art(pos=user1_input, user=1):
                    game_is_on = False
                    ai_mode = False
                else:
                    game_is_on = True
                    user2_input = int(input("User 2, What position? 1-9\n"))
                    if user2_input > 9 or user2_input < 1:
                        print('Pick a number between 1 and 9')
                        user2_input = int(input("User 2, What position? 1-9\n"))
                        if art(pos=user2_input, user=2):
                            game_is_on = False
                            ai_mode = False
                        else:
                            game_is_on = True
                    else:
                        game_is_on = True
                        if art(pos=user2_input, user=2):
                            game_is_on = False
                            ai_mode = False
                        else:
                            game_is_on = True
            else:
                if art(pos=user1_input, user=1):
                    game_is_on = False
                    ai_mode = False
                else:
                    game_is_on = True
                    user2_input = int(input("User 2, What position? 1-9\n"))
                    if user2_input > 9 or user2_input < 1:
                        print('Pick a number between 1 and 9')
                        user2_input = int(input("User 2, What position? 1-9\n"))
                        if art(pos=user2_input, user=2):
                            game_is_on = False
                            ai_mode = False
                        else:
                            game_is_on = True
                    else:
                        game_is_on = True
                        if art(pos=user2_input, user=2):
                            game_is_on = False
                            ai_mode = False
                        else:
                            game_is_on = True

    else:
        print('Please input "Yes" or "No"')
