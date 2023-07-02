from flask import Flask, render_template, request

from jpeg.app import Card

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        birthday = request.form["birthday"]
        language = request.form["language"]
        gender = request.form["gender"]
        card = Card(name, birthday, language, gender)
        return render_template("card.html", name=name, birthday=birthday, card=card)
    else:
        return render_template("index.html")


@app.route("/card")
def card():
    return render_template("card.html")


if __name__ == "__main__":
    app.run(debug=True)
