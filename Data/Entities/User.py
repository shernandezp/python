import json

class User:

    id = None
    username = None
    password = None
    last_login = None
    attempt = None
    status = None
    email = None

    def __init__(self, dict_ = None):
        if (dict_ is not None):
            self.__dict__.update(dict_)