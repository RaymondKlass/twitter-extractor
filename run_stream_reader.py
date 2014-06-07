import time
from twitter_interface.stream_reader import stream_reader
from twitter_interface.message_parser import message_parser as message_parser
import config as config


def processTexts(data):
    print 'data_parse'
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

reader = stream_reader(config.data['twitter_credentials'], processTexts) 
reader.start_consuming(['beer'])


