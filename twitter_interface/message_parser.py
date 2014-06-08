import re 
from twitter_interface.exceptions import EmptySearchList



class message_parser(object):
    """ Message parser to aid in message classification tasks """
    
    def __init__(self, message):
        self.message = message
   
        
    def regex_parser(self, field, expression):
        """ Parses a message field based on a given regular expression """
        
        try:
            return re.match(expression, self.message[field])
        except KeyError:
            return False
    
    
    
    def contains(self, field, search_list, case_sensitive = False, require_all = False):
        """ 
            Returns whether a message field contains any or all word from a search list 
            Accepts a single field to test upon, and a list of search terms 
        """
        
        try:
            search_field = self.message[field]
        except KeyError:
            return False

        
        if isinstance(search_list, basestring):
             search_list = search_list.strip().split(' ')
        
        try:
            el = search_list[0]
        except KeyError:
            raise EmptySearchList
        
        
        
        if not case_sensitive:
            search_field = search_field.lower()
            search_list = [word.lower() for word in search_list]
        
        
        for word in search_list:
            if word not in search_field and require_all:
                return False
            
            if word in search_field and not require_all:
                return True
        
        if require_all:
            return True
        else:
            return False
                
    