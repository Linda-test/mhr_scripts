import json
with open("./profile_data_list.json") as f:
    json_data = f.read()
json_to_python = json.loads(json_data)
print (json_to_python)
print('______________________')
print (type(json_to_python))
print (json_to_python['first_name'])