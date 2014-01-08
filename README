# API Server
## Sample implementation

### Core Technologies
- Flask
- Flask-RESTful
- requests (for testing)


### Installation
1. (Recommended) Create a virtualenv to enclose the repo
2. Install the prerequisite modules

```
pip install -r requirements.txt
```

3. python server.py


### Testing with HTTPie (recommended)
1. Install HTTPie

```
pip install --upgrade httpie
```

2. Run some test commands in shell

```
$ http http://127.0.0.1:5000/api/v1.0/tasks/1
$ http get http://127.0.0.1:5000/api/v1.0/tasks/2
$ http -v post http://127.0.0.1:5000/api/v1.0/tasks/3 title='Make a new todo' description='Try putting in a new todo item!' done:=false
$ http get http://127.0.0.1:5000/api/v1.0/tasks/3
$ http get http://127.0.0.1:5000/api/v1.0/query title=lol name=jason
```


### Testing with Python 
Run `client.py` for the above example replicated in Python using the Requests library
