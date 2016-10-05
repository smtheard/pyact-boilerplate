import os, subprocess
from os import path

staticjs = subprocess.check_output(["$(npm bin)/babel --plugins transform-react-jsx " + path.dirname(path.abspath(__file__)) + "/client/jsx/HelloWorld.jsx"], shell=True)
file = open("static/js/HelloWorld.js", "w")
file.write(staticjs)
file.close()
