import pika, json, sys
from twitter_interface.message_parser import message_parser as message_parser
from config import data as config_data


credentials = pika.PlainCredentials(config_data['rabbitMQ_credentials']['username'], config_data['rabbitMQ_credentials']['password'])
parameters = pika.ConnectionParameters(host = config_data['rabbitMQ_credentials']['host'], credentials = credentials)
queue_connection = pika.BlockingConnection(parameters)
rabbit_channel = queue_connection.channel()
rabbit_channel.queue_declare('raw_twitter')
rabbit_channel.basic_qos(prefetch_count=4) # This is the workaround

def callback(ch, method, properties, body):
    print 'consumer'
    body = json.loads(body)
    
    isCoors = message_parser(body)
    if isCoors.contains('text', ['coors', 'coors lite', 'coors light']):
        print body
    elif isCoors.contains('text', ['beer', 'drink', 'bar']):
        print 'BEER: ' +body['text']
    else:
        print 'NOT BAR: ' + body['text']
    if body['coordinates'] != None:
        print body['coordinates']
    
    ch.basic_ack(delivery_tag = method.delivery_tag)
        
        
rabbit_channel.basic_consume(callback, queue = 'raw_twitter')
print '[+] Waiting For Messages...'
rabbit_channel.start_consuming()
