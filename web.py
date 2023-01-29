from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html.j2")

@app.route("/aboutmodel")
def about_model():
    return render_template("about_model.html.j2")

@app.route("/testviewer")
def test_viewer():
    return render_template("test_viewer.html.j2")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

