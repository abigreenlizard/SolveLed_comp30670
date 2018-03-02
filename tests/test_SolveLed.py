import unittest
from SolveLed.main import *

class TestSolveLed(unittest.TestCase):

    def testGetLocalFile(self):
       text = getFile("{}/../temp/input.txt".format(os.path.dirname(os.path.realpath(__file__))))
       self.assertTrue(text != null)


    def testGetRemoteFile(self):
       text = getFile("http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt")
       self.assertTrue(text != null)

if __name__=="__main__":
    unittest.main()
