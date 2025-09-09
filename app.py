from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/prank")
def prank():
    return render_template("prank.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
