import os, subprocess

staticjs = subprocess.check_output(["$(npm bin)/babel --plugins transform-react-jsx " + os.getcwd() + "/client/jsx/HelloWorld.jsx"], shell=True)
file = open("static/js/HelloWorld.js", "w")
file.write(staticjs)
file.close()
