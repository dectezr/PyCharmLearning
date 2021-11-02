import json


# write your code here
json_object = input()
json_object_converted = json.loads(json_object)
print(type(json_object_converted))
print(json_object_converted)
