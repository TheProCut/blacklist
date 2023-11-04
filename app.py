from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_ban", methods=["POST"])
def check_ban():
    username = request.form["username"]

    is_banned = False

    if is_banned:
        return "true"
    else:
        return "false"

if __name__ == "__main__":
    app.run(debug=True)
