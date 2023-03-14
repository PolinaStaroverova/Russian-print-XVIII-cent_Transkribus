from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/aboutmodel")
def about_model():
    return render_template("about_model.html")

@app.route("/opisanie_lagerya_sobrannogo")
def opisanie_lagerya_sobrannogo():
    return render_template("opisanie_lagerya_sobrannogo.html")

@app.route("/kto_mojhet_byt_dobrym_grazhdaninom")
def kto_mojhet_byt_dobrym_grazhdaninom():
    return render_template("kto_mojhet_byt_dobrym_grazhdaninom.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

