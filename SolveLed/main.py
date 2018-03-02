import argparse
import re
import os
from urllib.request import urlretrieve
from shutil import copy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
#    parser.add_argument('--verbose')
    args = parser.parse_args()

    global text, ledGrid, gridLength #, count
    text = getFile(args.input)
    gridLength = int(text[0])
    ledGrid = [[False]*gridLength for i in range(gridLength)]
    count = 0

    for line in text:
       count += applyCommand(line)
#       if args.verbose=="t":
    print("Final number of lights on:", count)


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

    l = [outer1, outer2, inner1, inner2]
#    commandList = []
#    for i in l:
#        if i<0:
#            commandList.append(0)
#            print("caught", i)
#        elif i>gridLength:
#            commandList.append(gridLength)
#            print("caught", i)
#        else:
#            commandList.append(i)
#    commandList = [i for i in l]
    commandList = [0 if i<0 else gridLength if i>gridLength else i for i in l]

    if command.group(1)=="turn on":
       for i in range(commandList[0], commandList[1]):
           for j in range(commandList[2], commandList[3]):
               if ledGrid[i][j] == False:
                   tempCount += 1
               ledGrid[i][j] = True

    elif command.group(1)=="turn off":
       for i in range(commandList[0], commandList[1]):
           for j in range(commandList[2], commandList[3]):
               if ledGrid[i][j] == True:
                   tempCount -= 1
               ledGrid[i][j] = False

    else:
       for i in range(commandList[0], commandList[1]):
           for j in range(commandList[2], commandList[3]):
               if ledGrid[i][j] == False:
                   tempCount += 1
               else:
                   tempCount -= 1
               ledGrid[i][j] = not ledGrid[i][j]

    return tempCount
