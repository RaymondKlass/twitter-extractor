import config as config
from twitter_interface.stream_reader import stream_reader

import time

reader = stream_reader(config.data['twitter_credentials'], config.data['rabbitMQ_credentials'])
reader.start_consuming(['beer'])


