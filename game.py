import sys
import os
import random
from sty import fg, rs

def play():
    arts = {
            'r': 
            '''
                _______
            ---'   ____)
                (_____)
                (_____)
                (____)
            ---.__(___)
            ''', 
            'p':
            '''
                _______
            ---'    ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            ''',
            's':
            '''
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
            '''}

    signs = ['rock', 'paper', 'scissors']
    matches = 0
    wins = 0 
    losts = 0 
    draws = 0
    rounds = 0
    already = -1

    print(fg(128,0,0) + "Hello my friend, welcome to rock-paper-scissors game!\n" + fg.rs)

    while True:
        ask = input("Please choose your tool!\n 1: Rock\n 2: Paper\n 3: Scissors\n Number of your choice: ")
        print(chr(27) + "[2J")
        
        def statics(used):
            return fg(255,127,80) + '\nYour statics: ' + str(matches - used) + ' matches, ' + str(wins) + ' wins, ' + str(draws) + ' draws, ' + str(losts) + ' losts\n' + fg.rs

        if ask == 'statics' and matches >= 1:
            rounds -= 1 
            already += 1
            print(statics(already))

        if ask == 'quit':
            print(statics(already + 1))
            print('Hope to see you soon!')
            sys.exit()

        if (ask.isdigit() and int(ask) <= 3 and int(ask) > 0) or ask == "statics":
            matches += 1
            rounds += 1
            if ask != "statics":
                print(fg(0,191,255) + "\nRound " + str(rounds) + fg.rs)

            if ask == '1':
                cpu = random.choice(signs)
                if cpu == 'rock':
                    print(fg(255, 255, 10) + 'rock <> rock'+ fg.rs)
                    print(fg(139,69,19) + "It is a draw\n"+ fg.rs)
                    draws += 1
                elif cpu == 'paper':
                    print(fg(255, 255, 10) + 'rock <> paper'+ fg.rs)
                    print(fg(255, 10, 10) + 'Paper beats rock, so you lost :(\n'+ fg.rs)
                    losts += 1  
                elif cpu == 'scissors':
                    print(fg(255, 255, 10) + 'rock <> scissors')
                    print(fg(10, 255, 10) + "Scissors lost against rock, so you won :)\n"+ fg.rs)
                    wins += 1
                else:
                    print("Please give me a valid name!\n")

            elif ask == '2':
                cpu = random.choice(signs)
                if cpu == 'rock':
                    print(fg(255, 255, 10) + 'paper <> rock'+ fg.rs)
                    print(fg(10, 255, 10) + "Paper beats rock, so you won :)\n"+ fg.rs)
                    wins += 1
                elif cpu == 'paper':
                    print(fg(255, 255, 10) + 'paper <> paper'+ fg.rs)
                    print(fg(139,69,19) + 'It is a draw\n'+ fg.rs)
                    draws += 1  
                elif cpu == 'scissors':
                    print(fg(255, 255, 10) + 'paper <> scissors'+ fg.rs)
                    print(fg(255, 10, 10) + "Scissors beats paper, so you lost :(\n"+ fg.rs)
                    losts += 1
                else:
                    print("Please give me a valid name!\n")
            
            elif ask == '3':
                cpu = random.choice(signs)
                if cpu == 'rock':
                    print(fg(255, 255, 10) + 'scissors <> rock'+ fg.rs)
                    print(fg(255, 10, 10) + "Rock beats scissors, so you lost :(\n"+ fg.rs)
                    losts += 1
                elif cpu == 'paper':
                    print(fg(255, 255, 10) + 'scissors <> paper'+ fg.rs)
                    print(fg(10, 255, 10) + 'Scissors beats paper, so you won :)\n'+ fg.rs)
                    wins += 1  
                elif cpu == 'scissors':
                    print(fg(255, 255, 10) + 'scissors <> scissors'+ fg.rs)
                    print(fg(139,69,19) + "It is a draw!\n"+ fg.rs)
                    draws += 1
                else:
                    print("Please give me a valid name!\n")
        else:
            print(fg(255, 10, 10) + "\nYou have to type a number between 1 and 3!\n"+ fg.rs)

if sys.argv[1] == "start":
    play()