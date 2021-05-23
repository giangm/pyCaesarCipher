#!/usr/bin/python3

import sys, time, colorama
from colorama import Fore, Style

def main():

    # Print banner
    banner()

    # Colored text
    colorama.init(autoreset=True)

    if len(sys.argv) != 4 or not sys.argv[3].isdigit():
        print(Fore.RED + Style.BRIGHT + '[!] Wrong usage...')
        print(Fore.RED + Style.BRIGHT + '[!] Sample usage - python3 main.py -e \'Hello World\' 4')
    else:
        print(Fore.GREEN + '[+] Starting up Caesar Cipher\n')
        time.sleep(2)

        if sys.argv[1] == '-e' or sys.argv[1] == '--encrypt':
            # -e for encryption
            print(Fore.GREEN + '[+] Beginning encryption process')
            time.sleep(1)

            print(Fore.GREEN + '[+] Encryption completed:\n')
            print(Fore.YELLOW + encryption(sys.argv[2], int(sys.argv[3])))
        elif sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            # -d for decryption
            print(Fore.GREEN + '[+] Beginning decryption process')
            time.sleep(1)

            print(Fore.GREEN + '[+] Decryption completed:\n')
            print(Fore.YELLOW + decryption(sys.argv[2], int(sys.argv[3])))
        else:
            print(Fore.RED + Style.BRIGHT + '[!] Wrong usage...')

def banner():
    banner_ascii = '''
+-------------------------------------------------------------------+
|   ____                              ____ _       _                |
|  / ___|__ _  ___  ___  __ _ _ __   / ___(_)_ __ | |__   ___ _ __  |
| | |   / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__| |
| | |__| (_| |  __/\__ \ (_| | |    | |___| | |_) | | | |  __/ |    |
|  \____\__,_|\___||___/\__,_|_|     \____|_| .__/|_| |_|\___|_|    |
|                                           |_|                     |
|                                                                   |
+-------------------------------------------------------------------+
    '''
    print(Fore.WHITE + banner_ascii)

def encryption(plain_text, key):

    # Store a string of the cipher text
    cipher_text = ''

    # Covert plain_text to uppercase
    plain_text = plain_text.upper()

    # Iterate through plain_text to get each character
    for character in plain_text:
        if not character.isalpha():
            # Append without shifting
            cipher_text += character
        else:
            # Shift character by key
            new_character = (ord(character) + key) % 128 if (ord(character) + key) % 128 <= 90 else ((ord(character) + key) % 26) + 52

            # Append shifted character
            cipher_text += chr(new_character)

    return cipher_text

def decryption(cipher_text, key):

    # Store a string of the plain text
    plain_text = ''

    # Convert cipher_text to uppercase
    cipher_text = cipher_text.upper()

    for character in cipher_text:
        if not character.isalpha():
            # Append without shifting
            plain_text += character
        else:
            # Shift character by key
            new_character = (ord(character) - key) % 128 if (ord(character) - key) % 128 >= 65 else ((ord(character) - key) % 26) + 52

            # Append shifted character
            plain_text += chr(new_character)

    return plain_text

if __name__ == '__main__':
    main()
