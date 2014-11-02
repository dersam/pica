__name__   = 'config'
__author__ = 'Sam'

import ConfigParser

params = []

def load(path):
    params = ConfigParser.ConfigParser()
    params.read(path)