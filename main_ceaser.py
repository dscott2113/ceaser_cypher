import string

#opening selections
en_or_de = int(input("1 = Encrypt or 2 = Decrypt? "))
clear_text = input("what is your message? ")
entry_shift = input("passphrase? ")

#change alpha to numbers so we can jumble everything
txt_to_numbers = []

for c in entry_shift:
    txt_to_numbers.append(ord(c) - 96)

passphrase = sum(txt_to_numbers)

shift = passphrase
shift %= 26

#encryption or decryption
def cypher():
    plain_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    shifted_alphabet = plain_alphabet[shift:] + plain_alphabet[:shift]
    table = str.maketrans(plain_alphabet, shifted_alphabet)
    encrypted_message = clear_text.translate(table)
    print(encrypted_message)

def decypher():
    plain_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    shifted_alphabet = plain_alphabet[shift:] + plain_alphabet[:shift]
    rev_table = str.maketrans(shifted_alphabet, plain_alphabet)
    encrypted_message = clear_text.translate(rev_table)
    print(encrypted_message)

#output
if en_or_de ==1:
    print("Encrypted message... ")
    cypher()
if en_or_de ==2:
    print("decrypted message...")
    decypher()
