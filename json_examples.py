# Showcases how to load, write and interact with json
# I know lame, but I always spent 5 mins searching for the correct syntax
import json

# Load json from string
user = json.loads('{ "name":"John", "age":30, "city":"New York"}')
print(user['name'])

# Write json
with open('user.json', 'w') as f:
    json.dump(user, f)

# Load json from file
members = json.load(open("user.json"))