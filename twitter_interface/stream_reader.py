from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json, pika

""" Handles the raw stream of data coming from the twitter stream
    Relies on the Tweepy library for twitter integration https://github.com/tweepy/tweepy/ """

class stream_reader(object):
    
    
    def __init__(self, twitter_credentials, rabbitMQ_credentials, queue='raw_twitter'):
        
        self.rabbit_queue = queue
        self.auth = OAuthHandler(twitter_credentials['consumer_key'], twitter_credentials['consumer_secret'])
        self.auth.set_access_token(twitter_credentials['access_token'], twitter_credentials['access_token_secret'])
        
        queue_connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitMQ_credentials['host']))
        self.rabbit_channel = queue_connection.channel()
        
        try:
            self.rabbit_channel.queue_declare(self.rabbit_queue)
        except:
            pass # Could error if the queue has already been created under a different user - than the one running the script (permissions)
        
        self.listener = stdOutListener(self.rabbit_channel, self.rabbit_queue)
        
    
    def start_consuming(self, filter_list):
        
        self.stream = Stream(self.auth, self.listener)
        self.stream.filter(track = filter_list)
        
    
    
class stdOutListener(StreamListener):
    
    def __init__(self, rabbit_channel, queue):
        self.rabbit_queue = queue
        self.rabbit_channel = rabbit_channel
            
    
    def on_data(self, data):
        print json.loads(data).keys()
        self.rabbit_channel.basic_publish(exchange = '',
                                         routing_key = self.rabbit_queue,
                                         body = data ) 
        
    def on_error(self, status):
        print status
        
        

if __name__ == '__main__':
    pass
            