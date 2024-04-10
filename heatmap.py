import Database as db
import json
file_path = './JSON/users.json'
data = 0
data2 = 0
db.register_new_user('fp', 'sangilan', file_path=file_path)
with open(file_path, 'r') as f:
    data = json.load(f)

with open('./JSON/activities.json', 'r') as f:
    data2 = json.load(f)
for i in data:
    if i["id"] == 1:
        i["activities"].append(data2[0])

for i in data:
    print(i)

with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)