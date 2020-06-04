'''
reloadll_679.py - transitive reload nested modules
'''

import types
from imp import reload

def status(module):
    print('reloading' + module.__name__)
