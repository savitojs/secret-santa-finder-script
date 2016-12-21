#!/usr/bin/python
# Written by: Savitoj Singh (savitoj@gmail.com)
# Very raw written but working ;)
import random
import os
import time
_from = ['bob','foo','bar','savsingh','tom','jack','mac','hex']
_to = ['bob','foo','bar','savsingh','tom','jack','mac','hex']

for i in range(len(_from)):
    user_name = raw_input('Welcome.. What is your nick name? [ENTER] ')
    print('')
    print('Hey ' + user_name + '!, Hold on!! Looking for your secret santa')
    print('')
    random.shuffle(_from)
    _from.remove(user_name)
    print('Any guess... ?')
    print('')
    time.sleep(1)
    a = random.choice(_to)
    _to.remove(a)
    print('Here you go .. ' + a)
    raw_input('Enter to clear screen [ENTER]')
    os.system('clear')
