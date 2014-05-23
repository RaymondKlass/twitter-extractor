import pika, json
from twitter_interface.message_parser import message_parser as message_parser

queue_connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
rabbit_channel = queue_connection.channel()

def callback(ch, method, properties, body):
    print 'consumer'
    body = json.loads(body)
    
    isCoors = message_parser(body)
    if isCoors.contains('text', ['coors', 'coors lite', 'coors light']):
        print body
    elif isCoors.contains('text', ['beer', 'drink', 'bar']):
        print 'BEER PLUS: ' +body['text']
    else:
        print 'NOT COORS: ' + body['text']
    if body['coordinates'] != None:
        print body['coordinates']
        raw_input()
    
    ch.basic_ack(delivery_tag = method.delivery_tag)
        
        
rabbit_channel.basic_consume(callback, queue = 'raw_twitter')