import random

names = ["aliaaa", "mohaaaammad", "cinaaaa", "rezaaaa", "amiaarali"]

selected_name = random.choice(names).lower()

guess_count = len(selected_name)
guessed_list = ["-"] * len(selected_name )

corrent_guess = " ". join(guessed_list)
print(corrent_guess)

while guess_count > 0:
    guessed_char = input("enter a char:\n")
    if guessed_char.isalpha():
        if guessed_char in selected_name:
            if guessed_char in guessed_list:
                print("you have guessed before, try new charter")
            else:
                for idx, char in enumerate(selected_name):
                    if char == guessed_char:
                        guessed_list[idx] = guessed_char
                corrent_guess = " ". join(guessed_list)
                print(f'perfect => {corrent_guess}')
                
                if not "-" in guessed_list:
                    print(" winner!")
                    break
            
        else:
            guess_count -= 1
            print(f'Wrong! => remained guesses:{guess_count}')
        
    else:
        print("Please enter a valid charcter")