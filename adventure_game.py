import time
import random
items = []
monsters = ['Dragon', 'Cerberus', 'Minotaur', 'Vampire', 'Werewolf', 'Gollum']
monster = random.choice(monsters)
def print_sleep(dialogue):
    print(dialogue)
    time.sleep(1)

def valid_input(prompt, options):
    while True:
        response = input(prompt)
        for choices in options:
            if response in options:
                return response
        print('Please choose between 1 or 2.')

def intro():
    print_sleep(f'You are a bounty hunter who is trying to kill the {monster} that\'s destroying the village.')
    print_sleep('However, you must find a new weapon since your sword has been worn out from all the fighting.')
    print_sleep(f'While walking around to find some clues to hunt the {monster}, you see a ruined temple and a firepit.')
    print_sleep('To your left, there is a ruined temple.')
    print_sleep('To your right, there\'s a firepit.')


intro()
while True:
    print_sleep('Enter 1 to enter the ruined temple.')
    print_sleep('Enter 2 to peek at the firepit.')
    answer = valid_input('What would you like to do?\n', ['1','2'])
    if '1' in answer:
        print_sleep(f'You went inside the ruined temple, and then you see a vicious {monster} staring at you.')
        print_sleep(f'A {monster} began to charge on you to battle!')
        print_sleep(' ')
        sec_answer = valid_input('Would you like to (1)Fight or (2)Run away? \n', ['1','2'])
        if 'Sword' in items:
            if '1' in sec_answer:
                print_sleep(f'You bravely fought back against the {monster} with the new sword you found, and have slayed it!')
                print_sleep('Congratulations! You have saved the village! You won the game!')
                replay = input('Would you like to play again? (y/n)')
                if replay == 'y':
                    print_sleep('Great! restarting the game...')
                    print_sleep(' ')
                    intro()
                elif replay == 'n':
                    print_sleep('sad to see you go! see you next time!')
                    break
            elif '2' in sec_answer:
                    print_sleep(f'You ran away as fast as you can, and {monster} don\'t seem to follow you...')
                    print_sleep(' ')
        else:
            if '1' in sec_answer:
                print_sleep(f'You tried to fight against the {monster} with your wornout sword...')
                print_sleep(f'But the {monster} have destroyed your weapon and defeated you!')
                print_sleep('You died! Game over!')
                replay = input('Would you like to play again? (y/n)')
                if replay == 'y':
                    print_sleep('Great! restarting the game...')
                    print_sleep(' ')
                    intro()
                elif replay == 'n':
                    print_sleep('sad to see you go! see you next time!')
                    break
            elif '2' in sec_answer:
                print_sleep(f'You ran away as fast as you can, and {monster} don\'t seem to follow you...')
                print_sleep(' ')
    elif '2' in answer:
        if 'Sword' in items:
            print_sleep('You already have searched this area, and there\'s nothing more for you to look for.')
            print_sleep(' ')
        else:
            print_sleep('You walked to take a peek inside the firepit, and you see a shiny metal underneath the ashe.')
            print_sleep('The shiny metal was a sword made with Adamentium steel! Good job!')
            print_sleep(' ')
            items.append('Sword')



                        


            
