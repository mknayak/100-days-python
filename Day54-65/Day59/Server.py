from flask import Flask, request, jsonify, render_template, redirect
import requests
from post import Post
from message import Message
import smtplib
FROM_ADDRESS = 'study.creekworm@gmail.com'
APP_USERNAME='PythonApp'
APP_PASSWORD = 'ltxt jazu irfo arku'

def send_email(name,email,message,phone):
 with smtplib.SMTP('smtp.gmail.com', 25) as smtp_client:
     smtp_client.starttls()
     login = smtp_client.login(FROM_ADDRESS, APP_PASSWORD)
     subject="Hello User"
     body=f"name:{name}\nemail:{email}\nmessage:{message}\nphone:{phone}"

     message=f"SUBJECT:{subject}\n\n{body}"
     smtp_client.sendmail(FROM_ADDRESS,email,message)
app = Flask(__name__)

@app.route('/')
def index():
    url="https://api.npoint.io/674f5423f73deab1e9a7"
    api_json = requests.get(url).json()
    posts= [Post(n) for n in api_json]
    return render_template("index.html",blogs=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    url="https://api.npoint.io/674f5423f73deab1e9a7"
    api_json = requests.get(url).json()
    post = [Post(n) for n in api_json if n["id"] == post_id][0]
    return render_template("post.html",post=post)

messages=[]
@app.route('/contact')
def contact():
    return render_template("contact.html", messages=messages)

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    phone = request.form['phone']
    messages.append(Message(name,email,message,phone))
    send_email(name,email,message,phone)
    return redirect('/contact')

@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)