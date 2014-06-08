class TwitterInterfaceExceptions(Exception):
    """ Exception base class """
    pass

class EmptySearchList(TwitterInterfaceExceptions):
    """ Search list of terms was empty """
    pass