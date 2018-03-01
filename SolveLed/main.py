import argparse
import re
import os
from urllib.request import urlretrieve
from shutil import copy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    args = parser.parse_args()

    global text, ledGrid #, count
    text = getFile(args.input)
    ledGrid = [[False]*int(text[0]) for i in range(int(text[0]))]
    count = 0

    for line in text:
       count += applyCommand(line)
#       print("Total lights on", count)
#    print(count)


def getFile(input):
    tempFile = "{}/../temp/input.txt".format(os.path.dirname(os.path.realpath(__file__)))
    print(os.path.realpath(__file__))
    isURL = re.match(r'http://*', input)
    if isURL:
        urlretrieve(input, tempFile)
    else:
        copy(input, tempFile)
    file = open(tempFile, 'r')
    textArray = [i for i in file.readlines()]
    return textArray

def applyCommand(line):
    pat = re.compile(r'.*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*')
    command = re.match(pat, line)
    if not command:
        return 0

    outer1, outer2 = int(command.group(2)), int(command.group(4))+1
    inner1, inner2 = int(command.group(3)), int(command.group(5))+1
    tempCount = 0

    for i in [outer1, outer2, inner1, inner2]:
        if i<0:
            i=0
        if i>999:
            i=999

    if command.group(1)=="turn on":
       for i in range(outer1, outer2):
           for j in range(inner1, inner2):
               if ledGrid[i][j] == False:
                   tempCount += 1
               ledGrid[i][j] = True

    elif command.group(1)=="turn off":
       for i in range(outer1, outer2):
           for j in range(inner1, inner2):
               if ledGrid[i][j] == True:
                   tempCount -= 1
               ledGrid[i][j] = False

    else:
       for i in range(outer1, outer2):
           for j in range(inner1, inner2):
               if ledGrid[i][j] == False:
                   tempCount += 1
               else:
                   tempCount -= 1
               ledGrid[i][j] = not ledGrid[i][j]

#    print("number of lightts changed", tempCount)
    return tempCount
