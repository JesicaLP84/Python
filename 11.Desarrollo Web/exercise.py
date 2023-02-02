from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/sumar/<int:n1>/<int:n2>')
def suma(n1, n2):
    return f"La suma de {n1} y {n2} es: " + str(n1 + n2)


@app.route("/usuario/<name>/<surname>")
def create_username(name: str, surname: str):
    username = name[0].lower() + surname.lower()
    return username


users = ["Antonia Gomez", "Sonia Gutierrez", "Antonio López", "Andrea Soler", "Ana Rincon"]


@app.route("/search_user")
def count_users():
    text = request.args.get("texto")
    count = 0
    for user in users:
        if text in user:
            count += 1
    return f"Se encontraron {count} usuarios que coinciden con la búsqueda: " + text


if __name__ == '__main__':
    app.run(debug=True)
