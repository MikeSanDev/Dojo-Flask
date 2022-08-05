from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def blueboxes():
    return render_template("play.html")


@app.route("/play/<number_of_boxes>")
def block_repeat(number_of_boxes):
    repeat = int(number_of_boxes)
    return render_template('play2.html', repeat=repeat)


@app.route("/play/<number_of_boxes>/<color_change>")
def box_color(number_of_boxes, color_change):
    repeat = (int(number_of_boxes))
    colorChange = color_change
    return render_template('play3.html', repeat=repeat, colorChange=colorChange)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
