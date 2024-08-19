import random
player_wins=0
computer_wins=0
options=['rock','paper','scissors']
print('Hello there! welcome to my game ;)')
while True:

    player_pick=input('please pick a rock/paper/scissors or Q to quit: ').lower()
    if player_pick=='q':
        break
    if player_pick not in options :
        continue 

    random_number=random.randint(0,2)
    # 0=rock and 1=paper and 2= scissors
    
    computer_pick=options[random_number]
    print('computer_pick',computer_pick + '.')
    if player_pick == 'rock' and computer_pick == 'scissors':
        print(' you win!')
        player_wins+=1
    elif player_pick == 'paper' and computer_pick == 'rock':
        print(' you win!')
        player_wins+=1
    elif player_pick =='scissors' and computer_pick == 'paper':
        print(' you win!')
        player_wins+=1
    elif player_pick == computer_pick:
        print('tie')
    else:
        print('computer win !')
        computer_wins+=1

print('you wins',player_wins,'times')
print('computer wins',computer_wins ,'times')