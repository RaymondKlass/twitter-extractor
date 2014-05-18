import re


class iterableException(Exception):
    pass

# Basic parsing methods for twitter messages 
# Accepts a twitter message in the form of a dictionary
class message_parser(object):
    
    def __init__(self, message):
        
        self.message = message
        print self.message
    
    
    def regex_parser(self, field, expression):

        try:
            f = self.message[field]
        except KeyError:
            return False

        return re.match(expression, self.message[field])
        
    
    def contains(self, field, search_list):
        
        try:
            f = self.message[field]
        except KeyError:
            return False
        
        if isinstance(search_list, basestring):
             search_list = search_list.split(' ')
        
        try:
            el = search_list[0]
        except:
            raise iterableException
        
        