#!/usr/bin/python
#===============================================================================
#
#          FILE:  secret_santa.py
# 
#         USAGE:  ./secret_santa.py
# 
#   DESCRIPTION:  It can help you to find your secret santa, add participants name in _from and _to list
# 
#  REQUIREMENTS:  python 2.6+, _from list and _to list should be same to work perfectly.
#        AUTHOR:  Savitoj Singh (savitojs@gmail.com)
#       VERSION:  1.1
#       CREATED:  12/21/2016 05:13:38 AM IST
#      REVISION:  * Initial release
#                 * Fixed minor bugs
#===============================================================================
import random
import os
import time
import sys
'''Add participants to list'''
_from = ['bob','foo','bar','savsingh','tom','jack','mac','hex']
'''Add participants to list'''
_to = ['bob','foo','bar','savsingh','tom','jack','mac','hex']


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for i in range(len(_from)):
    try:
        user_name = raw_input('Hi.. What is your nick name? [ENTER] ')
        if user_name not in _from and user_name not in _to:
            try:
              print("")
              print(bcolors.FAIL + bcolors.BOLD + "Nick name doesn't seem to be in `_from` or `_to` list" + bcolors.ENDC)
              print(bcolors.HEADER + "\nDo you expect me to look in galaxy ? It may take many x'mas to retrive results :P" + bcolors.ENDC)
              break
            except:
              pass
        else:
            print('Hey ' + bcolors.OKBLUE + bcolors.BOLD + str(user_name) + bcolors.ENDC + '!, Hold on!! Searching...')
            random.shuffle(_from)
            _from.remove(user_name)
            print(bcolors.WARNING + 'Any guess... ?' + bcolors.ENDC)
            print('')
            time.sleep(1)
            a = random.choice(_to)
            while str(a) == str(user_name):
                a = random.choice(_to)
            _to.remove(a)
            print(bcolors.BOLD + 'Your secret santa is: ' + bcolors.ENDC + bcolors.OKGREEN + bcolors.BOLD + str(a) + bcolors.ENDC)
            raw_input('Clear the screen [ENTER]: ')
            os.system('reset')
    except:
        print(bcolors.FAIL + bcolors.BOLD + "\n\nOops!!, Something went wrong..." + bcolors.ENDC)
        sys.exit(1)

