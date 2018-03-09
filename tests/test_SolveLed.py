import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../SolveLed'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
from SolveLed.main import *

class TestSolveLed(unittest.TestCase):


    def test_GetLocalFile(self):
       text = getFile("test.txt")
       self.assertTrue(text != None)


    def test_GetRemoteFile(self):
       text = getFile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
       self.assertTrue(text != None)

    def test_getBadFile(self):
        text = getFile("aMadeUpFile.txt")

    def test_applyTurnOnCommand(self):
        gridLength = 5
        ledGrid =  [[False]*5 for i in range(5)]
        count = applyCommand("turn on 0,2 through 3,4", ledGrid, gridLength)
        self.assertTrue(count == 12)

    def test_applyTurnOffCommand(self):
        ledGrid = [[True]*5 for i in range(5)]
        gridLength = 5
        count = 25
        count += applyCommand("turn off 1,2 through 3,4", ledGrid, gridLength)
        self.assertTrue(count == 25-9)

    def test_applySwitchCommand(self):
        ledGrid = [[True, False]*2 for i in range(4)]
        gridLength = 4
        count = 8
        count += applyCommand("switch 0,4 through 3,4", ledGrid, gridLength)
        self.assertTrue(count == 8)

    def test_applyOutOfRangeCommand(self):
        ledGrid = [[False]*2 for i in range(2)]
        gridLength = 2
        count = applyCommand("turn on -1,-2 through 3,3", ledGrid, gridLength)
        self.assertTrue(count==4)

    def test_applyBadCommand(self):
        gridLength = 5
        ledGrid = [[True]*5 for i in range(5)]
        count = 25
        count += applyCommand("this is a bad command", ledGrid, gridLength)
        self.assertTrue(count==25)


if __name__=="__main__":
    unittest.main()
