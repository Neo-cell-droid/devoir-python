from flask import Flask, render_template, request
app = Flask(__name__)  


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bonjour/<nom>")
def bonjour(nom):
    return render_template("bonjour.html", nom=nom)

@app.route("/somme/<int:a>/<int:b>")
def somme(a, b):
    resultat = a + b
    if resultat > 0:
        texte = "positif"
    elif resultat < 0:
        texte = "négatif"
    else:
        texte = "nul"
    return render_template("somme.html", a=a, b=b, resultat=resultat, texte=texte)

@app.route("/operation", methods=["GET", "POST"])
def operation():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        operation = request.form["operation"]
        if operation == "+":
            resultat = a + b
        elif operation == "-":
            resultat = a - b
        elif operation == "*":
            resultat = a * b
        elif operation == "/":
            resultat = a / b
        return render_template("operation.html", resultat=resultat)
    return render_template("operation.html")


if __name__ == "__main__":
    app.run(debug=True)
