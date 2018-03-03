import argparse
import re
import os
from urllib.request import urlretrieve
from shutil import copy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    args = parser.parse_args()

    text = getFile(args.input)
    if text==0:
        exit()
    gridLength = int(text[0])
    ledGrid = [[False]*gridLength for i in range(gridLength)]
    count = 0

    for line in text:
       count += applyCommand(line, ledGrid, gridLength)
    print("Final number of lights on:", count)


def getFile(input):
    tempFile = "{}/../temp/input.txt".format(os.path.dirname(os.path.realpath(__file__)))
    isURL = re.match(r'http://*', input)

    if isURL:
        try:
            urlretrieve(input, tempFile)
        except FileNotFoundError:
            print("File not found, please check the URL and connection to the internet")
            return 0
    else:
        try:
            copy(input, tempFile)
        except FileNotFoundError:
            print("File not found, please check input file name and path")
        return 0

    file = open(tempFile, 'r')
    textArray = [i for i in file.readlines()]
    file.close()
    return textArray

def applyCommand(line, ledGrid, gridLength):
    pat = re.compile(r'.*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*')
    command = re.match(pat, line)
    if not command:
        return 0

    tempCount = 0
    uncleanCommandList = [int(command.group(2)), int(command.group(4))+1, int(command.group(3)), int(command.group(5))+1]
    commandList = [0 if i<0 else gridLength if i>gridLength else i for i in uncleanCommandList]

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
