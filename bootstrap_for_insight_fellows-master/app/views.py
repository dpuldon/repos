from flask import render_template
from app import app
from flask import request




@app.route('/')
def index():
   user = '' # fake user
   return render_template("index.html",
       title = 'Home',
       user = user)


