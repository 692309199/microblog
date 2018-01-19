from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'owen'}
    return render_template("index.html",
           title = 'Home',
           user = user)
#<html>
#  <head>
#   <title>Home Page</title>
#  </head>
#  <body>
#    <h1>hello, ''' + user['nickname'] + '''</h1>
#  </body>
#<html>
#'''
