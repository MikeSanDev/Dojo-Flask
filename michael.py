from flask import Flask  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/success')
def success():
    return "success"


@app.route('/dojo')
def dojo():
    return "Dojo!"


@app.route('/say/<string:flask>/')
def flask(flask):
    return f"Hi {flask}"


@app.route('/say/<michael>')
def michael(michael):
    return f"Hi {michael}"


@app.route('/say/<john>')
def john(john):
    return f"Hi {john}"


@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    return f"{word * num}"


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
