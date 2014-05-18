import re


class iterableException(Exception):
    pass

# Basic parsing methods for twitter messages 
# Accepts a twitter message in the form of a dictionary
class message_parser(object):
    
    def __init__(self, message):
        
        self.message = message
    
    
    def regex_parser(self, field, expression):

        try:
            f = self.message[field]
        except KeyError:
            return False

        return re.match(expression, self.message[field])
        
    
    #  case sensitive is whether the search is case sensitive, require all is whether all words must be present - otherwise at least one is required
    def contains(self, field, search_list, case_sensitive = False, require_all = False):
        
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
        
        if not case_sensitive:
            search_field = self.message[field].lower()
        else:
            search_field = self.message[field]
        
        
        for word in search_list:
            if not case_sensitive:
                test_word = word.lower()
            else:
                test_word = word
                
            if test_word not in search_field and require_all:
                return False
            
            if test_word in search_field and not require_all:
                return True
        
        if require_all:
            return True
        else:
            return False
                
    