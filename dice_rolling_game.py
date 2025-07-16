import random

while True:
    choice = input("Roll the Dice? (y/n): ").lower()
    if choice == 'y':
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        print (f'({dice_1}, {dice_2})')
    elif choice == 'n':
        print ('Thanks for Playing')
        break
    else:
        print("Invalid Choice!")
