import unittest
import sys, os, datetime

path = os.path.dirname(__file__)
if path:
    os.chdir(path)
sys.path.insert(0, '../../')

from twitter_interface.stream_reader import stream_reader
import config as config

                               
class stream_reader_test(unittest.TestCase):

    def setUp(self):
        self.tweets = []
        self.stream_reader = stream_reader(config.data['twitter_credentials'])
    
    
    def checkFilter(self):
        pass
    
    
    
    def test2(self):    
        pairs = [(1,2), (1,4), (8,-5), (10, 0)]
        
        for p in pairs:
            self.assertEqual(self.stream_reader.add2(p[0], p[1]), p[0] + p[1])
            

if __name__ == '__main__':
    unittest.main()