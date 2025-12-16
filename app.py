from flask import Flask, render_template

app = Flask(__name__)  


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bonjour/<nom>")
def bonjour(nom):
    return render_template("bonjour.html", nom=nom)


if __name__ == "__main__":
    app.run(debug=True)
