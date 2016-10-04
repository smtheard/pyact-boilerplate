import bottle

@bottle.route('/')
def hello():
  return bottle.template('index.tpl')
