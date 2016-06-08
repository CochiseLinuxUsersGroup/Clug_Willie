# coding=utf-8
"""
ping.py - Sopel Ping Module
Author: Sean B. Palmer, inamidst.com

bye.py
2016, hippyjake [hippyjake@gmail.com]

About: http://sopel.chat
"""
from __future__ import unicode_literals

import random
import re

from sopel.module import priority, rate

# list of all the regexes and their associated responses
regexes = [
    {
        'regex': r'(?i).*(later).*$',
        'response': ["Have a good one!","Bye!","Go on, Get! {} Go! Be Free","Good riddance. Crap {} is still here."]
    }
]

authorized_chans = ['#cochiselinux']


@priority('high')
@rate(120)
def helper(bot, trigger):
    """
    Scan messages and react on some well-chosen keywords
    """
    if trigger.sender in authorized_chans:
        # only reply if we are in an authorized channel
        for regex in regexes:
            if re.match(regex['regex'], trigger.group(1)):
                response = random.choice(regex['response']).replace(
                    '{}', trigger.nick)
                bot.say(response)

# add the @rules to the func
helper.rule = []
for regex in regexes:
    helper.rule.append(regex['regex'])
