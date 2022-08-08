from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "survey sauce"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_form', methods=['POST'])
def redirect_submit():
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['favorites'] = request.form['favorites']
    session['comments'] = request.form['comments']
    print(request.form)
    print(session)
    return redirect('/result')


@app.route('/result')
def result():
    result_form = {
        'name': session['name'],
        'locations': session['locations'],
        'favorites': session['favorites'],
        'comments': session['comments'],
    }
    return render_template('result.html', result_form=result_form)


if __name__ == "__main__":
    app.run(debug=True)
