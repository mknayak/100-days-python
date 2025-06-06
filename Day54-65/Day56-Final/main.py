from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

@app.route('/')
def home():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(url).json()
    blogs=[]
    for post in all_posts:
        blogs.append(Post(post))
    return render_template("index.html",blog_posts=blogs)

@app.route('/post/<blog_id>')
def posts(blog_id):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_posts = requests.get(url).json()
    blog_post = Post([ n for n in all_posts if n["id"]==int(blog_id) ][0])

    return render_template("post.html",post=blog_post)

if __name__ == "__main__":
    app.run(debug=True)
