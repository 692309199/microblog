from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'owen'}
    posts = [
	{
		'author':{'nickname':'John'},
		'body': 'Beautiful day in Portland!'
	},
	{
                'author':{'nickname':'Susan'},
                'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
	title = 'Home',
        user = user,
	posts = posts)
#<html>
#  <head>
#   <title>Home Page</title>
#  </head>
#  <body>
#    <h1>hello, ''' + user['nickname'] + '''</h1>
#  </body>
#<html>
#'''
