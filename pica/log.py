__name__   = 'log'
__author__ = 'Sam'

from pica import config


def debug(line):
    if config.get('General','debug'):
        print(line+"\n")