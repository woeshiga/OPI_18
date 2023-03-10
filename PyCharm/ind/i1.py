#!/user/bin/env python3
# -*- coding: utf-8 -*-

LETTERS = 'eyuioa'

if __name__ == '__main__':
    with open('individual1.txt', 'r') as fileptr:
        content = fileptr.read()

    content = content.replace('\n', '').split(' ')
    result = list()

    for letter in content:
        if letter[0].lower() in LETTERS:
            print(letter)
