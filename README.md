
# Pyact Boilerplate (Python (Bottle.py) + React)
I decided I wanted to build a game in python/react (https://github.com/smtheard/push-game) and implemented this as a proof of concept. Turned out to be a pretty nice boilerplate so I am saving it here for future projects.


## Instructions

Deps:
```sh
sudo apt-get install python-pip
sudo pip install bottle
```

### Start Server
```sh
python server.py
```
That's it. You can visit localhost:8080 to see the react being rendered.


There are a ton of improvements that could be made to this but I want to keep it really light weight as well. 

Future Improvements:
- static file serving should just be at /static/app.js and then something should compile the jsx to js, the js should be served from there

The problem with this is I want to do it without having an external node.js microservice dependency. I will need to spend more time to get this to work.