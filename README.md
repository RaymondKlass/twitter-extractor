twitter-extractor
=================

General Framework for Extracting Information From a Twitter Feed


This is very much a work in progress, so use at your own risk.


A general framework for working with the keyword twitter feed.  Information extraction based upon keyword, inference, and statistical natural language processing.

A live demonstration of the framework is available at: http://www.semanticneural.net
- As I get a chance, I will Open Source this implementation, and make the archive available via GitHub.  Right now the extractor searches for tweets that contain the word beer and also contain an image.  Tweets are live, and sent to the client via socket.io from a node.io server.


Dependencies:

Tweepy library (provides basic twitter integration) https://github.com/tweepy/tweepy/