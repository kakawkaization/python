def addDict(dict1, dict2):
    dict_templ = type({})
    list_keys = []
    #d_1, d_2 = {}, {}
    d_1 = dict1.copy()
    d_2 = dict2.copy()
    if type(dict1) == dict_templ:
        for i in dict1:
            for j in dict2:
                if i == j:
                    list_keys.append(i)
        if list_keys:
            d_2.update(dict1)
            d_1.update(dict2)
            return ('same key, when key',  i, "=", dict1[i], d_2, '\n',
            'same key, when key', j, '=', dict2[j], d_1)
        else:
            dict1.update(dict2)
            return dict1
    else:
        print('not dict')

#print(addDict({'a': 1}, {'b': 2}))
print(addDict({'a': 1, 'f': 7, 'c': 4, 'd': 5}, {'b': 3, 'd': 3, 'f': 2, 'c': 2}))
#print(addDict([1, 2], [3, 4]))
