#!/usr/bin/env python3

import random
import argparse

lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits_chars = '0123456789'
punctuation_chars = '!"#$%&()*+,-./:;<=>?@^_`{|}~'

def generate_password(length=10, uppercase=True, lowercase=True, digits=True, punctuation=True):
    if length < 4:
        return "Задана довжина пароля повинна бути не менша 4 символів"

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
        return "Принаймні одна опція повинна бути увімкнена"

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
    arg_parser = argparse.ArgumentParser(description="Генератор випадкового пароля.")
    arg_parser.add_argument('-l', '--length', type=int, default=10, metavar='', help='Довжина пароля (за замовчуванням 10)')
    arg_parser.add_argument('-U', '--no-uppercase', action='store_false', help='Виключити великі літери')
    arg_parser.add_argument('-L', '--no-lowercase', action='store_false', help='Виключити малі літери')
    arg_parser.add_argument('-D', '--no-digits', action='store_false', help='Виключити цифри')
    arg_parser.add_argument('-P', '--no-punctuation', action='store_false', help='Виключити символи пунктуації')
    return arg_parser.parse_args()

if __name__ == '__main__':
    args = parser()
    print(generate_password(args.length, args.no_uppercase, args.no_lowercase, args.no_digits, args.no_punctuation))

