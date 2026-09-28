import random
import time

treasure_count = 0
draconic_snacks_eaten = 0

while True:
    def display_intro():
        print('You are in a land full of dragons. In front of you, you see two caves')
        print('    ')
        print('In one cave, the dragon is friendly and will share his treasure with you.')
        print('    ')
        print('The other dragon is greedy and hungry and will eat you on the spot.')
        print('    ')
        print('    ')
        
    display_intro()
    
    def choose_cave():
        while True:
            choice = int(input('Do you want to go to cave 1 or 2? (Enter 1 or 2) '))
            
            if choice == 1:
                print('    ')
                print('You have chosen cave 1!')
                break
            elif choice == 2:
                print('    ')
                print('You have chosen cave 2!')
                break
            else:
                choice = int(input('Do you want to go to cave 1 or 2? (Enter 1 or 2) '))
                
            return choice
        
    c = choose_cave()
    def check_cave(chosen_cave):
        global treasure_count
        global draconic_snacks_eaten
        
        print('   ')
        print('You approach the cave…')
        time.sleep(2)
        print('It is dark and spooky…')
        time.sleep(2)
        print('A large dragon jumps out in front of you! He opens his jaws and…')
        print('   ')
        time.sleep(2)
        cave = random.randint(1, 2)
        
        if cave == chosen_cave:
            print('The dragon shares his treasure with you!')
            print(' ')
            treasure_count += 1
        else:
            print('The hungry dragon devours you in 2 seconds and you are offcially his snack!')
            print(' ')
            draconic_snacks_eaten += 1
            
    check_cave(c)

    print('How many times you gained life-changing wealth: ' + str(treasure_count))
    print("How many times you have satisfied the dragon's greed at 3 on an average midnight: " + str(draconic_snacks_eaten))
    print(' ')

    again = input('Do you wish to play again? (Yes or No) ')

    if again == 'Yes':
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        print(' ')
        continue
    else:
        break
    




