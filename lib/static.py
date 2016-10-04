import bottle

@bottle.get('/<filename:re:.*\.js>')
def javascripts(filename):
  return bottle.static_file(filename, root='static/js')

@bottle.get('/<filename:re:.*\.css>')
def stylesheets(filename):
  return bottle.static_file(filename, root='static/css')

@bottle.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
  return bottle.static_file(filename, root='static/img')
