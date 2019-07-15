def addDict(dict1, dict2):
    if type(dict1) == 'dict':
        dict1.update(dict2)
        return dict1
    else:
        print('not dict')

print(addDict({'a': 1}, {'b': 2}))
#print(addDict([1, 2], [3, 4]))
