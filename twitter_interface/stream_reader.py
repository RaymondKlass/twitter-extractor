from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

""" Handles the raw stream of data coming from the twitter stream
    Relies on the Tweepy library for twitter integration https://github.com/tweepy/tweepy/ """
class stream_reader(object):
    
    
    def __init__(self, twitter_credentials):
        
        self.listener = self.stdOutListener()
        self.auth = OAuthHandler(twitter_credentials['consumer_key'], twitter_credentials['consumer_secret'])
        self.auth.set_access_token(twitter_credentials['access_token'], twitter_credentials['access_token_secret'])
        
    
    def start_consuming(self, filter_string):
        
        self.stream = Stream(self.auth, self.listener)
        self.stream.filter(track = filter_string)
    
    
    
    class stdOutListener(StreamListener):
        
        def on_data(self, data):
            print json.loads(data)
            
        
        def on_error(self, status):
            print status
        
        

if __name__ == '__main__':
    pass
            