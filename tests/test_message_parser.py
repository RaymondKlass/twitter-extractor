import unittest
from twitter_interface.message_parser import message_parser
from copy import deepcopy


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
        
        message1 = {'text' : 'an alphanumberic 1 2 message'}
        parser1 = message_parser(message1)
        
        self.assertTrue(parser1.regex_parser('text', '[a-z]'))
        self.assertTrue(parser1.regex_parser('text', '[a-z0-9]'))
        self.assertTrue(not parser1.regex_parser('text', '[@$%]'))
        self.assertTrue(not parser1.regex_parser('textual', '[a-z]'))
    
    def test_contains(self):
        
        message1 = {'text' : 'alpha numeric word bank'}
        parser1 = message_parser(message1)
        
        self.assertTrue(parser1.contains('text', 'numeric'))
        self.assertTrue(parser1.contains('text', 'numeric', case_sensitive=True))
        self.assertTrue(not parser1.contains('text', 'numeriC', case_sensitive=True))
        self.assertTrue(parser1.contains('text', 'numeric', require_all = True))
        self.assertTrue(parser1.contains('text', ['numeric', 'word'], require_all = True))
        self.assertTrue(not parser1.contains('text', ['numeric', 'wordle'], require_all = True))
        self.assertTrue(parser1.contains('text', ['numeric'], require_all = True, case_sensitive=True))
        self.assertTrue(not parser1.contains('texted', 'numeric', require_all = True))
        
        
    def test_media_url(self):
        
        message = deepcopy(self.expected_message_format)
        parser = message_parser(message)
        
        self.assertEqual(parser.media_url, [])
        
        message['entities'] = {'media' : [{'media_url' : 'http://www.example.com'}]}
        parser = message_parser(message)
        self.assertEqual(parser.media_url[0], 'http://www.example.com')
        self.assertEqual(len(parser.media_url), 1)
        
        message['entities']['media'].append({'media_url' : 'http://www.example2.com'})
        parser = message_parser(message)
        self.assertEqual(parser.media_url[0], 'http://www.example.com')
        self.assertEqual(parser.media_url[1], 'http://www.example2.com')
        self.assertEqual(len(parser.media_url), 2)
        
        message['entities']['media'].append({'media_url' : 'http://www.example.com'})
        parser = message_parser(message)
        self.assertEqual(parser.media_url[0], 'http://www.example.com')
        self.assertEqual(parser.media_url[1], 'http://www.example2.com')
        self.assertEqual(len(parser.media_url), 2)
        
        
    
    

if __name__ == '__main__':
    unittest.main()