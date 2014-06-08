Twitter Extractor
=================

General Framework for Extracting Information From a Twitter Feed


This is very much a work in progress, so use at your own risk.


A general framework for working with the keyword twitter feed.  Information extraction based upon keyword, inference, and statistical natural language processing.

A live demonstration of the framework is available at: http://www.semanticneural.net
- As I get a chance, I will Open Source this implementation, and make the archive available via GitHub.  Right now the extractor searches for tweets that contain the word beer and also contain an image.  Tweets are live, and sent to the client via socket.io from a node.js server.


Dependencies:

Tweepy library (provides basic twitter integration) https://github.com/tweepy/tweepy/

Usage:

You will need to register with Twitter as a developer: https://dev.twitter.com/
The files are setup to use a twitter credential dictionary located in a /config folder at the top level.

```
data = {}

data['twitter_credentials'] = {'consumer_key' : "CONSUMER_KEY",
                               'consumer_secret' : "CONSUMER_SECRET",
                               'access_token' : "ACCESS_TOKEN",
                               'access_token_secret' : "ACCESS_TOKEN_SECRET"}
```

For an example of using the library checkout example_stream_reader.py

First we import the appropriate files from the twitter_interface package
```
from twitter_interface.stream_reader import stream_reader
from twitter_interface.message_parser import message_parser as message_parser
```    

Next, we create the stream reader object by passing our twitter credentials, and a callback function to handle the stream of tweets
```
reader = stream_reader(config.data['twitter_credentials'], processTexts)
```

The start_consuming method of the stream reader creates the streaming connection with twitter and feeds received tweets to the callback function, this stream reader filters for tweet that have the word "beer" in some part of the tweet
```
reader.start_consuming(['beer'])
```

For this simple example, I'm using a callback function that analyzes the tweets and catagorizes them as either being about Budweiser, Coors, or some other beer.  A message parser object provides options for inspecting the tweet and it's various properties.  In this case, it simply looks for presence of certain words.  
```
def processTexts(data):
    m_parser = message_parser(data)
    if m_parser.contains('text', ['coors', 'coors lite', 'coors light', ]):
        print 'Coors Beer Tweet: '
        print data
    elif m_parser.contains('text', ['bud', 'bud light', 'budweiser', 'bud lite', ]):
        print 'Budeweiser Tweet: '
        print data
    else:
        print 'Other Beer Tweet: '
        print data
```

If you're thinking about using this in a production environment, it is highly advisable NOT to have you're callback function do any heavy processing.  The twitter stream can be quite resoure instensive, and it is best to place raw tweets into a queue like rabbitMQ, zeroMQ etc., and then consume from the queue.  If you're consumer is directly attached to the twitter stream, you will be disconnected by Twitter's streaming server if you can't keep up with incoming messages, so placing them in a queue is the best way to insure stable operation.

