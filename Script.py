import string


def alpha_to_num(in_alpha):

    # Upper- and lowercase characters have different ascii decimal values.
    # Therefore we need to set a different starting position for each.
    if in_alpha.isupper():
        ascii_start_position = 65
    else:
        ascii_start_position = 97

    # Gives us a number between 0 and 25
    num = ord(in_alpha) - ascii_start_position

    return num


# ENCRYPTION WITH SINGLE KEY
def encrypt(in_plaintext, in_key, in_rot):

    ciphertext = ""

    # Counts the number of alphanumerical characters in the plaintext
    alpha_count = 0

    # Loop over every character in the plaintext
    for plaintext_char in in_plaintext:

        # We need to do this check to ensure we only encrypt alphanumerical characters
        if plaintext_char.isalpha():

            # Defines two different lists of letters (a to z or A to Z) depending
            # on whether or not the character is upper or lowercase.
            if plaintext_char.isupper():
                alphabet_list = list(string.ascii_uppercase)
            else:
                alphabet_list = list(string.ascii_lowercase)

            # Gives us the current letter of the repeating key.
            # Modulation is used to make the key repeat itself.
            key_char = in_key[alpha_count % len(in_key)]

            # Converts the current key and plaintext character to a number value
            # from 0 to 25
            key_num = alpha_to_num(key_char)
            plaintext_num = alpha_to_num(plaintext_char)

            # Determines the index needed to get the correct ciphertext-character.
            # This operation translates to one caesar cipher.
            index = (key_num + plaintext_num + in_rot) % 26

            # Finds the correct ciphertext-character and adds it to the ciphertext.
            ciphertext += alphabet_list[index]

            alpha_count += 1
        else:
            # If the current character is not alphanumerical, we just add it to the ciphertext.
            # This happens for spaces, punctuations, question marks, hyphens, etc.
            ciphertext += plaintext_char

    return ciphertext


# ENCRYPTION WITH TWO KEYS
def encrypt_with_two_keys(in_plaintext, in_key_1, in_key_2, in_rot):

    # To encrypt with two keys is the same as encrypting one time with
    # each key. Where the first encryption with the first key is the
    # plaintext (actually ciphertext) of the next encryption with the second key.
    return encrypt(encrypt(in_plaintext, in_key_1, in_rot), in_key_2, in_rot)

    # It is also possible to combine the two keys, and from there use
    # the ordinary encryption.


while True:

    print("Type 1 for encryption with single key")
    print("Type 2 for encryption with two keys")
    option = input()

    if option == '1':
        plaintext = input("Insert plaintext: ")
        key = input("Insert key: ")
        rot = int(input("Value of ROT: "))
        ciphertext = encrypt(plaintext, key, rot)
        print("Ciphertext: ", ciphertext)
    elif option == '2':
        plaintext = input("Insert plaintext: ")
        key_1 = input("Insert the first key: ")
        key_2 = input("Insert the second key: ")
        rot = int(input("Value of ROT: "))
        ciphertext_two_keys = encrypt_with_two_keys(plaintext, key_1, key_2, rot)
        print("Ciphertext: ", ciphertext_two_keys)
    else:
        print("This choice is illegal. Please try again.")
        continue

    print("Do you want to try again? (y/n)")
    option = input()

    if option == 'n':
        break