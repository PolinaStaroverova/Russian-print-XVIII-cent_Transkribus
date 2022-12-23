from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/about_model.html")
def about_model():
    return render_template("about_model.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

