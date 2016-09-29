import bottle

@bottle.route('/')
def hello():
  return bottle.template('client/index.tpl')
