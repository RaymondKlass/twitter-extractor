import unittest
import sys, os, datetime, time

path = os.path.dirname(__file__)
if path:
    os.chdir(path)
sys.path.insert(0, '../../')

from twitter_interface.message_parser import message_parser


class message_parser_test(unittest.TestCase):
    
    def setUp(self):
        self.expected_message_format = {u'contributors' : None, 
                                        u'truncated': None, 
                                        u'text' : None, 
                                        u'in_reply_to_status_id' : None, 
                                        u'id' : None, 
                                        u'favorite_count' : None, 
                                        u'source' : None, 
                                        u'retweeted' : None, 
                                        u'coordinates' : None, 
                                        u'entities' : None, 
                                        u'in_reply_to_screen_name' : None, 
                                        u'id_str' : None, 
                                        u'retweet_count' : None, 
                                        u'in_reply_to_user_id' : None, 
                                        u'favorited' : None, 
                                        u'retweeted_status' : None, 
                                        u'user' : None, 
                                        u'geo' : None, 
                                        u'in_reply_to_user_id_str' : None, 
                                        u'possibly_sensitive' : None, 
                                        u'lang' : None, 
                                        u'created_at' : None, 
                                        u'filter_level' : None, 
                                        u'in_reply_to_status_id_str' : None, 
                                        u'place' : None}

    
    def test_regex_parser(self):
        
        message1 = {'text' : 'an alphanumberic12 message'}
        parser1 = message_parser(message1)
        
        self.assertTrue(parser1.regex_parser('text', '[a-z]'))
        

if __name__ == '__main__':
    unittest.main()