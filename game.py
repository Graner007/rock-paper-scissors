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

    arts2 = {
            'r2':
             '''
 ______
(___   '---
 (____)
 (____)
  (___)
(___)__.---
            ''',
            'p2':
            '''
     ______          
___(___     '---
  (_____
 (______
 (______
  (________.---       

            ''',
            's2':
            '''
    _______
___(____    '---
 (____
 (_________
    (_____)
      (___)__.---    
            '''
    }

    signs = ['rock', 'paper', 'scissors']
    matches = 0
    wins = 0 
    losts = 0 
    draws = 0
    rounds = 0
    already = -1
    rank = ''

    print(fg(128,0,0) + "Hello my friend, welcome to rock-paper-scissors game!\n" + fg.rs)

    def rank(wins):

        if wins >= 0 and wins < 5:
            rank = 'Verdant'
        
        elif wins >= 5 and wins < 10:
            rank = "Beginner"

        elif wins >= 10 and wins < 20:
            rank = "Medium"

        elif wins >= 20 and wins < 30:
            rank = "Advanced"

        elif wins >= 30 and wins < 40:
            rank = "Professional"

        elif wins >= 40 and wins < 50:
            rank = "Expert"
        
        elif wins >= 50: 
            rank = "Legend"

        return rank

    def statics(used):
        return fg(255,127,80) + '\nYour statics: ' + str(matches - used) + ' matches, ' + str(wins) + ' wins, ' + str(draws) + ' draws, ' + str(losts) + ' losts, ' + str(rank(wins)) + ' rank\n'+ fg.rs

    while True:
        ask = input("Please choose your tool!\n 1: Rock\n 2: Paper\n 3: Scissors\nNumber of your choice: ")
        print(chr(27) + "[2J")

        def print_rank(level):
            if ask == "statics" and ask == "quit":
                print("Your rank is: " + level)

        if ask == 'statics' and matches >= 1:
            rounds -= 1 
            already += 1
            print(statics(already))

        if ask == 'quit':
            print(statics(already + 1))
            print(fg(255,255,0) + 'Hope to see you soon!'+ fg.rs)
            sys.exit()

        if (ask.isdigit() and int(ask) <= 3 and int(ask) > 0) or ask == "statics":
            matches += 1
            rounds += 1
            if ask != "statics":
                print(fg(0,191,255) + "\nRound " + str(rounds) + fg.rs)

            if ask == '1':
                print(arts.get("r"), end = '')
                cpu = random.choice(signs)
                if cpu == 'rock':
                    print(arts2.get("r2"))
                    print(fg(255, 255, 10) + 'rock <> rock'+ fg.rs)
                    print(fg(255,105,180) + "It is a draw\n"+ fg.rs)
                    draws += 1
                elif cpu == 'paper':
                    print(arts2.get("p2"))
                    print(fg(255, 255, 10) + 'rock <> paper'+ fg.rs)
                    print(fg(255, 10, 10) + 'Paper beats rock, so you lost :(\n'+ fg.rs)
                    losts += 1  
                elif cpu == 'scissors':
                    print(arts2.get("s2"))
                    print(fg(255, 255, 10) + 'rock <> scissors')
                    print(fg(10, 255, 10) + "Scissors lost against rock, so you won :)\n"+ fg.rs)
                    wins += 1

            elif ask == '2':
                print(arts.get("p"), end = '')
                cpu = random.choice(signs)
                if cpu == 'rock':
                    print(arts2.get("r2"))
                    print(fg(255, 255, 10) + 'paper <> rock'+ fg.rs)
                    print(fg(10, 255, 10) + "Paper beats rock, so you won :)\n"+ fg.rs)
                    wins += 1
                elif cpu == 'paper':
                    print(arts2.get("p2"))
                    print(fg(255, 255, 10) + 'paper <> paper'+ fg.rs)
                    print(fg(255,105,180) + 'It is a draw\n'+ fg.rs)
                    draws += 1  
                elif cpu == 'scissors':
                    print(arts2.get("s2"))
                    print(fg(255, 255, 10) + 'paper <> scissors'+ fg.rs)
                    print(fg(255, 10, 10) + "Scissors beats paper, so you lost :(\n"+ fg.rs)
                    losts += 1
            
            elif ask == '3':
                print(arts.get("s"), end = '')
                cpu = random.choice(signs)
                if cpu == 'rock':
                    print(arts2.get("r2"))
                    print(fg(255, 255, 10) + 'scissors <> rock'+ fg.rs)
                    print(fg(255, 10, 10) + "Rock beats scissors, so you lost :(\n"+ fg.rs)
                    losts += 1
                elif cpu == 'paper':
                    print(arts2.get("p2"))
                    print(fg(255, 255, 10) + 'scissors <> paper'+ fg.rs)
                    print(fg(10, 255, 10) + 'Scissors beats paper, so you won :)\n'+ fg.rs)
                    wins += 1  
                elif cpu == 'scissors':
                    print(arts2.get("s2"))
                    print(fg(255, 255, 10) + 'scissors <> scissors'+ fg.rs)
                    print(fg(255,105,180) + "It is a draw!\n"+ fg.rs)
                    draws += 1
        else:
            print(fg(255, 10, 10) + "\nYou have to type a number between 1 and 3!\n"+ fg.rs)

if len(sys.argv) > 1 and sys.argv[1] == "start":
    play()

else:
    if __name__ == '__main__':
        play()