
# Pyact Boilerplate (Python (Bottle.py) + React)
I decided I wanted to build a game in python/react (https://github.com/smtheard/push-game) and implemented this as a proof of concept. Turned out to be a pretty nice boilerplate so I am saving it here for future projects.


## Instructions

Deps:
```sh
sudo apt-get install python-pip
sudo pip install bottle
npm install
# On some linux distros you may need this command:
sudo ln -s /usr/bin/nodejs /usr/bin/node
# if you get the error: /usr/bin/env: ‘node’: No such file or directory
```

### Start Server
```sh
python server.py
```
That's it. You can visit localhost:8080 to see the react being rendered.
