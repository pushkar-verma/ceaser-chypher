# this is a encryptor & decrypter

import string
import collections

# this encrypts the given word


def encryptor(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(
        str.maketrans(string.ascii_lowercase, lower))


# this decrypts the given word


def decrypter(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).translate(
        str.maketrans(string.ascii_lowercase, lower))


option = input('type A encryption ||| type B for decryption: ')

if option.upper() == 'A':
    text = input('write your text: ')
    A = encryptor(text, 3)
    print(A)
else:
    text = input('write your text: ')
    B = decrypter(text, -3)
    print(B)
