# coding=utf8
"""
welcome.py
Copyright 2015, dimaahawk [gist.github.com/dimaahawk]
2016, hippyjake [hippyjake@gmail.com]

An module for the Phenny/Willie/Sopel IRC Bots.
"""

from sopel.module import *
import random

welcomes = ['Welcome to CLUG. Also I\'m a bot','Nice of you to join us.','What is the secret password?']
vipList = ['Clug_Willie']

@event('JOIN')
@rule(r'.*')
def welcome(bot, trigger):
        nickname = trigger.nick
        choice = random.choice(welcomes)
        if nickname in vipList:
                return
        else:
                bot.say(nickname + ', ' + choice)
