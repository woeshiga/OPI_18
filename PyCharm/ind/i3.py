#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise AttributeError("Path and keyword expected")

    if sys.argv[0] not in os.listdir():
        raise NotADirectoryError("Directory is not found")

    os.chdir(sys.argv[1])

    result = dict()

    for file in os.listdir():
        if '.txt' in file:
            with open(file, 'r') as fileptr:
                content = fileptr.readlines()

            for index, line in enumerate(content):
                if sys.argv[2] in line:
                    result[file] = (index, line)

    print(result)
