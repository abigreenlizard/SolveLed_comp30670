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

#    def test_GetPhonyFile(self):
#        text = getFile("a non-existent file")

    def test_applyTurnOnCommand(self):
        global ledGrid
        ledGrid =  [[False]*5 for i in range(5)]
        count = applyCommand("turn on 0,2 through 3,4")
        self.assertTrue(count == 12)

    def test_applyTurnOffCommand(self):
        ledGrid = [[True]*5 for i in range(5):
        count = 25
        count += applyCommand("turn off 1,2 through 3,4")
        self.assertTrue(count == 25-9)

    def test_applySwitchCommand(self):
        ledGrid = [[True, False]*2 for i in range(4):
        count = 8
        count += applyCommand("switch 0,1 through 1,1")
        self.assertTrue(count == 8)

    def test_applyBadCommand(self):
        ledGrid = [[True]*5 for i in range(5):
        count = 25
        count += applyCommand("this is a bad command")
        self.assertTrue(count==25)

    def test_applyOutOfRangeCommand(self)
        ledGrid = [[True]*5 for i in range(5):
        count = 25
        count += applyCommand("turn off -5,50, -10,20")
        self.assertTrue(count==0)

if __name__=="__main__":
    unittest.main()
