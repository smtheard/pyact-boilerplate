import bottle
# Static Routes:
@bottle.get('/<filename:re:.*\.js>')
def javascripts(filename):
  return bottle.static_file(filename, root='client/js')

@bottle.get('/<filename:re:.*\.jsx>')
def jsxs(filename):
  return bottle.static_file(filename, root='client/jsx')

@bottle.get('/<filename:re:.*\.css>')
def stylesheets(filename):
  return bottle.static_file(filename, root='client/css')

@bottle.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
  return bottle.static_file(filename, root='client/img')

import lib.hello
