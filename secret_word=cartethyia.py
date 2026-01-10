cartethyia = any
secret_word = "cartethyia"

user_letter = input("Please enter a letter: ")

if len(user_letter) == 1 and user_letter.isalpha():
    if user_letter.lower() in secret_word.lower():
        print("The letter is in the secret word.")
    else:
        print("The letter is not in the secret word.")
else:
    print("Invalid input. Please enter a single letter.")