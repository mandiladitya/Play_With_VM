import os
from flask import Flask,render_template,send_file
app = Flask(__name__)
@app.route('/button')
def content():
	os.system('./some.sh > textfile.txt')
	with open('textfile.txt','r') as f:
		return render_template('content.html',text=f.read())

# Ubuntu VM
@app.route('/ubuntu')
def ubuntu():
	os.system('./script/ubuntu.sh > ./textfiles/ubuntu.txt')
	with open('./textfiles/ubuntu.txt','r') as f:
		return render_template('ubuntu.html',text=f.read())

@app.route('/404')
def four():
	return "Right now only Ubuntu"

# Download KEY
@app.route('/getkey')
def getkey():
	path="password.txt"
	return send_file(path,as_attachment=True)

# Service Page
@app.route('/service')
def service():
	return render_template('services.html')

# unodejs
@app.route('/unodejs')
def unodejs():
	os.system('./script/unodejs.sh > ./textfiles/unodejs.txt')
	with open('./textfiles/unodejs.txt','r') as f:
		return render_template('unodejs.html',text=f.read())

# contact page
@app.route('/contact')
def contact():
	return render_template('contact.html')
# upython
@app.route('/upython')
def upython():
        os.system('./script/upython.sh > ./textfiles/upython.txt')
        with open('./textfiles/upython.txt','r') as f:
                return render_template('upython.html',text=f.read())

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/centos')
def centos():
	os.system('./script/centos.sh > ./textfiles/centos.txt')
	with open('./textfiles/centos.txt','r') as f:
		return render_template('centos.html',text=f.read())



@app.route('/cpython')
def cpython():
        os.system('./script/cpython.sh > ./textfiles/cpython.txt')
        with open('./textfiles/cpython.txt','r') as f:
                return render_template('cpython.html',text=f.read())

@app.route('/cnodejs')
def cnodejs():
        os.system('./script/cnodejs.sh > ./textfiles/cnodejs.txt')
        with open('./textfiles/cnodejs.txt','r') as f:
                return render_template('cnodejs.html',text=f.read())
app.run(host='0.0.0.0',debug=True)
