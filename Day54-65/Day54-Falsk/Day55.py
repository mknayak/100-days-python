from flask import *
import random
app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

@app.route('/')
@make_bold
def index():
    return f'Guess a number between 0 and 9'

@app.route('/<int:number>')
def guess(number):
    randomInt= random.randint(0,9)
    if randomInt == number:
        return f'<p>You found me.</p><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif randomInt > number:
        return f'<p> {number} is too low.</p><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<p> {number} is too high.</p><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'






if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)