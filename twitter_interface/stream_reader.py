from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json



class stream_reader(object):
    
    
    def __init__(self, twitter_credentials, data_callback):
        """ Create a stream reader by passing:
            1. twitter credentials ex. {access_token, access_token_secret, consumer_key, consumer_secret}
            2. function to handle data 
        """
        
        self.auth = OAuthHandler(twitter_credentials['consumer_key'], twitter_credentials['consumer_secret'])
        self.auth.set_access_token(twitter_credentials['access_token'], twitter_credentials['access_token_secret'])
        self.listener = stdOutListener(data_callback)
        
    
    def start_consuming(self, filter_list):
        """ Start consuming a twitter stream - filtering by a list passed to this method """
        
        self.stream = Stream(self.auth, self.listener)
        self.stream.filter(track = filter_list)
        
        
    
    
class stdOutListener(StreamListener):
    
    def __init__(self, callback, api=None):
        super(stdOutListener, self).__init__()
        self.callback = callback
            
    
    def on_data(self, data):
        self.callback(json.loads(data))

        
    def on_error(self, status):
        # log status
        pass
        

if __name__ == '__main__':
    pass
            