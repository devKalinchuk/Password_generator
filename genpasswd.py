#!/usr/bin/env python3

import random
import argparse

lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits_chars = '0123456789'
punctuation_chars = '!"#$%&()*+,-./:;<=>?@^_`{|}~'

def generate_password(length=10, uppercase=True, lowercase=True, digits=True, punctuation=True):
    """Generate a random password."""
    if length < 1:
        return "Password length must be at least 1"

    character_pool = ''
    if uppercase:
        character_pool += uppercase_chars
    if lowercase:
        character_pool += lowercase_chars
    if digits:
        character_pool += digits_chars
    if punctuation:
        character_pool += punctuation_chars

    if not character_pool:
        return "At least one character type must be selected"

    while True:
        secure = random.SystemRandom()
        password = ''.join(secure.choice(character_pool) for _ in range(length))
        if (not uppercase or any(c in uppercase_chars for c in password)) and \
           (not lowercase or any(c in lowercase_chars for c in password)) and \
           (not digits or any(c in digits_chars for c in password)) and \
           (not punctuation or any(c in punctuation_chars for c in password)):
            break
    return password

def parser():
    """Parse command line arguments."""
    arg_parser = argparse.ArgumentParser(description="Generate a random password.")
    arg_parser.add_argument('-l', '--length', type=int, default=10, metavar='', help='Length of the password (default: 10)')
    arg_parser.add_argument('-U', '--no-uppercase', action='store_false', help='Exclude uppercase letters')
    arg_parser.add_argument('-L', '--no-lowercase', action='store_false', help='Exclude lowercase letters')
    arg_parser.add_argument('-D', '--no-digits', action='store_false', help='Exclude digits')
    arg_parser.add_argument('-P', '--no-punctuation', action='store_false', help='Exclude punctuation characters')
    return arg_parser.parse_args()

if __name__ == '__main__':
    args = parser()
    print(generate_password(args.length, args.no_uppercase, args.no_lowercase, args.no_digits, args.no_punctuation))

