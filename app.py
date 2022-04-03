from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))
    Q1 = db.Column(db.String(80))
    Q2 = db.Column(db.String(80))
    Q3 = db.Column(db.String(80))
    Q4 = db.Column(db.String(80))
    Q5 = db.Column(db.String(80))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/win")
def win():
    return render_template("win.html")

@app.route("/cheat")
def cheat():
    return render_template("cheat.html")

@app.route("/cheat2")
def cheat2():
    return render_template("cheat2.html")

@app.route("/ning")
def ning():
    return render_template("ning.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        if uname == "camilatesorero":
            login = user.query.filter_by(username=uname, password=passw).first()
            if login is not None:
                return redirect(url_for("win"))
            return render_template("login.html")
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("cheat2"))
    return render_template("login.html")

@app.route("/forget",methods=["GET", "POST"])
def forget():
    if request.method == "POST":
        email = request.form["email"]
        A4 = request.form["A4"]
        if email == "camila.tesorero@my.jru.edu":
            login = user.query.filter_by(email=email, Q4=A4).first()
            if login is not None:
                return redirect(url_for("ning"))
            return render_template("forget.html")
        login = user.query.filter_by(email=email, Q4=A4).first()
        if login is not None:
            return redirect(url_for("cheat"))
    return render_template("forget.html")

# @app.route("/forget",methods=["GET", "POST"])
# def forget():
#     if request.method == "POST":
#         uname = request.form["uname"]
#         A4 = request.form["A4"]
#         login = user.query.filter_by(username=uname, Q4=A4).first()
#         if login is not None:
#             return redirect(url_for("ning"))
#     return render_template("forget.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']
        Q1 = request.form['Q1']
        Q2 = request.form['Q2']
        Q3 = request.form['Q3']
        Q4 = request.form['Q4']
        Q5 = request.form['Q5']
        

        register = user(username = uname, email = mail, password = passw, Q1 = Q1, Q2 = Q2, Q3 = Q3, Q4 = Q4,Q5 = Q5)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    port=int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)