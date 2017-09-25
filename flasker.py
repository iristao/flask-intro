from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')

def root():
	print 'HelloFirst'
	return "Hellow Route"

@my_app.route('/route1')
def route1():
	print 'hey route1'
	return 'hi route1'

@my_app.route('/route2')
def route2():
	print 'hey route2'
	return 'hi route2'

if __name__ == '__main__':
	my_app.debug = True
	my_app.run()

