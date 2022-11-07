from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    name_1 = "name 01"
    msg_1  = "Message 01"

    name_2 = "name 02"
    msg_2  = "Message 02"

    name_3 = "name 03"
    msg_3  = "Message 03"

    name_4 = "name 04"
    msg_4  = "Message 04"

    name_5 = "name 05"
    msg_5  = "Message 05"

    return render_template("index.html", name_1, msg_1, name_2, msg_2, name_3, msg_3, name_4, msg_4, name_5, msg_5)

@app.errorhandler(404)
def page_not_found(e):
    return "Page Not Found...", 404

#--------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0')