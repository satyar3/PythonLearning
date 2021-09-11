import json

data = '{"name1" : "Satya", "Age": 26}'

parse_data = json.loads(data)
print(parse_data)
print(parse_data['Age'])

'''
Difference Between json.load and json.load

json.loads = accepts data in string format

json.load = accepts the file path inside which json data is present

json.dumps = accepts data in string format and make it javascript compatible

'''

data2 = {
    "ll" : [1,2,3,4,5],
    "tup" : ("somethig", 340),
    "isThere": False
}

new_data = json.dumps(data2)
print(new_data)

new_data = json.dumps(data2,sort_keys=True)
print(new_data)