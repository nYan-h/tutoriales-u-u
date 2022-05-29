import random

def new_game():
    again = input('\nWould you like to play again? [Y/n] ').lower()
    return again

again = 'y'

print('                       Hello ^^\n')
print('Let\'s play a guessing game. Pick a number from <1-9>.')

while again == 'y':
    secret = random.randint(1, 9)
    tries = 5
    while tries != 0:
        guess = int(input('\nYour guess: '))
        if guess > secret:
            print('The secret is lower.')
            tries -= 1
            print(f'Number of tries -> [{tries}]')
        elif guess < secret:
            print('The secret is higher.')
            tries -= 1
            print(f'Number of tries -> [{tries}]')
        else:
            print(' ____________________________________________')
            print('|  Correct! Here take this sweet cookie! ^^  |')
            print('|                                            |')
            print('|                     @                      |')
            print('|___________________.---.____________________|')
            break

    if tries == 0:
        print('Ah >< You were so close.. Better luck next time!\n')
    again = new_game()
print('Goodbye <3')
