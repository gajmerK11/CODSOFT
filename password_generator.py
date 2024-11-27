import string
import random

user_input = int(input("Enter the desired length of the password: "))
ask_numbers = input("Include numbers (yes/no): ").lower()
ask_symbols = input("Include symbols (yes/no): ").lower()

def password_generator(user_input, ask_numbers, ask_symbols):
    normal_password = string.ascii_letters
    if ask_numbers == "yes":
        normal_password = normal_password + string.digits
    if ask_symbols == "yes":
        normal_password = normal_password + string.punctuation
    return ''.join(random.choices(normal_password, k = user_input))

print(f"Here is your password: {password_generator(user_input, ask_numbers, ask_symbols)}")

