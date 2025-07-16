import random

number_to_guess = random.randint(1,100)
while True:
    try:
        guess = int(input ("guess the number 1-100: " ))
        if guess > number_to_guess:
            print("Its too high")
        elif guess < number_to_guess:
            print("Its too low")
        else:
            print("Congratulation! you find it")
            break
    except ValueError:
        print('Please enter the valid number')
    