import json
import requests
from pprint import pprint

# See tutorial page for more info:
# http://docs.python-requests.org/en/latest/user/quickstart/

r1 = requests.get("http://127.0.0.1:5000/api/v1.0/tasks/1")
print "JSON response for GET on /api/v1.0/tasks/1"
pprint(r1.json())
print ""

r2 = requests.get("http://127.0.0.1:5000/api/v1.0/tasks/2")
print "JSON response for GET on /api/v1.0/tasks/2"
pprint(r2.json())
print ""

payload = {
            "title": 'Make a new todo',
            "description": 'Try putting in a new todo item!',
            "done": False
            }
r3 = requests.post("http://127.0.0.1:5000/api/v1.0/tasks/3",
                   data=json.dumps(payload))
print "JSON response for POST on /api/v1.0/tasks/3"
pprint(r3.json())
print ""


r4 = requests.get("http://127.0.0.1:5000/api/v1.0/tasks/3")
print "JSON response for GET on /api/v1.0/tasks/3"
pprint(r4.json())
print ""

query = {'title': 'lol', 'name': 'Jason'}
r5 = requests.get("http://127.0.0.1:5000/api/v1.0/query", data=query)
print "JSON response for GET on /api/v1.0/query with query parameters"
pprint(r5.json())
print ""
