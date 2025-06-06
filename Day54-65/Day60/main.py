from flask import Flask, render_template
from login import LoginModel
from flask_bootstrap import Bootstrap5
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key="asdasdadlk nlanjslkdad;asdasdadlk nlanjslkdad"

bootstrap = Bootstrap5(app)
@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginModel()
    form.validate_on_submit()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        if form.username.data == 'admin' and form.password.data == 'password':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
