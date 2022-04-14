from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = {
            'user': 'stefany',
            'gender': 'm',
            'email': 'stefany@gmail.com',
            'pelis': ['titanic', 'garfly']
            }
    return render_template("home.html", ctx=data)


@app.route("/blog")
def blog():
    data = {
            'user': 'stefany',
            'gender': 'm',
            'email': 'stefany@gmail.com',
            'pelis': ['titanic', 'garfly']
            }
    return render_template("blog.html", ctx=data)

if __name__ == "__main__":
    app.run(debug=False)