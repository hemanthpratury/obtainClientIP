from flask import Flask, render_template
import requests
import cgi
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/cakes')
def cakes():
    return 'Yummy Cakes!'

@app.route('/statusAPI')
def statusAPI():
    return

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name = name)


@app.route('/net')
def net():
	print "content-type: text/html"
	print ""
	print cgi.escape(os.environ["REMOTE_ADDR"])

@app.route('/connectedToInternet')
def connectedToInternet():
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip="blank"
	print('ip')
	return ip


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
