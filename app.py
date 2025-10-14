from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    # Get name and age from query params
    name = request.args.get('name', 'Player')
    age = request.args.get('age', 0)
    return render_template('game.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
