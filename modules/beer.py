# coding=utf8
"""
beer.py - Because beer is not a lie!
Copyright 2016, Kharidiron [kharidiron@gmail.com]
2016, hippyjake [hippyjake@gmail.com]
Licensed under the WTFPL. Do whatever the fuck you want with this. You just
  can't hold me responsible if it breaks something either.

An module for the Phenny/Willie/Sopel IRC Bots.
"""

from __future__ import unicode_literals, absolute_import, print_function, division
import sys

from sopel.module import commands

if sys.version_info.major >= 3:
    unichr = chr


@commands('beer')
def beer(bot, trigger):
    """Give someone some beer"""
    if not trigger.group(2):
        bot.action(u'gives {} a beer!'
                    '\U0001F37A'.format(trigger.nick))
        return

    target = trigger.group(2)
    bot.action(u'gives {} a beer! '
                'courtesy of {}! \U0001F37B'.format(target, trigger.nick))
    return 

if __name__ == '__main__':
    pass

