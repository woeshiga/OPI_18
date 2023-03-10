#!/user/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('individual2.txt', 'r', encoding='utf-8') as fileptr:
        content = fileptr.readlines()

    with open('individual2_result.txt', 'w', encoding='utf-8') as fileptr:
        for num, line in enumerate(content):
            fileptr.write(f"{num + 1}: {line}")
