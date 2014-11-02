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
    if p.lower() in ('yes', 'on'):
        return True
    elif p.lower() in ('no', 'off'):
        return False
    return p