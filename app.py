from flask import Flask , render_template, flash

app = Flask(__name__)
app.secret_key = b'\xb3\xf0\x1dR\x08o\xc8\xff'

@app.route("/")
def index():
    name01 = "name 01"
    msg01  = "Message 01"
    flash(name01)
    flash(msg01)
    name02 = "name 02"
    msg02  = "Message 02"
    flash(name02)
    flash(msg02)

    # return render_template("index.html", name_1 = name01, msg_1 = msg01, name_2 = name02, msg_2 = msg02)
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return "Page Not Found...", 404

#--------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0')