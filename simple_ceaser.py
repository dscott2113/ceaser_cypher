import string

entry_text = input("What would you like encrypted? ")
entry_shift = input("How much shift? ")

clear_text = entry_text
shift = int(entry_shift)
shift %= 26

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase
numerals = string.digits

shifted_lower = lower_alphabet[shift:] + lower_alphabet[:shift]
shifted_upper = upper_alphabet[shift:] + upper_alphabet[:shift]
shifted_numerals = numerals[shift:] + numerals[:shift]

plain_alphabet = lower_alphabet + upper_alphabet + numerals
shifted_alphabet = shifted_lower + shifted_upper + shifted_numerals

table = str.maketrans(plain_alphabet, shifted_alphabet)

encrypted_message = clear_text.translate(table)

print("Here is your message")
print(encrypted_message)
