import json
name_list = {
        'tanaka':{
            'age':20,
            'bloodtype':'A',
            'gender':'male'
            },
        'satou':{
            'age':19,
            'bloodtype':'O',
            'gender':'female'
            },
        'suzuki':{
            'age':20,
            'bloodtype':'AB',
            'gender':'male'
            }
        }
with open('name_list.json', 'w') as f:
    json.dump(name_list, f)

with open('name_list.json', 'r') as f:
    name_list = json.load(f)

for key, val in name_list.items():
        print(key, val)

