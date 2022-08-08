from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)

app.secret_key = "number sauce"


@app.route('/')
def index():
    if "num" not in session:
        session["num"] = random.randint(1, 100)

    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
