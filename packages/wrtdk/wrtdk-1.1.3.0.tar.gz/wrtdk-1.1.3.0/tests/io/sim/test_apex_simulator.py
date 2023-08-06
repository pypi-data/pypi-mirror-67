'''
Created on Apr 14, 2020

@author: Reynolds
'''
import unittest
from wrtdk.io.sim.apex_simulator import apex_simulator

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testRead(self):
        sim = apex_simulator()
        self.assertTrue(sim.read(r'apex_emv2.dat'))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()