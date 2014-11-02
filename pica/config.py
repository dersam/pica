__name__   = 'config'
__author__ = 'Sam'

import ConfigParser

params = None


def load(path):
    global params
    params = ConfigParser.ConfigParser()
    params.read(path)


def get(section, var):
    p = params.get(section, var)
    if p.lower() == 'yes':
        return True
    elif p.lower() == 'no':
        return False
    return p