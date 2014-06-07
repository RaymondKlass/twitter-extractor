import unittest
import sys, os, datetime, time

path = os.path.dirname(__file__)
if path:
    os.chdir(path)
sys.path.insert(0, '../../')

from twitter_interface.stream_reader import stream_reader
import config as config

                               
class stream_reader_test(unittest.TestCase):

    def setUp(self):
        self.tweets = []
        self.stream_reader = stream_reader(config.data['twitter_credentials'], self._callback)
    
    
    def _callback(data):
        pass
    
    
    def test_filter(self):
        pass
    
    
            

if __name__ == '__main__':
    unittest.main()