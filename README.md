
# Pyact Boilerplate (Python (Bottle.py) + React)
I decided I wanted to build a game in python/react (https://github.com/smtheard/push-game) and implemented this as a proof of concept. Turned out to be a pretty nice boilerplate so I am saving it here for future projects.


## Instructions

### Dependencies:
```sh
sudo pip install bottle
npm install
# if you get the error: /usr/bin/env: ‘node’: No such file or directory
# you may need this command to symlink nodejs -> node (happens on some linux distros)
sudo ln -s /usr/bin/nodejs /usr/bin/node
```

### Start Server
```sh
python server.py
```
That's it. You can visit localhost:8080 to see the react being rendered.


## Extra Details

This is transpiling jsx -> js for front end consumption. You can check static/js/HelloWorld.js to see the compiled version of the client/jsx/HelloWorld.jsx file. Generally I don't think you would want to check this in, but it is here for demonstration. This gets generated automagically every time you run server.py via importing transpile.py. 

A couple improvements I would recommend making post-clone:
- transpile.py could just take everything in the client/jsx directory and compile it to a static js file one by one.
- index.tpl could use some python magic to generate the imports for each js file in the static directory
- serving statics should happen through nginx or lighttpd, several orders of magnitude faster than serving them from python (thanks to https://github.com/rayluu for the suggestion)

I want to keep this as lean as possible so I am going to not include those here. They will be in my push-game repo however.
