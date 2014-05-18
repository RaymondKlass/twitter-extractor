import unittest
import sys, os, datetime, time
import pika

path = os.path.dirname(__file__)
if path:
    os.chdir(path)
sys.path.insert(0, '../../')

from twitter_interface.stream_reader import stream_reader
import config as config

                               
class stream_reader_test(unittest.TestCase):

    def setUp(self):
        self.tweets = []
        self.test_queue = 'raw_twitter_automated_test'
        self.stream_reader = stream_reader(config.data['twitter_credentials'], config.data['rabbitMQ_credentials'], self.test_queue)
    
    
    def test_filter(self):
        pass
    
    
            

if __name__ == '__main__':
    unittest.main()