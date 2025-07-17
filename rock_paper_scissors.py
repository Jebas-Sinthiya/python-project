import random

choices = ('r','p','s')
emojis = {'r':'🪨' , 'p':'📄' , 's': '✂️'}

while True:
    user_choice = input("Rock,Paper,Scissors?(r,p,s): ").lower()
    if user_choice not in (choices):
        print('Invalid Choices!')
        continue
    computer_choice = random.choice(choices)
    print(f'you chose {user_choice} --> {emojis[user_choice]}')
    print(f'Computer chose {computer_choice} --> {emojis[computer_choice]}')
    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'r' and computer_choice == 's' 
        or user_choice == 'p' and computer_choice == 'r'
        or user_choice == 's' and computer_choice == 'p'
        ):
            print("You Win!")
    else:
        print("You Lose!")

    user_continue = input("You Want To Continue?(y/n): ").lower()
    if user_continue == "n":
        break 


