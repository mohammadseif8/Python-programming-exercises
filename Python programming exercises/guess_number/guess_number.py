import random

try:
    low = int(input("Enter lower bound :")) 
    high = int(input("Enter higher bound :")) 
except:
    print("Please enter valid number.")

r = random.randint(low, high)

guess_count = 5

while  guess_count > 0:
    try:
        new_guess_str = input(f'remained guess:{guess_count} ==> Enter your next guess: \n')
        new_guess = int(new_guess_str)
        
        if r == new_guess:
            print("great! your guess is correct!")
            break
        elif r > new_guess:
            print("your guess is lower than selected number.")
        elif r < new_guess:
            print("your guess is higher than selected number.")
        
        guess_count -=1
    except:
        print("Please enter a valid number.")
        
    
        