from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():
	greeting = "Hello World"
	
	if request.method == "POST":
		name = request.form['name']
		greet = request.form['greet']
		greeting = "%s, %s." % (greet, name)
		return render_template("index.html", greeting=greeting)	
	else:
		return render_template("hello_form.html")
	
@app.route('/foo')
def foo():
	greeting = 'Welcome to Foo!'
	return render_template("foo.html", greeting=greeting)
	
if __name__ == "__main__":
	app.run()


