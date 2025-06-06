from flask import Flask, render_template, request
import random
from datetime import datetime
import requests
app = Flask(__name__)

@app.route('/')
def index(name=None):
    random_number= random.randint(1, 100)
    copy_right= datetime.now().year
    return render_template("index.html",num=random_number,year=copy_right)

@app.route('/guess/<name>')
def guess(name):
    url= "https://api.genderize.io"
    response = requests.get(url,params={'name':name}).json()
    age_url= "https://api.agify.io"
    age_response= requests.get(age_url,params={'name':name}).json()
    return render_template("guess.html",name=response['name'],gender=response['gender'],age=age_response['age'])

@app.route('/blog')
def blogs():
    url="https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(url).json()

    return render_template("blog.html",all_posts=all_posts)



if __name__ == '__main__':
    app.run(debug=True)
