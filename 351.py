fruits_reference = {1: "apple", 2: "banana", 3: "cherry"}

class MyDictKeyError(Exception):
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return '登録されていません　{0}'.format(self.key)

def get_dict_value(dict_tbl, key):
    if key not in dict_tbl:
        raise MyDictKeyError(key)
    else:
        return dict_tbl[key]
my_dict = {1: 'apple', 2: 'banana'}

try:
    my_dict = get_dict_value(my_dict, 3)
except MyDictKeyError as a:
    print(a)
    key = a.args[0]
    my_dict[key] = fruits_reference[key]
    print(key, fruits_reference[key], '追加')
    my_dict = fruits_reference[key]
    print(my_dict)
