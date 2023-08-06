'''
Created on Apr 3, 2020

@author: Reynolds
'''
import unittest
from wrtdk.io.read.apex_reader import apex_reader

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_apex_reader(self):
        aread = apex_reader()
        self.assertNotEquals(aread,None)
        self.assertEqual(aread.get_version(),1)
        
    def test_version(self):
        aread = apex_reader(version=1)
        self.assertEqual(aread.get_version(),1)
        aread.set_version(2)
        self.assertEqual(aread.get_version(),2)
        
    def test_read_error(self):
        aread = apex_reader(version=2)
        data = aread.read('')
        self.assertFalse(data)
        
    def test_read_v2(self):
        aread = apex_reader(version=2)
        data = aread.read(r'apex_emv2.dat')
        #print(data)
        #print(data['IMU']['data'])
        #print(data['HEADER'])
        self.assertTrue(data)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_apex_reader']
    unittest.main()