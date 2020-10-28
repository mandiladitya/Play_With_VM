import requests
import os
from flask import Flask,render_template,send_file,request,url_for,session,redirect

import pyrebase

config = {
      "apiKey": "AIzaSyCOVRvLK4SdQBHw2BNAmPXF45Nhck8ddaY",
    "authDomain": "issac-8543d.firebaseapp.com",
    "databaseURL": "https://issac-8543d.firebaseio.com",
    "projectId": "issac-8543d",
    "storageBucket": "issac-8543d.appspot.com",
    "messagingSenderId": "314588981800",
    "appId": "1:314588981800:web:71aa8a1f04f88cd94e231d"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
un="Please Check Your Crendtials !"
app = Flask(__name__)
app.secret_key = 'any random string'
@app.route('/button')
def content():
	os.system('./some.sh > textfile.txt')
	with open('textfile.txt','r') as f:
		return render_template('content.html',text=f.read())

# Ubuntu VM
@app.route('/ubuntu')
def ubuntu():
	if 'username' in session:
		name=session['username']
		os.system('./script/ubuntu.sh > ./textfiles/ubuntu.txt')
		with open('./textfiles/ubuntu.txt','r') as f:
			return render_template('ubuntu.html',text=f.read(),name=name)
	else:
		return redirect(url_for('home'))
@app.route('/',methods = ['POST', 'GET'])
def home():
	if 'username' in session:
		name=session['username']
		return render_template('index.html',name=name)
	if (request.method == 'POST'):
		name =request.form["name"]
		email =request.form["email"]
		password =  request.form["password"]
		session['username'] = name
		try:
			user = auth.sign_in_with_email_and_password(email, password)
			return render_template('index.html',name=name)
		except:
			return render_template('login.html',un=un)
	return render_template('login.html')
@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('home'))
@app.route('/index')
def index1():
	return render_template('index.html')
@app.route('/signup',methods = ['POST', 'GET'])
def signup():
	if 'username' in session:
		name=session['username']
		return render_template('index.html',name=name)
	if (request.method == 'POST'):
		name =request.form["name"]
		email =request.form["email"]
		password =  request.form["password"]
		try:
			user = auth.create_user_with_email_and_password(email, password)
			return render_template('index.html',name=name)
		except:
			return render_template('signup.html',un=un)
	return render_template('signup.html')


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
	if 'username' in session:
		name=session['username']
		os.system('./script/unodejs.sh > ./textfiles/unodejs.txt')
		with open('./textfiles/unodejs.txt','r') as f:
			return render_template('unodejs.html',text=f.read(),n1=name)
	else:
		return redirect(url_for('home'))

# contact page
@app.route('/contact')
def contact():
	return render_template('contact.html')
# upython
@app.route('/upython')
def upython():
	if 'username' in session:
		name=session['username']
		os.system('./script/upython.sh > ./textfiles/upython.txt')
		with open('./textfiles/upython.txt','r') as f:
			return render_template('upython.html',text=f.read(),name=name)
	else:
		return redirect(url_for('home'))

@app.route('/centos')
def centos():
	if 'username' in session:
		name=session['username']
		os.system('./script/centos.sh > ./textfiles/centos.txt')
		with open('./textfiles/centos.txt','r') as f:
			return render_template('centos.html',text=f.read(),name=name)
	else:
		return redirect(url_for('home'))



@app.route('/cpython')
def cpython():
	if 'username' in session:
		name=session['username']
		os.system('./script/cpython.sh > ./textfiles/cpython.txt')
		with open('./textfiles/cpython.txt','r') as f:
			return render_template('cpython.html',text=f.read(),name=name)
	else:
		return redirect(url_for('home'))
@app.route('/cnodejs')
def cnodejs():
	#if 'username' in session:
	#	name=session['username']
	#	os.system('./script/cnodejs.sh > ./textfiles/cnodejs.txt')
	#	with open('./textfiles/cnodejs.txt','r') as f:
	#		return render_template('cnodejs.html',text=f.read(),name=name)
	#else:
	#	return redirect(url_for('home'))
	return " Sorry Right Now Centos + Nodejs NOT Working "

@app.errorhandler(404)
def error(e):
	return render_template('error.html')


@app.route('/login2')
def login2():
	return render_template('login2.html')
app.run(host='0.0.0.0',debug=True)
