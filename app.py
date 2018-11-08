from flask import Flask
from flask import render_template
from database import *

app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def cat_route(id):
    name = get_cat_name(id)
    return render_template(
        'cat.html', n = id,m = name) 


if __name__ == '__main__':
   app.run(debug = True)
