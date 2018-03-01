import argparse
import re
import os
from urllib.request import urlretrieve
from shutil import copy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    args = parser.parse_args()

    text  = getFile(args.input)
    length = int(text[0])
    myArray = [[False]*length for i in range(length)]
    print(myArray)

def getFile(input):
    tempFile = "{}/../temp/input.txt".format(os.path.dirname(os.path.realpath(__file__)))
    isURL = re.match(r'http://*', input)
    if isURL:
        urlretrieve(input, tempFile)
    else:
        copy(input, tempFile)
    file = open(tempFile, 'r')
    textArray = [i for i in file.readlines()]
    return textArray
