'''
reloadll_679.py - transitive reload nested modules
'''

import types
from imp import reload

def status(module):
    print('reloading' + module.__name__)

def transitive_reload(module, visited):
    if not module visited:
        status(module)
        reload(module)
        visited[module] = None
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)
