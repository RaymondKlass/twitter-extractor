from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, pika

""" Handles the raw stream of data coming from the twitter stream
    Relies on the Tweepy library for twitter integration https://github.com/tweepy/tweepy/ """

class stream_reader(object):
    
    
    def __init__(self, twitter_credentials, rabbitMQ_credentials):
        
        self.auth = OAuthHandler(twitter_credentials['consumer_key'], twitter_credentials['consumer_secret'])
        self.auth.set_access_token(twitter_credentials['access_token'], twitter_credentials['access_token_secret'])
        
        queue_connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitMQ_credentials['host']))
        self.rabbitChannel = queue_connection.channel()
        
        self.listener = stdOutListener(self.rabbitChannel)
        
    
    def start_consuming(self, filter_list):
        
        self.stream = Stream(self.auth, self.listener)
        self.stream.filter(track = filter_list)
    
    def add2(self, num1, num2):
        return num1 + num2
    
    
class stdOutListener(StreamListener):
    
    def __init__(self, rabbitChannel):
        self.rabbitChannel = rabbitChannel
    
    def on_data(self, data):
        
        self.rabbitChannel.basic_publish(exchange = '',
                                         routing_key = 'raw_twitter',
                                         body = data ) 
        
        
    
    def on_error(self, status):
        print status
        
        

if __name__ == '__main__':
    pass
            