import bottle

@bottle.get('/static/js/<filename:re:.*\.js>')
def javascripts(filename):
  return bottle.static_file(filename, root='static/js')
