from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def main():  # put application's code here
    return render_template("main.html")


@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):  # put application's code here
    return f'User name: {name}, id: {id}'


if __name__ == '__main__':
    app.run(debug=True)
