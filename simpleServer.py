from flask import Flask

app = Flask('simpleServer')

@app.route('/')
def index():
	return 'Hello, Amperka!'
	
app.run(port=3000, host='0.0.0.0')
